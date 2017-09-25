Name:           way-cooler-bg
Version:        0.2.1
Release:        2%{?dist}
Summary:        The program that draws a background for Way Cooler

License:        MIT
URL:            https://github.com/way-cooler/%{name}
Source0:        https://github.com/way-cooler/%{name}/archive/v%{version}.tar.gz

ExclusiveArch:  %{rust_arches}

BuildRequires:  dbus
BuildRequires:  dbus-devel
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  rust-packaging
Requires:       dbus
Requires:       atk
Requires:       pango
Requires:       gdk-pixbuf2
Requires:       gtk3
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
%{_bindir}/%{name}

%doc README.md

%changelog
* Thu Sep 21 2017 Hendrik Schröter <hendrik.m.schroeter@fau.de> 0.2.1-2
- Initial version of the package
