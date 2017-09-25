%global executable wc-lock

Name:           way-cooler-lock
Version:        0.1.0
Release:        1%{?dist}
Summary:        Lock screen for Way Cooler

License:        MIT
URL:            https://github.com/way-cooler/%{name}
Source0:        https://github.com/way-cooler/%{name}/archive/v%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  rust-packaging
BuildRequires:  pam-devel
Requires:       wlc
Requires:       pam
Supplements:    way-cooler
Supplements:    way-cooler-bg

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}

%build
%cargo_build

%install
%cargo_install
cd %{_builddir}/%{name}-%{version}
mkdir -p %{buildroot}/%{_sysconfdir}/pam.d
cp -p pam/wc-lock %{buildroot}/%{_sysconfdir}/pam.d

%files
%attr(644, -, -) %config(noreplace) %{_sysconfdir}/pam.d/wc-lock
%{_bindir}/%{executable}

%doc README.md
%license LICENSE

%changelog
* Thu Sep 21 2017 Hendrik Schröter <hendrik.m.schroeter@fau.de> 0.1.0-1
- Initial version of the package
