Summary:	Qt-based SAP music files player
Summary(pl):	Oparty na Qt odtwarzacz plików muzycznych SAP
Name:		saper
Version:	0.28
Release:	1
License:	GPL/freeware
Group:		X11/Applications/Multimedia
Source0:	http://asma.dspaudio.com/bin/%{name}-%{version}-src.tar.bz2
Patch0:		%{name}-system-libsap.patch
Patch1:		%{name}-ac-am.patch
URL:		http://asma.dspaudio.com/
BuildRequires:	libsap-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Qt-based SAP music files (known from Atari XL/XE) player.

%description -l pl
Oparty na Qt odtwarzacz plików muzycznych SAP (znanych z Atari XL/XE).

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
automake -a -c -f
%configure \
	--enable-mt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install saper/saper $RPM_BUILD_ROOT%{_bindir}
mv -f saper/stilview/README.txt README.stilview

gzip -9nf AUTHORS README README.stilview

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz saper/docs/en/*.html
%attr(755,root,root) %{_bindir}/saper
