# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function

import io
import sys

import six.moves


def prompt(msg):
    #print(msg, end=u'')
    orig_out = sys.stdout
    try:
        sys.stdout = io.StringIO()
        return six.moves.input(msg)
    finally:
        sys.stdout = orig_out


if __name__ == '__main__':
    text = prompt(u"Give me input: ")
    print(u"Do you mean '{0}'?".format(text))
