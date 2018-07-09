%global gitcommit 8b243e38737fdd0f1e2d5f67445b8980e11d854c
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})

Name: kdump-anaconda-addon
Version: 005
Release: 1.git%{gitshortcommit}%{?dist}

License: GPLv2
Group: Applications/System
Summary: Kdump configuration anaconda addon

BuildArch: noarch
Requires: anaconda >= 21.33
BuildRequires: intltool gettext
Obsoletes: kdump-anaconda-addon <= 2.0.17-3

Source0: https://github.com/daveyoung/kdump-anaconda-addon/archive/%{gitcommit}/kdump-anaconda-addon-%{gitshortcommit}.tar.gz

%description
Kdump anaconda addon

%prep
%autosetup -n %{name}-%{gitcommit}

%build

%install
DESTDIR=%{buildroot} make install

%find_lang kdump-anaconda-addon

%files -f kdump-anaconda-addon.lang
%{_datadir}/anaconda/addons/com_redhat_kdump
%{_datadir}/icons/hicolor/scalable/apps/kdump.svg

%changelog
* Mon Jul 9 2018 Kairui Song <kasong@redhat.com>
- Initial package for kdump-anaconda-addon
