#!/usr/bin/env python3

'''
    File Name: bibtex_cleaner.py
    Author: Adam Walker
    Date Created: 11/03/2018
    Date Last Modified: 11/03/2018
    Python Version: 3.6.3
'''

## Imports ##
import bibtexparser

## Properties ##
filename = "references.bib"


with open(filename) as bibtex_file:
    bibtex_str = bibtex_file.read()


bib_database = bibtexparser.loads(bibtex_str)
print(bib_database.entries)
