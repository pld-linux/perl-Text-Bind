%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Bind
Summary:	Text::Bind perl module
Summary(pl):	Modu³ perla Text::Bind
Name:		perl-Text-Bind
Version:	0.04
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Bind - allows to bind Perl structures (strings, routines,
filehandles, objects) to specific locations in text files.

%description -l pl
Text::Bind - pozwala na wi±zanie struktur perla (³añcuchów, rutyn,
uchwytów pliku, obiektów) z okre¶lonymi pozycjami w pliku tekstowym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Text/Bind.pm
%{_mandir}/man3/*
