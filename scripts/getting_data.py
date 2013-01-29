#!/usr/bin/env python
"""
Script for fetching and calculating outages for NYC subway.
Specifically the fraction of outages that are marked "Repair"

This script fetches the xml file:
http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml
to disk and prints a number.
"""

def main():
    from tjarnberg import fetchNYCoutages
    from tjarnberg import calcFracOutages

    doc = fetchNYCoutages()
    answer = calcFracOutages(doc)

    print answer

if __name__ == "__main__":
    main()