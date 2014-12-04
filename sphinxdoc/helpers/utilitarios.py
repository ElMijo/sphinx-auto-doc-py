# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys,os, shutil
from distutils.util import strtobool
from terminal_text_color import TextColor,AlertTextColor

tc = TextColor()



def raw_input_yes_no(question):

    question  = '%s [y/n]: ' % question
    errortext = tc.bold_yellow('por favor responda con \'y\' or \'n\'.\n') 
    while True:
        try:
            return strtobool(raw_input(question).lower())
        except ValueError:
            sys.stdout.write(errortext)