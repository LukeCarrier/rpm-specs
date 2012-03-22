Name:    powerdns-authoritative	
Version: 3.0.1
Release: 1%{?dist}
Summary: The complete high-performance resolving solution.

Group:     Applications/Internet
License:   I don't bloody know
URL:       http://powerdns.com/
Source0:   http://downloads.powerdns.com/releases/pdns-%{version}.tar.gz
Source1:   http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/powerdns-authoritative-sysvinit.sh
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: boost-devel gcc gcc-c++ lua-devel make mysql-devel
Requires:      lua

%global user pdns

%description
The PowerDNS Recursive Server is the only resolving solution that offers:
 
    * Maximum data integrity
    * Consistent sustained performance of over 100000 queries/second
    * Rich monitoring of interactive performance


%prep
%setup -q -n pdns-%{version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mv "$RPM_BUILD_ROOT/%{_sysconfdir}/pdns.conf-dist" "$RPM_BUILD_ROOT/%{_sysconfdir}/pdns.conf"
mkdir -p "$RPM_BUILD_ROOT/%{_sysconfdir}/init.d"
cp "%{SOURCE1}" "$RPM_BUILD_ROOT/%{_sysconfdir}/init.d/pdns"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root, -)
                           %{_bindir}
                           %{_sbindir}
                           %{_libdir}
                           %{_sysconfdir}
%doc
                           %{_mandir}


%post
useradd -c 'PowerDNS server' -d '/var/lib/pdns' -mr '%{user}'


%postun
userdel '%{user}'


%changelog

