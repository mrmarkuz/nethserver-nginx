Name: nethserver-mrmarkuz
Version: 0.0.1
Release: 1%{?dist}
Summary: nginx for NethServer
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: nethserver-devtools

%description
nginx for NethServer, fast scalable webserver with advanced reverse proxy functions

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update


%changelog
* Fri Mar 09 2018 Markus Neuberger <dev@markusneuberger.at> - 0.0.1-1
- First release
