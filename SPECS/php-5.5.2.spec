Name:    php
Version: 5.5.2
Release: 1%{?dist}
Summary: hypertext preprocessor: CLI utilities

Group:     Development/Languages
License:   PHP
URL:       http://php.net
Source0:   http://php.net/distributions/php-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: bzip2-devel, curl-devel, freetype-devel, gcc, gd-devel
BuildRequires: gmp-devel, httpd-devel, krb5-devel, libicu-devel
BuildRequires: libjpeg-devel, libmcrypt-devel, libtool-ltdl-devel
BuildRequires: libxml2-devel, libxslt-devel, libXpm-devel, make, mysql-devel
BuildRequires: net-snmp, net-snmp-devel, net-snmp-utils, openssl-devel
BuildRequires: pcre-devel, postgresql-devel sqlite-devel, t1lib-devel
BuildRequires: zlib-devel

# Extras for different SAPIs
Source1: http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/php-fpmsysvinit.sh
Source2: http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/php-fpm.conf

# Version constants for extensions
%global api_ver 20121212

# Which SAPIs should be built?
#   The CGI SAPI cannot be disabled, since it's required for all shared
#   libraries. It'll be possible to cherry pick extensions soon, though.
%global with_embedded 1
%global with_fpm      1
%global with_httpd    1
%global with_zts      1

# Run test suite?
#   The PHP test suite requires user input (for report sending). If you're
#   unable to deal with these prompts, disable this. I'll patch the test
#   harness when I get chance; promise.
%global run_tests 1


%description
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This package contains its command line interface binaries.


%package bcmath
Summary:  hypertext preprocessor: BCMath extension
Requires: php
Group:    Development/Languages


%description bcmath
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. BCMath provides arbitrary precision mathematics to PHP applications.


%package bz2
Summary:  hypertext preprocessor: BZip2 extension
Requires: bzip2 php
Group:    Development/Languages


%description bz2
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. BZip2 is an efficient file compression library. This extension enables the creation and extraction of such archives from within the PHP language.


%package curl
Summary:  hypertext preprocessor: cURL extension
Requires: curl, php
Group:    Development/Languages


%description curl
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. libcurl is a free and easy-to-use client-side URL transfer library, supporting DICT, FILE, FTP, FTPS, Gopher, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, Telnet and TFTP. libcurl supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies, cookies, user+password authentication (Basic, Digest, NTLM, Negotiate, Kerberos), file transfer resume, http proxy tunneling and more! 


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


%package gd
Summary:  hypertext preprocessor - GD extension
Requires: freetype, gd, php
Group:    Development/Languages


%description gd
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This FTP extension enables image manipulation operations.


%if %{with_httpd}
%package httpd
Summary:  hypertext preprocessor: Apache HTTPd module (DSO)
Requires: php, httpd
Group:    Development/Languages


%description httpd
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This Apache module enables processing of PHP files requested through Apache via an embedded PHP interpreter. It can be dynamically loaded as a DSO module, as is the standard configuration.
%endif


%package intl
Summary:  hypertext preprocessor: internationalisation extension
Requires: icu, php
Group:    Development/Languages


%description intl
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. Internationalization extension (further is referred as Intl) is a wrapper for ICU library, enabling PHP programmers to perform UCA-conformant collation and date/time/number/currency formatting in their scripts.


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


%package pdo-mysql
Summary:  hypertext preprocessor - data objects MySQL extension
Requires: mysql, php, php-pdo
Group:    Development/Languages


%description pdo-mysql
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. The MySQL PDO extension enables connecting to MySQL databases via the PDO library.


%package opcache
Summary:  hypertext preprocessor - opcache extension
Requires: php
Group:    Development/Languages

%description opcache
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. This extension provides an opcode cache.


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


%package pgsql
Summary:  hypertext preprocessor - PgSQL library
Requires: php
Group:    Development/Languages


%description pgsql
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This library extends it with support for the PostgreSQL database server.


%package phar
Summary:  hypertext preprocessor - source code archiving utility
Requires: php
Group:    Development/Languages


%description phar
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. Some applications and libraries may be distributed as archive files (PH(p)AR(chives)). This utility enables their compression and extraction.


%package snmp
Summary:  hypertext preprocessor - SNMP extension
Requires: net-snmp, net-snmp-utils, php
Group:    Development/Languages


%description snmp
PHP is a widely used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The SNMP extension allows monitoring of network devices.


%package soap
Summary:  hypertext preprocessor - SOAP extension
Requires: libxml2, php
Group:    Development/Languages


%description soap
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The SOAP extension can be used to write SOAP Servers and Clients. It supports subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.


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


%package xmlrpc
Summary:  hypertext preprocessor - XMLRPC extension
Requires: php


%description xmlrpc
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The XMLRPC extension makes it easier for web developers to work with existing web services.


%package zip
Summary:  hypertext preprocessor - zip extension
Requires: php
Group:    Development/Languages


%description zip
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables the manipulation of compressed zip files.


%package zlib
Summary:  hypertext preprocessor - zlib extension
Requires: php, zlib
Group:    Development/Languages


%description zlib
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The zlib extension provides compression functionality.


%if %{with_zts}
%package zts-bcmath
Summary:  hypertext preprocessor: thread-safe BCMath extension
Requires: php
Group:    Development/Languages


%description zts-bcmath
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. BCMath provides arbitrary precision mathematics to PHP applications.


%package zts-bz2
Summary:  hypertext preprocessor: thread-safe BZip2 extension
Requires: bzip2, php, php-zts
Group:    Development/Languages


%description zts-bz2
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. BZip2 is an efficient file compression library. This extension enables the creation and extraction of such archives from within the PHP language.


%package zts-curl
Summary:  hypertext preprocessor: thread-safe cURL extension
Requires: curl, php
Group:    Development/Languages


%description zts-curl
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. libcurl is a free and easy-to-use client-side URL transfer library, supporting DICT, FILE, FTP, FTPS, Gopher, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMTP, SMTPS, Telnet and TFTP. libcurl supports SSL certificates, HTTP POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies, cookies, user+password authentication (Basic, Digest, NTLM, Negotiate, Kerberos), file transfer resume, http proxy tunneling and more!


%package zts-ftp
Summary:  hypertext preprocessor - thread-safe FTP extension
Requires: php, php-zts
Group:    Development/Languages


%description zts-ftp
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This thread-safe FTP extension enables communication with FTP servers.


%package zts-gd
Summary:  hypertext preprocessor - thread-safe GD extension
Requires: freetype, gd, php
Group:    Development/Languages


%description zts-gd
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This FTP extension enables image manipulation operations.


%package zts-intl
Summary:  hypertext preprocessor: thread-safe internationalisation extension
Requires: icu, php
Group:    Development/Languages


%description zts-intl
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. Internationalization extension (further is referred as Intl) is a wrapper for ICU library, enabling PHP programmers to perform UCA-conformant collation and date/time/number/currency formatting in their scripts.


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


%package zts-opcache
Summary:  hypertext preprocessor - opcache extension
Requires: php
Group:    Development/Languages

%description zts-opcache
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. This extension provides an opcode cache.


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


%package zts-pdo-mysql
Summary:  hypertext preprocessor - thread-safe data objects MySQL extension
Requires: mysql, php, php-pdo
Group:    Development/Languages


%description zts-pdo-mysql
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. The MySQL PDO extension enables connecting to MySQL databases via the PDO library.


%package zts-pdo-sqlite
Summary:  hypertext preprocessor - thread-safe data objects SQLite extension
Requires: php, php-pdo
Group:    Development/Languages


%description zts-pdo-sqlite
PHP is a widely-used general-purpose scripting language that is especially suited for web development and can be embedded into HTML. The SQLite PDO extension enables connecting to SQLite databases via the PDO library.


%package zts-pgsql
Summary:  hypertext preprocessor - thread-safe PgSQL library
Requires: php
Group:    Development/Languages


%description zts-pgsql
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This library extends it with support for the PostgreSQL database server.


%package zts-snmp
Summary:  hypertext preprocessor - thread-safe SNMP extension
Requires: net-snmp, net-snmp-utils, php
Group:    Development/Languages


%description zts-snmp
PHP is a widely used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The SNMP extension allows monitoring of network devices.


%package zts-soap
Summary:  hypertext preprocessor - thread-safe SOAP extension
Requires: libxml, php
Group:    Development/Languages


%description zts-soap
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The SOAP extension can be used to write SOAP Servers and Clients. It supports subsets of SOAP 1.1, SOAP 1.2 and WSDL 1.1 specifications.


%package zts-sqlite3
Summary:  hypertext preprocessor - thread-safe SQLite 3 extension
Requires: php
Group:    Development/Languages


%description zts-sqlite3
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This optional extension enables connecting to SQLite 3 databases.


%package zts-xmlrpc
Summary:  hypertext preprocessor - thread-safe XMLRPC extension
Requires: php


%description zts-xmlrpc
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The XMLRPC extension makes it easier for web developers to work with existing web services.


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


%package zts-zlib
Summary:  hypertext preprocessor - zlib extension
Requires: php, zlib
Group:    Development/Languages


%description zts-zlib
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. The zlib extension provides compression functionality.


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
      --with-config-file-path=%{_sysconfdir}/php/php.ini \
      --with-config-file-scan-dir=%{_sysconfdir}/php/conf.d \
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
with_shared="--enable-bcmath=shared \
             --enable-ftp=shared \
             --enable-intl=shared \
             --enable-mbstring=shared \
             --enable-opcache=shared \
             --enable-pdo=shared \
             --enable-soap=shared \
             --enable-zip=shared \
             --with-bz2=shared \
             --with-curl=shared \
             --with-freetype-dir=/usr \
             --with-gd=shared \
             --with-mcrypt=shared \
             --with-mysql=shared,mysqlnd \
             --with-mysqli=shared,mysqlnd \
             --with-openssl=shared \
             --with-pdo-mysql=shared \
             --with-pdo-sqlite=shared,/usr \
             --with-pgsql=shared \
             --with-snmp=shared \
             --with-sqlite=shared \
             --with-sqlite3=shared \
             --with-xmlrpc=shared \
             --with-xsl=shared \
             --with-zlib=shared"

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

# CGI build
pushd build-cgi
export PEAR_CONFIG_SYSCONFDIR="%{_sysconfdir}/php"
build_tree \
  $with_shared \
  --with-pear=%{_sharedstatedir}/php/pear
unset PEAR_CONFIG_SYSCONFDIR
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
mkdir -p "$RPM_BUILD_ROOT/%{_sysconfdir}/php"
cp php.ini-production "$RPM_BUILD_ROOT/%{_sysconfdir}/php/php.ini"
mv "$RPM_BUILD_ROOT/%{_sysconfdir}/pear.conf" "$RPM_BUILD_ROOT/%{_sysconfdir}/php/pear.conf"

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
cp "%{SOURCE2}" "$RPM_BUILD_ROOT/%{_sysconfdir}/php/php-fpm.conf"
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


%check
%if %{run_tests}
    for b in cgi embedded fpm httpd zts; do
        if [ "$b" = "embedded" ] || [ "%{with_$b}" = "1" ]; then
            pushd "build-$b"
            make test
            popd
        fi
    done
%endif


%clean
rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root, -)
                           %{_bindir}/php
                           %{_bindir}/php-cgi
                           %{_bindir}/php-config
                           %{_bindir}/phpize
                           %{_sysconfdir}/php/php.ini
                           %{_mandir}/man1/php.*
                           %{_mandir}/man1/php-cgi.*
                           %{_mandir}/man1/php-config.*
                           %{_mandir}/man1/phpize.*
%exclude                   /_list


%files bcmath
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/bcmath.*


%files bz2
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/bz2.*


%files curl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/curl.*


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
                           %{_sysconfdir}/php/php-fpm.conf
                           %{_mandir}/man8/php-fpm.*
%endif


%files ftp
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/ftp.*


%files gd
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/gd.*


%if %{with_httpd}
%files httpd
%defattr(-, root, root, -)
                           %{_libdir}/httpd/modules/mod_php5.so
%endif


%files intl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/intl.*


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


%files opcache
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/opcache.*


%files openssl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/openssl.*


%files pdo
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/pdo.*


%files pdo-mysql
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/pdo_mysql.*


%files pdo-sqlite
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/pdo_sqlite.*


%files pear -f "%{buildroot}/_list/pear"
%defattr(-, root, root, -)
                           %{_bindir}/pear
                           %{_bindir}/peardev
                           %{_bindir}/pecl
                           %{_sysconfdir}/php/pear.conf
                           %{_sharedstatedir}/php/pear



%files phar
%defattr(-, root, root, -)
                           %{_bindir}/phar
                           %{_bindir}/phar.phar
                           %{_mandir}/man1/phar.*


%files pgsql
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/pgsql.*


%files snmp
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/snmp.*


%files soap
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/soap.*


%files sqlite3
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/sqlite3.*


%files xmlrpc
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/xmlrpc.*


%files xsl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/xsl.*


%files zip
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/zip.*


%files zlib
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-non-zts-%{api_ver}/zlib.*


%if %{with_zts}
%files zts-bcmath
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/bcmath.*


%files zts-bz2
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/bz2.*


%files zts-curl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/curl.*


%files zts-ftp
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/ftp.*


%files zts-gd
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/gd.*


%files zts-intl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/intl.*


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


%files zts-opcache
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/opcache.*


%files zts-openssl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/openssl.*


%files zts-pdo
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/pdo.*


%files zts-pdo-mysql
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/pdo_mysql.*


%files zts-pdo-sqlite
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/pdo_sqlite.*


%files zts-xsl
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/xsl.*


%files zts-pgsql
%defattr(-, root, root, -)

                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/pgsql.*


%files zts-snmp
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/snmp.*


%files zts-soap
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/soap.*


%files zts-sqlite3
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/sqlite3.*


%files zts-xmlrpc
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/xmlrpc.*


%files zts-zip
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/zip.*


%files zts-zlib
%defattr(-, root, root, -)
                           %{_libdir}/php/extensions/no-debug-zts-%{api_ver}/zlib.*
%endif


%changelog

