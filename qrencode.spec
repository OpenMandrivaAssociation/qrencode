%define major 3
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	QR Code encoder into PNG image
Name:		qrencode
Version:	3.4.3
Release:	7
Group:		File tools
License:	LGPLv2+
Url:		http://megaui.net/fukuchi/works/qrencode/index.en.html
Source0:	http://megaui.net/fukuchi/works/qrencode/%{name}-%{version}.tar.bz2
Patch0:		qrencode-aarch64.patch
BuildRequires:	doxygen
BuildRequires:	libtool
BuildRequires:	pkgconfig(libpng)

%description
Qrencode is a utility software using libqrencode to encode string data in a
QR Code and save as a PNG image.

%package -n	%{libname}
Summary:	A C library for encoding data in a QR Code symbol
Group:		System/Libraries

%description -n	%{libname}
Libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D
symbology that can be scanned by handy terminals such as a mobile phone with
CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and is
highly robustness.

Libqrencode supports QR Code model 2, described in JIS (Japanese Industrial
Standards) X0510:2004 or ISO/IEC 18004.

%package -n	%{devname}
Summary:	The development files for the qrencode library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{devname}
This package contains the development files for the qrencode library.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-shared

%make

%install
%makeinstall_std

# manual
doxygen

%files
%{_bindir}/%{name}
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libqrencode.so.%{major}*

%files -n %{devname}
%doc COPYING ChangeLog NEWS README TODO html/
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

