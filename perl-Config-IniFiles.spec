%include	/usr/lib/rpm/macros.perl
Summary:	Config-IniFiles perl module
Summary(pl):	Modu³ perla Config-IniFiles
Name:		perl-Config-IniFiles
Version:	2.13
Release:	0
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	Config-IniFiles-%{version}.tar.gz
# this is not needed, and i dont know for what i put that in spec
#Source1:	Config-IniFiles-%{version}.readme 
BuildRequires:	rpm-perlprov >= 3.0.3-16
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n Config-IniFiles-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Config/IniFiles
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)


gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Config/IniFiles.pm
%{perl_sitearch}/auto/Config/IniFiles
