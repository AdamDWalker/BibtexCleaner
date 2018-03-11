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
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.customization import *


## Properties ##
references_file = "references.bib" # This is the file you read in
output_file = "clean_references.bib" # This is the file you write out
unwanted_tags = ["abstract", "file", "url", "keywords"]


## Functions ##
def customizations(record):
    record = type(record)
    record = convert_to_unicode(record)
    for val in unwanted_tags:
        record.pop(val, None)
    return record


with open(references_file) as bibtex_file:
    #bibtex_str = bibtex_file.read()
    parser = BibTexParser()
    parser.customization = customizations
    bib_database = bibtexparser.load(bibtex_file, parser=parser)
    #print(bib_database.entries)
    print("Cleaning complete")


with open("clean_refs.bib", 'w') as bibfile:
    writer = BibTexWriter()
    bibfile.write(writer.write(bib_database))
    print("Writing new file complete")
