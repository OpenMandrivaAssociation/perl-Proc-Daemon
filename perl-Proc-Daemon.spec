%define modname	Proc-Daemon
%define modver	0.23

Summary:	Run a perl program as a daemon process
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Proc/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Proc::Daemon provides the capability for a Perl program to run
as a Unix daemon process.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# FIXME for reasons yet to be discerned, tests fail in abf but work locally
#make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Proc
%{_mandir}/man3/*
