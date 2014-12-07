%define major 0
%define libname %mklibname OpenVG %{major}
%define devname %mklibname OpenVG -d
%define debug_package %nil

Name: shivavg
Version: 0.2.1
Release: 2
Source0: http://garr.dl.sourceforge.net/project/shivavg/ShivaVG/%{version}/ShivaVG-%{version}.zip
Patch0: ShivaVG-0.2.1-compile.patch
Summary: An implementation of the OpenVG vector graphics API
URL: http://shivavg.sf.net/
License: LGPLv2.1
Group: System/Libraries
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(glut)
BuildRequires: jpeg-devel

%description
An implementation of the OpenVG vector graphics API on top of OpenGL

%package -n %{libname}
Summary: An implementation of the OpenVG vector graphics API
Group: System/Libraries

%description -n %{libname}
An implementation of the OpenVG vector graphics API on top of OpenGL

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
# ShivaVG 0.2.1 implements the OpenVG standard 1.0, so...
Provides: openvg-devel = 1.0

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -qn ShivaVG-%{version}
%apply_patches
chmod +x autogen.sh ; ./autogen.sh

%configure

%build
%make

%install
%makeinstall_std

# Since there seems to be some disagreement about
# %{_includedir}/vg vs. %{_includedir}/VG in the standard,
# let's support both...
ln -s vg %{buildroot}%{_includedir}/VG

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/vg
%{_includedir}/VG
%{_libdir}/*.so
