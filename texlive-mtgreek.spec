Name:		texlive-mtgreek
Version:	1.1+
Release:	1
Summary:	Use italic and upright greek letters with mathtime
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mtgreek
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package is an add-on to the MathTime a style to provide
TeX support for the use of the MathTime(tm) fonts (formerly
distributed by YandY, Inc.). The MathTime package has uppercase
Greek letters hardwired to be upright and only upright; this
package provides a switch to choose between the two kinds of
Greek uppercase letters.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
