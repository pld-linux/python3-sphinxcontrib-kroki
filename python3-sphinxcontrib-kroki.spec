Summary:	Kroki integration into Sphinx
Summary(pl.UTF-8):	Integracja Kroki ze Sphinksem
Name:		python3-sphinxcontrib-kroki
Version:	1.3.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-kroki/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-kroki/sphinxcontrib-kroki-%{version}.tar.gz
# Source0-md5:	a3c7fe6c119fdcc302167fc812d47710
URL:		https://pypi.org/project/sphinxcontrib-kroki/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
Requires:	python3-sphinxcontrib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Embed PlantUML, DOT, etc. diagrams in your Sphinx-based documentation
using kroki (<https://kroki.io/>).

%description -l pl.UTF-8
Osadzanie diagramów PlantUML, DOT itp. w dokumentacji opertej na
Sphinksie przy użyciu kroki (<https://kroki.io/>).

%prep
%setup -q -n sphinxcontrib-kroki-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/sphinxcontrib/kroki
%{py3_sitescriptdir}/sphinxcontrib_kroki-%{version}-py*.egg-info
