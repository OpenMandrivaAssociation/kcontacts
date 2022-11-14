%define major 5
%define libname %mklibname KF5Contacts %{major}
%define devname %mklibname KF5Contacts -d
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kcontacts
Version:	5.100.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: KDE library for handling contact data
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Test)
BuildRequires: pkgconfig(iso-codes)
# For API docs
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: qt5-assistant
Conflicts:	kde-l10n < 17.04.0

%description
KDE library for handling contact data.

%package -n %{libname}
Summary: KDE library for handling contact data
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for handling MIME types.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kcontacts5

%files -f kcontacts5.lang
%{_datadir}/qlogging-categories5/kcontacts.categories
%{_datadir}/qlogging-categories5/kcontacts.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/KF5Contacts.*
