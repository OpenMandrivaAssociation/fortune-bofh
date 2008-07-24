%define base_name	bofh
%define name		fortune-%{base_name}
%define version		1.0
%define release		%mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	BOFH excuses fortune
License:	Public Domain
Group:		Toys
Source:		%{base_name}-%{version}.tar.bz2
URL:		http://www.cs.wisc.edu/~ballard/bofh
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-buildroot
Requires:	fortune-mod
BuildRequires:	fortune-mod

%description
This is a set of BOFH-style excuses.

%prep
%setup -q -n %{base_name}-%{version}

%build
perl -ni -e 'print "BOFH excuse #" . ++$i . ":\n\n$_%\n"' excuses
/usr/sbin/strfile excuses

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_gamesdatadir}/fortunes
install -m 644 excuses $RPM_BUILD_ROOT%{_gamesdatadir}/fortunes/%{base_name}
install -m 644 excuses.dat $RPM_BUILD_ROOT%{_gamesdatadir}/fortunes/%{base_name}.dat

%files
%defattr(-,root,root)
%{_gamesdatadir}/fortunes/*
