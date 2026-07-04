all: main.pdf

main.pdf: main.md
pandoc main.md -o output/main.pdf \
--from markdown \
--pdf-engine=xelatex \
--citeproc \
--bibliography=references.bib \
--csl=chicago-author-date.csl \
--toc \
--number-sections

clean:
rm -rf output/

.PHONY: all clean
