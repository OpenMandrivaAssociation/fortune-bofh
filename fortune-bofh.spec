%define base_name	bofh

Name:		fortune-%{base_name}
Version:	1.2
Release:	2
Summary:	BOFH excuses fortune
License:	Public Domain
Group:		Toys
Source:		%{base_name}-%{version}.tar.bz2
URL:		http://www.cs.wisc.edu/~ballard/bofh
BuildArch:	noarch
Requires:	fortune-mod
BuildRequires:	fortune-mod

%description
This is a set of BOFH-style excuses.

%prep
%setup -q -n %{base_name}-%{version}

%build
%__perl -ni -e 'print "BOFH excuse #" . ++$i . ":\n\n$_%\n"' excuses
/usr/sbin/strfile excuses

%install
%__rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_gamesdatadir}/fortunes
install -m 644 excuses %{buildroot}%{_gamesdatadir}/fortunes/%{base_name}
install -m 644 excuses.dat %{buildroot}%{_gamesdatadir}/fortunes/%{base_name}.dat

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesdatadir}/fortunes/*


%changelog
* Thu Feb 09 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2-1mdv2011.0
+ Revision: 772287
- New version 1.2, spec cleanup

* Wed Jul 27 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-9
+ Revision: 691824
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-8mdv2011.0
+ Revision: 245317
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.0-6mdv2008.1
+ Revision: 136417
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-6mdv2008.0
+ Revision: 71617
- Import fortune-bofh



* Fri Aug 25 2006 Götz Waschk <waschk@mandriva.org> 1.0-6mdv2007.0
- mkrel

* Wed Aug 24 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.0-5mdk
- Rebuild

* Fri Aug 13 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-4mdk
- rebuild

* Sat Jul 26 2003 Götz Waschk <waschk@linux-mandrake.com> 1.0-3mdk
- really split the strings

* Mon Jul 21 2003 Götz Waschk <waschk@linux-mandrake.com> 1.0-2mdk
- fix buildrequires

* Sat Jul 19 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 1.0-1mdk
- first Mandrake release
