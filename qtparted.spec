%define		subver		1
Summary:	QTParted is a Partition Magic clone
Summary(pl):	QTParted to klon Partition Magica
Name:		qtparted
Version:	0.2.2
Release:	1
License:	GPL v2
Vendor:		Vanni Brutto <zanac@libero.it>
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}_%{version}-%{subver}.tar.gz
URL:		http://qtparted.sourceforge.net/
BuildRequires:	parted-devel >= 1.6.3
BuildRequires:	progsreiserfs-devel >= 0.3.1
BuildRequires:	qt-devel >= 3.0.3
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
./configure \
	 --prefix=/usr \
	 --qtdir=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/qtparted $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README TODO AUTHORS TODO
%attr(755,root,root) %{_bindir}/*
