%define	major 3
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	A C library for encoding data in a QR Code symbol
Name:		qrencode
Version:	3.0.3
Release:	%mkrel 1
Group:		File tools
License:	LGPLv2+
URL:		http://megaui.net/fukuchi/works/qrencode/index.en.html
Source0:	http://megaui.net/fukuchi/works/qrencode/%{name}-%{version}.tar.bz2
BuildRequires:	libtool
BuildRequires:	libpng-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D
symbology that can be scanned by handy terminals such as a mobile phone with
CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and is
highly robustness.

%package -n	%{libname}
Summary:	A C library for encoding data in a QR Code symbol
Group:          System/Libraries

%description -n	%{libname}
Libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D
symbology that can be scanned by handy terminals such as a mobile phone with
CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and is
highly robustness.

%package -n	%{develname}
Summary:	Static library and header files for the qrencode library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%mklibname -d qrencode 1

%description -n	%{develname}
Libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D
symbology that can be scanned by handy terminals such as a mobile phone with
CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and is
highly robustness.

This package contains the static qrencode library and its header files.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x \
    --enable-static \
    --enable-shared
make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
