Name:    doxygen
Version: 1.8.6
Release: 1%{?dist}
Summary: generate documentation from source code

Group:     Development
License:   GNU GPL
URL:       http://www.stack.nl/~dimitri/doxygen
Source0:   http://ftp.stack.nl/pub/users/dimitri/doxygen-%{version}.src.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: bison, flex, gcc, gcc-c++, make, perl

%description
Doxygen is a documentation system for C++, C, Java, Objective-C, Python, IDL (Corba and Microsoft flavors), Fortran, VHDL, PHP, C#, and to some extent D.


%package wizard
Summary: GUI configuration editor for Doxygen.

BuildRequires: qt-devel
Requires:      qt


%description wizard
Doxygen is a documentation system for C++, C, Java, Objective-C, Python, IDL (Corba and Microsoft flavors), Fortran, VHDL, PHP, C#, and to some extent D. This package provides a means of generating configuration files for documentation builds using a graphical user interface.


%prep
%setup -q


%build
# Well, this is nice, isn't it?
if [ -z "$QTDIR" ]
then
    arch="$(arch)"
    [  "$arch" =  "x86_64"  ] && export QTDIR=/usr/lib64/qt4
    [[ "$arch" =~ "i?86"   ]] && export QTDIR=/usr/lib/qt4
fi
PATH=$PATH:$QTDIR/bin

./configure \
    --prefix /usr \
    --shared \
    --release \
    --with-doxywizard

make %{?_smp_mflags}


%install
rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

# Relocate man pages in preparation for packaging
mkdir "$RPM_BUILD_ROOT/%{_datadir}"
mv "$RPM_BUILD_ROOT/usr/man" "$RPM_BUILD_ROOT/%{_mandir}"
rm -rf "$RPM_BUILD_ROOT/man"


%files
%defattr(-, root, root, -)
                           %{_bindir}/doxygen
                           %{_mandir}/man1/doxygen.1.gz


%files wizard
%defattr(-, root, root, -)
                           %{_bindir}/doxywizard
                           %{_mandir}/man1/doxywizard.1.gz


%changelog

