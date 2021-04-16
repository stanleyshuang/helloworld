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
    line = line.replace("<u>product support status</u>", "<a href=\"https://www.qnap.com/go/product/eol.php\">product support status</a>")
    line = line.replace("<li>Open the <strong>App Center</strong> and then click <img src=\"cid:Image_0.png\" />.</li></ol>", "<li>Open the <strong>App Center</strong> and then click <img src=\"https://www.qnap.com/i/_upload/support/images/magnifier.png\" style=\"width: 18px;\"> .<br>")

    print(line)
