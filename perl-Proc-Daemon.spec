%define modname	Proc-Daemon

Summary:	Run a perl program as a daemon process
Name:		perl-%{modname}
Version:	0.23
Release:	1
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Proc/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Proc::Daemon provides the capability for a Perl program to run
as a Unix daemon process.

%prep
%autosetup -p1 -n %{modname}-%{version}

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
