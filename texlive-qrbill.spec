Name:		texlive-qrbill
Version:	67724
Release:	1
Summary:	Create QR bills using LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/qrbill
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qrbill.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qrbill.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/qrbill.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides support for creating QR-bills for
the new Swiss payment standards. This open source
implementation is intended to offer a free option to support
these regulations and can be adapted for international use.
Packages loaded by qrbill are expl3, fontspec (except if one is
using a custom font setup), graphicx, scrbase, qrcode, iftex,
l3keys2e, and numprint.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/qrbill
%{_texmfdistdir}/tex/latex/qrbill
%{_texmfdistdir}/scripts/qrbill
%doc %{_texmfdistdir}/doc/latex/qrbill

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
