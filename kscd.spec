%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Summary:	KDE Audio CD Player
Name:		kscd
Version:	17.04.0
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/multimedia/kscd
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kscd-4.12.1-fix-multiple-CD-device.patch
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(libmusicbrainz3)
Requires:	kdebase4-runtime
Conflicts:	kdemultimedia4-core < 3:4.5.71
Conflicts:	kdemultimedia4-devel < 3:4.8.95
Suggests:	gstreamer0.10-cdparanoia

%description
KsCD is a small, fast, CDDB enabled audio CD player which supports
multiple platforms.

%files
%{_bindir}/kscd                                                                                        
%{_datadir}/applications/kde4/kscd.desktop                                                             
%{_datadir}/config.kcfg/kscd.kcfg                                                                      
%{_datadir}/apps/kscd                                                                                  
%{_iconsdir}/*/*/apps/kscd.*                                                                           
%{_datadir}/apps/solid/actions/kscd-play-audiocd.desktop                                               
%{_datadir}/dbus-1/interfaces/org.kde.kscd.cdplayer.xml 

#------------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

