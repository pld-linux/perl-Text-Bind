#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Text
%define		pnam	Bind
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Bind - bind Perl structures to text files
Summary(pl.UTF-8):	Text::Bind - wiązanie struktur Perla z plikami tekstowymi
Name:		perl-Text-Bind
Version:	0.04
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0cc04468bf01c3a5c093612093d05888
URL:		http://search.cpan.org/dist/Text-Bind/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Bind - allows to bind Perl structures (strings, routines,
filehandles, objects) to specific locations in text files.

%description -l pl.UTF-8
Text::Bind - pozwala na wiązanie struktur Perla (łańcuchów, funkcji,
uchwytów pliku, obiektów) z określonymi pozycjami w pliku tekstowym.

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
