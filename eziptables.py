#!/usr/bin/python3
'''
EZ IPTables Application for adding (and maybe someday deleting) IPTables entries
'''

import argparse

def main(args):
	
	# This section opens the input files as lists, making each line accessible as a list element
	with open(args.targetlist,'r') as input:
		tgts = [x for x in input.read().splitlines()] # this example simply stores each line as it's own element
	with open(args.cmdlist,'r') as input:
		cmds = [x.encode() for x in input.read().splitlines()] # this example encodes the lines as bytes

	#The rest of the working code of the program goes here.



if __name__=="__main__":
	
	parser = argparse.ArgumentParser(description="SCRIPT DESCRIPTION HELP TEXT")
	parser.add_argument("targetlist", type=str, help=".txt file with target IP's, one per line") #required argument
	parser.add_argument("cmdlist", help='.txt file with instructions to be wrapped')
	args = parser.parse_args()

	main(args)
