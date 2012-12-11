%define upstream_name    Net-Google-AuthSub
%define upstream_version 0.5

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A response from a Net::Google::AuthSub request
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
A response from a Net::Google::AuthSub request.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.500.0-2mdv2011.0
+ Revision: 656948
- rebuild for updated spec-helper

* Fri Dec 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.500.0-1mdv2011.0
+ Revision: 607257
- import perl-Net-Google-AuthSub

