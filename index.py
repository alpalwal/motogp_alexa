## TO DO -
# Add in localization for time zone

import requests
import re

track = "Malaysia"
race_class = "Moto3"
event = "RAC"

url = "http://www.motogp.com/en/event/" + track + "#schedule"

response = requests.get(url)
html = response.text
#print(response.text)


only_start_time_pattern = re.compile(r'c-schedule__table-cell\">(?P<class>Moto\S*)\s.*\n.*\n*.*\n\s*<span\sclass=\"visible-xs\">(?P<name>\S*)<.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n\s*<span\sdata-ini-time=\"[0-9-T:]*(?P<offset>[\+|\-]\d{4})\"\sclass=\"single\">(?P<time>\d{2}:\d{2})')
start_time_matches = only_start_time_pattern.findall(html)

## All of the matches for single start times
# print(start_time_matches)


start_and_end_time_pattern = re.compile(r'c-schedule__table-cell\">(?P<class>Moto\S*)\s.*\n.*\n.*\n\s*<span\sclass=\"visible-xs\">(?P<name>\S*)<.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n\s*<span\sdata-ini-time=\"[0-9-T:]*(?P<offset>[\+|\-]\d{4})">(?P<time>\d{2}:\d{2})<\/span>\s-\s<span\sdata-end=\"[0-9-T:\+]*\">(?P<time2>\d{2}:\d{2})')
start_and_end_matches = start_and_end_time_pattern.findall(html)

## All of the matches for single start times
# print(start_and_end_matches)


if event == "FP1" or event == "FP2" or event == "FP3" or event == "WUP":
    for session in start_and_end_matches:
        if session[0] == race_class:
            if session[1] == event:
                print(session)
                break

if event == "PRESS" or event == "RAC":
    for session in start_time_matches:
        if session[0] == race_class:
            if session[1] == event:
                print(session)
                break