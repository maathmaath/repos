import abc
import os
import sys


class One(object):

    def __init__(self, statement):
        self.statement = statement

    def print(self):
        x = 10
        x, y = 10, 20
        print(self.statement)
