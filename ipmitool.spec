#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipmitool
Version  : 1.8.18
Release  : 17
URL      : https://sourceforge.net/projects/ipmitool/files/ipmitool/1.8.18/ipmitool-1.8.18.tar.bz2
Source0  : https://sourceforge.net/projects/ipmitool/files/ipmitool/1.8.18/ipmitool-1.8.18.tar.bz2
Summary  : ipmitool - Utility for IPMI control
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ipmitool-bin = %{version}-%{release}
Requires: ipmitool-data = %{version}-%{release}
Requires: ipmitool-license = %{version}-%{release}
Requires: ipmitool-man = %{version}-%{release}
BuildRequires : ncurses-dev
BuildRequires : openssl-dev
BuildRequires : readline-dev
Patch1: 0002-openssl.patch
Patch2: ipmitool-1.8.18-fno-common.patch
Patch3: 0009-best-cipher.patch
Patch4: 0010-pef-missing-newline.patch
Patch5: CVE-2020-5208.patch

%description
This package contains a utility for interfacing with devices that support
the Intelligent Platform Management Interface specification.  IPMI is
an open standard for machine health, inventory, and remote power control.

This utility can communicate with IPMI-enabled devices through either a
kernel driver such as OpenIPMI or over the RMCP LAN protocol defined in
the IPMI specification.  IPMIv2 adds support for encrypted LAN
communications and remote Serial-over-LAN functionality.

It provides commands for reading the Sensor Data Repository (SDR) and
displaying sensor values, displaying the contents of the System Event
Log (SEL), printing Field Replaceable Unit (FRU) information, reading and
setting LAN configuration, and chassis power control.

%package bin
Summary: bin components for the ipmitool package.
Group: Binaries
Requires: ipmitool-data = %{version}-%{release}
Requires: ipmitool-license = %{version}-%{release}

%description bin
bin components for the ipmitool package.


%package data
Summary: data components for the ipmitool package.
Group: Data

%description data
data components for the ipmitool package.


%package doc
Summary: doc components for the ipmitool package.
Group: Documentation
Requires: ipmitool-man = %{version}-%{release}

%description doc
doc components for the ipmitool package.


%package license
Summary: license components for the ipmitool package.
Group: Default

%description license
license components for the ipmitool package.


%package man
Summary: man components for the ipmitool package.
Group: Default

%description man
man components for the ipmitool package.


%prep
%setup -q -n ipmitool-1.8.18
cd %{_builddir}/ipmitool-1.8.18
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594874447
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -fzero-call-used-regs=used "
%configure --disable-static --enable-intf-lanplus --enable-intf-usb --enable-intf-imb
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1594874447
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ipmitool
cp %{_builddir}/ipmitool-1.8.18/COPYING %{buildroot}/usr/share/package-licenses/ipmitool/4193a874862867b180608c3297b0239cc883b7d2
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipmievd
/usr/bin/ipmitool

%files data
%defattr(-,root,root,-)
/usr/share/ipmitool/oem_ibm_sel_map

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/ipmitool/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ipmitool/4193a874862867b180608c3297b0239cc883b7d2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ipmitool.1
/usr/share/man/man8/ipmievd.8
