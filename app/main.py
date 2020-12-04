#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  helloworld 1.0
# Date:     2020-12-04
#
from util.util_text_file import get_lines

print('Hello World..\n')

all_lines = get_lines("./data/sample.txt")
for line in all_lines:
    print(line)
