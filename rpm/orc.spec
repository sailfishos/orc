Name:       orc
Summary:    The Oil Run-time Compiler
Version:    0.4.26
Release:    1
Group:      System/Libraries
License:    BSD
URL:        http://code.entropywave.com/projects/orc/
Source0:    http://code.entropywave.com/download/orc/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  libtool

%description
Orc is a library and set of tools for compiling and executing
very simple programs that operate on arrays of data.  The "language"
is a generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%package compiler
Summary:    Orc compiler
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description compiler
The Orc compiler, to produce optimized code.

%package devel
Summary:    Development files and static libraries for Orc
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-compiler
Requires:   pkgconfig

%description devel
This package contains the files needed to build packages that depend
on orc.

%prep
%setup -q -n %{name}-%{version}/orc

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
  --disable-gtk-doc \
  --enable-shared \
  --disable-static

make %{?jobs:-j%jobs}

%install
%make_install

# Remove unneeded files.
find %{buildroot}/%{_libdir} -name \*.a -or -name \*.la -delete

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/liborc-*.so.*

%files compiler
%defattr(-,root,root,-)
%{_bindir}/orcc

%files devel
%defattr(-,root,root,-)
%{_includedir}/orc-0.4/
%{_libdir}/liborc-*.so
%{_libdir}/pkgconfig/orc-0.4.pc
%{_bindir}/orc-bugreport
%{_datadir}/aclocal/orc.m4
