%define		line	ubuntu-9.10
Summary:	On-screen-display notification agent
Name:		notify-osd
Version:	0.9.24
Release:	1
License:	GPLv3
Group:		Applications/System
URL:		https://edge.launchpad.net/notify-osd
Source0:	http://edge.launchpad.net/notify-osd/trunk/%{line}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	b3670469df029546c585d35377025d52
BuildRequires:	GConf2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel
Obsoletes:	dbus(org.freedesktop.Notifications)
Provides:	dbus(org.freedesktop.Notifications)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Desktop Notifications framework provides a standard way of doing
passive pop-up notifications on the Linux desktop. These are designed
to notify the user of something without interrupting their work with a
dialog box that they must close. Passive popups can automatically
disappear after a short period of time.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS COPYING
%attr(755,root,root) %{_libexecdir}/notify-osd
%{_datadir}/dbus-1/services/org.freedesktop.Notifications.service
%{_datadir}/notify-osd
