Name:		kscd
Summary:	KDE Audio CD Player
Version:	4.10.1
Release:	1
Epoch:		3
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org/applications/multimedia/kscd
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libmusicbrainz3)
Requires:	kdebase4-runtime
Conflicts:	kdemultimedia4-core < 3:4.5.71
Conflicts:	kdemultimedia4-devel < 3:4.8.95
Suggests:	gstreamer0.10-cdparanoia

%description
KsCD is a small, fast, CDDB enabled audio CD player which supports
multiple platforms.

%files
%{_kde_bindir}/kscd
%{_kde_applicationsdir}/kscd.desktop
%{_kde_datadir}/config.kcfg/kscd.kcfg
%{_kde_appsdir}/kscd
%{_kde_iconsdir}/*/*/apps/kscd.*
%{_kde_appsdir}/solid/actions/kscd-play-audiocd.desktop
%{_datadir}/dbus-1/interfaces/org.kde.kscd.cdplayer.xml

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.1-1
- New version 4.10.1
- Update files
- Drop no longer needed BuildRequires libkcddb-devel and libkcompactdisc-devel

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.1-1
- New version 4.9.1

* Tue Aug 14 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.9.0-1
- New version 4.9.0

* Sun Jul 22 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.97-1
- New version 4.8.97

* Wed Jul 11 2012 Andrey Bondrov <abondrov@mandriva.org> 3:4.8.95-1
+ Revision: 808895
- imported package kscd

* Tue Jul 10 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.8.95-1
- Follow upstream and move kscd from kdemultimedia4 to own package
