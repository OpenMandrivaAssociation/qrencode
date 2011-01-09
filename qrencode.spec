%define	major 3
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	QR Code encoder into PNG image
Name:		qrencode
Version:	3.1.1
Release:	%mkrel 2
Group:		File tools
License:	LGPLv2+
URL:		http://megaui.net/fukuchi/works/qrencode/index.en.html
Source0:	http://megaui.net/fukuchi/works/qrencode/%{name}-%{version}.tar.bz2
BuildRequires:	libtool
BuildRequires:	libpng-devel
BuildRequires:	doxygen
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Qrencode is a utility software using libqrencode to encode string data in a
QR Code and save as a PNG image.

%package -n	%{libname}
Summary:	A C library for encoding data in a QR Code symbol
Group:          System/Libraries

%description -n	%{libname}
Libqrencode is a C library for encoding data in a QR Code symbol, a kind of 2D
symbology that can be scanned by handy terminals such as a mobile phone with
CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and is
highly robustness.

Libqrencode supports QR Code model 2, described in JIS (Japanese Industrial
Standards) X0510:2004 or ISO/IEC 18004.

%package -n	%{develname}
Summary:	The development files for the qrencode library
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

Libqrencode supports QR Code model 2, described in JIS (Japanese Industrial
Standards) X0510:2004 or ISO/IEC 18004. 

This package contains the development files for the qrencode library.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x \
    --enable-shared
%make

%install
rm -rf %{buildroot}

%makeinstall_std

# manual
doxygen

# clean
rm -rf %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README TODO html/
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
