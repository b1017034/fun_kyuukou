from os.path import join, dirname
from dotenv import load_dotenv
import os
from .scraping_web import scraping
import re
import numpy as np


def split_array(l, n):
    left_array = []
    right_array = []
    for index, text in enumerate(l):
        if index < n:
            left_array.append(text)
        else:
            right_array.append(text)
    return left_array, right_array


def split_merge_array(l, n):
    l = []
    for index, text in enumerate(l):
        if index != n:
            l.append(text)


s = "休講　6/7(金)1限　人工知能続論(大澤)3-JKL 補講有　日時未定"
t = "6/7(金)1限"

print(re.split("\s", s))
print(re.split("\s", t))
print(split_array(re.split("\s", s), 2))
a, b = split_array(re.split("\s", t), 2)
