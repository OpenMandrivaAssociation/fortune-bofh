%define base_name	bofh

Name:		fortune-%{base_name}
Version:	1.2
Release:	%mkrel 1
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
