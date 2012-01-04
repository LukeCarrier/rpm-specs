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

[ ! -f "$1" ] && echo "$0: the first parameter should be the path to an RPM spec file" >&2 && exit 64

build_dependencies="$(get_meta_value $1 'BuildRequires' 'version' 'Version')"
source_packages="$(get_and_interpolate_meta_value $1 'Source[0-9]*' 'version' 'Version')"

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

echo "Attempting to install packages; you'll either need sudo with no password"
echo "enabled for this user ($USER) or its password to enter at the prompt."
echo " "
sudo yum -y install rpm-build wget $(echo "$build_dependencies" | sed 's/, / /g')
echo " "

echo "Attempting to download source code to the SOURCES directory relative to the"
echo "specified spec file."
echo " "
echo "$source_packages" | while read url
do
    echo '' # wget --continue --directory="$(dirname $0)/../SOURCES" --no-check-certificate --progress=dot "$url"
done
echo " "

echo "Running rpmbuild to generate the SRPM and RPM, since we managed to get all"
echo "necessary dependencies."
echo " "
rpmbuild -ba $1
echo " "
