%define sublime_text_version 3
%define sublime_text_build   3065
%define sublime_text_desktop /usr/share/applications/sublime_text.desktop
%define sublime_text_target  /opt/sublime_text

Name:    sublime-text-installer
Summary: Installer for Sublime Text 3.
Version: %{sublime_text_version}.%{sublime_text_build}
Release: 1%{?dist}

BuildArch: noarch

Group:   Development/Editors
License: Proprietary
URL:     http://sublimetext.com/3

Requires:      curl
BuildRequires: bzip2 tar

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
    Sublime Text is a sophisticated text editor for code, markup and prose.
    You'll love the slick user interface, extraordinary features and amazing performance.


%prep


%build


%install


%clean
    rm -rf $RPM_BUILD_ROOT


%post
    # Architecture (guess from architecture, abort if we fail)
    case "$(arch)" in
        "i686")
            ARCH="x32"
            ;;
        "x86_64")
            ARCH="x64"
            ;;
        *)
            echo "You appear to be installing on an unsupported architecture; bailing"
            exit 2
            ;;
    esac

    # Upgrade an existing installation if that's what RPM's expecting
    if [ -d "%{sublime_text_target}" ]; then
        if [ "$1" = "2" ]; then
            rm -rf "%{sublime_text_target}"
        else
            echo "Directory %{sublime_text_target} already exists; bailing"
            exit 2
        fi
    fi

    # Create temporary working directory
    TEMPDIR=$(mktemp -d)
    trap "{ cd - ; rm -rf $TEMPDIR; exit 255; }" SIGINT
    cd $TEMPDIR

    # Download application tarball, install to /opt
    curl -s -o sublime-text.tar.bz2 \
         "http://c758482.r82.cf2.rackcdn.com/sublime_text_%{sublime_text_version}_build_%{sublime_text_build}_${ARCH}.tar.bz2"
    tar -xjf sublime-text.tar.bz2
    mv "sublime_text_%{sublime_text_version}" "%{sublime_text_target}"

    # Clean up temporary directory
    cd - >/dev/null
    rm -rf $TEMPDIR

    # Add shortcuts
    ln -sf "%{sublime_text_target}/sublime_text"         "/usr/local/bin/subl"
    ln -sf "%{sublime_text_target}/sublime_text.desktop" "%{sublime_text_desktop}"

    # Add icon shortcuts
    for resolution in 16 32 48 128 256; do
        ln -sf "%{sublime_text_target}/Icon/${resolution}x${resolution}/sublime-text.png" \
              "/usr/share/icons/hicolor/${resolution}x${resolution}/apps/sublime-text.png"
    done
    gtk-update-icon-cache -f /usr/share/icons/hicolor &>/dev/null

    # Exit successfully
    exit 0


%preun
    # Remove application and shortcuts
    rm -f  "%{sublime_text_desktop}"
    rm -rf "%{sublime_text_target}"

    # Remove icon shortcuts
    for resolution in 16 32 48 128 256; do
        rm -f "/usr/share/icons/hicolor/${resolution}x${resolution}/apps/sublime-text.png"
    done
    gtk-update-icon-cache -f /usr/share/icons/hicolor &>/dev/null

    # Exit successfully
    exit 0


%files
