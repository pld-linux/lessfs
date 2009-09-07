Summary:	Lessfs is an inline data deduplicating filesystem
Summary(pl.UTF-8):	Lessfs is an inline data deduplicating filesystem.
Name:		lessfs
Version:	0.6.1
Release:	0.1
License:	GPL v3
Group:		Applications
Source0:	http://dl.sourceforge.net/lessfs/%{name}-%{version}.tar.gz
# Source0-md5:	792f3012eae343bc04314b868f6fd1b9
URL:		http://www.lessfs.com/
BuildRequires:	libfuse-devel >= 2.8.0
BuildRequires:	tokyocabinet-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lessfs is an inline data deduplicating filesystem.

%description -l pl.UTF-8
Lessfs is an inline data deduplicating filesystem.

%prep
%setup -q

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

install -D etc/lessfs.cfg $RPM_BUILD_ROOT%{_sysconfdir}/lessfs.cfg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/lessfs.1*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lessfs.cfg
