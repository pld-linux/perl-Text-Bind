#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Bind
Summary:	Text::Bind perl module
Summary(pl):	Modu³ perla Text::Bind
Name:		perl-Text-Bind
Version:	0.04
Release:	8
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0cc04468bf01c3a5c093612093d05888
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
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
%doc Changes README
%{perl_vendorlib}/Text/Bind.pm
%{_mandir}/man3/*
