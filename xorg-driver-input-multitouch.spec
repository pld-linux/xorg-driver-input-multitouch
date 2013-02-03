%define		subver 20110303
%define		rel		1
Summary:	Multitouch X input driver
Name:		xorg-driver-input-multitouch
Version:	1.0
Release:	0.rc2.%{subver}.%{rel}
License:	GPL v2+
Group:		X11/Applications
Source0:	xf86-input-multitouch-%{subver}.tar.bz2
Source1:	xf86-input-multitouch.conf
Patch0:		libdir.patch
URL:		http://bitmath.org/code/multitouch/
BuildRequires:	mtdev-devel >= 1.1.0
BuildRequires:	pixman-devel
BuildRequires:	sed >= 4.0
%{?requires_xorg_xserver_xinput}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This X input driver provides gestures support for multitouch
touchpads, in particular those with integrated button.

%prep
%setup -q -n xf86-input-multitouch-%{subver}
%patch0 -p1

%{__sed} -i -e 's,gcc,$(CC),g' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	OPTS="%{rpmcflags} -fPIC" \
	LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	LIBDIR=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/40-xf86-input-multitouch.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CREDITS
%{_datadir}/X11/xorg.conf.d/40-xf86-input-multitouch.conf
%{_libdir}/xorg/modules/input/multitouch.so
