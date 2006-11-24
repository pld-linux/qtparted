#
# Conditional build:
%bcond_without	ext3		# build without ext3 support
%bcond_without	jfs		# build without jfs support
%bcond_without	ntfs		# build without ntfs support
%bcond_without	reiserfs 	# build without reiserfs support
%bcond_without	xfs		# build without xfs support
%bcond_with	static		# build statically linked qtparted
#
Summary:	QTParted is a Partition Magic clone
Summary(pl):	QTParted to klon Partition Magica
Name:		qtparted
Version:	0.4.5
Release:	4
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/qtparted/%{name}-%{version}.tar.bz2
# Source0-md5:	4541c0aa5475ba38d3cc518c921c8a34
Patch0:		%{name}-desktop.patch
URL:		http://qtparted.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	parted-devel >= 1.6.6
%{?with_static:BuildRequires:	parted-static}
%if %{with reiserfs}
BuildRequires:	progsreiserfs-devel >= 0.3.1
%{?with_static:BuildRequires:	progsreiserfs-static >= 0.3.1}
%endif
BuildRequires:	qt-devel >= 3.0.3
BuildRequires:	qt-linguist >= 3.0.3
BuildRequires:	rpm-build >= 4.3
Requires:	parted >= 1.6.6
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
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
export QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++
export PATH="$PATH:/usr/sbin:/sbin"
%{__make} -f admin/Makefile.common cvs
%configure \
	FSPATH_MKNTFS=/usr/sbin/mkntfs \
	FSPATH_NTFSRESIZE=/usr/sbin/ntfsresize \
	FSPATH_MKFSEXT3=/sbin/mkfs.ext3 \
	FSPATH_MKFSJFS=/sbin/mkfs.jfs \
	FSPATH_MKFSXFS=/sbin/mkfs.xfs \
	FSPATH_MOUNT=/bin/mount \
	FSPATH_UMOUNT=/bin/umount \
	FSPATH_XFS_GROWFS=/usr/sbin/xfs_growfs \
	%{!?with_xfs:--disable-xfs} \
	%{!?with_ntfs:--disable-ntfs} \
	%{!?with_ext3:--disable-ext3} \
	%{!?with_jfs:--disable-jfs} \
	%{!?with_reiserfs:--disable-reiserfs} \
	--%{?with_static:en}%{!?with_static:dis}able-static \
	--with-qt-libraries=%{_libdir}
%{__make}
sed -i -e "s/gksu/kdesu/g" data/qtparted.desktop

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	menudir=%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO doc
%attr(755,root,root) %{_sbindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%lang(ca) %{_datadir}/%{name}/locale/qtparted_ca.qm
%lang(cs) %{_datadir}/%{name}/locale/qtparted_cs.qm
%lang(de) %{_datadir}/%{name}/locale/qtparted_de.qm
%lang(es) %{_datadir}/%{name}/locale/qtparted_es.qm
%lang(fr) %{_datadir}/%{name}/locale/qtparted_fr.qm
%lang(it) %{_datadir}/%{name}/locale/qtparted_it.qm
%lang(pl) %{_datadir}/%{name}/locale/qtparted_pl.qm
%lang(ru) %{_datadir}/%{name}/locale/qtparted_ru.qm
%lang(ua) %{_datadir}/%{name}/locale/qtparted_ua.qm
%{_datadir}/%{name}/pics
%{_pixmapsdir}/*.xpm
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
