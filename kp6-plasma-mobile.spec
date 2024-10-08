#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.2.0
%define		qtver		6.6.0
%define		kpname		plasma-mobile
%define		kf6_ver		6.1.0

Summary:	plasma-mobile
Name:		kp6-%{kpname}
Version:	6.2.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	3c9bec6261444ddaec3f98da448a7414
URL:		https://kde.org/
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
BuildRequires:	kf6-knotifications-devel >= %{kf6_ver}
BuildRequires:	kf6-kservice-devel >= %{kf6_ver}
BuildRequires:	kf6-modemmanager-qt-devel >= %{kf6_ver}
BuildRequires:	kirigami-addons-devel >= 0.11.90
BuildRequires:	kp6-kwayland-devel >= %{kdeplasmaver}
BuildRequires:	kp6-kwin-devel >= %{kdeplasmaver}
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qcoro-qt6-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
Obsoletes:	kp5-%{kpname} < %{version}
Obsoletes:	kp6-plasma-phone-components < 5.24.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

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
%{_libdir}/qt6/qml/org/kde/plasma/private/mobileshell
%{_datadir}/wayland-sessions/plasma-mobile.desktop
%dir %{_libdir}/qt6/qml/org/kde/plasma/mm
%{_libdir}/qt6/qml/org/kde/plasma/mm/libppc-mmqmlplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/mm/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/nightcolor
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/nightcolor/libnightcolorplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/nightcolor/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/flashlight
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/flashlight/libflashlightplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/flashlight/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/powermenu
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/powermenu/libpowermenuplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/powermenu/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenrotation
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenrotation/libscreenrotationplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenrotation/qmldir
%dir %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenshot
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenshot/libscreenshotplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/screenshot/qmldir
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/metadata.json
%attr(755,root,root) %{_bindir}/startplasmamobile
%{_libdir}/qt6/plugins/plasma/kcms/systemsettings/kcm_mobileshell.so
%{_datadir}/metainfo/org.kde.plasma.quicksetting.airplanemode.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.audio.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.battery.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.bluetooth.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.caffeine.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.donotdisturb.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.flashlight.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.keyboardtoggle.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.mobiledata.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.nightcolor.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.powermenu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenrotation.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenshot.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.settingsapp.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.wifi.appdata.xml

%attr(755,root,root) %{_bindir}/plasma-mobile-envmanager
%attr(755,root,root) %{_bindir}/plasma-mobile-initial-start
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/kded_plasma_mobile_start.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kwin/effects/plugins/mobiletaskswitcher.so
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
%{_libdir}/qt6/qml/org/kde/plasma/mm/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/plasma/mm/ppc-mmqmlplugin.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/cellular/libcellularplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/cellular/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/prepare/libprepareplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/prepare/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/time/libtimeplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/time/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/wifi/libwifiplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/mobileinitialstart/wifi/qmldir
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/private/mobile/homescreen/halcyon/libhalcyonplugin.so
%{_libdir}/qt6/qml/org/kde/private/mobile/homescreen/halcyon/qmldir
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/kded_plasma_mobile_autodetect_apn.so
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/plasma/quicksetting/record/librecordplugin.so
%{_libdir}/qt6/qml/org/kde/plasma/quicksetting/record/qmldir
%{_datadir}/knotifications6/plasma_mobile_quicksetting_record.notifyrc
%{_datadir}/kwin/effects/mobiletaskswitcher/mobiletaskswitcher.json
%{_datadir}/kwin/effects/mobiletaskswitcher/qml/TaskSwitcherHelpers.qml
%{_desktopdir}/kcm_cellular_network.desktop
%{_desktopdir}/kcm_mobile_hotspot.desktop
%{_desktopdir}/kcm_mobile_info.desktop
%{_desktopdir}/kcm_mobile_onscreenkeyboard.desktop
%{_desktopdir}/kcm_mobile_power.desktop
%{_desktopdir}/kcm_mobile_time.desktop
%{_desktopdir}/kcm_mobile_wifi.desktop
%{_desktopdir}/kcm_mobileshell.desktop
%{_datadir}/dbus-1/interfaces/org.kde.plasmashell.Mobile.xml
%{_datadir}/knotifications6/plasma_mobile_quicksetting_screenshot.notifyrc
%{_datadir}/kwin/effects/mobiletaskswitcher/qml/FlickContainer.qml
%{_datadir}/kwin/effects/mobiletaskswitcher/qml/Task.qml
%{_datadir}/kwin/effects/mobiletaskswitcher/qml/TaskList.qml
%{_datadir}/kwin/effects/mobiletaskswitcher/qml/TaskSwitcher.qml
%{_datadir}/kwin/scripts/convergentwindows/contents/ui/main.qml
%{_datadir}/kwin/scripts/convergentwindows/metadata.json
%{_datadir}/metainfo/org.kde.breeze.mobile.appdata.xml
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
%{_datadir}/metainfo/org.kde.plasma.quicksetting.hotspot.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksettings.docked.appdata.xml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.mobile/contents/defaults
%{_datadir}/plasma/look-and-feel/org.kde.breeze.mobile/contents/layouts/layout.js
%{_datadir}/plasma/look-and-feel/org.kde.breeze.mobile/contents/logout/ActionButton.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.mobile/contents/logout/Logout.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.mobile/contents/systemdialog/SystemDialog.qml
%{_datadir}/plasma/look-and-feel/org.kde.breeze.mobile/metadata.json
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.cellular/contents/ui/EditProfileDialog.qml
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.cellular/contents/ui/main.qml
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.cellular/metadata.json
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.finished/contents/ui/konqi-calling.png
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.finished/contents/ui/konqi-calling.png.license
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.finished/contents/ui/main.qml
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.finished/metadata.json
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.prepare/contents/ui/main.qml
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.prepare/metadata.json
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.time/contents/ui/main.qml
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.time/metadata.json
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.wifi/contents/ui/ConnectDialog.qml
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.wifi/contents/ui/ConnectionItemDelegate.qml
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.wifi/contents/ui/PasswordField.qml
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.wifi/contents/ui/main.qml
%{_datadir}/plasma/mobileinitialstart/org.kde.plasma.mobileinitialstart.wifi/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/AppDrawer.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/AppDrawerGrid.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/AppDrawerHeader.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/DelegateDragItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/FavouritesBar.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/FolderView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/FolderViewTitle.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/HomeScreen.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/HomeScreenPage.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/HomeScreenPages.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/PlaceholderDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/WidgetDragItem.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/delegate/AbstractDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/delegate/AppDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/delegate/AppFolderDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/delegate/DelegateAppIcon.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/delegate/DelegateFolderIcon.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/delegate/DelegateIconLoader.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/delegate/DelegateLabel.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/delegate/DelegateShadow.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/delegate/WidgetDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/delegate/WidgetDelegateConfig.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/private/DarkenEffect.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/private/FlickableOpacityGradient.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/private/Orientation.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/private/WidgetHandlePosition.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/private/WidgetResizeHandle.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/private/WidgetResizeHandleFrame.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/settings/AppletListViewer.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/settings/SettingsComponent.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/settings/SettingsWindow.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/contents/ui/Clock.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/contents/ui/FavoritesAppDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/contents/ui/FavoritesGrid.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/contents/ui/FavoritesView.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/contents/ui/FolderGrid.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/contents/ui/GridAppDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/contents/ui/GridAppList.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/contents/ui/HomeScreen.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/contents/ui/SettingsScreen.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.halcyon/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.panel/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.panel/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.taskpanel/contents/ui/NavigationPanelComponent.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.taskpanel/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.taskpanel/metadata.json
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.donotdisturb/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.donotdisturb/metadata.json
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.hotspot/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.hotspot/metadata.json
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksettings.docked/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksettings.docked/metadata.json
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/configuration/AppletConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/configuration/ConfigurationAppletPage.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/configuration/ConfigurationContainmentAppearance.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/configuration/ConfigurationKcmPage.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/configuration/ContainmentConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/defaults
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/layout.js
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/updates/5_24_update.js
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/updates/panelsfix.js
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/views/Desktop.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/views/Panel.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/metadata.json
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/metadata.json.license
%{_datadir}/plasma-mobile-apn-info/apns-full-conf.xml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/private/ConfirmDeleteFolderDialogLoader.qml
%{_datadir}/plasma/plasmoids/org.kde.plasma.mobile.homescreen.folio/contents/ui/private/ContextMenuLoader.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/lockscreen/BottomIconIndicator.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/lockscreen/Clock.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/lockscreen/FlickContainer.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/lockscreen/HeaderComponent.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/lockscreen/Keypad.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/lockscreen/LockScreen.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/lockscreen/LockScreenState.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/lockscreen/NotificationsComponent.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/lockscreen/PasswordBar.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/lockscreen/WallpaperBlur.qml
%{_datadir}/metainfo/org.kde.plasma.mobile.defaultNavigationPanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mobile.defaultStatusBar.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.record.appdata.xml
%{_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultNavigationPanel/contents/layout.js
%{_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultNavigationPanel/metadata.json
%{_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultStatusBar/contents/layout.js
%{_datadir}/plasma/layout-templates/org.kde.plasma.mobile.defaultStatusBar/metadata.json
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.record/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.record/metadata.json
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/applet/AppletError.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/applet/CompactApplet.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/applet/DefaultCompactRepresentation.qml
%{_datadir}/plasma/shells/org.kde.plasma.mobileshell/contents/lockscreen/LockScreenContent.qml
