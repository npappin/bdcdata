#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Feb 10 2025.

@author: npappin-wsu
@license: MIT

Updated on Feb 11 2025.
"""

from . import logger

from requests_ratelimiter import LimiterSession

def get_session(apiKey, username, cache=False):
    session = LimiterSession(max_retries=3, per_minute=10)
    session.headers.update({"User-Agent": "python-bdc"})
    session.headers.update({"hash_value": apiKey})
    session.headers.update({"username": username})
    logger.debug(session.headers)
    logger.info("Session created.")
    return session
