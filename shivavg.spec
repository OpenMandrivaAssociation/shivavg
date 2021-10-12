# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define major 0
%define libname %mklibname OpenVG %{major}
%define devname %mklibname OpenVG -d

Summary: An implementation of the OpenVG vector graphics API
Name: shivavg
Version: 0.2.1
Release: 7
License: LGPLv2.1
Group: System/Libraries
URL: http://shivavg.sf.net/
Source0: http://garr.dl.sourceforge.net/project/shivavg/ShivaVG/%{version}/ShivaVG-%{version}.zip
Patch0: ShivaVG-0.2.1-compile.patch
Patch1: ShivaVG-0.2.1-GL-linkage.patch
Patch2: ShivaVG-0.2.1-fix-build.patch
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(glut)
BuildRequires: pkgconfig(libjpeg)

%description
An implementation of the OpenVG vector graphics API on top of OpenGL.

%package -n %{libname}
Summary: An implementation of the OpenVG vector graphics API
Group: System/Libraries

%description -n %{libname}
An implementation of the OpenVG vector graphics API on top of OpenGL.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
# ShivaVG 0.2.1 implements the OpenVG standard 1.0, so...
Provides: openvg-devel = 1.0

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -n ShivaVG-%{version} -p1

chmod +x autogen.sh ; ./autogen.sh

%build
%configure
%make_build

%install
%make_install

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
