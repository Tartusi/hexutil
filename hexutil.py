#! /usr/bin/python3
from sys import exit
import argparse


def htt(args):
	return_textv=""
	to_textify = args.hex.strip('0x')
	if len(to_textify) % 2 != 0 :
		print("Wrong hex, must be even")
		exit(0)
	cpt=0
	while cpt<len(to_textify) :
		return_textv+=chr(int(to_textify[cpt:cpt+2],16))
		cpt+=2
	return return_textv

def tth(args):
	rotate_each=3
	nb_rotate=0
	return_hexv=""
	if args.rotate:
		rotate_each=args.rotate-1
	if args.reverse:
		texttohex=args.text[::-1]
	else:
		texttohex=args.text
	for c in texttohex:
		return_hexv+="{:0<2}".format(hex(ord(c)).strip('0x'))
		if(nb_rotate<rotate_each):
			nb_rotate+=1
		else:
			nb_rotate=0
			return_hexv+="\n"
	return return_hexv			


parser = argparse.ArgumentParser(description="help to manipulate hex and text")
subparser = parser.add_subparsers(help="htt|tth help",dest='mode')
subparser.required=True
parser_htt = subparser.add_parser('htt',help="hex to text mode")
parser_tth = subparser.add_parser('tth',help="text to hex mode")
parser_tth.add_argument("-rotate",help="Print a new line each [rotate] char",type=int)
parser_tth.add_argument("-reverse",help="reverse the hex printed on the line",action="store_true")
parser_tth.add_argument("text",help="text to hexify")
parser_htt.add_argument("hex",help="hex to textify")
args = parser.parse_args()

if args.mode=="tth":
	print(tth(args))
	exit(0)
if args.mode=="htt":
	print(htt(args))
	exit(0)
