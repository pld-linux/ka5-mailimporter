%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		mailimporter
Summary:	mailimporter
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	221c79ac888a21582214ba1184b7bf9e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-akonadi-devel >= %{kdeappsver}
BuildRequires:	ka5-akonadi-mime-devel >= %{kdeappsver}
BuildRequires:	ka5-kmime-devel >= %{kdeappsver}
BuildRequires:	ka5-libkdepim-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-karchive-devel >= 5.51.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library which provides support for mail apps.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/mailimporter.categories
/etc/xdg/mailimporter.renamecategories
%attr(755,root,root) %ghost %{_libdir}/libKF5MailImporter.so.5
%attr(755,root,root) %{_libdir}/libKF5MailImporter.so.5.*.*
%attr(755,root,root) %ghost %{_libdir}/libKF5MailImporterAkonadi.so.5
%attr(755,root,root) %{_libdir}/libKF5MailImporterAkonadi.so.5.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/MailImporter
%{_includedir}/KF5/MailImporterAkonadi
%{_includedir}/KF5/mailimporter
%{_includedir}/KF5/mailimporter_version.h
%{_includedir}/KF5/mailimporterakonadi
%{_includedir}/KF5/mailimporterakonadi_version.h
%{_libdir}/cmake/KF5MailImporter
%{_libdir}/cmake/KF5MailImporterAkonadi
%attr(755,root,root) %{_libdir}/libKF5MailImporter.so
%attr(755,root,root) %{_libdir}/libKF5MailImporterAkonadi.so
%{_libdir}/qt5/mkspecs/modules/qt_MailImporter.pri
%{_libdir}/qt5/mkspecs/modules/qt_MailImporterAkonadi.pri
