Name:    doxygen
Version: 1.7.6.1
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


%prep
%setup -q


%build
./configure \
  --prefix /usr \
  --shared \
  --release
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
                           %{_bindir}/doxytag
                           %{_mandir}/man1/doxygen.1.gz
                           %{_mandir}/man1/doxytag.1.gz


%changelog

