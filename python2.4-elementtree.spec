%define module		elementtree
%define name		python2.4-%{module}
%define version		1.2.6
%define date_version	20050316
%define release		%mkrel 3
%define __python    %{_bindir}/python2.4

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:        Fast XML parser and writer
Group: 		Development/Python
License:	Python license
URL:            http://effbot.org/zone/element-index.htm
Source0:        http://effbot.org/downloads/%{module}-%{version}-%{date_version}.tar.gz
Requires:       expat
Requires:       python >= 2.2
BuildRequires:	python2.4-devel
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
The Element type is a simple but flexible container object, designed
to store hierarchical data structures, such as simplified XML
infosets, in memory. The element type can be described as a cross
between a Python list and a Python dictionary.

%prep
%setup -q -n %{module}-%{version}-%{date_version}

# fix encoding
for file in `find . -type f`; do
    perl -pi -e 'BEGIN {exit unless -T $ARGV[0];} tr/\r//d;' $file
done


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --record INSTALLED_FILES


%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc docs samples README* CHANGES* benchmark.py

