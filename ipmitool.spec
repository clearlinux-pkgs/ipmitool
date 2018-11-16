#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ipmitool
Version  : 1.8.18
Release  : 11
URL      : http://downloads.sourceforge.net/project/ipmitool/ipmitool/1.8.18/ipmitool-1.8.18.tar.bz2
Source0  : http://downloads.sourceforge.net/project/ipmitool/ipmitool/1.8.18/ipmitool-1.8.18.tar.bz2
Summary  : ipmitool - Utility for IPMI control
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ipmitool-bin
Requires: ipmitool-doc
Requires: ipmitool-data
BuildRequires : ncurses-dev
BuildRequires : openssl-dev
BuildRequires : readline-dev

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
Requires: ipmitool-data

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

%description doc
doc components for the ipmitool package.


%prep
%setup -q -n ipmitool-1.8.18

%build
export LANG=C
%configure --disable-static --enable-intf-lanplus --enable-intf-usb --enable-intf-imb
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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
%defattr(-,root,root,-)
%doc /usr/share/doc/ipmitool/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*
