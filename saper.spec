Summary:	Qt-based SAP music files player
Summary(pl.UTF-8):	Oparty na Qt odtwarzacz plików muzycznych SAP
Name:		saper
Version:	0.3
Release:	1
Epoch:		1
License:	GPL/Freeware
Group:		X11/Applications/Sound
Source0:	http://asma.atari.org/bin/%{name}-%{version}-src.tar.bz2
# Source0-md5:	58db7dd8798129b01309e2440b351ae7
Patch0:		%{name}-system-libsap.patch
Patch1:		%{name}-ac-am.patch
URL:		http://asma.atari.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libsap-devel
BuildRequires:	qt-devel >= 2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt-based SAP music files (known from Atari XL/XE) player.

%description -l pl.UTF-8
Oparty na Qt odtwarzacz plików muzycznych SAP (znanych z Atari XL/XE).

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-mt \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install saper/saper $RPM_BUILD_ROOT%{_bindir}
mv -f saper/stilview/README.txt README.stilview

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README README.stilview
%attr(755,root,root) %{_bindir}/saper
