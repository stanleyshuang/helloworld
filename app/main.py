#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  helloworld 1.0
# Date:     2020-12-04
#
import sys
from util.util_text_file import get_lines

### get argv[1] as input
if len(sys.argv) >=2 and sys.argv[1]:
	input_file = sys.argv[1]
else:
	input_file = "./data/sample.txt"

### read file in all_lines
all_lines = get_lines(input_file)

### process all lines
for line in all_lines:
    line = line.replace("<li style=\"font-weight: 400;\">", "<li>")
    line = line.replace("<span style=\"font-weight: 400;\">", "")
    line = line.replace("</span>", "")
    line = line.replace("<p><strong>Summary</strong></p>", "<h3>Summary</h3>")
    line = line.replace("<p><strong>Recommendation</strong></p>", "<h3>Recommendation</h3>")
    line = line.replace("<li>Open the <strong>App Center</strong> and then click .<br>", "<li>Open the <strong>App Center</strong> and then click <img src=\"https://www.qnap.com/i/_upload/support/images/magnifier.png\" style=\"width: 18px;\"> .<br>.<br>")

    print(line)
