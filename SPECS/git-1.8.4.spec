Name:    git
Version: 1.8.4
Release: 1%{?dist}
Summary: the stupid content manager

Group:     Development
License:   GNU GPL v2
URL:       http://git-scm.com/
Source0:   https://codeload.github.com/git/git/tar.gz/v%{version}
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: asciidoc gettext make perl-ExtUtils-MakeMaker xmlto

%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations
and full access to internals.


%prep
%setup -q


%build
make configure
./configure --prefix=/usr
make %{?_smp_mflags} all doc


%install
rm -rf "$RPM_BUILD_ROOT"
make install install-doc install-html DESTDIR="$RPM_BUILD_ROOT"

%files
%defattr(-, root, root, -)
                           %{_bindir}/*
                           /usr/lib/python2.6/site-packages/git_remote_helpers*
                           /usr/lib64/perl5
                           %{_libexecdir}/git-core
%doc                       %{_defaultdocdir}/git
                           %{_mandir}
                           %{_datadir}

%changelog

