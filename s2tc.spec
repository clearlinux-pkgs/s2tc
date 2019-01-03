#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : s2tc
Version  : f6ec862d7594e29ae80a6e49f66ad4c76cf09abc
Release  : 6
URL      : https://github.com/divVerent/s2tc/archive/f6ec862d7594e29ae80a6e49f66ad4c76cf09abc.tar.gz
Source0  : https://github.com/divVerent/s2tc/archive/f6ec862d7594e29ae80a6e49f66ad4c76cf09abc.tar.gz
Summary  : Library for S2TC texture compression
Group    : Development/Tools
License  : MIT
Requires: s2tc-bin = %{version}-%{release}
Requires: s2tc-lib = %{version}-%{release}
Requires: s2tc-license = %{version}-%{release}
Requires: s2tc-man = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : mesa-dev

%description
S2TC Environment Variables
==========================
Color Distance Function
-----------------------
The following color distance functions can be selected by setting the
environment variable `S2TC_COLORDIST_MODE`:

%package bin
Summary: bin components for the s2tc package.
Group: Binaries
Requires: s2tc-license = %{version}-%{release}
Requires: s2tc-man = %{version}-%{release}

%description bin
bin components for the s2tc package.


%package dev
Summary: dev components for the s2tc package.
Group: Development
Requires: s2tc-lib = %{version}-%{release}
Requires: s2tc-bin = %{version}-%{release}
Provides: s2tc-devel = %{version}-%{release}

%description dev
dev components for the s2tc package.


%package dev32
Summary: dev32 components for the s2tc package.
Group: Default
Requires: s2tc-lib32 = %{version}-%{release}
Requires: s2tc-bin = %{version}-%{release}
Requires: s2tc-dev = %{version}-%{release}

%description dev32
dev32 components for the s2tc package.


%package lib
Summary: lib components for the s2tc package.
Group: Libraries
Requires: s2tc-license = %{version}-%{release}

%description lib
lib components for the s2tc package.


%package lib32
Summary: lib32 components for the s2tc package.
Group: Default
Requires: s2tc-license = %{version}-%{release}

%description lib32
lib32 components for the s2tc package.


%package license
Summary: license components for the s2tc package.
Group: Default

%description license
license components for the s2tc package.


%package man
Summary: man components for the s2tc package.
Group: Default

%description man
man components for the s2tc package.


%prep
%setup -q -n s2tc-f6ec862d7594e29ae80a6e49f66ad4c76cf09abc
pushd ..
cp -a s2tc-f6ec862d7594e29ae80a6e49f66ad4c76cf09abc build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546521363
%autogen --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32"
%autogen --disable-static   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1546521363
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/s2tc
cp COPYING %{buildroot}/usr/share/package-licenses/s2tc/COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/s2tc_compress
%exclude /usr/bin/s2tc_decompress
%exclude /usr/bin/s2tc_from_s3tc

%files dev
%defattr(-,root,root,-)
%exclude /usr/include/txc_dxtn.h
%exclude /usr/lib64/pkgconfig/txc_dxtn.pc

%files dev32
%defattr(-,root,root,-)
%exclude /usr/lib32/pkgconfig/32txc_dxtn.pc
%exclude /usr/lib32/pkgconfig/txc_dxtn.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtxc_dxtn.so

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libtxc_dxtn.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/s2tc/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/s2tc_compress.1
/usr/share/man/man1/s2tc_decompress.1
/usr/share/man/man1/s2tc_from_s3tc.1
