Name:           exec-maven-plugin
Version:        1.2.1
Release:        12%{?dist}
Summary:        Exec Maven Plugin

Group:          Development/Libraries
# Most of the files are under ASL 2.0 license, but there are some files
# with no license specified. The project contains MIT license text,
# but there is no file which uses such a license.
License:        ASL 2.0 and MIT
URL:            http://mojo.codehaus.org/exec-maven-plugin
Source0:        http://repo1.maven.org/maven2/org/codehaus/mojo/exec-maven-plugin/1.2.1/exec-maven-plugin-1.2.1-source-release.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-invoker-plugin
BuildRequires:  apache-commons-exec

Obsoletes:      maven-plugin-exec < %{version}-%{release}
Provides:       maven-plugin-exec = %{version}-%{release}

%description
A plugin to allow execution of system and Java programs

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q -n exec-maven-plugin-%{version}

sed -i 's/\r$//' LICENSE.txt
find . -name *.jar -delete

cp -p %{SOURCE1} .

%pom_add_dep org.apache.maven:maven-compat pom.xml
%pom_remove_plugin :animal-sniffer-maven-plugin pom.xml

%build
# There are missing dependencies for tests
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt LICENSE-2.0.txt
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt LICENSE-2.0.txt

%changelog
* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-12
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Jun  5 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.1-11
- Clean up BuildRequires

* Thu Feb 14 2013 Michal Srb <msrb@redhat.com> - 1.2.1-10
- Disable animal-sniffer plugin

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2.1-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Jan 11 2013 Michal Srb <msrb@redhat.com> - 1.2.1-7
- Fixed rpmlint warnings
- Remove bundled JAR files before building the package

* Wed Jan 09 2013 Michal Srb <msrb@redhat.com> - 1.2.1-6
- maven-plugin-exec renamed (Resolves: #893451)
- Migrated to xmvn

* Wed Nov 28 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.1-5
- Fix license tag
- Install license files
- Resolves: rhbz#880290

* Wed Nov 28 2012 Tomas Radej <tradej@redhat.com> - 1.2.1-4
- Removed (B)R on plexus-container-default

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 6 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2.1-1
- Update to latest upstream.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 11 2009 Alexander Kurtakov <akurtako@gmail.com> 1.1-1
- Initial package.
