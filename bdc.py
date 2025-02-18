#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb 10 2025.

@author: npappin-wsu
@license: MIT

Updated on Feb 11 2025.
"""

from . import logger, session, metadata
import pandas as pd
import json
# from . import config

def availability(state: int | str | list, technology: int | str | list, release: str | list="j24") -> pd.DataFrame:
    logger.info("Collecting availability...")
    logger.debug(f"State: {state}")
    logger.debug(f"Technology: {technology}")
    logger.debug(f"Release: {release}")
    df = pd.DataFrame()
    session.get("https://api.bdc.com/availability")
    # Your code here
    return df

def get_metadata():
    logger.info("Collecting metadata...")
    r = session.get("https://broadbandmap.fcc.gov/api/public/map/listAsOfDates")
    logger.debug(r.json())
    parsed = json.loads(r.text)
    logger.debug(parsed)
    logger.debug(parsed["data"])
    logger.info("Metadata collected.")
    types = set([item['data_type'] for item in parsed["data"]])
    metadata = {}
    for type in types:
        if type not in metadata.keys():
            metadata[type] = list()
        for item in parsed["data"]:
            if item['data_type'] == type:
                logger.info(f"Data type: {type}")
                logger.debug(item)
                metadata[type].append(item['as_of_date'])
    return metadata

def echo(message):
    logger.info(message)
    print(message)
    pass

def main():
    logger.info("Starting the application...")
    # Your code here


if __name__ == "__main__":
    main()
