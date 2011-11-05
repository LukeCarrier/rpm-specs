# Known issues:
#   * PEAR's target directory specified at configure-time with the --with-pear
#     parameter is completely ignored at compile-time, so some arch-independent
#     files are in the arch-specific libdir instead of the sharedstatedir
#     https://bugs.php.net/bug.php?id=60163

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

# Extras for different SAPIs
Source1: https://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/php-fpmsysvinit.sh
Source2: https://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/php-fpm.conf

# Version constants for extensions
%global php_ver  5.3.8
%global api_ver  20090626
%global zend_ver 220090626

# Which SAPIs should be built?
#   The CGI SAPI cannot be disabled, since it's required for all shared
#   libraries. It'll be possible to cherry pick extensions soon, though.
%global with_embedded 1
%global with_fpm      1
%global with_httpd    1
%global with_zts      0


%description
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This package contains its command line interface binaries.


%package devel
Summary: hypertext preprocessor: development headers and tools
Requires: php


%description devel
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This package contains development header files which may be necessary for applications that require the Zend Engine.


%if %{with_embedded}
%package embedded
Summary: hypertext preprocessor: generic embedded interpreter library
Requires: php


%description embedded
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This shared library enables the use of PHP code within native applications, providing an embedded PHP interpreter.
%endif


%if %{with_fpm}
%package fpm
Summary: hypertext preprocessor: FastCGI Process Manager SAPI
Requires: php


%description fpm
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The PHP FPM server API enables resource efficient request processing via lighterweight web servers such as nginx.
%endif


%if %{with_httpd}
%package httpd
Summary: hypertext preprocessor: Apache HTTPd module (DSO)
Requires: php, httpd


%description httpd
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This Apache module enables processing of PHP files requested through Apache via an embedded PHP interpreter. It can be dynamicalloy loaded as a DSO module, as is the standard configuration.
%endif


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
      --with-config-file-path=%{_sysconfdir} \
      --with-config-file-scan-dir=%{_sysconfdir}/php.ini.d \
      $*
    make %{?_smp_mflags}
}

# Shared libraries
#   Any shared libraries that're to be built only as part of the CGI compilation
#   should be listed here.
with_shared="--with-pear"

# No shared libraries
#   Any shared libraries handled by the CGI build should be excluded here to
#   reduce compile-time.
without_shared="--without-pear"

# CGI build (TODO add shared libraries))
pushd build-cgi
build_tree \
  $with_shared
popd

# Embdedded build
%if %{with_embedded}
pushd build-embedded
build_tree \
  --enable-embed \
  $without_shared
popd
%endif

# FPM build
%if %{with_fpm}
pushd build-fpm
build_tree \
  --enable-fpm \
  $without_shared
popd
%endif

# Apache HTTPd build
%if %{with_httpd}
pushd build-httpd
build_tree \
  --with-apxs2=%{_sbindir}/apxs \
  $without_shared
popd
%endif

# TODO ZTS (thread-safe) build
#if %{with_zts}
#pushd build-zts
#build_tree
#popd
#%endif

%install
# Generate a file list
#   Does magic on a directory to produce a file list with fake absolute names.
#   This seems disgusting, but yey RPM!
#   $1 | directory path
#   $2 | filename regex
generate_file_list() {
    echo "$(find "$RPM_BUILD_ROOT/$1" -type f -regex "$2" | sed "s:^$RPM_BUILD_ROOT/::" | sort -u)"
}

rm -rf "$RPM_BUILD_ROOT"

# CGI build
make -C build-cgi install INSTALL_ROOT=$RPM_BUILD_ROOT
for file in .channels .depdb .depdblock .filemap .lock .registry
do
    rm -rf "$RPM_BUILD_ROOT/$file"
done
for file in INSTALL LICENSE README
do
    mv "$RPM_BUILD_ROOT/%{_libdir}/php/doc/PEAR/$file" \
      "$RPM_BUILD_ROOT/%{_libdir}/php/doc/PEAR_$file"
done
mv "$RPM_BUILD_ROOT/%{_libdir}/php/data/Structures_Graph/LICENSE" \
  "$RPM_BUILD_ROOT/%{_libdir}/php/doc/STRUCTURES_GRAPH_LICENSE"

# Embedded build
%if %{with_embedded}
make -C build-embedded install-sapi install-headers INSTALL_ROOT=$RPM_BUILD_ROOT
mv "$RPM_BUILD_ROOT/usr/lib/libphp5.so" "$RPM_BUILD_ROOT/%{_libdir}"
%endif

# FPM build
%if %{with_fpm}
make -C build-fpm install-fpm INSTALL_ROOT=$RPM_BUILD_ROOT
[ ! -d "$RPM_BUILD_ROOT/%{_initddir}" ] && mkdir -p "$RPM_BUILD_ROOT/%{_initddir}"
cp "%{SOURCE1}" "$RPM_BUILD_ROOT/%{_initddir}/php-fpm"
rm -f "$RPM_BUILD_ROOT/%{_sysconfdir}/php-fpm.conf.default"
cp "%{SOURCE2}" "$RPM_BUILD_ROOT/%{_sysconfdir}/php-fpm.conf"
%endif

# Apache HTTPd build
%if %{with_httpd}
[ ! -d "$RPM_BUILD_ROOT/%{_libdir}/httpd/modules" ] && mkdir -p "$RPM_BUILD_ROOT/%{_libdir}/httpd/modules"
install -m 755 build-httpd/libs/libphp5.so "$RPM_BUILD_ROOT/%{_libdir}/httpd/modules/mod_php5.so"
%endif

# The build directories are no longer necessary
cd "$RPM_BUILD_ROOT"


# The build directory seems to lose its way, too
[ ! -d "$RPM_BUILD_ROOT/%{_libdir}/php" ] && mkdir "$RPM_BUILD_ROOT/%{_libdir}/php"
mv "$RPM_BUILD_ROOT/%{_libdir}/build" "$RPM_BUILD_ROOT/%{_libdir}/php/build"

# Build file lists
mkdir _list
generate_file_list "/usr/lib64/php" ".*\.\(css\|depdb\|depdblock\|dtd\|filemap\|html\|lock\|php\|phpt\|pkg\|reg\|sh\|spec\|txt\|xml\)" | grep -vP "^%{_libdir}/php/doc" > _list/pear


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
%exclude                   /_list


%files devel
%defattr(-, root, root, -)
                           %{_includedir}/php
                           %{_libdir}/php/build


%if %{with_embedded}
%files embedded
%defattr(-, root, root, -)
                           %{_libdir}/libphp5.so
%endif


%if %{with_fpm}
%files fpm
%defattr(-, root, root, -)
                           %{_sbindir}/php-fpm
%attr(755, -, -)           %{_initddir}/php-fpm
                           %{_sysconfdir}/php-fpm.conf
                           %{_mandir}/man8/php-fpm.8*
%endif


%if %{with_httpd}
%files httpd
%defattr(-, root, root, -)
                           %{_libdir}/httpd/modules/mod_php5.so
%endif

%files pear -f %{buildroot}/_list/pear
%defattr(-, root, root, -)
                           %{_bindir}/pear
                           %{_bindir}/peardev
                           %{_bindir}/pecl
                           %{_sysconfdir}/pear.conf
%doc                       %{_libdir}/php/doc/*



%files phar
%defattr(-, root, root, -)
                           %{_bindir}/phar
                           %{_bindir}/phar.phar


%changelog

