# revision 32277
# category Package
# catalog-ctan /macros/latex/contrib/gnuplottex
# catalog-date 2013-11-29 10:11:23 +0100
# catalog-license gpl2
# catalog-version 0.8
Name:		texlive-gnuplottex
Version:	0.8.0
Release:	1
Summary:	Embed Gnuplot commands in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gnuplottex
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gnuplottex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gnuplottex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gnuplottex.source.tar.xz
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
%{_texmfdistdir}/tex/latex/gnuplottex/gnuplottex.sty
%doc %{_texmfdistdir}/doc/latex/gnuplottex/README
%doc %{_texmfdistdir}/doc/latex/gnuplottex/SomeValuesForGnuplot.txt
%doc %{_texmfdistdir}/doc/latex/gnuplottex/example-pdf.tex
%doc %{_texmfdistdir}/doc/latex/gnuplottex/example.gnuplot
%doc %{_texmfdistdir}/doc/latex/gnuplottex/gnuplottex.pdf
%doc %{_texmfdistdir}/doc/latex/gnuplottex/gpl.txt
#- source
%doc %{_texmfdistdir}/source/latex/gnuplottex/gnuplottex.dtx
%doc %{_texmfdistdir}/source/latex/gnuplottex/gnuplottex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
