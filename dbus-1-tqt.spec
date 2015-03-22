%define	tde_ver	R14.0.0
Summary:	DBus bindings for the Trinity Qt interface
Name:		dbus-1-tqt
Version:	0.9
Release:	0.1
# AFL v2.1 or GPL v2+, but Qt license enforces GPL
License:	GPL v2+
Group:		Libraries
Source0:	http://tde-mirror.yosemite.net/trinity/releases/R14.0.0/dependencies/%{name}-%{tde_ver}.tar.bz2
# Source0-md5:	851c2184a4fcf2df48601499b793a74f
Patch0:		qt.patch
URL:		http://www.freedesktop.org/Software/DBusBindings
BuildRequires:	cmake >= 2.8
BuildRequires:	dbus-devel >= 0.91
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt-devel >= 6:3.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
D-BUS add-on library to integrate the standard D-BUS library with the
Qt thread abstraction and main loop.

%description -l pl.UTF-8
Dodatkowa biblioteka D-BUS do integracji standardowej biblioteki D-BUS
z abstrakcją wątków i główną pętlą Qt.

%package devel
Summary:	Header files for Qt-based library for using D-BUS
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki do używania D-BUS opartej o Qt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-devel >= 0.91

%description devel
Header files for Qt-based library for using D-BUS.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki do używania D-BUS opartej o Qt.

%package static
Summary:	Static Qt-based library for using D-BUS
Summary(pl.UTF-8):	Statyczna biblioteka do używania D-BUS oparta o Qt
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Qt-based library for using D-BUS.

%description static -l pl.UTF-8
Statyczna biblioteka do używania D-BUS oparta o Qt.

%prep
%setup -qc
mv dependencies/dbus-1-tqt/* .
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DWITH_GCC_VISIBILITY=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libdbus-1-tqt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdbus-1-tqt.so.0
%attr(755,root,root) %{_bindir}/dbusxml2qt3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdbus-1-tqt.so
%{_libdir}/libdbus-1-tqt.la
%{_includedir}/dbus-1-tqt
%{_pkgconfigdir}/dbus-1-tqt.pc
