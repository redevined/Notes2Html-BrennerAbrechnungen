#!/usr/bin/env python

import sys, re
import htmlport


def addToIndex(line, ind) :
		
	exp = r"^(\d{2}(?:\.\d{2}){2}) ([\w\s\*]+?) (\d{2}:\d{2} - \d{2}:\d{2})$"
	match = re.match(exp, line)
	
	if match :
		match = match.group(1), match.group(3), match.group(2)
		
		months = [ "Januar", "Februar", "M&auml;rz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember" ]
		name = match[0].split(".")[1:]
		name = months[int(name[0])-1] + " 20" + name[1]
		
		if ind.has_key(name) :
			ind[name].append(match)
		else :
			ind[name] = [match]


def main(path="notes.txt", user="Oliver Wirth") :
	
	indices = {}
	
	with open(path) as notes :
		for line in notes :
			addToIndex(line, indices)
	
	htmlport.export(user, "Abrechnungen", indices)


if __name__ == "__main__" :
	main(*sys.argv[1:3])
