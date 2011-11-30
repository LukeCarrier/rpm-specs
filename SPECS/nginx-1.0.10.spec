Name:    nginx
Version: 1.0.10
Release: 1%{?dist}
Summary: lightweight web and reverse proxy server

Group:     Applications/Internet
License:   BSD (two-clause)
URL:       http://nginx.org
Source0:   http://nginx.org/download/nginx-%{version}.tar.gz
Source1:   http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/nginx-sysvinit.sh
Source2:   http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/nginx-phpfpmvhostenable.conf
Source3:   http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/nginx-fastcgicore.conf
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: gcc, make, openssl-devel, pcre-devel, sed, zlib-devel
Requires:                 openssl,       pcre,            zlib

%description
nginx [engine x] is a HTTP and reverse proxy server, as well as a mail proxy server written by Igor Sysoev. It has been running since 2004 on many heavily loaded Russian sites including Yandex, Mail.Ru, VKontakte, and Rambler. According to Netcraft nginx served or proxied 7.29% busiest sites in September 2011.


%package php-fpm
Summary: nginx - php-fpm per-virtualhost configuration files
Requires: nginx


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
  --user=nginx \
  --group=nginx \
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

# Remove default configuration files
#   RPM handles versioning, so we don't need to keep the million and one
#   *.default configuration files generated by Make. We'll handle creating
#   replacement configuration when a backwards incompatible change is released
#   upstream and move all affected files to *.rpmsaves.
etc="$RPM_BUILD_ROOT/%{_sysconfdir}/nginx"
rm -f \
  "$etc/fastcgi.conf" \
  "$etc/fastcgi.conf.default" \
  "$etc/fastcgi_params.default" \
  "$etc/mime.types.default" \
  "$etc/nginx.conf.default" \
  "$etc/scgi_params.default" \
  "$etc/uwsgi_params.default"

# Additional configuration files
cp "%{SOURCE2}" "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx/enable_php"
cp "%{SOURCE3}" "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx/fastcgi_core"

# Move the document root /var/www/html
#   If the directory seems a bit random, check the (Apache) httpd packages
#   shipped by Red Hat; we're only being consistent.
mkdir -p "$RPM_BUILD_ROOT/%{_localstatedir}/www"
mv "$RPM_BUILD_ROOT/usr/html" "$RPM_BUILD_ROOT/%{_localstatedir}/www/html"
sed -i 's%root   html%root   /%{_localstatedir}/www/html%' "$RPM_BUILD_ROOT/%{_sysconfdir}/nginx/nginx.conf"


# Create the nginx user's home directory
mkdir -p "$RPM_BUILD_ROOT/%{_sharedstatedir}/nginx"

%clean
rm -rf "$RPM_BUILD_ROOT"


%post
# Create the nginx user
useradd \
    --comment "nginx web server" \
    --home /var/lib/nginx \
    --system \
    -M \
    nginx
    # The home directory is created in the %files section!


%postun
# What goes up must come down and all that...
userdel nginx


%files
%defattr(-, root, root, -)
                   %{_sbindir}/nginx
%attr(755, -, -)   %{_initddir}/nginx
%config(noreplace) %{_sysconfdir}/nginx
%exclude           %{_sysconfdir}/nginx/enable_php
%dir               %{_sharedstatedir}/nginx
%dir               %{_localstatedir}/log/nginx
%config(noreplace) %{_localstatedir}/www/html


%files php-fpm
%defattr(-, root, root, -)
%config(noreplace) %{_sysconfdir}/nginx/enable_php

%changelog

