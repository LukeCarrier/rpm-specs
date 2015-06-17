%global selenium_series 2
%global selenium_major  46
%global selenium_minor  0

Name:    selenium-server
Summary: Selenium Server integration testing tool
Version: %{selenium_series}.%{selenium_major}.%{selenium_minor}
Release: 1%{?dist}

Group:   Development/Testing
License: Apache License v2.0
URL:     http://www.seleniumhq.org/

Requires: xorg-x11-server-Xvfb

Source0: http://selenium-release.storage.googleapis.com/%{selenium_series}.%{selenium_major}/selenium-server-standalone-%{version}.jar
Source1: http://github.com/LukeCarrier/rpm-specs/raw/master/SUPPORT/selenium-server
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
    The Selenium Server is needed in order to run either Selenium RC style
    scripts or Remote Selenium Webdriver ones. The 2.x server is a drop-in
    replacement for the old Selenium RC server and is designed to be backwards
    compatible with your existing infrastructure.


%prep


%build


%install
mkdir -p \
    "$RPM_BUILD_ROOT"/%{_bindir} \
    "$RPM_BUILD_ROOT"/%{_datarootdir}/java

cp %{SOURCE0} "$RPM_BUILD_ROOT"/%{_datarootdir}/java/selenium-server.jar
cp %{SOURCE1} "$RPM_BUILD_ROOT"/%{_bindir}/selenium-server

%clean
rm -rf %{buildroot}


%files
%defattr(755, root, root, -)
                             %{_bindir}/selenium-server
%defattr(-,   root, root, -)
                             %{_datarootdir}/java/selenium-server.jar
