#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python
# -*- coding: utf-8 -*-
# <bitbar.title>Avast Menu (Python)</bitbar.title>
# <bitbar.version>v1.0.1</bitbar.version>
# <bitbar.author>Ondrej Kratochvil</bitbar.author>
# <bitbar.desc>Show current weekly menu in Avast Perfect Canteen Restaurant in Prague</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

from __future__ import print_function
import lxml.html
import sys
from lxml.html import parse

print(" | templateImage=iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAADjSURBVDhPlZPBDcIwDEUrWIANYAPYAI4cWYEJWIEVmAA2YAWObAHc4ARMAP+n/iJx3Ug86ctxmv66cTJsSvbQG9pAS+gB3SGxgFbQOWVgYFHwIRfNoIlFwfkjNE2Z4Q1qsLpRO/wRGcwhfj1frIo6RAYslYsZRT4u8AYvi8LnHbzBGrpCfPEAnaAq3oAv7NphMvu7AsLN87vNalgZuVnshb3+QN6EneB8saFRBSI/RERtLOYjAy3wfVdeVBYZhAuBjnD1KOdf9QbKq7+Qt21sUfhf6oWX5gL548ub+oS2KUs0zRdBnB51d7aUvQAAAABJRU5ErkJggg==")
print("---")

i = 0

try:
	menu_lxml = parse("http://menu.perfectcanteen.cz/menu/getmenu/1/cz").getroot()
except IOError as err:
	print("There's an error reading the online menu | color=red")
	sys.exit(0)

days = menu_lxml.xpath("//h3[@class='day_name']/text()")
for table in menu_lxml.xpath("//div[@class='row'][1]//table"):
	print(days[i].upper()," | color=red")
	i = i + 1
	n = 1
	for item in table.xpath(".//td[contains(@class,'meal_name')]/text()[1]"):
	 	prefix = ""
	 	color = "gray"
	 	if n <= 2:
	 		prefix = "[P] "
	 		color = "green"
	 	if n == len(table):
	 		prefix = "[S] "
	 		color = "blue"
	 	print(prefix,item.strip()," | color="+color)
	 	n = n + 1
	print("---")
