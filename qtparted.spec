Summary:	QTParted is a Partition Magic clone
Summary(pl):	QTParted to klon Partition Magic'a
Name:		qtparted
Version:	0.1.8
Release:	0.2
License:	GPL v2
Vendor:		Vanni Brutto <zanac@libero.it>
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}_%{version}-1.tar.gz
Patch0:		%{name}-conf.patch
URL:		http://qtparted.sourceforge.net/
BuildRequires:	parted-devel >= 1.6.3
BuildRequires:	qt >= 3.0.3
BuildRequires:	progsreiserfs-devel >= 0.3.1
Requires:	parted >= 1.6.3
Requires:	progsreiserfs >= 0.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QTParted is a Partition Magic clone written in C++ using the Qt
toolkit.

%description -l pl
QTParted is a Partition Magic clone written in C++ using the Qt
toolkit.

%prep
%setup -q

%patch0 -p1

%build
export QTDIR=%{_prefix}
export QMAKESPEC=%{_datadir}/qt/mkspecs/linux-g++
./configure
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
%{_bindir}/*
