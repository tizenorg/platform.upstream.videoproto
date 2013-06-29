Name:           videoproto
Version:        2.3.1
Release:        1
License:        MIT
Summary:        X
Url:            http://www.x.org
Group:          Development/System
Source0:        %{name}-%{version}.tar.bz2
Source1001: 	videoproto.manifest

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)

%description
Description: %{summary}
This extension provides a protocol for a video output mechanism,
mainly to rescale video playback in the video controller hardware.

%prep
%setup -q
cp %{SOURCE1001} .

%build

%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs

%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
