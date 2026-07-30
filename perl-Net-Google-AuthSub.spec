%define upstream_name    Net-Google-AuthSub
%define upstream_version 0.5
Name:		perl-%{upstream_name}
Version:	0.5
Release:	1

Summary:	A response from a Net::Google::AuthSub request
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Net-Google-AuthSub
Source0:	https://cpan.metacpan.org/authors/id/S/SI/SIMONW/Net-Google-AuthSub-0.5.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
A response from a Net::Google::AuthSub request.

%prep
%setup -q -n %{upstream_name}-%{version}

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

