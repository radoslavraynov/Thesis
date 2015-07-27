FILES = intro-incl.tex preliminaries-incl.tex main-results-incl.tex main-proofs-incl.tex fast-method-incl.tex koszul-bpf-incl.tex examples-incl.tex

add: $(FILES)
	echo "OK DONE"

$(FILES): %-incl.tex: %.tex
	./makestrip.py $*

clean:
	rm *.aux *.bbl *.blg *.lb *.lof *.log *.lot *.out *.pdf *.synctex.gz *.toc *-incl.tex

pdf:
	pdflatex thesis.tex

bib:
	bibtex thesis
	pdflatex thesis.tex