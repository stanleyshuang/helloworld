#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Auther:   Stanley Huang
# Project:  helloworld 1.0
# Date:     2020-12-04
#
import datetime, json
import os, sys
# import elementpath
import xml.etree.ElementTree as ET
from util.util_text_file import get_lines

def output_text(filepath, content):
    fp = open(filepath, "w")    # 開啟檔案
    fp.write(content)           # 寫入 This is a testing! 到檔案
    fp.close()                  # 關閉檔案

### get argv[1] as input
if len(sys.argv) >=2 and sys.argv[1]:
    input_file = sys.argv[1]
else:
    input_file = "./data/sample.txt"

filename, file_extension = os.path.splitext(input_file)
'''
output_file = filename + ".o.json"

### read file in all_lines
all_lines = get_lines(input_file)
cve_str = ''.join(all_lines)

cve_dict = json.loads(cve_str)
if "CVE_data_meta" not in cve_dict:
    cve_dict["CVE_data_meta"] = {}

cve_data_meta = cve_dict["CVE_data_meta"]
cve_data_meta["ASSIGNER"] = "security@qnap.com"
cve_data_meta["DATE_PUBLIC"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")
cve_data_meta["TITLE"] = "the title"

if "affects" not in cve_dict:
    cve_dict["affects"] = {}

if "vendor" not in cve_dict["affects"]:
    cve_dict["affects"]["vendor"] = {}

if "vendor_data" not in cve_dict["affects"]["vendor"]:
    cve_dict["affects"]["vendor"]["vendor_data"] = []
    first_vendor = {}
    cve_dict["affects"]["vendor"]["vendor_data"].append(first_vendor)
first_vendor = cve_dict["affects"]["vendor"]["vendor_data"][0]

if "vendor_name" not in first_vendor:
    first_vendor["vendor_name"] = "QNAP Systems Inc."
if "product" not in first_vendor:
    first_vendor["product"] = {}
    first_vendor["product"]['product_data'] = []
    first_vendor["product"]['product_data'].append(
                {
                    "version": {
                        "version_data": []
                    }
                })
first_product = first_vendor["product"]['product_data'][0]

if "product_name" not in first_product:
    first_product["product_name"] = "Surveillance Station"
if "version" not in first_product:
    first_product["version"] = {}
    first_product["version"]["version_data"] = []
first_product_version_version_data = first_product["version"]["version_data"]
first_product_version_version_data = []
first_product_version_version_data.append({
                                            "platform": "ARM CPU NAS (64bit OS) and x86 CPU NAS (64bit OS)",
                                            "version_affected": "<",
                                            "version_value": "5.1.5.4.3"
                                        })
first_product_version_version_data.append({
                                            "platform": "ARM CPU NAS (32bit OS) and x86 CPU NAS (32bit OS) ",
                                            "version_affected": "<",
                                            "version_value": "5.1.5.3.3"
                                        })

first_product["version"]["version_data"] = first_product_version_version_data
first_vendor["product"]['product_data'][0] = first_product
cve_dict["affects"]["vendor"]["vendor_data"][0] = first_vendor

### "description" --> "description_data" --> [0] --> "value"
if "description" not in cve_dict:
    cve_dict["description"] = {}
if "description_data" not in cve_dict["description"]:
    cve_dict["description"]["description_data"] = []
if len(cve_dict["description"]["description_data"]) == 0:
    cve_dict["description"]["description_data"].append({
                "lang": "eng",
        })
cve_dict["description"]["description_data"][0]["value"] = "A stack-based buffer overflow vulnerability has been reported to affect QNAP NAS devices running Surveillance Station. If exploited, this vulnerability allows attackers to execute arbitrary code.\nQNAP have already fixed this vulnerability in the following versions:\n\nSurveillance Station 5.1.5.4.3 (and later) for ARM CPU NAS (64bit OS) and x86 CPU NAS (64bit OS)\nSurveillance Station 5.1.5.3.3 (and later) for ARM CPU NAS (32bit OS) and x86 CPU NAS (32bit OS)"

### "references" --> "reference_data" --> [0] --> "url"
if "references" not in cve_dict:
    cve_dict["references"] = {}
if "reference_data" not in cve_dict["references"]:
    cve_dict["references"]["reference_data"] = []
if len(cve_dict["references"]["reference_data"]) == 0:
    cve_dict["references"]["reference_data"].append({
                "refsource": "CONFIRM",
        })
cve_dict["references"]["reference_data"][0]["url"] = "https://www.qnap.com/en/security-advisory/qsa-21-07"

### "solution" --> [0] --> "value"
if "solution" not in cve_dict:
    cve_dict["solution"] = []
if len(cve_dict["solution"]) == 0:
    cve_dict["solution"].append({
                "lang": "eng",
        })
cve_dict["solution"][0]["value"] = "QNAP have already fixed this vulnerability in the following versions:\n\nSurveillance Station 5.1.5.4.3 (and later) for ARM CPU NAS (64bit OS) and x86 CPU NAS (64bit OS)\nSurveillance Station 5.1.5.3.3 (and later) for ARM CPU NAS (32bit OS) and x86 CPU NAS (32bit OS)"

### "credit" --> [0] --> "value"
if "credit" not in cve_dict:
    cve_dict["credit"] = []
if len(cve_dict["credit"]) == 0:
    cve_dict["credit"].append({
                "lang": "eng",
        })
cve_dict["credit"][0]["value"] = "Qian Chen from Codesafe Team of Legendsec at Qi'anxin Group"

### "source" --> [0] --> "value"
if "source" not in cve_dict:
    cve_dict["source"] = {}
cve_dict["source"]["advisory"] = "QSA-21-07"
cve_dict["source"]["discovery"] = "EXTERNAL"

cve_json_str = json.dumps(cve_dict, indent=4)
output_text(output_file, cve_json_str)
'''

'''
tree = ET.parse(input_file)
root = tree.getroot()

for child in root:
    print("{tag} - {attrib}".format(tag=child.tag, attrib=child.attrib))
'''

### read file in all_lines
all_lines = get_lines(input_file)

output = ""
### process all lines
for line in all_lines:
    if line == '\n':
        line = '<br>\n'
    line = line.replace("<p><strong>Summary</strong></p>", "<h3>Summary</h3>")
    line = line.replace("<p><strong>Recommendation</strong></p>", "<h3>Recommendation</h3>")
    line = line.replace("<img src=\"cid:Image_0.png\" />", "<img src=\"https://www.qnap.com/i/_upload/support/images/magnifier.png\" style=\"width: 18px;\">")
    output += line

output = output.replace("</li></ol>\n<p>", "<br>\n")
output = output.replace("</p>\n<li>", "</li>\n<li>")

output_text(filename + ".o.html", output)

