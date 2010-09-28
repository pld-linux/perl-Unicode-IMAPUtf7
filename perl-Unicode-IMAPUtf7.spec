#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unicode
%define		pnam	IMAPUtf7
Summary:	Unicode::IMAPUtf7 - extension to deal with IMAP UTF7
Name:		perl-Unicode-IMAPUtf7
Version:	2.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
# Source0:	http://search.cpan.org/CPAN/authors/id/F/FA/FABPOT/%{pdir}-%{pnam}-%{version}.tar.gz
# repackaged with proper permissions
Source0:	%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	06ec185c4b0b77a00e5a11fdff532fde
URL:		http://search.cpan.org/dist/Unicode-IMAPUtf7/
BuildRequires:	perl-Unicode-String
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IMAP mailbox names are encoded in a modified UTF7 when names contains
international characters outside of the printable ASCII range. The
modified UTF-7 encoding is defined in RFC2060 (section 5.1.3).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Unicode/IMAPUtf7.pm
%{_mandir}/man3/*.3pm*
