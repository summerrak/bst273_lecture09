#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to file we want to read",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )
print("args =", args) #shows that it is a namespace
print(args.data_file) #how we get args file . find the thing inside of it

fh = open(args.data_file) #fh is how we hold on to this file
print("the file handle is", fh)

lines = 0
words = 0
chars = 0

for line in fh:
	#print(line)  # to make sure were doing the right thing
	lines += 1

print(lines)




#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
