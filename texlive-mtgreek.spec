Name:		texlive-mtgreek
Version:	17967
Release:	2
Summary:	Use italic and upright greek letters with mathtime
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mtgreek
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is an add-on to the MathTime a style to provide
TeX support for the use of the MathTime(tm) fonts (formerly
distributed by YandY, Inc.). The MathTime package has uppercase
Greek letters hardwired to be upright and only upright; this
package provides a switch to choose between the two kinds of
Greek uppercase letters.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mtgreek/mtgreek.sty
%doc %{_texmfdistdir}/doc/latex/mtgreek/mtgreek.pdf
%doc %{_texmfdistdir}/doc/latex/mtgreek/mtgreek.tex
%doc %{_texmfdistdir}/doc/latex/mtgreek/mtgtest.tex
#- source
%doc %{_texmfdistdir}/source/latex/mtgreek/mtgreek.dtx
%doc %{_texmfdistdir}/source/latex/mtgreek/mtgreek.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
