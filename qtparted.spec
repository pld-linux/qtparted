# Conditional Build:
%bcond_without	ext3		# build without ext3 support
%bcond_without	jfs		# build without jfs support
%bcond_without	ntfs		# build without ntfs support
%bcond_without 	reiserfs 	# build without reiserfs support
%bcond_without	xfs		# build without xfs support
%bcond_with 	static		# don't build static
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
BuildRequires:	parted-devel >= 1.6.3
BuildRequires:	progsreiserfs-devel >= 0.3.1
BuildRequires:	qt-devel >= 3.0.3i
BuildRequires:	rpm-build >= 4.3
BuildRequires:	parted-static
%if %{with xfs}
BuildRequires:	xfsprogs
%endif 
%if %{with ntfs}
BuildRequires:	ntfsprogs
%endif
%if %{with ext3}
BuildRequires:	e2fsprogs
%endif
%if %{with jfs}
BuildRequires:	jfsutils
%endif
%if %{with reiserfs}
BuildRequires:	reiserfsprogs
BuildRequires:	progsreiserfs-static
%endif
%if %{with reiserfs} && %{with static}
BuildRequires:	reiserfsprogs-static
%endif
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
