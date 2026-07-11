SHELL := /bin/bash

TITLE := When Faith Becomes Law: Christianity, Political Power, and the Limits of Religious Authority
AUTHOR := Joshua Viles
OUTPUT_DIR := output
PDF_NAME ?= main.pdf

.PHONY: all validate pdf clean

all: validate pdf

validate:
	python3 tools/validate_article.py

pdf: $(OUTPUT_DIR)/$(PDF_NAME)

$(OUTPUT_DIR)/$(PDF_NAME): main.md references.bib
	mkdir -p $(OUTPUT_DIR)
	pandoc main.md \
		-o "$@" \
		--from=markdown \
		--standalone \
		--pdf-engine=xelatex \
		--filter pandoc-citeproc \
		--bibliography=references.bib \
		--toc \
		--number-sections \
		--metadata=title:"$(TITLE)" \
		--metadata=author:"$(AUTHOR)"

clean:
	rm -rf $(OUTPUT_DIR) submission_package
