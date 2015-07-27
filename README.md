## Latest version

The latest version of the thesis is the document `THESIS.pdf` in the main directory.
The other recent versions, along with the last version, are listed as `thesis_[date].pdf`

## How to run

Make sure you have Git. Get this repository locally

    $ git clone https://github.com/radoslavraynov/Thesis.git
	$ cd Thesis/tex

Make sure you have Python. Run the `make` as follows

    $ make strip
	$ make bib
	$ make pdf

This will produce the dissertation file `thesis.pdf`.
You can compile each of the chapters separately.
To incorporate the changes in the thesis, run `make strip` before runing `make pdf`.
Only run `make bib` after adding/removing bibliography (and the first time).
Alternatively, use your favourite TeX editor/compiler along with
`make strip` to incorporate any changes made to any chapter.
Run `make clean` to get rid of all LaTeX produced files, except for the pdf files.