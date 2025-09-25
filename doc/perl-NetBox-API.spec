Name:           perl-NetBox-API
Version:        0.1.0
Release:        1%{?dist}
Summary:        NetBox API perl module
License:        Distributable, see LICENSE
Group:          Development/Libraries
URL:            https://github.com/kornix/perl-NetBox-API
Source0:        NetBox-API-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	perl(LWP::UserAgent)
Requires:	perl(JSON)
Provides:	perl(NetBox::API)
Provides:	perl(NetBox::API::Tenant)
Provides:	perl(NetBox::API::Session)

%description
NetBox IPAM/DCIM REST API perl module.

%prep
%setup -q -n NetBox-API-%{version}

rm -f pm_to_blib

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

#check
#make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE MYMETA.json MYMETA.yml README.md
%dir %{perl_vendorlib}/NetBox
%{perl_vendorlib}/NetBox*
%{_mandir}/man3/NetBox*

%changelog

* Thu Sep 25 2025 Volodymyr Pidgornyi <vp@dtel-ix.net> 0.1.0
- Initial public release.

* Thu Apr 17 2025 Volodymyr Pidgornyi <vp@dtel-ix.net> 0.0.4
- Response fields filtering added.

* Mon Mar 04 2024 Volodymyr Pidgornyi <vp@dtel-ix.net> 0.0.1-1
- Initial release.
