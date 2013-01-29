#!/usr/bin/env python

"""
python course module with specific functions for solving tasks.
"""


def fetchNYCoutages():
    """
    Gets the file nyct_ene.xml and downloads it to disk
    """
    import requests
    import untangle

    url = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"

    xml_file = requests.get(url)
    doc = untangle.parse(xml_file.text)

    return doc

def calcFracOutages(doc):
    """
    Calculates the fraction of autages with reasion "Repair"
    """

    outages = doc.NYCOutages.outage
    nout = len(outages)

    counter = 0
    for outage in outages:
        if 'REPAIR' == outage.reason.cdata:
            counter = counter + 1

    frac = float(counter)/nout
    return frac
