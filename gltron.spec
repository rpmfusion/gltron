Name:           gltron
Version:        0.70
Release:        19%{?dist}
Summary:        A 3D game inspired by the movie TRON
Group:          Amusements/Games
License:        GPLv2
URL:            http://gltron.org
Source0:        http://download.sf.net/gltron/gltron-0.70-source.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         gltron-0.70-gcc.patch
Patch1:         gltron-0.70-no-use-misc.patch

#Debian patches, from gltron-0.70final/debian/patches/series
Patch20: amd64-ai.patch
Patch21: amd64-gcc40.patch
Patch22: cflags.patch
Patch23: disable-screenmenu.patch
Patch24: gcc-4.6.patch
Patch25: fix-clang-build.patch
Patch26: automake-error.patch
Patch27: gcc5.diff

BuildRequires:  SDL_sound-devel libpng-devel zlib-devel libGLU-devel
BuildRequires:  libvorbis-devel
BuildRequires:  desktop-file-utils
BuildRequires:  autoconf automake gcc-c++

%description
%{summary}.


%prep
%setup -q
%patch0 -p0 -b .gcc~
%patch1 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1

# remove generated files
rm aclocal.m4 config.guess config.sub configure depcomp install-sh missing \
mkinstalldirs Makefile.in

mv configure.in configure.ac


%build
autoreconf -iv
%configure --disable-warn
make %{?_smp_mflags}

%install
%make_install

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/pixmaps
desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications %{SOURCE1}


%files
%doc ChangeLog README
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.70-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.70-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.70-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.70-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.70-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.70-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.70-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.70-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 0.70-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 21 2016 Sérgio Basto <sergio@serjux.com> - 0.70-10
- Fix for rfbz #3926, copying some patches from Debian.
- Fix source URL.
- Add BR vorbis-devel.
- Use autoreconf (should suport better others arches).
- Add license tag.
- Change Licence from GPL to GPLv2.

* Sat May 16 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 0.70-9
- Fix FTBFS (rf#3631)

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 0.70-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.70-7
- Mass rebuilt for Fedora 19 Features

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.70-6
- Rebuilt for c++ ABI breakage

* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.70-5
- rebuild for new F11 features

* Sat Sep 27 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 0.70-4
- Fix rpm %%patch symantics change builderror

* Sun Aug 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.70-3
- rebuild

* Sun Nov 26 2006 Christopher Stone <chris.stone@gmail.com> 0.70-2
- Remove more unneeded BuildRequires

* Sun Nov 26 2006 Christopher Stone <chris.stone@gmail.com> 0.70-1
- Upstream sync
- Fix License tag
- Remove punctuation from Summary tag
- Remove unnecessary BR
- Some minor cleanups to spec file
- Remove CFLAGS patch
- Add --disable-warn to %%configure
- Add a gcc compile patch

* Sat Mar 25 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.70.0.3.beta.1
- fix BR

* Wed Mar 22 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
0.70.0.2.beta.1
- remove epoch
- fix release line

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Wed Nov 19 2003 Panu Matilainen <pmatilai@welho.com> 0.70-0.lvn.0.1.beta.1
- oops, release tag not right...

* Fri Nov 14 2003 Panu Matilainen <pmatilai@welho.com> 0.70-0.lvn.0.beta.1
- patch to honor RPM_OPT_FLAGS and remove -Werror causing build to fail

* Thu Nov 13 2003 Panu Matilainen <pmatilai@welho.com>
- Initial livna.org packaging.
