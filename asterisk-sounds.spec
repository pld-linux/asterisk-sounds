
Summary:	Additional sound files for Asterisk PBX
Summary(pl):	Dodatkowe pliki d�wi�kowe do centralki Asterisk
Name:		asterisk-sounds
Version:	1.0.0
Release:	1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.digium.com/pub/asterisk/%{name}-%{version}.tar.gz
# Source0-md5:	6f969ad544db7e222b01725c732b38a1
Requires:	asterisk >= 1.0.0
URL:		http://www.asterisk.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional sound files for Asterisk PBX.

%description -l pl
Dodatkowe pliki d�wi�kowe do centralki PBX Asterisk.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt sounds-extra.txt sounds/silence/README-silence 
%dir /var/lib/asterisk/sounds/silence
/var/lib/asterisk/sounds/*.gsm
/var/lib/asterisk/sounds/letters/*.gsm
/var/lib/asterisk/sounds/phonetic/*.gsm
/var/lib/asterisk/sounds/silence/*.gsm
