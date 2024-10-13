#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeplasmaver	6.2.0
%define		qtver		6.6.0
%define		kpname		plasma-mobile
%define		kf6_ver		6.1.0

Summary:	Plasma Mobile components
Summary(pl.UTF-8):	Komponenty Plasma Mobile
Name:		kp6-%{kpname}
Version:	6.2.0
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	3c9bec6261444ddaec3f98da448a7414
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
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qcoro-qt6-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	xz
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

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plasma-mobile-envmanager
%attr(755,root,root) %{_bindir}/plasma-mobile-initial-start
%attr(755,root,root) %{_bindir}/startplasmamobile
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/kded_plasma_mobile_autodetect_apn.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/kded_plasma_mobile_start.so
%dir %{_libdir}/qt6/plugins/kwin/effects/plugins
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/plugins/mobiletaskswitcher.so
%dir %{_libdir}/qt6/plugins/plasma/applets
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.mobile.homescreen.folio.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.mobile.homescreen.halcyon.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.mobile.panel.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/applets/org.kde.plasma.mobile.taskpanel.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_cellular_network.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobile_hotspot.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobile_info.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobile_onscreenkeyboard.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobile_power.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobile_time.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobile_wifi.so
%attr(755,root,root) %{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobileshell.so
%dir %{_libdir}/qt6/qml/org/kde/plasma/mm
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/mm/libppc-mmqmlplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/mm/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/mm/ppc-mmqmlplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/mm/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart
%dir %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/cellular
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/cellular/libcellularplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/cellular/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/prepare
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/prepare/libprepareplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/prepare/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/time
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/time/libtimeplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/time/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/wifi
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/wifi/libwifiplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/wifi/qmldir
%dir %{_libdir}/qt6/qml/org/kde/private/mobile
%dir %{_libdir}/qt6/qml/org/kde/private/mobile/homescreen
%dir %{_libdir}/qt6/qml/org/kde/private/mobile/homescreen/halcyon
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/private/mobile/homescreen/halcyon/libhalcyonplugin.so
%{_libdir}/qt6/qml/org/kde/private/mobile/homescreen/halcyon/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/libmobileshellplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/*.js
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/*.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/mobileshellplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/hapticsplugin
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/hapticsplugin/libhapticsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/hapticsplugin/hapticsplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/hapticsplugin/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/hapticsplugin/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/quicksettingsplugin
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/quicksettingsplugin/libquicksettingsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/quicksettingsplugin/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/quicksettingsplugin/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/quicksettingsplugin/quicksettingsplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/shellsettingsplugin
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/shellsettingsplugin/libshellsettingsplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/shellsettingsplugin/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/shellsettingsplugin/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/shellsettingsplugin/shellsettingsplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/state
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/state/libmobileshellstateplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/state/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/state/mobileshellstateplugin.qmltypes
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/state/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/wallpaperimageplugin
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/wallpaperimageplugin/libwallpaperimageplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/wallpaperimageplugin/*.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/wallpaperimageplugin/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/wallpaperimageplugin/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/wallpaperimageplugin/wallpaperimageplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/windowplugin
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/windowplugin/libwindowplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/windowplugin/*.qml
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/windowplugin/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/windowplugin/qmldir
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell/windowplugin/windowplugin.qmltypes
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/flashlight
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/flashlight/libflashlightplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/flashlight/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/nightcolor
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/nightcolor/libnightcolorplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/nightcolor/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/powermenu
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/powermenu/libpowermenuplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/powermenu/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/record
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/record/librecordplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/record/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenrotation
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenrotation/libscreenrotationplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenrotation/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenshot
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenshot/libscreenshotplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenshot/qmldir
%{_datadir}/dbus-1/interfaces/org.kde.plasmashell.Mobile.xml
%{_datadir}/knotifications6/plasma_mobile_quicksetting_record.notifyrc
%{_datadir}/knotifications6/plasma_mobile_quicksetting_screenshot.notifyrc
%{_datadir}/kwin/effects/mobiletaskswitcher
%{_datadir}/kwin/scripts/convergentwindows
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi
%{_datadir}/metainfo/org.kde.breeze.mobile.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.defaultNavigationPanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.defaultStatusBar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.homescreen.folio.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.homescreen.halcyon.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.panel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.taskpanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.cellular.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.finished.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.prepare.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.time.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileinitialstart.wifi.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobileshell.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.airplanemode.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.audio.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.battery.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.bluetooth.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.caffeine.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.donotdisturb.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.flashlight.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.hotspot.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.keyboardtoggle.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.mobiledata.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.nightcolor.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.powermenu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.record.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenrotation.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenshot.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.settingsapp.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.wifi.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksettings.docked.appdata.xml
%{_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultNavigationPanel
%{_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultStatusBar
%{_datadir}/plasma/look-and-feel/org.kde.breeze.mobile
%{_datadir}/plasma/mobileinitialstart
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.panel
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.taskpanel
%dir %{_datadir}/plasma/quicksettings
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.donotdisturb
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.hotspot
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.record
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksettings.docked
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell
%{_datadir}/plasma-mobile-apn-info
%{_datadir}/wayland-sessions/plasma-mobile.desktop
%{_desktopdir}/kcm_cellular_network.desktop
%{_desktopdir}/kcm_mobile_hotspot.desktop
%{_desktopdir}/kcm_mobile_info.desktop
%{_desktopdir}/kcm_mobile_onscreenkeyboard.desktop
%{_desktopdir}/kcm_mobile_power.desktop
%{_desktopdir}/kcm_mobile_time.desktop
%{_desktopdir}/kcm_mobile_wifi.desktop
%{_desktopdir}/kcm_mobileshell.desktop
