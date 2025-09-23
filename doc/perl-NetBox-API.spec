Name:           perl-NetBox-API
Version:        0.0.4
Release:        1%{?dist}
Summary:        NetBox IPAM/DCIM REST API perl module
License:        Distributable, see LICENSE
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/NetBox-API/
Source0:        http://www.cpan.org/modules/by-module/NetBox/NetBox-API-%{version}.tar.gz
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
%doc Changes LICENSE Makefile MYMETA.json MYMETA.yml README
%dir %{perl_vendorlib}/NetBox
%{perl_vendorlib}/NetBox*
%{_mandir}/man3/NetBox*

%changelog

* Thu Apr 17 2025 Volodymyr Pidgornyi <vp@dtel-ix.net> 0.0.4
- NetBox::API::Tenant and NetBox::API::Session modules removed;
- fields filtering in response added.

* Fri Oct 18 2024 Volodymyr Pidgornyi <vp@dtel-ix.net> 0.0.3
- NetBox::API::Tenant module added.

* Sat Oct 12 2024 Volodymyr Pidgornyi <vp@dtel-ix.net> 0.0.2
- NetBox::API::Session module added.

* Mon Mar 04 2024 Volodymyr Pidgornyi <vp@dtel-ix.net> 0.0.1-1
- Initial public release.
