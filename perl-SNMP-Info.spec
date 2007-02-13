#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	SNMP
%define		pnam	Info
Summary:	SNMP::Info - Perl interface to network devices and MIBs through SNMP
Summary(pl.UTF-8):	SNMP::Info - interfejs perlowy do urządzeń sieciowych i MIB-ów poprzez SNMP
Name:		perl-SNMP-Info
Version:	1.04
Release:	1
License:	BSD
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2cf580f142b7300fc12336b83c85f5eb
URL:		http://snmp-info.sourceforge.net/
%if %{with tests}
BuildRequires:	perl-SNMP >= 4
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SNMP::Info gives an object oriented interface to information obtained
through SNMP. This module is geared towards network devices.
Subclasses exist for a number of network devices and common MIBs. The
idea behind this module is to give a common interface to data from
network devices, leaving the device-specific hacks behind the scenes
in subclasses.

%description -l pl.UTF-8
SNMP::Info udostępnia zorientowany obiektowo interfejs do informacji
uzyskiwanych poprzez SNMP. Moduł jest dostosowany do urządzeń
sieciowych. Istnieją podklasy dla wielu urządzeń sieciowych i
popularnych MIB-ów. Ideą tego modułu jest dostarczenie wspólnego
interfejsu do danych z urządzeń sieciowych pozostawiając specyficzne
dla konkretnych urządzeń sztuczki ukryte w podklasach.

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
%doc COPYRIGHT ChangeLog DeviceMatrix.txt
%{perl_vendorlib}/SNMP/Info.pm
%{perl_vendorlib}/SNMP/Info
%{_mandir}/man3/*
