Summary:	Additional sound files for Asterisk PBX
Summary(pl.UTF-8):	Dodatkowe pliki dźwiękowe do centralki Asterisk
Name:		asterisk-sounds
Version:	1.2.1
Release:	1
License:	BSD
Group:		Applications/System
Source0:	ftp://ftp.digium.com/pub/asterisk/%{name}-%{version}.tar.gz
# Source0-md5:	bed4259905a7d7bc070c6319142b2075
URL:		http://www.asterisk.org/
Requires:	asterisk >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional sound files for Asterisk PBX.

%description -l pl.UTF-8
Dodatkowe pliki dźwiękowe do centralki PBX Asterisk.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt sounds-extra.txt sounds/silence/README-silence 
# /var/lib/asterisk/sounds{,/letters,/phonetic} belong to asterisk
/var/lib/asterisk/sounds/*.gsm
%dir /var/lib/asterisk/sounds/ha
/var/lib/asterisk/sounds/ha/*.gsm
/var/lib/asterisk/sounds/letters/*.gsm
/var/lib/asterisk/sounds/phonetic/*.gsm
%dir /var/lib/asterisk/sounds/silence
/var/lib/asterisk/sounds/silence/*.gsm
%dir /var/lib/asterisk/sounds/wx
/var/lib/asterisk/sounds/wx/*.gsm
