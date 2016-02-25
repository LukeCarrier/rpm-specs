%global selenium_series 2
%global selenium_major  52
%global selenium_minor  0

Name:    selenium-server
Summary: Selenium Server integration testing tool
Version: %{selenium_series}.%{selenium_major}.%{selenium_minor}
Release: 1%{?dist}

Group:   Development/Testing
License: Apache License v2.0
URL:     http://www.seleniumhq.org/

Requires:      xorg-x11-server-Xvfb
BuildRequires: unzip

Source0: http://selenium-release.storage.googleapis.com/%{selenium_series}.%{selenium_major}/selenium-server-standalone-%{version}.jar
Source1: http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/selenium-server
Source2: http://chromedriver.storage.googleapis.com/2.16/chromedriver_linux32.zip
Source3: http://chromedriver.storage.googleapis.com/2.16/chromedriver_linux64.zip

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
    The Selenium Server is needed in order to run either Selenium RC style
    scripts or Remote Selenium Webdriver ones. The 2.x server is a drop-in
    replacement for the old Selenium RC server and is designed to be backwards
    compatible with your existing infrastructure.


%prep
if [ ! -d %{_builddir}/selenium-server-%{release} ]; then
    mkdir -p %{_builddir}/selenium-server-%{release}/32 \
             %{_builddir}/selenium-server-%{release}/64
    unzip -d %{_builddir}/selenium-server-%{release}/32 %{SOURCE2}
    unzip -d %{_builddir}/selenium-server-%{release}/64 %{SOURCE3}
fi


%build


%install
mkdir -p \
    "$RPM_BUILD_ROOT"/%{_bindir} \
    "$RPM_BUILD_ROOT"/%{_datarootdir}/java \
    "$RPM_BUILD_ROOT"/%{_libexecdir}/selenium-server

cp %{SOURCE0} "$RPM_BUILD_ROOT"/%{_datarootdir}/java/selenium-server.jar
cp %{SOURCE1} "$RPM_BUILD_ROOT"/%{_bindir}/selenium-server

%ifarch ix86
    mv %{_builddir}/selenium-server-%{release}/32/* \
        "$RPM_BUILD_ROOT"/%{_libexecdir}/selenium-server
%endif

%ifarch amd64 x86_64
    mv %{_builddir}/selenium-server-%{release}/64/* \
        "$RPM_BUILD_ROOT"/%{_libexecdir}/selenium-server
%endif


%clean
rm -rf %{buildroot}


%files
%defattr(755, root, root, -)
                             %{_bindir}/selenium-server
                             %{_libexecdir}/selenium-server
%defattr(-,   root, root, -)
                             %{_datarootdir}/java/selenium-server.jar
