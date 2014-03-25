Name:    ncftp
Version: 3.2.5
Release: 1%{?dist}
Summary: powerful command line FTP client

Group:     Applications/Internet
License:   Clarified Artistic License
URL:       http://ncftp.com
Source:    ftp://ftp.ncftp.com/ncftp/ncftp-%{version}-src.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: gcc, make, ncurses-devel, openssl-devel
Requires:                 ncurses,       openssl

%description
The third major version of the popular free FTP client adds support for firewalls, intelligent ls caching, background and scheduled processing, Microsoft Windows, and more.


%prep
%setup -q


%build
./configure \
  --prefix=/usr
make %{?_smp_mflags}


%install
make install DESTDIR="$RPM_BUILD_ROOT"


%clean
rm -rf "$RPM_BUILD_ROOT"


%files
%defattr(-, root, root, -)
     /usr/bin/ncftp*
%doc /usr/share/man


%changelog

