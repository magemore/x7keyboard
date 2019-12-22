#!/usr/bin/python
import struct
import time
import sys
import os

infile_path = "/dev/input/event5"

#long int, long int, unsigned short, unsigned short, unsigned int
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)

#open file in binary mode
in_file = open(infile_path, "rb")

event = in_file.read(EVENT_SIZE)

lang = "us"

while event:
	(tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)
	if type != 0 or code != 0 or value != 0:
		if code == 40:
			if value == 1:
				# print("G1")
				os.system("xdotool key ctrl+shift+c")
				# also G9
			elif value == 2:
				# print("G2")								
				os.system("xdotool key ctrl+shift+v")
			elif value == 4:
				# also G11
				# print("G3")
				os.system("xdotool key ctrl+shift+t")
			elif value == 8:
				# also G12
				# print("G4")
				if lang == "us":
					lang = "ru"
				else:
					lang = "us"
				os.system("setxkbmap "+lang)
			elif value == 16:
				# print("G5")
				# os.system("xdotool key Escape")
				os.system("xdotool key ctrl+backslash")
			elif value == 32:
				# print("G6")
				os.system("xdotool key ctrl+p")
			elif value == 64:
				# print("G7")
				os.system("xdotool key ctrl+shift+p")
				
			else:
				if value != 0:
					print("Event type %u, code %u, value %u at %d.%d" % (type, code, value, tv_sec, tv_usec))
	# else:
		# Events with code, type and value == 0 are "separator" events
		# print("===========================================")

	event = in_file.read(EVENT_SIZE)

in_file.close()


