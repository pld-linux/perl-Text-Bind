%define	pdir	Text
%define	pnam	Bind
%include	/usr/lib/rpm/macros.perl
Summary:	Text-Bind perl module
Summary(pl):	Modu� perla Text-Bind
Name:		perl-Text-Bind
Version:	0.04
Release:	5

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Bind - allows to bind Perl structures (strings, routines,
filehandles, objects) to specific locations in text files.

%description -l pl
Text-Bind - pozwala na wi�zanie struktur perla (�a�cuch�w, rutyn,
uchwyt�w pliku, obiekt�w) z okre�lonymi pozycjami w pliku tekstowym.

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
