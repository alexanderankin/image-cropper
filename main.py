#!/usr/bin/env python3
"""Batch Image Processing

Just running the program will crop all the pictures in "in" according
to the dimensions specified in "config.yml" and then put them in "out".

You can specify your own file name, cropping dimensions, and in/output
folders via command line.

Version 0.1 only supports the default: reading options from config.yml 
and processing from "in" to "out".

Usage:
  ./main.py
  ./main.py [options]
  ./main.py -c FILE | --config FILE


Options:
  -s  --silent				silently do default behaviour
  -c FILE, --config FILE	do a thing
  -h --help					Show this screen.

"""
from docopt import docopt
from os.path import isfile
from lib import image_ops
from sys import version_info as vi

def load_config(config_file="config.yml"):
	file = open(config_file, 'r')
	from yaml import load, dump
	try:
		from yaml import CLoader as Loader, CDumper as Dumper
	except ImportError:
		from yaml import Loader, Dumper
	contents = load(file, Loader=Loader)
	image_ops.ls(contents["start"]["x"],
		contents["start"]["y"],
		contents["end"]["x"],
		contents["end"]["y"])

def main(arguments):
	no_arguments_given = True
	for x in arguments:
		if arguments[x] is not None and arguments[x] is not False: 
			no_arguments_given = False

	if no_arguments_given:
		if vi.major is 2:
			inp = raw_input("Proceed with default behaviour? (use -h for help) ")
		else:
			inp = input("Proceed with default behaviour? (use -h for help) ")

		if "y" in inp:
			load_config()
		else:
			print ("Bye!")
			exit()
	elif arguments["--config"] is not None:
		if (isfile(arguments["--config"])):
			print ("using " + arguments["--config"]); exit()
		else:
			print("Sorry, file not found."); exit()
		load_config(arguments["--config"])
	else:
		load_config()
		

if __name__ == '__main__':
	main(arguments = docopt(__doc__, 
		version=__doc__[:__doc__.find("\n")] + ' 0.1')) # 1st line of docstr
	# mything = thing(3)