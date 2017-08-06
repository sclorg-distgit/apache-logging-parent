%{?scl:%scl_package apache-logging-parent}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}apache-logging-parent
Version:        1
Release:        1.1%{?dist}
License:        ASL 2.0
Summary:        Parent pom for Apache Logging Services projects
URL:            https://logging.apache.org/
Source0:        https://repo1.maven.org/maven2/org/apache/logging/logging-parent/%{version}/logging-parent-%{version}-source-release.zip
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_maven}maven-local
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache:apache:pom:)

%description
Parent pom for Apache Logging Services projects.

%prep
%setup -q -n logging-parent-%{version}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Fri Jun 23 2017 Michael Simacek <msimacek@redhat.com> - 1-1.1
- Package import and sclization

* Wed Mar 29 2017 Michael Simacek <msimacek@redhat.com> - 1-1
- Initial packaging
