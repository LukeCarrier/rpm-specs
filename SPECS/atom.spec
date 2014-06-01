Name:    atom
Summary: A hackable text editor for the 21st century.
Version: 0.100.0
Release: 1%{?dist}

Group:   Development/Editors
License: MIT
URL:     https://atom.io/

Source0: https://github.com/atom/atom/archive/v%{version}.tar.gz

# We also require node and npm to be on PATH, but we're relying on the user to
# supply their own. This is because the node-gyp build in Fedora's repositories
# is currently incompatible.
#
# This build has been confirmed to run flawlessly on NodeJS 0.10.28 installed
# via NVM. node-gyp can fail to build if your system has the gyp RPM installed,
# so remove that first.
BuildRequires: libgnome-keyring-devel
Requires:      google-chrome-stable

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Don't try to extract debuginfo from built packages
%global debug_package %{nil}

# Attempts to guess dependencies will likely also fail
AutoReqProv: no


%description
    Atom is a desktop application based on web technologies. Like other desktop
    apps, it has its own icon in the dock, native menus and dialogs, and full
    access to the file system.

    Open the dev tools, however, and Atom's web-based core shines through.
    Whether you're tweaking the look of Atom's interface with CSS or adding
    major features with HTML and JavaScript, it's never been easier to take
    control of your editor.


%prep
%setup -q


%build
# Set the build directory as per grunt.option('build-dir') in Gruntfile.coffee.
# This prevents Atom from being built somewhere in /tmp.
script/build --build-dir=$PWD/build-rpm


%install
# The install task honours the INSTALL_PREFIX environment variable, so specify
# it for easier packaging.
export INSTALL_PREFIX=$RPM_BUILD_ROOT/opt/atom

# -d switch enables debugging output, -v enables verbose output
script/grunt -dv --build-dir=$PWD/build-rpm install


%clean
    rm -rf $RPM_BUILD_ROOT


%post
for binary in atom apm; do
    ln -sf /opt/atom/bin/$binary %{_bindir}/$binary
done


%postun
for binary in atom apm; do
    rm -f %{_bindir}/$binary
done

%files
%defattr(-, root, root, -)
                           /opt/atom
