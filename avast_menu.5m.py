#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/local/bin/python
# -*- coding: utf-8 -*-
# <bitbar.title>Avast Menu (Python)</bitbar.title>
# <bitbar.version>v1.0.0</bitbar.version>
# <bitbar.author>Ondrej Kratochvil</bitbar.author>
# <bitbar.desc>Show current weekly menu in Avast Perfect Canteen Restaurant in Prague</bitbar.desc>
# <bitbar.dependencies>python</bitbar.dependencies>

from __future__ import print_function
import lxml.html
from lxml.html import parse

print("MENU | size=11 color=blue")

i = 0
menu_lxml = parse("http://menu.perfectcanteen.cz/menu/getmenu/1/cz").getroot()
days = menu_lxml.xpath("//h3[@class='day_name']/text()")
for table in menu_lxml.xpath("//div[@class='row'][1]//table"):
	print("---")
	print(days[i].upper()," | color=red")
	i = i + 1
	n = 0
	for item in table.xpath(".//td[contains(@class,'meal_name')]/text()[1]"):
	 	prefix = ""
	 	color = "gray"
	 	if n < 2:
	 		prefix = "[P] "
	 		color = "green"
	 	if n == len(table) - 1:
	 		prefix = "[S] "
	 		color = "blue"
	 	colorcode = " | color=" + color
	 	print(prefix,item.strip(),colorcode)
	 	n = n + 1
	
