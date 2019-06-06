#!/usr/bin/python3
from random import *

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def prw(): #print random word
    list_length = file_len('words_alpha.txt')

    rline = randint(0,list_length)

    with open('words_alpha.txt') as f:
        for i, line in enumerate(f , 1):
            if i == rline:
                break
    return line



print( prw().rstrip()+"-"+prw())
