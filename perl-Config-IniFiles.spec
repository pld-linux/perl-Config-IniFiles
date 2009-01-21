#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Config
%define		pnam	IniFiles
Summary:	Config::IniFiles - a module for reading .ini-style configuration files
Summary(pl.UTF-8):	Config::IniFiles - moduł do odczytu plików konfiguracyjnych typu .ini
Name:		perl-Config-IniFiles
Version:	2.45
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a5fc99a3e1e1046626bfca21c24e0675
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::IniFiles Perl module provides a way to have readable
configuration files outside your Perl script.  Configurations can be
imported (inherited, stacked,...), sections can be grouped, and
settings can be accessed from a tied hash.

%description -l pl.UTF-8
Moduł Perla Config::IniFiles umożliwia posiadanie czytelnych plików
konfiguracyjnych poza skryptem perlowym. Konfigurację można
zaimportować (odziedziczyć, umieścić na stosie, ...), sekcje można
pogrupować a dostęp do łańcuchów tekstowych może się odbywać poprzez
stowarzyszony z plikiem hash.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/Config/IniFiles.pm
