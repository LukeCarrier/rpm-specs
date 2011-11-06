Name:    php
Version: 5.3.8
Release: 1%{?dist}
Summary: hypertext preprocessor: CLI utilities

Group:     Development/Languages
License:   PHP
URL:       http://php.net
Source0:   http://php.net/distributions/php-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: bzip2-devel gmp-devel httpd-devel krb5-devel libjpeg-turbo-devel libxml2-devel libXpm-devel openssl-devel pcre-devel t1lib-devel

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
%global with_zts      1


%description
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This package contains its command line interface binaries.


%package bz2
Summary: hypertext preprocessor: BZip2 extension
Requires: bzip2 php


%description bz2
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. BZip2 is an efficient file compression library. This extension enables the creation and extraction of such archives from within the PHP language.


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


%package ftp
Summary: hypertext preprocessor - FTP extension
Requires: php


%description ftp
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This FTP extension enables communication with FTP servers.


%if %{with_httpd}
%package httpd
Summary: hypertext preprocessor: Apache HTTPd module (DSO)
Requires: php, httpd


%description httpd
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This Apache module enables processing of PHP files requested through Apache via an embedded PHP interpreter. It can be dynamically loaded as a DSO module, as is the standard configuration.
%endif


%package openssl
Summary: hypertext preprocessor - OpenSSL encryption extension
Requires: openssl, php


%description openssl
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The OpenSSL extension for the language enables manipulation of SSL certificates and the encryption and decryption of data.


%package pdo
Summary: hypertext preprocessor - data objects extension
Requires: php


%description pdo
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. PDO (PHP Data Objects) enables the language to perform SQL queries on a variety of database types in a safe, object-orientated fashion.


%package pdo-sqlite
Summary: hypertext preprocessor - data objects SQLite extension
Requires: php, php-pdo


%description pdo-sqlite
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. The SQLite PDO extension enables connecting to SQLite databases via the PDO library.


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


%package sqlite
Summary: hypertext preprocessor - SQLite < 3 extension
Requires: php


%description sqlite
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables connecting to SQLite (< 3) databases.

%package sqlite3
Summary: hypertext preprocessor - SQLite 3 extension
Requires: php


%description sqlite3
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables connecting to SQLite 3 databases.


%if %{with_zts}
%package zts-bz2
Summary: hypertext preprocessor: thread-safe BZip2 extension
Requires: bzip2, php, php-zts


%description zts-bz2
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. BZip2 is an efficient file compression library. This extension enables the creation and extraction of such archives from within the PHP language.


%package zts-ftp
Summary: hypertext preprocessor - thread-safe FTP extension
Requires: php, php-zts


%description zts-ftp
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This thread-safe FTP extension enables communication with FTP servers.


%package zts-openssl
Summary: hypertext preprocessor - thread-safe OpenSSL encryption extension
Requires: openssl, php


%description zts-openssl
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The OpenSSL extension for the language enables manipulation of SSL certificates and the encryption and decryption of data.


%package zts-pdo
Summary: hypertext preprocessor - thread-safe data objects extension
Requires: php


%description zts-pdo
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. PDO (PHP Data Objects) enables the language to perform SQL queries on a variety of database types in a safe, object-orientated fashion.


%package zts-pdo-sqlite
Summary: hypertext preprocessor - thread-safe data objects SQLite extension
Requires: php, php-pdo


%description zts-pdo-sqlite
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. The SQLite PDO extension enables connecting to SQLite databases via the PDO library.


%package zts-sqlite
Summary: hypertext preprocessor - thread-safe SQLite < 3 extension
Requires: php


%description zts-sqlite
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables connecting to SQLite (< 3) databases.


%package zts-sqlite3
Summary: hypertext preprocessor - thread-safe SQLite 3 extension
Requires: php


%description zts-sqlite3
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables connecting to SQLite 3 databases.
%endif


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
      --disable-rpath \
      --with-config-file-path=%{_sysconfdir} \
      --with-config-file-scan-dir=%{_sysconfdir}/php.ini.d \
      --with-libxml-dir=/usr \
      --with-regex=php \
      $*
    make %{?_smp_mflags}
}

# Shared libraries
#   Any shared libraries that're to be built only as part of the CGI compilation
#   should be listed here.
with_shared="--enable-ftp=shared \
             --enable-pdo=shared \
             --with-bz2=shared \
             --with-openssl=shared \
             --with-pdo-sqlite=shared \
             --with-sqlite=shared \
             --with-sqlite3=shared"

# No shared libraries
#   Any shared libraries handled by the CGI build should be excluded here to
#   reduce compile-time.
without_shared="--disable-ftp \
                --disable-pdo \
                --without-bz2 \
                --without-pdo-sqlite \
                --without-sqlite \
                --without-sqlite3"

# CGI build (TODO add shared libraries))
pushd build-cgi
build_tree \
  $with_shared \
  --with-pear=$BUILD_ROOT/%{_sharedstatedir}/php/pear
popd

# Embdedded build
%if %{with_embedded}
pushd build-embedded
build_tree \
  --enable-embed \
  --without-pear \
  $without_shared
popd
%endif

# FPM build
%if %{with_fpm}
pushd build-fpm
build_tree \
  --enable-fpm \
  --without-pear \
  $without_shared
popd
%endif

# Apache HTTPd build
%if %{with_httpd}
pushd build-httpd
build_tree \
  --with-apxs2=%{_sbindir}/apxs \
  --without-pear \
  $without_shared
popd
%endif

# ZTS (thread-safe) build
%if %{with_zts}
pushd build-zts
build_tree \
  --enable-mysqlnd-threading \
  --enable-maintainer-zts \
  --without-pear \
  $with_shared
popd
%endif

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

# ZTS build
%if %{with_zts}
make -C build-zts install-modules INSTALL_ROOT=$RPM_BUILD_ROOT
%endif

# The build directories are no longer necessary
cd "$RPM_BUILD_ROOT"

# Extensions and build files shouldn't clutter the libdir
[ ! -d "$RPM_BUILD_ROOT/%{_libdir}/php" ] && mkdir "$RPM_BUILD_ROOT/%{_libdir}/php"
[ -d "$RPM_BUILD_ROOT/%{_libdir}/extensions" ] && mv "$RPM_BUILD_ROOT/%{_libdir}/extensions" "$RPM_BUILD_ROOT/%{_libdir}/php"
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


%files bz2
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/bz2.*


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


%files ftp
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/ftp.*


%if %{with_httpd}
%files httpd
%defattr(-, root, root, -)
                           %{_libdir}/httpd/modules/mod_php5.so
%endif


%files openssl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/openssl.*


%files pdo
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/pdo.*


%files pdo-sqlite
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/pdo_sqlite.*


%files pear -f %{buildroot}/_list/pear
%defattr(-, root, root, -)
                           %{_bindir}/pear
                           %{_bindir}/peardev
                           %{_bindir}/pecl
                           %{_sysconfdir}/pear.conf
                           %{_sharedstatedir}/php/pear



%files phar
%defattr(-, root, root, -)
                           %{_bindir}/phar
                           %{_bindir}/phar.phar


%files sqlite
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/sqlite.*


%files sqlite3
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/sqlite3.*


%if %{with_zts}
%files zts-bz2
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/bz2.*


%files zts-ftp
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/ftp.*


%files zts-openssl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/openssl.*


%files zts-pdo
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/pdo.*


%files zts-pdo-sqlite
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/pdo_sqlite.*


%files zts-sqlite
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/sqlite.*


%files zts-sqlite3
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/sqlite3.*
%endif


%changelog

