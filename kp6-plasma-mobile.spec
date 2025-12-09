#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeplasmaver	6.5.4
%define		qtver		6.6.0
%define		kpname		plasma-mobile
%define		kf6_ver		6.1.0

Summary:	Plasma Mobile components
Summary(pl.UTF-8):	Komponenty Plasma Mobile
Name:		kp6-%{kpname}
Version:	6.5.4
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	c4bfdd1c4eff9e43984b8b8d36b4ec2b
URL:		https://plasma-mobile.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Qml-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6Sensors-devel >= %{qtver}
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf6-extra-cmake-modules >= %{kf6_ver}
BuildRequires:	kf6-ki18n-devel >= %{kf6_ver}
BuildRequires:	kf6-kio-devel >= %{kf6_ver}
BuildRequires:	kf6-kirigami-addons-devel >= 0.11.90
BuildRequires:	kf6-knotifications-devel >= %{kf6_ver}
BuildRequires:	kf6-kservice-devel >= %{kf6_ver}
BuildRequires:	kf6-modemmanager-qt-devel >= %{kf6_ver}
BuildRequires:	kp6-kwayland-devel >= %{kdeplasmaver}
BuildRequires:	kp6-kwin-devel >= %{kdeplasmaver}
BuildRequires:	kp6-plasma-workspace-devel >= %{kdeplasmaver}
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qcoro-qt6-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
%requires_eq_to Qt6Core Qt6Core-devel
Obsoletes:	kp5-plasma-mobile < 6
Obsoletes:	kp6-plasma-phone-components < 5.24.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UI components for Plasma Phone.

%description -l pl.UTF-8
Komponenty interfejsu użytkownika Plasma Phone.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}

%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plasma-mobile-envmanager
%attr(755,root,root) %{_bindir}/plasma-mobile-initial-start
%attr(755,root,root) %{_bindir}/startplasmamobile
%{_libdir}/qt6/plugins/kf6/kded/kded_plasma_mobile_autodetect_apn.so
%{_libdir}/qt6/plugins/kf6/kded/kded_plasma_mobile_start.so
%dir %{_libdir}/qt6/plugins/plasma/applets
%{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.mobile.homescreen.folio.so
%{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.mobile.homescreen.halcyon.so
%{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.mobile.panel.so
%{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.mobile.taskpanel.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobile_info.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobile_onscreenkeyboard.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobile_time.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobileshell.so
%{_libdir}/qt6/qml/org/kde/plasma/mm
%{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_navigation.so
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_waydroidintegration.so
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/flashlighthelper
%attr(755,root,root) %{_prefix}/libexec/kf6/kauth/waydroidhelper
%{_desktopdir}/kcm_navigation.desktop
%{_desktopdir}/kcm_waydroidintegration.desktop
%{_datadir}/dbus-1/interfaces/org.kde.plasmashell.Mobile.xml
%{_datadir}/dbus-1/interfaces/org.kde.plasmashell.Waydroid.xml
%{_datadir}/dbus-1/interfaces/org.kde.plasmashell.WaydroidApplication.xml
%{_datadir}/dbus-1/system-services/org.kde.plasma.mobileshell.flashlighthelper.service
%{_datadir}/dbus-1/system-services/org.kde.plasma.mobileshell.waydroidhelper.service
%{_datadir}/dbus-1/system.d/org.kde.plasma.mobileshell.flashlighthelper.conf
%{_datadir}/dbus-1/system.d/org.kde.plasma.mobileshell.waydroidhelper.conf
%{_datadir}/knotifications6/plasma_mobile_quicksetting_record.notifyrc
%{_datadir}/knotifications6/plasma_mobile_quicksetting_screenshot.notifyrc
%{_datadir}/kwin/effects/mobiletaskswitcher
%{_datadir}/kwin/scripts/convergentwindows
%{_datadir}/plasma/quicksettings
%{_datadir}/metainfo/org.kde.breeze.mobile.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.defaultNavigationPanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.defaultStatusBar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.cellular.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.finished.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.prepare.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.systemnavigation.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.time.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.wifi.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileshell.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.airplanemode.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.audio.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.autohidepanels.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.battery.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.bluetooth.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.caffeine.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.docked.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.donotdisturb.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.flashlight.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.hotspot.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.keyboardtoggle.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.kscreenosd.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.mobiledata.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.nightcolor.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.powermenu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.record.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenrotation.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenshot.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.settingsapp.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.waydroid.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.wifi.appdata.xml
%{_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultNavigationPanel
%{_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultStatusBar
%{_datadir}/plasma/look-and-feel/org.kde.breeze.mobile
%{_datadir}/plasma/mobileinitialstart
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell
%{_datadir}/plasma-mobile-apn-info
%{_datadir}/wayland-sessions/plasma-mobile.desktop
%{_desktopdir}/kcm_mobile_info.desktop
%{_desktopdir}/kcm_mobile_onscreenkeyboard.desktop
%{_desktopdir}/kcm_mobile_time.desktop
%{_desktopdir}/kcm_mobileshell.desktop
%{_datadir}/polkit-1/actions/org.kde.plasma.mobileshell.flashlighthelper.policy
%{_datadir}/polkit-1/actions/org.kde.plasma.mobileshell.waydroidhelper.policy
