%include	/usr/lib/rpm/macros.perl
%define	pdir	SNMP
%define	pnam	Info
Summary:	SNMP::Info Perl module
Summary(cs):	Modul SNMP::Info pro Perl
Summary(da):	Perlmodul SNMP::Info
Summary(de):	SNMP::Info Perl Modul
Summary(es):	M�dulo de Perl SNMP::Info
Summary(fr):	Module Perl SNMP::Info
Summary(it):	Modulo di Perl SNMP::Info
Summary(ja):	SNMP::Info Perl �⥸�塼��
Summary(ko):	SNMP::Info �� ����
Summary(no):	Perlmodul SNMP::Info
Summary(pl):	Modu� Perla SNMP::Info
Summary(pt):	M�dulo de Perl SNMP::Info
Summary(pt_BR):	M�dulo Perl SNMP::Info
Summary(ru):	������ ��� Perl SNMP::Info
Summary(sv):	SNMP::Info Perlmodul
Summary(uk):	������ ��� Perl SNMP::Info
Summary(zh_CN):	SNMP::Info Perl ģ��
Name:		perl-SNMP-Info
Version:	0.7
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e9a139b420d270132b43c7f8470edc17
BuildRequires:	rpm-perlprov
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SNMP::Info - interface to network devices and MIBs through SNMP.

%description -l pl
SNMP::Info - interfejs do urz�dze� sieciowych i MIB�w przez SNMP.

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
%doc ChangeLog
%{perl_sitelib}/SNMP/Info.pm
%{perl_sitelib}/SNMP/Info
%{_mandir}/man3/*
