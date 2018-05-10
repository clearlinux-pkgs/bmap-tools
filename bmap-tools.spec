#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC1D2265F9856446F (kad@kad.name)
#
Name     : bmap-tools
Version  : 3.4
Release  : 2
URL      : https://github.com/intel/bmap-tools/releases/download/v3.4/bmap-tools-3.4.tgz
Source0  : https://github.com/intel/bmap-tools/releases/download/v3.4/bmap-tools-3.4.tgz
Source99 : https://github.com/intel/bmap-tools/releases/download/v3.4/bmap-tools-3.4.tgz.asc
Summary  : Tools to generate block map (AKA bmap) and flash images using bmap
Group    : Development/Tools
License  : GPL-2.0
Requires: bmap-tools-bin
Requires: bmap-tools-python3
Requires: bmap-tools-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Tools to generate block map (AKA bmap) and flash images using bmap. Bmaptool is
a generic tool for creating the block map (bmap) for a file, and copying files
using the block map. The idea is that large file containing unused blocks, like
raw system image files, can be copied or flashed a lot faster with bmaptool
than with traditional tools like "dd" or "cp". See
source.tizen.org/documentation/reference/bmaptool for more information.

%package bin
Summary: bin components for the bmap-tools package.
Group: Binaries

%description bin
bin components for the bmap-tools package.


%package python
Summary: python components for the bmap-tools package.
Group: Default
Requires: bmap-tools-python3

%description python
python components for the bmap-tools package.


%package python3
Summary: python3 components for the bmap-tools package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bmap-tools package.


%prep
%setup -q -n bmap-tools-3.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1524241285
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bmaptool

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
