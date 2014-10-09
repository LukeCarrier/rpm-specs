#!/bin/sh
# RPM build wrapper
#
# Simplifies the build process by handling installing dependencies and fetching
# source code and helper utilities necessary for the build process to complete,
# then runs rpmbuild for you.

# Trap an error and exit cleanly.
error_trap() {
    echo " "
    echo "$0: an error occurred during the execution of an action; aborting"
    echo " "
    exit 69
}

trap error_trap 1 2 3 15 ERR

rootdir="$(readlink -fn "$(dirname "$0")/..")"

# Get a metadata value from within the spec file.
#
# Grabs (and outputs, so run this in a subshell) a value for the specified
# parameter from within the specified spec file. This can handle multi-line
# definitions, but only if they're prefixed with the parameter again!
#
# @uses grep
# @uses sed
# @param $1 The spec file path.
# @param $2 The parameter we're seeking.
# @return The raw value, complete with newlines (or not), according to the
#         formatting of the spec file.
get_meta_value() {
    raw=$(grep -P "^$2:" "$1")
    echo "$raw" | while read line
    do
        echo ${line#*:}
    done
}

# Expand %{} tags to values.
#
# Interpolation is difficult with Bash, so to keep it simple you'll need to call
# specific methods to handle replacements.
#
# @uses get_meta_value
# @uses sed
# @param $1 The path to the spec file we're fiddling with.
# @param $2 The value to perform the replacement on.
# @param $3 The tag to interpolate.
# @param $4 The tag's capitalised form, as in its definition.
# @return The value with the interpolation complete.
get_and_interpolate_meta_value() {
    raw=$(get_meta_value "$1" "$2")
    tag=$(get_meta_value "$1" "$4")
    echo "$raw" | sed "s/%{$3}/$tag/g"
}

echo " "

# Parse our arguments
eval set -- "$(getopt -o "m:r:s:D" --long "mock:,remote-build:,spec:,no-dependencies" -- "$@")"
while true; do
    case "$1" in
        -D|--no-dependencies ) NO_DEPENDENCIES=1     ; shift 1 ;;
        -m|--mock            ) MOCK_ENVIRONMENT="$2" ; shift 2 ;;
        -r|--remote-builder  ) REMOTE_BUILDER="$2"   ; shift 2 ;;
        -s|--spec            ) SPEC="$2"             ; shift 2 ;;
        *                    ) break                 ;         ;;
    esac
done

# Make sure they're sane
[ -z "$SPEC" ] && echo "You must specify a --spec!" && exit 64

# Extract metadata
SPEC_DIST=$(rpm --eval '%{dist}')
SPEC_NAME=$(get_meta_value "$SPEC" "Name")
SPEC_RELEASE=$(get_meta_value "$SPEC" "Release" | grep -o "^[^%]")
SPEC_VERSION=$(get_meta_value "$SPEC" "Version")

# Print generic information
echo "Build information"
echo "-----------------"
echo " "
echo "Distribution: ${SPEC_DIST}"
echo "Package:      ${SPEC_NAME}"
echo "Version:      ${SPEC_VERSION}"
echo " "

# Handle a remote build
if [ -n "$REMOTE_BUILDER" ]; then
    echo "Remote build preparation"
    echo "------------------------"
    echo " "
    echo "Remote builds require the prior installation of rsync and wget and"
    echo "installation and configuration of the Mock build system. If your"
    echo "build fails, please ensure that your Mock build environment is"
    echo "functioning correctly."
    echo " "

    echo "Copying files to the remote build host."
    rsync -avrz --delete \
          --exclude ".git" --exclude "repodata" --exclude "BUILD" \
          --exclude "BUILDROOT" --exclude "RPMS" --exclude "SOURCES" \
          --exclude "SRPMS" \
          "$rootdir/" "$REMOTE_BUILDER:rpmbuild"

    build_cmd="cd rpmbuild && ~/rpmbuild/SUPPORT/auto-build.sh --mock $MOCK_ENVIRONMENT --spec $SPEC"
    echo "Starting build (with build command ${build_cmd})"
    ssh -tt "$REMOTE_BUILDER" "$build_cmd"

    exit
fi

build_dependencies="$(get_meta_value $SPEC 'BuildRequires' 'version' 'Version')"
source_packages="$(get_and_interpolate_meta_value $SPEC 'Source[0-9]*' 'version' 'Version')"

echo "Build dependencies"
echo "------------------"
echo " "
echo "$build_dependencies"
echo " "

echo "Source packages"
echo "---------------"
echo " "
echo "$source_packages"
echo " "

echo "Obtaining dependencies"
echo "----------------------"
echo " "
if [ "$NO_DEPENDENCIES" == "1" ]; then
    echo "Skipping downloading and installing dependencies. If the build fails,"
    echo "it's likely because you're missing some."
    echo " "
elif [ -n "$MOCK_ENVIRONMENT" ]; then
    echo "Skipping downloading dependencies, because mock will do it for us."
    echo " "
else
    echo "Attempting to install packages; you'll either need sudo with no"
    echo "password enabled for this user ($USER) or its password to enter at"
    echo "the prompt."
    echo " "
    echo "If you know the dependencies are installed, you can use -D (or"
    echo "--no-dependencies to skip this."
    echo " "
    sudo yum -y install rpm-build wget $(echo "$build_dependencies" | sed 's/, / /g')
    echo " "
fi
echo " "

echo "Obtaining source"
echo "----------------"
if [ "$NO_DEPENDENCIES" = "1" ]; then
    echo "Skipping obtaining source code. If the build fails, it's likely"
    echo "because you're missing some."
    echo " "
else
    echo "Attempting to download source code to the SOURCES directory relative to the"
    echo "specified spec file."
    echo " "
    if [ "x${source_packages}" != "x" ]; then
        echo "$source_packages" | while read url
        do
            wget --continue --directory="${rootdir}/SOURCES" --no-check-certificate \
                 --progress=dot "$url"
        done
    fi
    echo " "
fi

echo "Building"
echo "--------"
echo " "
if [ -n "$MOCK_ENVIRONMENT" ]; then
    echo "Running rpmbuild to generate the SRPM."
    rpmbuild -bs "${rootdir}/${SPEC}"

    echo "Running mock to generate the RPM. Whilst the build is in progress,"
    echo "watch ${rootdir}/MOCK/*.log for status information."
    srpm="${SPEC_NAME}-${SPEC_VERSION}-${SPEC_RELEASE}${SPEC_DIST}.src.rpm"
    mock -r "$MOCK_ENVIRONMENT" init
    mock -r "$MOCK_ENVIRONMENT" --chroot -- rm -rf /builddir/build
    mock -r "$MOCK_ENVIRONMENT" --copyin "${rootdir}" /builddir/build
    mock -r "$MOCK_ENVIRONMENT" --resultdir "${rootdir}/MOCK" \
         --rebuild "${rootdir}/SRPMS/${srpm}"
    mock -r "$MOCK_ENVIRONMENT" clean
else
    echo "Running rpmbuild to generate the SRPM and RPM."
    echo " "
    rpmbuild --define "_topdir ${rootdir}" -ba "${rootdir}/${SPEC}"
    echo " "
fi
