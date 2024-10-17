%define upstream_name	 Apache-LogRegex
%define upstream_version 1.52

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl module to parse a line from an Apache logfile into a hash
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Apache/Apache-LogRegex-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This implements a simple Perl class to parse Apache log files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%{perl_vendorlib}/Apache/*
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.500.0-2mdv2011.0
+ Revision: 680455
- mass rebuild

* Fri Feb 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.500.0-1mdv2011.0
+ Revision: 504565
- rebuild using %%perl_convert_version

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.5-2mdv2010.0
+ Revision: 440529
- rebuild

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdv2009.1
+ Revision: 305698
- update to new version 1.5

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.4-3mdv2009.0
+ Revision: 255275
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.4-1mdv2008.1
+ Revision: 136657
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 1.4-1mdv2008.0
+ Revision: 19179
-New version


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.3-1mdv2007.0
+ Revision: 73199
- import perl-Apache-LogRegex-1.3-1mdv2007.0

* Wed May 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.3-1mdv2007.0
- New release 1.3

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.2-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Sat Jun 25 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.2-1mdk
- First Mandriva release


