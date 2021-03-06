%global gitcommit 8b243e38737fdd0f1e2d5f67445b8980e11d854c
%global gitshortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global snapshotdate 20180626

Name: kdump-anaconda-addon
Version: 005
Release: 1.%{snapshotdate}git%{gitshortcommit}%{?dist}
Url: https://github.com/daveyoung/kdump-anaconda-addon
License: GPLv2
Summary: Kdump configuration anaconda addon

BuildArch: noarch
Requires: anaconda >= 21.33
Requires: hicolor-icon-theme
BuildRequires: intltool gettext
Obsoletes: kexec-tools-anaconda-addon <= 2.0.17-5
Provides: kexec-tools-anaconda-addon = %{version}-%{release}

Source0: https://github.com/daveyoung/kdump-anaconda-addon/archive/%{gitcommit}/kdump-anaconda-addon-%{gitshortcommit}.tar.gz

%description
Kdump anaconda addon

%prep
%autosetup -n %{name}-%{gitcommit}

%build

%install
%make_install

%find_lang kdump-anaconda-addon

%files -f kdump-anaconda-addon.lang
%doc README
%license LICENSE
%{_datadir}/anaconda/addons/com_redhat_kdump
%{_datadir}/icons/hicolor/scalable/apps/kdump.svg

%changelog
* Mon Jul 9 2018 Kairui Song <kasong@redhat.com> - 005-1.20180626git8b243e3
- Initial package for kdump-anaconda-addon
