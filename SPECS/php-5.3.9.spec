Name:    php
Version: 5.3.9
Release: 1%{?dist}
Summary: hypertext preprocessor: CLI utilities

Group:     Development/Languages
License:   PHP
URL:       http://php.net
Source0:   http://php.net/distributions/php-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: bzip2-devel, gcc, gmp-devel, httpd-devel, krb5-devel, libjpeg-devel, libmcrypt-devel, libtool-ltdl-devel, libxml2-devel, libxslt-devel, libXpm-devel, make, mysql-devel, openssl-devel, pcre-devel, sqlite-devel, t1lib-devel

# Extras for different SAPIs
Source1: http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/php-fpmsysvinit.sh
Source2: http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/php-fpm.conf

# Version constants for extensions
%global php_ver  5.3.9
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
Summary:  hypertext preprocessor: BZip2 extension
Requires: bzip2 php
Group:    Development/Languages


%description bz2
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. BZip2 is an efficient file compression library. This extension enables the creation and extraction of such archives from within the PHP language.


%package devel
Summary:  hypertext preprocessor: development headers and tools
Requires: php
Group:    Development/Languages


%description devel
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This package contains development header files which may be necessary for applications that require the Zend Engine.


%if %{with_embedded}
%package embedded
Summary:  hypertext preprocessor: generic embedded interpreter library
Requires: php
Group:    Development/Languages


%description embedded
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This shared library enables the use of PHP code within native applications, providing an embedded PHP interpreter.
%endif


%if %{with_fpm}
%package fpm
Summary:  hypertext preprocessor: FastCGI Process Manager SAPI
Requires: php
Group:    Development/Languages


%description fpm
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The PHP FPM server API enables resource efficient request processing via lighterweight web servers such as nginx.
%endif


%package ftp
Summary:  hypertext preprocessor - FTP extension
Requires: php
Group:    Development/Languages


%description ftp
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This FTP extension enables communication with FTP servers.


%if %{with_httpd}
%package httpd
Summary:  hypertext preprocessor: Apache HTTPd module (DSO)
Requires: php, httpd
Group:    Development/Languages


%description httpd
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This Apache module enables processing of PHP files requested through Apache via an embedded PHP interpreter. It can be dynamically loaded as a DSO module, as is the standard configuration.
%endif


%package mbstring
Summary:  hypertext preprocessor: multi-byte string extension
Requires: php
Group:    Development/Languages


%description mbstring
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This extension enables the use of character sets whose characters overflow 8-bit values.


%package mcrypt
Summary:  hypertext preprocessor: MCrypt extension
Requires: php
Group:    Development/Languages


%description mcrypt
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This extension provides crypotography functionality for PHP developers.


%package mysql
Summary:  hypertext preprocessor: MySQL extension
Requires: mysql, php
Group:    Development/Languages


%description mysql
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This extension provides functionality for accessing MySQL databases in procedural code.
endif


%package mysqli
Summary:  hypertext preprocessor: MySQLi extension
Requires: mysql, php
Group:    Development/Languages


%description mysqli
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This extension provides functionality for accessing MySQL databases using object-oriented code.


%package openssl
Summary:  hypertext preprocessor - OpenSSL encryption extension
Requires: openssl, php
Group:    Development/Languages


%description openssl
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The OpenSSL extension for the language enables manipulation of SSL certificates and the encryption and decryption of data.


%package pdo
Summary:  hypertext preprocessor - data objects extension
Requires: php
Group:    Development/Languages


%description pdo
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. PDO (PHP Data Objects) enables the language to perform SQL queries on a variety of database types in a safe, object-orientated fashion.


%package pdo-sqlite
Summary:  hypertext preprocessor - data objects SQLite extension
Requires: php, php-pdo
Group:    Development/Languages


%description pdo-sqlite
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. The SQLite PDO extension enables connecting to SQLite databases via the PDO library.


%package pear
Summary:  hypertext preprocessor - PEAR library repository
Requires: php, php-devel, php-phar
Group:    Development/Languages


%description pear
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. Many open source libraries exist for free use within PHP applications; this package provides the tools necessary to install them and extensions to the scripting language that provide new and improved functionality.


%package phar
Summary:  hypertext preprocessor - source code archiving utility
Requires: php
Group:    Development/Languages


%description phar
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. Some applications and libraries may be distributed as archive files (PH(p)AR(chives)). This utility enables their compression and extraction.


%package sqlite
Summary:  hypertext preprocessor - SQLite < 3 extension
Requires: php
Group:    Development/Languages


%description sqlite
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables connecting to SQLite (< 3) databases.

%package sqlite3
Summary:  hypertext preprocessor - SQLite 3 extension
Requires: php
Group:    Development/Languages


%description sqlite3
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables connecting to SQLite 3 databases.


%package xsl
Summary:  hypertext preprocessor - XSLT extension
Requires: libxslt, php


%description xsl
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The XSLT extension enables developers to perform advanced operations on XML data.


%package zip
Summary:  hypertext preprocessor - zip extension
Requires: php
Group:    Development/Languages


%description zip
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables the manipulation of compressed zip files.


%if %{with_zts}
%package zts-bz2
Summary:  hypertext preprocessor: thread-safe BZip2 extension
Requires: bzip2, php, php-zts
Group:    Development/Languages


%description zts-bz2
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. BZip2 is an efficient file compression library. This extension enables the creation and extraction of such archives from within the PHP language.


%package zts-ftp
Summary:  hypertext preprocessor - thread-safe FTP extension
Requires: php, php-zts
Group:    Development/Languages


%description zts-ftp
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This thread-safe FTP extension enables communication with FTP servers.


%package zts-mbstring
Summary:  hypertext preprocessor: multi-byte string extension
Requires: php
Group:    Development/Languages


%description zts-mbstring
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This extension enables the use of character sets whose characters overflow 8-bit values.


%package zts-mcrypt
Summary:  hypertext preprocessor: MCrypt extension
Requires: php
Group:    Development/Languages


%description zts-mcrypt
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This extension provides crypotography functionality for PHP developers.


%package zts-mysql
Summary:  hypertext preprocessor: MySQL extension
Requires: mysql, php
Group:    Development/Languages


%description zts-mysql
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This extension provides functionality for accessing MySQL databases in procedural code.


%package zts-mysqli
Summary:  hypertext preprocessor: MySQLi extension
Requires: mysql, php
Group:    Development/Languages


%description zts-mysqli
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This extension provides functionality for accessing MySQL databases using object-oriented code.


%package zts-openssl
Summary:  hypertext preprocessor - thread-safe OpenSSL encryption extension
Requires: openssl, php
Group:    Development/Languages


%description zts-openssl
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The OpenSSL extension for the language enables manipulation of SSL certificates and the encryption and decryption of data.


%package zts-pdo
Summary:  hypertext preprocessor - thread-safe data objects extension
Requires: php
Group:    Development/Languages


%description zts-pdo
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. PDO (PHP Data Objects) enables the language to perform SQL queries on a variety of database types in a safe, object-orientated fashion.


%package zts-pdo-sqlite
Summary:  hypertext preprocessor - thread-safe data objects SQLite extension
Requires: php, php-pdo
Group:    Development/Languages


%description zts-pdo-sqlite
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. The SQLite PDO extension enables connecting to SQLite databases via the PDO library.


%package zts-sqlite
Summary:  hypertext preprocessor - thread-safe SQLite < 3 extension
Requires: php
Group:    Development/Languages


%description zts-sqlite
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables connecting to SQLite (< 3) databases.


%package zts-sqlite3
Summary:  hypertext preprocessor - thread-safe SQLite 3 extension
Requires: php
Group:    Development/Languages


%description zts-sqlite3
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables connecting to SQLite 3 databases.


%package zts-xsl
Summary:  hypertext preprocessor - thread-safe XSLT extension
Requires: libxslt, php


%description zts-xsl
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The XSLT extension enables developers to perform advanced operations on XML data.


%package zts-zip
Summary:  hypertext preprocessor - zip extension
Requires: php
Group:    Development/Languages


%description zts-zip
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables the manipulation of compressed zip files.
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

# Before attempting the build, work around deficiencies in PHP's build system
export PHP_MYSQLND_ENABLED=yes # Cannot load module 'mysql' because required
                               # module 'mysqlnd' is not loaded

# Shared libraries
#   Any shared libraries that're to be built only as part of the CGI compilation
#   should be listed here.
with_shared="--enable-ftp=shared \
             --enable-mbstring=shared \
             --enable-pdo=shared \
             --enable-zip=shared \
             --with-bz2=shared \
             --with-mcrypt=shared \
             --with-mysql=shared,mysqlnd \
             --with-mysqli=shared,mysqlnd \
             --with-openssl=shared \
             --with-pdo-sqlite=shared \
             --with-sqlite=shared \
             --with-sqlite3=shared
             --with-xsl=shared"

# No shared libraries
#   Any shared libraries handled by the CGI build should be excluded here to
#   reduce compile-time.
without_shared="--disable-ftp \
                --disable-pdo \
                --without-bz2 \
                --without-openssl \
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
  --with-fpm-user=www-server \
  --with-fpm-group=www-server \
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
cp php.ini-production "$RPM_BUILD_ROOT/%{_sysconfdir}/php.ini"

# Embedded build
%if %{with_embedded}
make -C build-embedded install-sapi install-headers INSTALL_ROOT=$RPM_BUILD_ROOT

# Sometimes the libdir specification is ignored..?
if [ ! -f "$RPM_BUILD_ROOT/%{_libdir}/libphp5.so" ]
then
   mv "$RPM_BUILD_ROOT/usr/lib/libphp5.so" "$RPM_BUILD_ROOT/%{_libdir}"
fi
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
                           %{_sysconfdir}/php.ini
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
                           %{_datadir}/fpm/status.html
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


%files mbstring
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/mbstring.*


%files mcrypt
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/mcrypt.*


%files mysql
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/mysql.*


%files mysqli
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/mysqli.*


%files openssl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/openssl.*


%files pdo
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/pdo.*


%files pdo-sqlite
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/pdo_sqlite.*


%files pear -f "%{buildroot}/_list/pear"
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


%files xsl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/xsl.*


%files zip
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/zip.*


%if %{with_zts}
%files zts-bz2
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/bz2.*


%files zts-ftp
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/ftp.*


%files zts-mbstring
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/mbstring.*


%files zts-mcrypt
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/mcrypt.*


%files zts-mysql
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/mysql.*


%files zts-mysqli
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/mysqli.*


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


%files zts-xsl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/xsl.*


%files zts-sqlite3
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/sqlite3.*


%files zts-zip
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/zip.*
%endif


%changelog

