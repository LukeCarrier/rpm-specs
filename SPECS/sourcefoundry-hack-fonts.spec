%global hack_major  2
%global hack_minor  010

Name:    sourcefoundry-hack-fonts
Summary: A typeface designed for source code
Version: %{hack_major}.%{hack_minor}
Release: 1%{?dist}

Group:   User Interface/X
License: Modified SIL Open Font License
URL:     http://sourcefoundry.org/hack/

BuildArch: noarch

BuildRequires: unzip

Source0: https://github.com/chrissimpkins/Hack/releases/download/v%{version}/Hack-v%{hack_major}_%{hack_minor}-ttf.zip

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
No frills. No gimmicks. Hack is hand groomed and optically balanced to be a
workhorse face for code.

It has deep roots in the libre, open source typeface community and expands upon
the contributions of the Bitstream Vera & DejaVu projects. The face has been
re-designed with a larger glyph set, modifications of the original glyph shapes
(including distinct point styles and semi-bold punctuation weight in the
regular set to make analphabetic characters less transparent), and meticulous
attention to metrics (including numerous spacing adjustments to improve the
rhythm of the face and the legibility of code at small text sizes). The large
x-height + wide aperture + low contrast design combined with PostScript
hinting/hint replacement programs and a TrueType instruction set make it highly
legible at commonly used source code text sizes with a sweet spot that runs in
the 8px - 12px range on modern desktop and laptop monitors. Combine it with an
HD monitor and you can comfortably work at 6 or 7px sizes. The full set of
changes are available in the changelog.


%prep


%build


%install
mkdir -p "$RPM_BUILD_ROOT"%{_datarootdir}/fonts/sourcefoundry-hack
pushd "$RPM_BUILD_ROOT"%{_datarootdir}/fonts/sourcefoundry-hack
unzip %{SOURCE0}
popd


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, -)
                           %{_datarootdir}/fonts/sourcefoundry-hack
