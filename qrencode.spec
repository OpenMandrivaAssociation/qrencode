%define	major 1
%define libname	%mklibname %{name} %{major}

Summary:	A C library for encoding data in a QR Code symbol
Name:		qrencode
Version:	1.0.2
Release:	%mkrel 1
Group:		File tools
License:	LGPL
URL:		http://megaui.net/fukuchi/works/qrencode/index.en.html
Source0:	http://megaui.net/fukuchi/works/qrencode/%{name}-%{version}.tar.gz
BuildRequires:	autoconf2.5
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

%package -n	%{libname}-devel
Summary:	Static library and header files for the qrencode library
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
Libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D
symbology that can be scanned by handy terminals such as a mobile phone with
CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and is
highly robustness.

This package contains the static qrencode library and its header files.

%prep

%setup -q -n %{name}-%{version}

%build
#sh ./autogen.sh

%configure2_5x \
    --enable-static \
    --enable-shared

make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
