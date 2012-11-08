Name:           videoproto
Version:        2.3.1
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          Development/System
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)

%description
Description: %{summary}
This extension provides a protocol for a video output mechanism,
mainly to rescale video playback in the video controller hardware.

%prep
%setup -q

%build

%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs

%files
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
