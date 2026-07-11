%global tl_name mtgreek
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1+
Release:	%{tl_revision}.1
Summary:	Use italic and upright greek letters with mathtime
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mtgreek
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mtgreek.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is an add-on to the MathTime a style to provide TeX support
for the use of the MathTime(tm) fonts (formerly distributed by YandY,
Inc.). The MathTime package has uppercase Greek letters hardwired to be
upright and only upright; this package provides a switch to choose
between the two kinds of Greek uppercase letters.

