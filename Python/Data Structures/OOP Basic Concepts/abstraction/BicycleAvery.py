"""
***************************************************************
* Class Name: Bicycle
* Author: Brogan Avery
* Created: 2021-01-29
***************************************************************
"""

from CycleAvery import Cycle

class Bicycle(Cycle):

    def __init__(self, numberOfTires=2, numberOfFlats=0):
        self._numberOfTires = numberOfTires
        self._numberOfFlats = numberOfFlats

    def ride(self):
        print("start")

    def stop(self):
        print("stop")

    def __str__(self):
        return "Tires: " + str(self._numberOfTires) + " Flats: " + str(self._numberOfFlats)
