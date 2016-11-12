%include SPECS/.buildid.rpmmacro

Name:		upsilon-reactor
Version:	%{version_formatted_short}
Release:	%{version_formatted_short}.%{timestamp}.%{?dist}
Summary:	Upsilon Reactor
BuildArch: noarch

Group:		Applications/System
License:	GPLv2
URL:		http://upsilon-project.co.uk
Source0:	upsilon-reactor.zip

BuildRequires:	python
Requires:	upsilon-pycommon

%description


%prep
%setup -q -n upsilon-reactor-%{tag}


%build

%install

mkdir -p %{buildroot}/usr/share/upsilon-reactor/
cp src/* %{buildroot}/usr/share/upsilon-reactor/

mkdir -p %{buildroot}/usr/lib/systemd/system
cp var/upsilon-reactor.service %{buildroot}/var/lib/systemd/system/

%files
/usr/share/upsilon-reactor
/usr/lib/systemd/system/upsilon-reactor.service
