#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb 10 2025.

@author: npappin-wsu
@license: MIT

Updated on Feb 11 2025.
"""

from . import logger
import json

from requests_ratelimiter import LimiterSession


def get_session(apiKey, username, cache=False):
    session = LimiterSession(max_retries=3, per_minute=10)
    session.headers.update({"User-Agent": "bdclib"})
    session.headers.update({"hash_value": apiKey})
    session.headers.update({"username": username})
    logger.debug(session.headers)
    logger.info("Session created.")
    return session


def get_metadata():
    from . import session

    logger.info("Collecting metadata...")
    r = session.get("https://broadbandmap.fcc.gov/api/public/map/listAsOfDates")
    logger.debug(r.json())
    parsed = json.loads(r.text)
    logger.debug(parsed)
    logger.debug(parsed["data"])
    logger.info("Metadata collected.")
    types = set([item["data_type"] for item in parsed["data"]])
    metadata = {}
    for t in types:
        if t not in metadata.keys():
            metadata[t] = list()
        for item in parsed["data"]:
            if item["data_type"] == t:
                logger.debug(f"Data type: {t}")
                logger.debug(item)
                metadata[t].append(item["as_of_date"])
    return metadata
