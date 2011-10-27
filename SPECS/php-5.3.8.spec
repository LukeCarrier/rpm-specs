Name:    php
Version: 5.3.8
Release: 1%{?dist}
Summary: hypertext preprocessor: CLI utilities

Group:     Applications/Internet
License:   PHP
URL:       http://php.net
Source0:   http://php.net/distributions/php-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires: 
#Requires:      

# Version constants for extensions
%global phpver  5.3.8
%global apiver  20090626
%global zendver 220090626


%description
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This package contains its command line interface binaries.


%package devel
Summary: hypertext preprocessor: development headers and tools
Requires: php


%description devel
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This package contains development header files which may be necessary for applications that require the Zend Engine.


%package pear
Summary: hypertext preprocessor - PEAR library repository
Requires: php, php-devel, php-phar


%description pear
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. Many open source libraries exist for free use within PHP applications; this package provides the tools necessary to install them and extensions to the scripting language that provide new and improved functionality.


%package phar
Summary: hypertext preprocessor - source code archiving utility
Requires: php


%description phar
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. Some applications and libraries may be distributed as archive files (PH(p)AR(chives)). This utility enables their compression and extraction.


%prep
%setup -q


%build
%configure \
  --disable-rpath \
  --disable-static \
  --enable-shared \
  --with-config-file-path=%{_sysconfdir}/php.ini \
  --with-config-file-scan-path=%{_sysconfdir}/php.ini.d
make %{?_smp_mflags}


%install
rm -rf "$RPM_BUILD_ROOT"
make install INSTALL_ROOT="$RPM_BUILD_ROOT"
cd "$RPM_BUILD_ROOT"

# These PEAR/PECL cache files don't belong here (build system bug?)
rm -rfv .channels/ .depdb .depdblock .filemap .lock

# The build directory seems to lose its way, too
mv "$RPM_BUILD_ROOT/%{_libdir}/build" "$RPM_BUILD_ROOT/%{_libdir}/php/build"


%clean
rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root, -)
                   %{_bindir}/php
                   %{_bindir}/php-cgi
                   %{_bindir}/php-config
                   %{_mandir}/man1


%files devel
%defattr(-, root, root, -)
                   %{_bindir}/phpize
                   %{_libdir}/php/build
                   %{_includedir}/php


%files pear
%defattr(-, root, root, -)
                   %{_bindir}/pear
                   %{_bindir}/peardev
                   %{_bindir}/pecl
                   %{_sysconfdir}/pear.conf
                   %{_libdir}/php/.depdb
                   %{_libdir}/php/.depdblock
                   %{_libdir}/php/.filemap
                   %{_libdir}/php/.lock
                   %{_libdir}/php/.channels
                   %{_libdir}/php/.registry
                   %{_libdir}/php/Archive
                   %{_libdir}/php/Console
                   %{_libdir}/php/OS
                   %{_libdir}/php/PEAR.php
                   %{_libdir}/php/PEAR5.php
                   %{_libdir}/php/PEAR
                   %{_libdir}/php/Structures
                   %{_libdir}/php/System.php
                   %{_libdir}/php/XML
                   %{_libdir}/php/data
                   %{_libdir}/php/doc
                   %{_libdir}/php/pearcmd.php
                   %{_libdir}/php/peclcmd.php
                   %{_libdir}/php/test


%files phar
%defattr(-, root, root, -)
                   %{_bindir}/phar
                   %{_bindir}/phar.phar


%changelog

