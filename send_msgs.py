import sys
import time
import argparse
import applescript

send_message ='''
	set targetService to 1st service whose service type = iMessage
	set targetBuddy to buddy "{number}" of targetService
	send "{message}" to targetBuddy
'''

parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument('number')
parser.add_argument('-t', required=False, type=int)
parser.add_argument('--byline', action='store_true', required=False)
args = parser.parse_args()

by_line = args.byline
time_delay = args.t if args.t else 1.75

with open(args.filename) as file:
	while True: 
		time.sleep(time_delay)
		line = file.readline()
		if not line: 
			break
		if not by_line:
			for word in line.split():
				applescript.tell.app('Messages', send_message.format(number=args.number, message=word), background=False)
				print(word)
		else:
			applescript.tell.app('Messages', send_message.format(number=args.number, message=line.strip()), background=False)
			print(line)
