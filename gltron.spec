Name:           gltron
Version:        0.70
Release:        9%{?dist}
Summary:        A 3D game inspired by the movie TRON
Group:          Amusements/Games
License:        GPL
URL:            http://gltron.org
Source0:        http://dl.sf.net/gltron/gltron-0.70-source.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         gltron-0.70-gcc.patch
Patch1:         gltron-0.70-no-use-misc.patch
BuildRequires:  SDL_sound-devel libpng-devel zlib-devel libGLU-devel
BuildRequires:  desktop-file-utils

%description
%{summary}.


%prep
%setup -q
%patch0 -p0 -b .gcc~
%patch1 -p1


%build
%configure --disable-warn
make %{?_smp_mflags}

%install
%make_install

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_datadir}/pixmaps
desktop-file-install --dir $RPM_BUILD_ROOT/%{_datadir}/applications %{SOURCE1}


%files
%doc COPYING ChangeLog README 
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
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
