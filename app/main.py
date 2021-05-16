#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  helloworld 1.0
# Date:     2020-12-04
#
import os
import sys
from util.util_text_file import get_lines

def output_text(filepath, content):
	fp = open(filepath, "a")	# 開啟檔案
 	fp.write(content)			# 寫入 This is a testing! 到檔案
 	fp.close()					# 關閉檔案

### get argv[1] as input
if len(sys.argv) >=2 and sys.argv[1]:
	input_file = sys.argv[1]
else:
	input_file = "./data/sample.txt"

### read file in all_lines
all_lines = get_lines(input_file)


output = ""
### process all lines
for line in all_lines:
    line = line.replace("<p><strong>Summary</strong></p>", "<h3>Summary</h3>")
    line = line.replace("<p><strong>Recommendation</strong></p>", "<h3>Recommendation</h3>")
    line = line.replace("<img src=\"cid:Image_0.png\" />", "<img src=\"https://www.qnap.com/i/_upload/support/images/magnifier.png\" style=\"width: 18px;\">")
    output += line

filename, file_extension = os.path.splitext(input_file)
output_text(filename + ".o.html", output)
