%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	KDE Audio CD Player
Name:		kscd
Version:	18.08.20180907
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/multimedia/kscd
# git://anongit.kde.org/kscd.git -- taken from kf5 branch
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kscd-4.12.1-fix-multiple-CD-device.patch
BuildRequires:	cmake cmake(ECM) ninja
BuildRequires:	pkgconfig(libdiscid)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(Qt5Test)

%description
KsCD is a small, fast, CDDB enabled audio CD player which supports
multiple platforms.

%files
%{_bindir}/kscd
%{_datadir}/applications/org.kde.kscd.desktop
%{_datadir}/config.kcfg/kscd.kcfg
%{_iconsdir}/*/*/apps/kscd.*
%{_datadir}/dbus-1/interfaces/org.kde.kscd.cdplayer.xml
%{_datadir}/kscd
%{_datadir}/solid/actions/kscd-play-audiocd.desktop

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

