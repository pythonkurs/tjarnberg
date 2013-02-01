#!/usr/bin/env python
"""
Script for fetching and calculating outages for NYC subway.
Specifically the fraction of outages that are marked "Repair"

This script fetches the xml file:
http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml
to disk and prints a number.
"""

def main():
    from tjarnberg.session2 import fetchNYCoutages
    from tjarnberg.session2 import calcFracOutages

    doc = fetchNYCoutages()
    repairs, total = calcFracOutages(doc)

    print "Total number of outages = "+str(total)
    print "Repair status = "+str(repairs)
    print "Fraction = "+str(float(repairs)/total)+"\n"

if __name__ == "__main__":
    main()
