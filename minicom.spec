Summary: 	TTY mode communications package ala Telix
Summary(de): 	TTY-Modus-Kommunikationspaket (�hnlich Telix)
Summary(fr): 	Package de communication en mode terminal � la Telix
Summary(pl):	Program komunikacyjny (podobny do Telix-a)
Summary(tr): 	Telix benzeri, TTY kipi ileti�im paketi
Name: 		minicom
Version: 	1.82
Release: 	2
Copyright: 	GPL
Group: 		Applications/Communications
Source: 	ftp://sunsite.unc.edu/pub/Linux/apps/serialcomm/dialout/%{name}-%{version}.src.tar.gz
Source1: 	minicom.wmconfig
Patch: 	        minicom.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Minicom is a communications program that resembles the MSDOS Telix
somewhat. It has a dialing directory, color, full ANSI and VT100
emulation, an (external) scripting language and more.

%description -l de
Minicom ist ein Kommunikationsprogramm, das �hnlichkeiten mit Telix 
unter MSDOS aufweist. Es enth�lt ein W�hlverzeichnis, Farbe, vollst�ndige ANSI-
und VT100-Emulation, eine (externe) Scriptsprache usw.

%description -l fr
Minicom est un programme de communication ressemblant a Telix sous
MSDOS. Il a un r�pertoire de num�rotation, des couleurs, une �mualtion
ANSI et VT100, un langage de script externe et plus encore.

%description -l pl
Minicom jest programem komunikacyjnym, przypominaj�cym DOSowy program
Telix. Posiada ksi��k� telefoniczn�, emulacj� terminali ANSI i VT100,
zewn�trzny j�zyk skryptowy, obs�ug� kolor�w i wiele innych zalet.

%description -l tr
Minicom, MSDOS Telix program�na benzeyen bir ileti�im program�d�r. Numara
�evirme dizini, renk, tam ANSI uyumu ve VT100 �yk�n�m� ile script gibi
�zellikleri vard�r.

%prep
%setup -q
%patch -p1 

%build
LDFLAGS=-s make -C src
 
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/{bin,man/man1}}

make -C src install R=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/minicom
strip $RPM_BUILD_ROOT%{_bindir}/* || :

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc demos doc tables
%attr(640,root, uucp) %config(noreplace) %verify(not size md5 mtime) /etc/minicom.users
%attr(2710,root, uucp) %{_bindir}/minicom
%attr(755,root,root) %{_bindir}/runscript
%attr(755,root,root) %{_bindir}/xminicom
%attr(755,root,root) %{_bindir}/ascii-xfr
%{_mandir}/man1/*
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/minicom

%changelog
* Thu Nov 12 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.82-2]
- added to minicom.patch allow build on system without libtermcap-devel and
  enables using $RPM_OPT_FLAGS on compile time.

* Sat Oct 10 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- added pl translation,
- defined files permission,
- allow building from non root account,
- moved changelog to the end of spec.

* Sun May 10 1998 Cristian Gafton <gafton@redhat.com>
- security fixes (alan cox, but he forgot about the changelog)

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu May 07 1998 Cristian Gafton <gafton@redhat.com>
- BuildRoot; updated .make patch to cope with the buildroot
- fixed the spec file

* Tue May 06 1998 Michael Maher <mike@redhat.com>
- update of package (1.81)

* Wed Oct 29 1997 Otto Hammersmith <otto@redhat.com>
- added wmconfig entries

* Tue Oct 21 1997 Otto Hammersmith <otto@redhat.com>
- fixed source url

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glib
