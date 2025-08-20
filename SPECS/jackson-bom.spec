Name:          jackson-bom
Version:       2.19.1
Release:       1%{?dist}
Summary:       Bill of materials POM for Jackson projects
License:       Apache-2.0

URL:           https://github.com/FasterXML/jackson-bom
Source0:       %{url}/archive/%{name}-%{version}.tar.gz
# Upstream chooses not to include licenses with their pom only projects:
# https://github.com/FasterXML/jackson-parent/issues/1
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson:jackson-parent:pom:) >= 2.19

BuildArch:      noarch
%if 0%{?fedora}
ExclusiveArch:  %{java_arches} noarch
%endif

%description
A "bill of materials" POM for Jackson dependencies.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Disable plugins not needed during RPM builds
%pom_remove_plugin ":maven-enforcer-plugin" base
%pom_remove_plugin "org.sonatype.central:central-publishing-maven-plugin" base

# New EE coords
%pom_change_dep "javax.activation:javax.activation-api" "jakarta.activation:jakarta.activation-api:2" base


# Remove dep on junit-bom
%pom_remove_dep "org.junit:junit-bom" base

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
* Thu Jul 31 2025 Red Hat PKI Team <rhcs-maint@redhat.com> - 2.19.1-1
- Rebase to version 2.19.1
- Resolves: RHEL-103106

* Wed Nov 22 2023 Red Hat PKI Team <rhcs-maint@redhat.com> - 2.14.2-1
- Rebase to upstream version 2.14.2

* Tue Nov 12 2019 Red Hat PKI Team <rhcs-maint@redhat.com> - 2.10.0-1
- Update to latest upstream release

* Wed Jul 31 2019 Red Hat PKI Team <rhcs-maint@redhat.com> - 2.9.9-1
- Update to latest upstream release

* Wed Feb 06 2019 Mat Booth <mat.booth@redhat.com> - 2.9.8-1
- Update to latest upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Mat Booth <mat.booth@redhat.com> - 2.9.4-1
- Update to latest upstream release

* Thu Jan 18 2018 Mat Booth <mat.booth@redhat.com> - 2.9.3-1
- Initial packaging

