%define major 1
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %{name} -d
%define libnamedevst %mklibname %{name} -d -s

Name:		alure
Summary:	Audio Library Tools REloaded
Group:		System/Libraries
Version:	1.2
Release:	5
License:	LGPLv2+
URL:		http://kcat.strangesoft.net/alure.html
Source0:	http://kcat.strangesoft.net/%{name}-releases/%{name}-%{version}.tar.bz2
Patch0:		alure-gcc47.patch
Patch1:		alure-dumb2.patch
BuildRequires:	cmake
BuildRequires:	dumb-devel
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(openal)

%description
ALURE is a utility library to help manage common tasks with OpenAL 
applications. This includes device enumeration and initialization, 
file loading, and streaming.


#------------------------------------------------------------------------------
%package -n %{libname}
Summary:	%{name} library
Group:		System/Libraries

%files -n %{libname}
%{_libdir}/libalure.so.%{major}*

%description -n %{libname}
Libraries needed by %{name}.

ALURE is a utility library to help manage common tasks with OpenAL 
applications. This includes device enumeration and initialization, 
file loading, and streaming.


#------------------------------------------------------------------------------
%package -n %{libnamedev}
Summary:	Alure development files
Group:		Development/C++
License:	LGPLv2+,GPLv2+
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{libnamedev}
Libraries and header files to develop applications that use %{name}.

ALURE is a utility library to help manage common tasks with OpenAL 
applications. This includes device enumeration and initialization, 
file loading, and streaming.

%files -n %{libnamedev}
%doc COPYING
%{_docdir}/%{name}
%{_includedir}/AL
%{_libdir}/libalure.so
%{_libdir}/pkgconfig/alure*.pc


#------------------------------------------------------------------------------
%package -n %{libnamedevst}
Summary:	Alure static library
Group:		Development/C++
License:	LGPLv2+,GPLv2+
Requires:	%{libnamedev} = %{version}-%{release}

%description -n %{libnamedevst}
Static library file to develop applications that use %{name}.

ALURE is a utility library to help manage common tasks with OpenAL
applications. This includes device enumeration and initialization,
file loading, and streaming.

%files -n %{libnamedevst}
%{_libdir}/libalure-static.a


#------------------------------------------------------------------------------
%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
%cmake

%install
%make_install -C build

%files
%{_bindir}/*
