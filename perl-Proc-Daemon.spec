%define upstream_name    Proc-Daemon
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Run a perl program as a daemon process
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Proc/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-devel
BuildArch:	noarch

%description
Proc::Daemon provides the capability for a Perl program to run
as a Unix daemon process.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/Proc


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.140.0-3mdv2012.0
+ Revision: 765608
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.140.0-2
+ Revision: 764135
- rebuilt for perl-5.14.x

* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.140.0-1
+ Revision: 684822
- update to new version 0.14

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.120.0-1
+ Revision: 682144
- update to new version 0.12

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1
+ Revision: 660013
- update to new version 0.10

* Fri Mar 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1
+ Revision: 646397
- update to new version 0.09

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1
+ Revision: 644796
- update to new version 0.08

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2
+ Revision: 640780
- rebuild to obsolete old packages

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-1
+ Revision: 638943
- update to new version 0.07

* Wed Feb 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1
+ Revision: 635215
- update to new version 0.06

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 596010
- update to new version 0.05

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 404351
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.03-5mdv2009.0
+ Revision: 241847
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-3mdv2008.0
+ Revision: 86819
- rebuild


* Sun Apr 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdk
- contributed by Kyle Yencer <kyle@yencer.net>

