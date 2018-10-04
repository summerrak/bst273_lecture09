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
print(args) #shows that it is a namespace
print(args.data_file) #how we get args file . find the thing inside of it
#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
