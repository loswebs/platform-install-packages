%define baseurl installrepo.kaltura.org
%define path 9.11.0/RPMS
Summary: Kaltura Server release file and package configuration
Name: kaltura-release
Version: 9.11.0
Release: 2 
License: AGPLv3+
Group: Server/Platform 
URL: http://kaltura.org

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Kaltura Server release file. This package contains yum 
configuration for the Kaltura RPM Repository, as well as the public
GPG keys used to sign them.




%build
%{__cat} <<EOF >kaltura.repo
# URL: http://kaltura.org/
[Kaltura]
name = Kaltura Server
baseurl = http://%{baseurl}/%{path}/\$basearch/
#gpgkey = file:///etc/pki/rpm-gpg/
gpgcheck = 0

[Kaltura-noarch]
name = Kaltura Server arch independent
baseurl = http://%{baseurl}/%{path}/noarch
#gpgkey = file:///etc/pki/rpm-gpg/
gpgcheck = 0
EOF

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 kaltura.repo %{buildroot}%{_sysconfdir}/yum.repos.d/kaltura.repo

%clean
%{__rm} -rf %{buildroot}

%post
#rpm -q gpg-pubkey-e42d547b-3960bdf1 &>/dev/null || rpm --import %{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-matthias
exit 0

%files
#%defattr(-, root, root, 0755)
#%if %{!?_without_rpmpubkey:1}0
#%pubkey RPM-GPG-KEY-rpmforge-dag
#%else
#%doc RPM-GPG-KEY-rpmforge-matthias
#%endif
%dir %{_sysconfdir}/yum.repos.d/
%config %{_sysconfdir}/yum.repos.d/kaltura.repo
#%dir %{_sysconfdir}/pki/rpm-gpg/
#%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmforge-*

%changelog
* Sun Feb 23 2014 Jess Portnoy <jess.portnoy@kaltura.com> - 9.11.0-2
- dont need i686

* Sun Feb 23 2014 Jess Portnoy <jess.portnoy@kaltura.com> - 9.11.0-1
- 9.11.0

* Mon Jan 27 2014 Jess Portnoy <jess.portnoy@kaltura.com> - 9.9.0-1
- 9.9.0

* Sun Jan 26 2014 Jess Portnoy <jess.portnoy@kaltura.com> - 9.7.0-3
- Added 32bit repos.

* Wed Jan 22 2014 Jess Portnoy <jess.portnoy@kaltura.com> - 9.7.0-1
- initial release.

