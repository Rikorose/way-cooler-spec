%global executable wc-grab

Name:           way-cooler-grab
Version:        0.2.0
Release:        1%{?dist}
Summary:        A screenshot taker for Way Cooler

License:        MIT
URL:            https://github.com/way-cooler/%{name}
Source0:        https://github.com/way-cooler/%{name}/archive/v%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  dbus
BuildRequires:  dbus-devel
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  rust-packaging
BuildRequires:  pam-devel
Requires:       wlc
Requires:       dbus
Supplements:    way-cooler

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}

%build
%cargo_build

%install
%cargo_install

%files
%{_bindir}/%{executable}

%license LICENSE

%changelog
* Thu Sep 21 2017 Hendrik Schröter <hendrik.m.schroeter@fau.de> 0.2.0-1
- Initial version of the package
