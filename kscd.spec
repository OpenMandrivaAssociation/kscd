Name:		kscd
Summary:	KDE Audio CD Player
Version: 4.9.0
Release: 1
Epoch:		3
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org/applications/multimedia/kscd
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	libkcddb-devel
BuildRequires:	libkcompactdisc-devel
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
%{_kde_iconsdir}/*/*/*/kscd-dock.*
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

