Summary:	Qt-based SAP music files player
Summary(pl):	Oparty na Qt odtwarzacz plików muzycznych SAP
Name:		saper
Version:	0.28
Release:	3
License:	GPL/Freeware
Group:		X11/Applications/Sound
Source0:	http://asma.dspaudio.com/bin/%{name}-%{version}-src.tar.bz2
# Source0-md5:	b83162cd134de6de23192acbf0705c2d
Patch0:		%{name}-system-libsap.patch
Patch1:		%{name}-ac-am.patch
Patch2:		%{name}-gcc3.patch
URL:		http://asma.dspaudio.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsap-devel
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt-based SAP music files (known from Atari XL/XE) player.

%description -l pl
Oparty na Qt odtwarzacz plików muzycznych SAP (znanych z Atari XL/XE).

%prep
%setup -q -n %{name}-%{version}-src
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-mt

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
%doc AUTHORS README README.stilview saper/docs/en/*.html
%attr(755,root,root) %{_bindir}/saper
