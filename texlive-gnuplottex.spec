# revision 23918
# category Package
# catalog-ctan /macros/latex/contrib/gnuplottex
# catalog-date 2011-09-12 16:50:58 +0200
# catalog-license gpl2
# catalog-version 0.4.4
Name:		texlive-gnuplottex
Version:	0.4.4
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Gnuplot code is extracted from the document and written to
.gnuplot files. Then, if shell escape is enabled, the graph
files are automatically processed and converted to PostScript
or PDF files, which will then be included. If shell escape is
disabled, the user will have to manually run the files through
gnuplot and re-run the LaTeX job.

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
%{_texmfdistdir}/tex/latex/gnuplottex/gnuplottex.sty
%doc %{_texmfdistdir}/doc/latex/gnuplottex/README
%doc %{_texmfdistdir}/doc/latex/gnuplottex/example-pdf.tex
%doc %{_texmfdistdir}/doc/latex/gnuplottex/gnuplottex.pdf
%doc %{_texmfdistdir}/doc/latex/gnuplottex/gpl.txt
#- source
%doc %{_texmfdistdir}/source/latex/gnuplottex/gnuplottex.dtx
%doc %{_texmfdistdir}/source/latex/gnuplottex/gnuplottex.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
