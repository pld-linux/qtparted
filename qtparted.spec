# Conditional Build:
# _without_ntfs		build without ntfs support
# _without_ext3		build without ext3 support
# _without_xfs		build without xfs support
# _without_jfs		build without jfs support
# _without_reiserfs	build without reiserfs support
# _without_static	don't build static
Summary:	QTParted is a Partition Magic clone
Summary(pl):	QTParted to klon Partition Magica
Name:		qtparted
Version:	0.3.2
Release:	0.1
License:	GPL v2
Vendor:		Vanni Brutto <zanac@libero.it>
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	fad16013cb070c8cac0f820489cbf75f
Patch0:		%{name}-conf.patch
URL:		http://qtparted.sourceforge.net/
BuildRequires:	parted-devel >= 1.6.3
BuildRequires:	progsreiserfs-devel >= 0.3.1
BuildRequires:	qt-devel >= 3.0.3i
%{!?_without_xfs:BuildRequires:		xfsprogs}
%{!?_without_ntfs:BuildRequires:	ntfsprogs}
%{!?_without_ext3:BuildRequires:	e2fsprogs}
%{!?_without_jfs:BuildRequires:		jfsutils}
%{!?_without_reiserfs:BuildRequires:	reiserfsprogs}
Requires:	parted >= 1.6.3
Requires:	progsreiserfs >= 0.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QTParted is a Partition Magic clone written in C++ using the Qt
toolkit.

%description -l pl
QTParted to klon Partition Magica napisany w C++ przy u¿yciu toolkitu
Qt.

%prep
%setup -q
#%patch -p1

%build
export QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++
export PATH="$PATH:/usr/sbin:/sbin"
%configure \
	%{?_without_xfs:--disable-xfs} \
	%{?_without_ntfs:--disable-ntfs} \
	%{?_without_ext3:--disable-ext3} \
	%{?_without_jfs:--disable-jfs} \
	%{?_without_reiserfs:--disable-reiserfs} \
	--%{?_without_static:dis}%{!?_without_static:en}able-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README TODO AUTHORS TODO doc
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
%{_pixmapsdir}/*
%{_datadir}/%{name}/*
