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
from bibtexparser.customization import *

## Properties ##
references_file = "references.bib"
unwanted_tags = ["abstract", "file", "url"]



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
    print(bib_database.entries)



#bib_database = bibtexparser.loads(bibtex_str)
#print(bib_database.entries)
