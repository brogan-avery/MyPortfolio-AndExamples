"""
***************************************************************
* Class Name: Cycle
* Author: Brogan Avery
* Created: 2021-01-29
***************************************************************
"""

from abc import ABC, abstractmethod

class Cycle(ABC):

    # constructor / attribute variables initialized
    def __init__(self, numberOfTires=None, numberOfFlats=None):
        self._numberOfTires = numberOfTires
        self._numberOfFlats = numberOfFlats

    def ride(self):
        pass

    def stop(self):
        pass


