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


class availability:

    def state(
        states: int | str | list = 53,
        technology: int | str | list = 50,
        release: str | list = "2024-06-30",
    ) -> pd.DataFrame:
        logger.info("Collecting availability...")
        logger.debug(f"State: {states}")
        logger.debug(f"Technology: {technology}")
        logger.debug(f"Release: {release}")
        if type(states) is not list:
            state = [states]
        if type(technology) is not list:
            technology = [technology]
        if type(release) is not list:
            release = [release]
        # Add normalization code here

        # Retrieve availability data
        availability = dict()
        for r in release:
            response = session.get(
                f"https://broadbandmap.fcc.gov/api/publvic/map/downloads/listAvailabilityData/{r}"
            )
            if response.status_code != 200:
                logger.error(f"Failed to retrieve availability data for {r}.")
                return response
                raise Exception(f"Failed to retrieve availability data for {r}.")
            availability[r] = pd.DataFrame.from_dict(response.json())
        return availability
        for r in release:
            rlocal = availability[r]
            for s in states:
                for t in technology:
                    logger.debug(f"State: {s}, Technology: {t}, Release: {r}")

                    # session.get("https://api.bdc.com/availability")
        logger.debug(f"State: {state}, Technology: {technology}, Release: {release}")
        df = pd.DataFrame()
        # Your code here
        return df


def echo(message):
    logger.info(message)
    print(message)
    pass


def main():
    logger.info("Starting the application...")
    # Your code here


if __name__ == "__main__":
    main()
