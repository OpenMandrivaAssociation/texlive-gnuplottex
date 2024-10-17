Name:		texlive-gnuplottex
Version:	54758
Release:	2
Summary:	Embed Gnuplot commands in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gnuplottex
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gnuplottex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gnuplottex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gnuplottex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extracts Gnuplot code from the document and writes
it to .gnuplot files. If shell escape is enabled, the graph
files are automatically processed and converted to PostScript
or PDF files, which will then be included. If shell escape is
disabled, the user has to run the files through gnuplot, and
re-run the LaTeX job.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gnuplottex
%doc %{_texmfdistdir}/doc/latex/gnuplottex
#- source
%doc %{_texmfdistdir}/source/latex/gnuplottex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
