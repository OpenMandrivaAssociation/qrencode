%define	major 3
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Summary:	QR Code encoder into PNG image
Name:		qrencode
Version:	3.4.2
Release:	1
Group:		File tools
License:	LGPLv2+
URL:		http://megaui.net/fukuchi/works/qrencode/index.en.html
Source0:	http://megaui.net/fukuchi/works/qrencode/%{name}-%{version}.tar.bz2
Patch0:		qrencode-aarch64.patch
BuildRequires:	libtool
BuildRequires:	libpng-devel
BuildRequires:	doxygen

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
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--disable-static \
    --enable-shared

%make

%install
%makeinstall_std

# manual
doxygen

# clean
rm -rf %{buildroot}%{_libdir}/*.la

%files
%{_bindir}/%{name}
%{_mandir}/man1/*

%files -n %{libname}
%doc COPYING ChangeLog NEWS README TODO html/
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Tue Apr 03 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.3.0-1
+ Revision: 788988
- version update 3.3.0

* Tue Mar 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.2.0-1
+ Revision: 782459
- version update 3.2.0

* Sun Jan 09 2011 Jani Välimaa <wally@mandriva.org> 3.1.1-2mdv2011.0
+ Revision: 630746
- drop support for old mdv releases

* Sat Jul 10 2010 Jani Välimaa <wally@mandriva.org> 3.1.1-1mdv2011.0
+ Revision: 550023
- new version 3.1.1
- fix summary/description
- build doxygen docs
- clean spec

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 3.0.3-3mdv2010.0
+ Revision: 433041
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 3.0.3-2mdv2009.0
+ Revision: 269054
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Jun 06 2008 Funda Wang <fwang@mandriva.org> 3.0.3-1mdv2009.0
+ Revision: 216514
- New version 3.0.3

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.0.2-2mdv2008.1
+ Revision: 140742
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2-2mdv2008.0
+ Revision: 90202
- rebuild

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdv2008.0
+ Revision: 16112
- Import qrencode

