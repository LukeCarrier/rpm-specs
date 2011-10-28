Name:    php
Version: 5.3.8
Release: 1%{?dist}
Summary: hypertext preprocessor: CLI utilities

Group:     Development/Languages
License:   PHP
URL:       http://php.net
Source0:   http://php.net/distributions/php-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: bzip2-devel gmp-devel httpd-devel krb5-devel libjpeg-turbo-devel libXpm-devel openssl-devel pcre-devel t1lib-devel
# TODO - add these for each sub package Requires:      

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

# Prepare for multiple builds (for different SAPIs)
#   Don't remove the "build" directory, since it breaks the build. PHP's build
#   system sucks *real* bad.
mkdir build-{cgi,embedded,fpm,httpd,zts}


%build

# Perform a basic build
#   Defaults for all SAPIs to be compiled; no shared libraries should be built.
#   All parameters will be passed to the configure script!
build_tree() {
    ln -sf ../configure

    %configure \
      --srcdir=.. \
      --cache-file=../config.cache \
      --with-config-file-path=%{_sysconfdir}/php.ini \
      --with-config-file-scan-dir=%{_sysconfdir}/php.ini.d \
      --without-pear \
      $*
    make %{?_smp_mflags}
}

# No shared libraries
#   Any shared libraries handled by the CGI build should be excluded here to
#   reduce compile-time.
without_shared=""

# CGI build (TODO add shared libraries))
pushd build-cgi
build_tree
popd

# TODO Embdedded build
#pushd build-embedded
#build_tree \
#  --enable-embed \
#  $without_shared
#popd

# TODO FPM build
#pushd build-fpm
#build_tree \
#  --enable-fpm \
#  $without_shared
#popd

# TODO Apache HTTPd build
#pushd build-httpd
#build_tree \
#  --with-apxs2=%{_sbindir}/apxs \
#  $without_shared
#popd

# TODO ZTS (thread-safe) build
#pushd build-zts
#build_tree
#popd

%install
rm -rf "$RPM_BUILD_ROOT"

# CGI build
make -C build-cgi install INSTALL_ROOT=$RPM_BUILD_ROOT

# The build directory seems to lose its way, too
mkdir "$RPM_BUILD_ROOT/%{_libdir}/php"
mv "$RPM_BUILD_ROOT/%{_libdir}/build" "$RPM_BUILD_ROOT/%{_libdir}/php/build"


%clean
rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root, -)
                           %{_bindir}/php
                           %{_bindir}/php-cgi
                           %{_bindir}/php-config
                           %{_bindir}/phpize
                           %{_mandir}/man1/php.1*
                           %{_mandir}/man1/php-config.1*
                           %{_mandir}/man1/phpize.1*


%files devel
%defattr(-, root, root, -)
                           %{_includedir}/php
                           %{_libdir}/php/build


%files pear
%defattr(-, root, root, -)


%files phar
%defattr(-, root, root, -)
                           %{_bindir}/phar
                           %{_bindir}/phar.phar


%changelog

