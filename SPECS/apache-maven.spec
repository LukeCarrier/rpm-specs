Name:    apache-maven
Version: 3.2.1
Release: 1%{?dist}
Summary: Java build management tool

Group:     Development
License:   Apache Software License
URL:       http://maven.apache.org/
Source0:   http://www.mirrorservice.org/sites/ftp.apache.org/maven/maven-3/%{version}/binaries/apache-maven-%{version}-bin.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: dos2unix gzip tar

%description
Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information.


%prep
%setup -q
rm -f bin/*.bat

for winfile in conf/settings.xml bin/m2.conf lib/ext/README.txt; do
    dos2unix $winfile
    chmod a-x $winfile
done


%build


%install
mkdir -p "$RPM_BUILD_ROOT"%{_bindir} \
         "$RPM_BUILD_ROOT"/usr/share/java/maven

mv bin boot conf lib "$RPM_BUILD_ROOT"/usr/share/java/maven


for binary in mvn mvnDebug mvnyjp; do 
    %__ln_s /usr/share/java/maven/bin/$binary "$RPM_BUILD_ROOT"%{_bindir}
done

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-, root, root, -)
                           /usr/bin/mvn
                           /usr/bin/mvnDebug
                           /usr/bin/mvnyjp
                           /usr/share/java/maven


%changelog

