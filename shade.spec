%global sum     Simple client library for interacting with OpenStack clouds

Name:           shade
Version:        1.20.0
Release:        1%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            http://docs.openstack.org/infra/shade/
Source0:        http://tarballs.openstack.org/shade/shade-%{version}.tar.gz

BuildArch:      noarch


%description
shade is a simple client library for interacting with OpenStack clouds. The
key word here is *simple*. Clouds can do many many many things - but there are
probably only about 10 of them that most people care about with any
regularity. If you want to do complicated things, you should probably use
the lower level client libraries - or even the REST API directly. However,
if what you want is to be able to write an application that talks to clouds
no matter what crazy choices the deployer has made in an attempt to be
more hipster than their self-entitled narcissist peers, then shade is for you.


%package -n python2-shade
Summary:        %sum

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-pbr

Requires:       python2-pbr
Requires:       python-munch
Requires:       python-decorator
Requires:       python2-jmespath
Requires:       python2-jsonpatch
Requires:       python-ipaddress
Requires:       python2-os-client-config
Requires:       python2-requestsexceptions
Requires:       python-six
Requires:       python2-keystoneauth1
Requires:       python-netifaces
Requires:       python-dogpile-cache

Requires:       python-novaclient
Requires:       python-keystoneclient
Requires:       python-ironicclient
Requires:       python-designateclient


%description -n python2-shade
%{sum}

%prep
%autosetup -n %{name}-%{version}


%build
PBR_VERSION=%{version} %{__python2} setup.py build


%install
PBR_VERSION=%{version} %{__python2} setup.py install --skip-build --root %{buildroot}


%files
%license LICENSE


%files -n python2-shade
%{python2_sitelib}/shade-%{version}-py*.egg-info
%{python2_sitelib}/shade
%{_bindir}/shade-inventory


%changelog
* Wed May 31 2017 David Moreau Simard <dmsimard@redhat.com> - 1.20.0-1
- Update to upstream 1.20.0

* Tue Mar 14 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 1.13.2-1
- Initial packaging
