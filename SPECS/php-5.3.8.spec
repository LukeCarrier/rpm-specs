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
# Generate a file list
#   Does magic on a directory to produce a file list with fake absolute names.
#   This seems disgusting, but yey RPM!
#   $1 | directory path
#   $2 | filename regex
#   $3 | file list name
generate_file_list() {
    find "$RPM_BUILD_ROOT/$1" -type f -regex "$2" | sed "s:^$RPM_BUILD_ROOT/:/:" | sort | uniq > _list/$3
}

rm -rf "$RPM_BUILD_ROOT"

# CGI build
make -C build-cgi install INSTALL_ROOT=$RPM_BUILD_ROOT

# The build directories are no longer necessary
cd "$RPM_BUILD_ROOT"

# Reorganise PEAR files
rm -rfv .channels/ .depdb .depdblock .filemap .lock
for file in INSTALL LICENSE README
do
    mv "$RPM_BUILD_ROOT/%{_libdir}/php/doc/PEAR/$file" \
      "$RPM_BUILD_ROOT/%{_libdir}/php/doc/PEAR_$file"
done
mv "$RPM_BUILD_ROOT/%{_libdir}/php/data/Structures_Graph/LICENSE" \
  "$RPM_BUILD_ROOT/%{_libdir}/php/doc/STRUCTURES_GRAPH_README"

# The build directory seems to lose its way, too
[ ! -d "$RPM_BUILD_ROOT/%{_libdir}/php" ] && mkdir "$RPM_BUILD_ROOT/%{_libdir}/php"
mv "$RPM_BUILD_ROOT/%{_libdir}/build" "$RPM_BUILD_ROOT/%{_libdir}/php/build"

# Build file lists
mkdir _list
generate_file_list "/usr/lib64/php" ".*\.\(css\|depdb\|depdblock\|dtd\|filemap\|html\|lock\|php\|phpt\|pkg\|reg\|sh\|spec\|txt\|xml\)" pear


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

