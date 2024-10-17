Name:		texlive-novel
Version:	54512
Release:	2
Summary:	Class for printing fiction, such as novels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/novel
License:	lppl1.3c ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/novel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/novel.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LuaLaTeX document class is specifically written to meet
the needs of original fiction writers, who are typesetting
their own novels for non-color print-on-demand technology.
Built-in PDF/X is available, using new technology. The package
is well suited for detective novels, science fiction, and short
stories. It is however not recommended for creating color
picture books or dissertations.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/novel
%{_texmfdistdir}/fonts/opentype/novel
%doc %{_texmfdistdir}/doc/lualatex/novel

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
