# $Id$
# Authority: dries
# Upstream: <tujikawa$rednoah,com>

Summary: Download utility with BitTorrent and Metalink support
Name: aria2
Version: 1.18.10
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://aria2.sourceforge.net/

Source: http://downloads.sf.net/project/aria2/stable/aria2-%{version}/aria2-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: boost >= 1.34
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: libxml2-devel
BuildRequires: openssl-devel >= 0.9.6
BuildRequires: pkgconfig

%description
aria2 is a download utility with resuming and segmented downloading.
Supported protocols are HTTP/HTTPS/FTP/BitTorrent/Metalink.

%prep
%setup
 
%build
### Add correct CFLAGS for EL3 and RH9
%{expand: %%define optflags %{optflags} %(pkg-config --cflags openssl)}
%configure \
    --disable-xmltest \
    --enable-metalink
%{__make} %{?_smp_mflags}

%install
%make_install
%find_lang aria2 --with-man
%{__mv} -v %{buildroot}%{_docdir}/aria2 _rpmdocs

%clean
%{__rm} -rf %{buildroot}
  
%files -f aria2.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS AUTHORS _rpmdocs/*
%doc %{_mandir}/man1/aria2c.1*
%doc %{_mandir}/*/man1/aria2c.1*
%{_bindir}/aria2c
%{_datadir}/doc
%{_datadir}/locale

%changelog
<<<<<<< HEAD
* Wed Mar 11 2015 Derrick Hammer <derrick@derrickhammer.com> - 1.18.10-1
- Updated to release 1.18.10.
- Fixed source URL due to sourceforge file url structure changes
- Updated macros
- Added new files to %files macro

* Wed Mar 20 2013 Dag Wieers <dag@wieers.com> - 1.16.4-1
- Updated to release 1.16.4.

* Tue Feb 12 2013 Dag Wieers <dag@wieers.com> - 1.16.3-1
- Updated to release 1.16.3.

* Fri Jun 08 2012 Dag Wieers <dag@wieers.com> - 1.15.1-1
- Updated to release 1.15.1.

* Sat Jan 21 2012 Dag Wieers <dag@wieers.com> - 1.14.1-1
- Updated to release 1.14.1.

* Sun Aug 29 2010 Dag Wieers <dag@wieers.com> - 1.10.1-1
- Updated to release 1.10.1.

* Wed Jul 07 2010 Dag Wieers <dag@wieers.com> - 1.9.5-1
- Updated to release 1.9.5.

* Thu Jun 10 2010 Dag Wieers <dag@wieers.com> - 1.9.4-1
- Updated to release 1.9.4.

* Mon Aug 31 2009 Dries Verachtert <dries@ulyssis.org> - 1.5.1-1
- Updated to release 1.5.1.

* Tue Jul 21 2009 Dries Verachtert <dries@ulyssis.org> - 1.5.0-1
- Updated to release 1.5.0.

* Tue Apr 14 2009 Dries Verachtert <dries@ulyssis.org> - 1.3.1-1
- Updated to release 1.3.1.

* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 1.3.0-1
- Updated to release 1.3.0.

* Sat Jan  3 2009 Dries Verachtert <dries@ulyssis.org> - 1.1.2-1
- Updated to release 1.1.2.

* Wed Nov 26 2008 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Updated to release 1.0.1.

* Thu Nov 20 2008 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Updated to release 1.0.0.

* Wed Oct 15 2008 Dag Wieers <dag@wieers.com> - 0.16.1-1
- Updated to release 0.16.1.

* Tue Oct  7 2008 Dries Verachtert <dries@ulyssis.org> - 0.16.0-1
- Updated to release 0.16.0.

* Tue Sep  9 2008 Dries Verachtert <dries@ulyssis.org> - 0.15.3-1
- Updated to release 0.15.3.

* Mon Aug 18 2008 Dries Verachtert <dries@ulyssis.org> - 0.15.2-1
- Updated to release 0.15.2.

* Tue Aug  5 2008 Dries Verachtert <dries@ulyssis.org> - 0.15.1-1
- Updated to release 0.15.1.

* Thu Jul 24 2008 Dries Verachtert <dries@ulyssis.org> - 0.15.0-1
- Updated to release 0.15.0.

* Sun Jun 22 2008 Dries Verachtert <dries@ulyssis.org> - 0.14.0-1
- Updated to release 0.14.0.

* Fri May 30 2008 Dries Verachtert <dries@ulyssis.org> - 0.13.2-1
- Updated to release 0.13.2.

* Tue Mar 18 2008 Dries Verachtert <dries@ulyssis.org> - 0.13.1-1
- Updated to release 0.13.1.

* Mon Feb 11 2008 Dag Wieers <dag@wieers.com> - 0.12.1-1
- Updated to release 0.12.1.

* Mon Dec 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.12.0-1
- Updated to release 0.12.0.

* Tue Nov 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.5-1
- Updated to release 0.11.5.

* Mon Oct 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.4-1
- Updated to release 0.11.4.

* Sun Sep 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.3-1
- Updated to release 0.11.3.

* Fri Aug 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.2-1
- Updated to release 0.11.2.

* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.1-1
- Updated to release 0.11.1.

* Tue Jun 12 2007 Dag Wieers <dag@wieers.com> - 0.11.0-1
- Updated to release 0.11.0.

* Tue May 15 2007 Dag Wieers <dag@wieers.com> - 0.10.2.1-1
- Updated to release 0.10.2.1.

* Wed Mar 28 2007 Dries Verachtert <dries@ulyssis.org> - 0.10.2-1
- Updated to release 0.10.2.

* Tue Feb 13 2007 Dries Verachtert <dries@ulyssis.org> - 0.10.1-1
- Updated to release 0.10.1.

* Mon Jan 29 2007 Dag Wieers <dag@wieers.com> - 0.10.0-1
- Updated to release 0.10.0.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Updated to release 0.9.0.

* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 0.8.1-2
- Fixed group name.

* Mon Oct 02 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.1-1
- Updated to release 0.8.1.

* Mon Aug 21 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.2-1
- Updated to release 0.7.2.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org>
- Updated to release 0.7.1.

* Sat Aug 12 2006 Dries Verachtert <dries@ulyssis.org>
- Updated to release 0.7.0.

* Fri Jul 28 2006 Anthony Bryan <anthonybryan@gmail.com>
- Update to version 0.6.0+1 and FC6
 
* Mon Jun 5 2006 Malcolm A Hussain-Gambles <malcolm@secpay7.force9.co.uk>
- First release of this package by me
