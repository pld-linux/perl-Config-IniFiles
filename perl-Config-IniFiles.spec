%include	/usr/lib/rpm/macros.perl
%define	pdir	Config
%define	pnam	IniFiles
Summary:	Config-IniFiles perl module
Summary(pl):	Modu� perla Config-IniFiles
Name:		perl-Config-IniFiles
Version:	2.21
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config::IniFiles - A module for reading .ini-style configuration
files.

%description -l pl
Config::IniFiles - - modu� do czytania plik�w configuracyjnych .ini.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Config/IniFiles.pm
