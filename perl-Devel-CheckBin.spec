#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Devel-CheckBin
Version  : 0.04
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Devel-CheckBin-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Devel-CheckBin-0.04.tar.gz
Summary  : 'check that a command is available'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Devel-CheckBin-license = %{version}-%{release}
Requires: perl-Devel-CheckBin-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
# NAME
Devel::CheckBin - check that a command is available
# SYNOPSIS
use Devel::CheckBin;

%package dev
Summary: dev components for the perl-Devel-CheckBin package.
Group: Development
Provides: perl-Devel-CheckBin-devel = %{version}-%{release}
Requires: perl-Devel-CheckBin = %{version}-%{release}

%description dev
dev components for the perl-Devel-CheckBin package.


%package license
Summary: license components for the perl-Devel-CheckBin package.
Group: Default

%description license
license components for the perl-Devel-CheckBin package.


%package perl
Summary: perl components for the perl-Devel-CheckBin package.
Group: Default
Requires: perl-Devel-CheckBin = %{version}-%{release}

%description perl
perl components for the perl-Devel-CheckBin package.


%prep
%setup -q -n Devel-CheckBin-0.04
cd %{_builddir}/Devel-CheckBin-0.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Devel-CheckBin
cp %{_builddir}/Devel-CheckBin-0.04/LICENSE %{buildroot}/usr/share/package-licenses/perl-Devel-CheckBin/cbc561be3b1630fa2f6cdb69dfc4215b3e1a51bb
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Devel::CheckBin.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Devel-CheckBin/cbc561be3b1630fa2f6cdb69dfc4215b3e1a51bb

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Devel/CheckBin.pm
