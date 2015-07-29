## Latest version

The latest version of the thesis is the document `THESIS.pdf` in the main directory.
Previous versions are available through the 'history' interface for the file.

## How to run

Make sure you have Git. Get this repository locally

    $ git clone https://github.com/radoslavraynov/Thesis.git
	$ cd Thesis/tex

Make sure you have Python. We provide a `makefile` with rules `add`, `pdf`, `bib` and `clean`.
Run

    $ make bib
	$ make

the first time, and then every time a bibliography changed.
Otherwise, simply running `make` should do.

You can compile each of the chapters separately using your favorite TeX editor/compiler.
To incorporate the changes in the thesis, run `make add` before compiling `thesis.tex`
You can also do this running `make pdf`.
Run `make clean` to get rid of all LaTeX produced files.