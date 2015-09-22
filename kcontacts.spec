%define major 5
%define libname %mklibname KF5Contacts %{major}
%define devname %mklibname KF5Contacts -d

Name: kcontacts
Version:	15.08.1
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for handling contact data
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Gui)

%description
KDE library for handling contact data

%package -n %{libname}
Summary: KDE library for handling contact data
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for handling MIME types

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

%files
%{_datadir}/kf5/kcontacts

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.4*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
