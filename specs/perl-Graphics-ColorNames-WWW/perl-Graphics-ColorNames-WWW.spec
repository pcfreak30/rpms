# $Id$
# Authority: dries
# Upstream: Claus F&#228;rber <perl$faerber,muc,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Graphics-ColorNames-WWW

Summary: Color names and equivalent RGB values
Name: perl-Graphics-ColorNames-WWW
Version: 0.01
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Graphics-ColorNames-WWW/

Source: http://search.cpan.org/CPAN/authors/id/C/CF/CFAERBER/Graphics-ColorNames-WWW-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This module contains color names and their equivalent RGB values.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Graphics/ColorNames/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1.2
- Rebuild for Fedora Core 5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
