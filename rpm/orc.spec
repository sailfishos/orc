Name:       orc
Summary:    The Oil Run-time Compiler
Version:    0.4.34
Release:    1
License:    BSD
URL:        https://github.com/sailfishos/orc
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: meson

%description
Orc is a library and set of tools for compiling and executing
very simple programs that operate on arrays of data.  The "language"
is a generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.

%package compiler
Summary:    Orc compiler
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description compiler
The Orc compiler, to produce optimized code.

%package devel
Summary:    Development files and static libraries for Orc
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-compiler
Requires:   pkgconfig

%description devel
This package contains the files needed to build packages that depend
on orc.

%prep
%autosetup -p1 -n %{name}-%{version}/orc

%build
%meson -Ddefault_library=shared -Dgtk_doc=disabled
%meson_build

%install

%meson_install

# Remove unneeded files.
find %{buildroot}/%{_libdir} -name \*.a -delete

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/liborc-*.so.*

%files compiler
%defattr(-,root,root,-)
%{_bindir}/orcc

%files devel
%defattr(-,root,root,-)
%{_includedir}/orc-0.4/
%{_libdir}/liborc-*.so
%{_libdir}/pkgconfig/orc-0.4.pc
%{_libdir}/pkgconfig/orc-test-0.4.pc
%{_bindir}/orc-bugreport
