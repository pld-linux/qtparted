%bcond_without	ext3		# build without ext3 support
%bcond_without	jfs		# build without jfs support
%bcond_without	ntfs		# build without ntfs support
%bcond_without 	reiserfs 	# build without reiserfs support
%bcond_without	xfs		# build without xfs support
%bcond_with 	static		# build statically linked qtparted
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
URL:		http://qtparted.sourceforge.net/
%{?with_ext3:BuildRequires:	e2fsprogs}
%{?with_jfs:BuildRequires:	jfsutils}
%if %{with ntfs}
%{?with_ntfs:BuildRequires:	ntfsprogs}
%endif
BuildRequires:	parted-devel >= 1.6.3
%{?with_static:BuildRequires:	parted-static}
%if %{with reiserfs}
BuildRequires:	progsreiserfs-devel >= 0.3.1
%{?with_static:BuildRequires:	progsreiserfs-static >= 0.3.1}
%endif
BuildRequires:	qt-devel >= 3.0.3
%{?with_reiserfs:BuildRequires:	reiserfsprogs}
BuildRequires:	rpm-build >= 4.3
%{?with_xfs:BuildRequires:	xfsprogs}
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

%build
export QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++
export PATH="$PATH:/usr/sbin:/sbin"
%configure \
	%{?_without_xfs:--disable-xfs} \
	%{?_without_ntfs:--disable-ntfs} \
	%{?_without_ext3:--disable-ext3} \
	%{?_without_jfs:--disable-jfs} \
	%{?_without_reiserfs:--disable-reiserfs} \
	--%{?with_static:en}%{!?with_static:dis}able-static
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
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%lang(cs) %{_datadir}/%{name}/locale/qtparted_cs.qm
%lang(de) %{_datadir}/%{name}/locale/qtparted_de.qm
%lang(es) %{_datadir}/%{name}/locale/qtparted_es.qm
%lang(fr) %{_datadir}/%{name}/locale/qtparted_fr.qm
%lang(it) %{_datadir}/%{name}/locale/qtparted_it.qm
%lang(pl) %{_datadir}/%{name}/locale/qtparted_pl.qm
%{_datadir}/%{name}/pics
