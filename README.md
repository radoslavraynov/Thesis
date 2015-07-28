## Latest version

The latest version of the thesis is the document `THESIS.pdf` in the main directory.
The other recent versions, along with the last version, are listed as `thesis_[date].pdf`

## How to run

Make sure you have Git. Get this repository locally

    $ git clone https://github.com/radoslavraynov/Thesis.git
	$ cd Thesis/tex

Make sure you have Python. We provide a `makefile` with rules `add`, `pdf`, `bib` and `clean`.
Running

    $ make

really runs

    $ make add
	$ make pdf
	$ open theis.pdf

This will produce the dissertation file `thesis.pdf`.
However, whenever you edit a bibliography, or run this for the first time, do

    $ make add
	$ make pdf
	$ make bib
	$ make

You can compile each of the chapters separately.
To incorporate the changes in the thesis, run `make add` before running `make pdf`.
Alternatively, use your favorite TeX editor/compiler along with
`make add` to incorporate any changes made to any chapter.
Run `make clean` to get rid of all LaTeX produced files, except for the pdf files.