%define debug_package %{nil}

Name:           sqlbeat
Version:        0.1.6
Release:        1%{?dist}
Summary:        Fully customizable Beat for MySQL/Microsoft SQL Server/PostgreSQL servers
ExclusiveArch:  x86_64

Group:          System Environment/Daemons
License:        Apache
URL:            https://github.com/abraverm/sqlbeat
Source0:        sqlbeat
Source1:        sqlbeat.service
Source2:        sqlbeat.sysconfig
Source3:        sqlbeat.yml
Source4:        LICENSE
BuildRequires:  golang
Requires:       systemd

%description
Fully customizable Beat for MySQL/Microsoft SQL Server/PostgreSQL servers - this beat can ship the results of any query defined on the config file to Elasticsearch.

%install
install -D %{SOURCE0} %{buildroot}/%{_bindir}/%{name}
install -D %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
install -D %{SOURCE2} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
install -D %{SOURCE3} %{buildroot}/%{_sysconfdir}/%{name}/%{name}.yml
install -D %{SOURCE4} %{buildroot}/%{_docdir}/%{name}/LICENSE

%clean
rm -rf %{buildroot}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/%{name}
%dir %attr(750, root, root) %{_sysconfdir}/%{name}
%attr(644, root, root) %{_unitdir}/%{name}.service
%config(noreplace) %attr(640, root, root) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %attr(640, root, root) %{_sysconfdir}/%{name}/%{name}.yml
%doc %{_docdir}/%{name}/LICENSE


%changelog
* Mon May 10 2018 Alexander Braverman Masis<alexbmasis@gmail.com> - 0.1.6
* Mon Apr 30 2018 Alexander Braverman Masis<alexbmasis@gmail.com> - 0.1.3
- Initial packaging
