Name:    libechonest
Version: 2.2.0
Release: 2%{?dist}
Summary: C++ wrapper for the Echo Nest API

License: GPLv2+
URL:     https://projects.kde.org/projects/playground/libs/libechonest
Source0: https://github.com/lfranchi/libechonest/archive/%{version}.zip

BuildRequires: cmake
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(QtNetwork)


%description
libechonest is a collection of C++/Qt classes designed to make a developer's
life easy when trying to use the APIs provided by The Echo Nest.


%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libechonest)" = "%{version}"
# TODO: identify cause of indefinite hang
#make test -C %{_target_platform}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING README TODO
     %{_libdir}/libechonest.so.2.2*


%files devel
%{_includedir}/echonest/
%{_libdir}/libechonest.so
%{_libdir}/pkgconfig/libechonest.pc

%changelog

