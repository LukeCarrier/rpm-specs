Name:    nginx
Version: 1.2.3
Release: 1%{?dist}
Summary: lightweight web and reverse proxy server

Group:     Applications/Internet
License:   BSD (two-clause)
URL:       http://nginx.org
Source0:   http://nginx.org/download/nginx-%{version}.tar.gz
Source1:   http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/nginx-sysvinit.sh
Source2:   http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/nginx-phpfpmvhostenable.conf
Source3:   http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/nginx-fastcgicore.conf
Source4:   http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/nginx-fastcgiparams.conf
Source5:   http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/nginx-nginx.conf
Source6:   http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/nginx-sitesdefault.conf
Source7:   http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/nginx-mimetypes.conf
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: gcc, make, openssl-devel, pcre-devel, sed, zlib-devel
Requires:                 openssl,       pcre,            zlib

%description
nginx [engine x] is a HTTP and reverse proxy server, as well as a mail proxy server written by Igor Sysoev. It has been running since 2004 on many heavily loaded Russian sites including Yandex, Mail.Ru, VKontakte, and Rambler. According to Netcraft nginx served or proxied 7.29% busiest sites in September 2011.


%package php-fpm
Summary:  nginx - php-fpm per-virtualhost configuration files
Requires: nginx
Group:    Applications/Internet


%description php-fpm
nginx [engine x] is a HTTP and reverse proxy server, as well as a mail proxy server written by Igor Sysoev. It has been running since 2004 on many heavily loaded Russian sites including Yandex, Mail.Ru, VKontakte, and Rambler. According to Netcraft nginx served or proxied 7.29% busiest sites in September 2011. This package provides extended configuration to enable the pre-hypertext processor (PHP) to serve dynamic web applications when requested via nginx.


%prep
%setup -q


%build
./configure \
  --with-cc-opt="-w" \
  --prefix=/usr \
  --conf-path=%{_sysconfdir}/nginx/nginx.conf \
  --error-log-path=%{_localstatedir}/log/nginx/error.log \
  --http-log-path=%{_localstatedir}/log/nginx/access.log \
  --lock-path=%{_localstatedir}/lock/nginx.lock \
  --pid-path=%{_localstatedir}/run/nginx.pid \
  --sbin-path=%{_sbindir}/nginx \
  --user=www-server \
  --group=www-server \
  --with-ipv6 \
  --with-http_ssl_module \
  --with-http_stub_status_module
make %{?_smp_mflags}


%install
rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR="$RPM_BUILD_ROOT"

# Move our init script here
#   nginx doesn't ship one, so it's in the repository.
mkdir -p "$RPM_BUILD_ROOT/%{_initddir}"
cp "%{SOURCE1}" "$RPM_BUILD_ROOT/%{_initddir}/nginx"

# Replace default configuration with our own
rm -rf "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx"
mkdir "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx"
cp "%{SOURCE2}" "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx/enable_php"
cp "%{SOURCE3}" "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx/fastcgi_core"
cp "%{SOURCE4}" "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx/fastcgi_params"
cp "%{SOURCE5}" "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx/nginx.conf"
cp "%{SOURCE7}" "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx/mime_types"
mkdir -p "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx/sites"
cp "%{SOURCE6}" "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx/sites/_default_"

mkdir -p "$RPM_BUILD_ROOT/%{_localstatedir}/www/sites"
mv "$RPM_BUILD_ROOT/usr/html" "$RPM_BUILD_ROOT/%{_localstatedir}/www/sites/_default_"

# Create the www-server user's home directory
mkdir -p "$RPM_BUILD_ROOT/%{_sharedstatedir}/www-server"


%clean
rm -rf "$RPM_BUILD_ROOT"


%post
# Create the nginx user
useradd \
    --comment "System web server" \
    --home "%{_sharedstatedir}/www-server" \
    -r \
    -M \
    www-server


%postun
# What goes up must come down and all that...
userdel www-server


%files
%defattr(-, root, root, -)
                   %{_sbindir}/nginx
%attr(755, -, -)   %{_initddir}/nginx
%config(noreplace) %{_sysconfdir}/nginx
%exclude           %{_sysconfdir}/nginx/enable_php
%dir               %{_sharedstatedir}/www-server
%dir               %{_localstatedir}/log/nginx
%config(noreplace) %{_localstatedir}/www/sites


%files php-fpm
%defattr(-, root, root, -)
%config(noreplace) %{_sysconfdir}/nginx/enable_php


%changelog

