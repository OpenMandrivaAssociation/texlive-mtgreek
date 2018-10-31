# revision 17967
# category Package
# catalog-ctan /macros/latex/contrib/mtgreek
# catalog-date 2010-04-21 23:25:04 +0200
# catalog-license lppl
# catalog-version 1.1+
Name:		texlive-mtgreek
Version:	1.1+
Release:	2
Summary:	Use italic and upright greek letters with mathtime
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mtgreek
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 754182
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719078
- texlive-mtgreek
- texlive-mtgreek
- texlive-mtgreek
- texlive-mtgreek

