# Cooker used to ship this tree as gradle-8.11.1. Gradle 9 is built from
# source and replaced that package. The Gradle 9 build and the Gradle 8.11
# plugin packages still expect /usr/share/gradle from 8.11.1, so keep those
# already-published files installable under a name that does not replace
# the user-facing gradle package.
# The payload is the rpm -V clean cooker gradle-8.11.1-1 install, not a
# new download.

%global __jar_repack 0
%global __provides_exclude_from .*
%global __requires_exclude_from .*
%global __noautoreq '^.*$'
%global __noautoprov '^.*$'

Name:		gradle-bootstrap
Version:	8.11.1
Release:	1
Summary:	Gradle 8.11.1 bootstrap compiler
License:	Apache 2.0
URL:		https://gradle.org/
Group:		Development/Tools
BuildArch:	noarch

Source0:	gradle-bootstrap-%{version}.tar.xz

Provides:	gradle = %{version}
Conflicts:	gradle

Requires:	javapackages-tools
Requires:	java-devel

%description
Gradle %{version}, kept only as the offline bootstrap compiler for building
Gradle 9 from source. The user-facing Gradle package is built from source
and conflicts with this one.

%prep
%autosetup -n gradle-bootstrap-%{version}

%install
install -d -m 755 %{buildroot}%{_datadir}/gradle
/bin/cp -a payload/. %{buildroot}%{_datadir}/gradle/
rm -f %{buildroot}%{_datadir}/gradle/bin/gradle.bat
install -d -m 755 %{buildroot}%{_bindir}
ln -s %{_datadir}/gradle/bin/gradle %{buildroot}%{_bindir}/gradle

%files
%{_bindir}/gradle
%{_datadir}/gradle
%license LICENSE
%doc NOTICE
