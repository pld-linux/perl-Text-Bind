%include	/usr/lib/rpm/macros.perl
Summary:	Text-Bind perl module
Summary(pl):	Modu³ perla Text-Bind
Name:		perl-Text-Bind
Version:	0.04
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Bind-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Bind - allows to bind Perl structures (strings, routines,
filehandles, objects) to specific locations in text files.

%description -l pl
Text-Bind - pozwala na wi±zanie struktur perla (³añcuchów, rutyn,
uchwytów pliku, obiektów) z okre¶lonymi pozycjami w pliku tekstowym.

%prep
%setup -q -n Text-Bind-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/Bind.pm
%{_mandir}/man3/*
