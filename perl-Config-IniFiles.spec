#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	IniFiles
Summary:	Config::IniFiles - a module for reading .ini-style configuration files
Summary(pl):	Config::IniFiles - modu³ do odczytu plików konfiguracyjnych typu .ini
Name:		perl-Config-IniFiles
Version:	2.38
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	17e39e4244ede0061939dcb80ab6294e
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::IniFiles Perl module provides a way to have readable
configuration files outside your Perl script.  Configurations can be
imported (inherited, stacked,...), sections can be grouped, and
settings can be accessed from a tied hash.

%description -l pl
Modu³ Perla Config::IniFiles umo¿liwia posiadanie czytelnych plików
konfiguracyjnych poza skryptem perlowym. Konfiguracjê mo¿na
zaimportowaæ (odziedziczyæ, umie¶ciæ na stosie, ...), sekcje mo¿na
pogrupowaæ a dostêp do ³añcuchów tekstowych mo¿e siê odbywaæ poprzez
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
