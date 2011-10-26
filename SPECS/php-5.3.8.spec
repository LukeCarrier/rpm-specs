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


%description
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This package contains its command line interface binaries.


%package devel
Summary: hypertext preprocessor: development headers


%description devel
PHP is a widely-used general-purpose scripting language that is especially suited for Web development and can be embedded into HTML. This package contains development header files which may be necessary for applications that require the Zend Engine.


%prep
%setup -q


%build
# There's probably a macro that does this for you...
./configure \
  --prefix=/usr \
  --bindir=%{_bindir} \
  --datadir=%{_datadir} \
  --includedir=%{_includedir} \
  --infodir=%{_infodir} \
  --libdir=%{_libdir}/php \
  --libexecdir=%{_libexecdir} \
  --localstatedir=%{_localstatedir} \
  --mandir=%{_mandir} \
  --oldincludedir=%{_includedir} \
  --sbindir=%{_sbindir} \
  --sharedstatedir=%{_sharedstatedir} \
  --sysconfdir=%{_sysconfdir} \
  --disable-all
make %{?_smp_mflags}


%install
rm -rf "$RPM_BUILD_ROOT"
make install INSTALL_ROOT="$RPM_BUILD_ROOT"


%clean
rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root, -)
                   %{_bindir}/php
                   %{_bindir}/php-cgi
                   %{_bindir}/php-config
                   %{_bindir}/phpize
                   %{_libdir}/php/build
                   %{_mandir}/man1


%files devel
%defattr(-, root, root, -)
                   %{_includedir}/php

%changelog

