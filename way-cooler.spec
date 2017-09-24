Name:           way-cooler
Version:        0.6.2
Release:        1%{?dist}
Summary:        Customizable Wayland compositor (window manager) 

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
Requires:       wlc
Recommends:     way-cooler-bg

%description
Way Cooler is a customizable tiling window manager written in Rust for Wayland 
and configurable using Lua. It is heavily inspired by the tiling of i3 and the 
extensibility of awesome.

%prep
%autosetup -n %{name}-%{version}

%build
%cargo_build

%install
%cargo_install
mkdir -p %{buildroot}/%{_datadir}/wayland-sessions
cp -p %{name}.desktop %{buildroot}/%{_datadir}/wayland-sessions
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
cp -p config/init.lua %{buildroot}/%{_sysconfdir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/wayland-sessions/%{name}.desktop
%config(noreplace) %{_sysconfdir}/%{name}/init.lua

%doc README.md
%license LICENSE

%changelog
* Thu Sep 21 2017 Hendrik Schröter <hendrik.m.schroeter@fau.de> 0.6.2-1
- Initial version of the package
