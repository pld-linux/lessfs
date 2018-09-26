Summary:	Lessfs is an inline data deduplicating filesystem
Summary(pl.UTF-8):	Lessfs is an inline data deduplicating filesystem.
Name:		lessfs
Version:	1.7.0
Release:	1
License:	GPL v3
Group:		Applications
Source0:	http://downloads.sourceforge.net/lessfs/%{name}-%{version}.tar.gz
# Source0-md5:	8afdb925dba24a58b74fff74d7f3180e
Patch0:		openssl.patch
URL:		http://www.lessfs.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libfuse-devel >= 2.8.0
BuildRequires:	libtool
BuildRequires:	mhash-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	tokyocabinet-devel >= 1.4.21
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lessfs is an inline data deduplicating filesystem.

%description -l pl.UTF-8
Lessfs is an inline data deduplicating filesystem.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-crypto
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ ChangeLog README* etc/lessfs.cfg
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/lessfs.1*
%{_mandir}/man1/replogtool.1*
