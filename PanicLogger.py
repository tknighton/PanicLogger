#borrowed heavily from https://encoretechnologies.github.io/blog/2020/05/kernel-composure/

#!/usr/bin/env python3

import argparse
import json
import re
import sys
import glob
import sys
import os

#Delete any existing logs
if os.path.exists("/Users/Shared/Panic_Log.txt"):
  os.remove("/Users/Shared/Panic_Log.txt")

#Glob for panic files. Scoped only to machines that have had at least one panic
def paths():
	return(glob.glob("/Library/Logs/DiagnosticReports/*panic*"))	

list = paths()

#Print to file. Appending in case there's multiple panics
sys.stdout = open('/Users/Shared/Panic_Log.txt', 'a')

# Parses a given log file for every match of a specific regex
def parse_log_file(log_file_path, regex):
    match_list = []
    with open(log_file_path, "r") as log_file:
        content = log_file.read().splitlines()

    for line in content:
        for match in re.finditer(regex, line, re.S):
            match_text = match.group()
            match_list.append(match_text)

    return match_list


def main():
    kernel_panic = parse_log_file(log_file_path, regex)

    initial_info = json.loads(kernel_panic[0])

    for key, value in initial_info.items():
        print(f"{key}: {value}")

    panic_json = json.loads(kernel_panic[1])

    print(panic_json["macOSPanicString"])


if __name__ == "__main__":
    regex = r"\{(.*?)\}"
for item in list:
    log_file_path = item

    main()