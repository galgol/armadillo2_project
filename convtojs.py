import json
import os

keep_phrases = []

wanted_val = input("enter wanted value to search in log,to finish type done:")
while wanted_val != "done":
    keep_phrases.append(wanted_val)
    wanted_val = input("enter another value:")


def test():
    with open("data_file.json", "w") as write_file:
        path = input("enter path to log files :")
        for filename in os.listdir(path):
            if filename.endswith('.log'):
                with open(os.path.join(path, filename), "r") as infile:
                    for line in infile:
                        for phrase in keep_phrases:
                            if phrase in line:
                                data = {filename: line}
                                json.dump(data, write_file, indent=1)
                                break


test()
