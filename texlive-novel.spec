%global tl_name novel
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2
Release:	%{tl_revision}.1
Summary:	Class for printing fiction, such as novels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/novel
License:	lppl1.3c ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/novel.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/novel.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LuaLaTeX document class is specifically written to meet the needs
of original fiction writers, who are typesetting their own novels for
non-color print-on-demand technology. Built-in PDF/X is available, using
new technology. The package is well suited for detective novels, science
fiction, and short stories. It is however not recommended for creating
color picture books or dissertations.

