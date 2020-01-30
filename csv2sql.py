import os
import sys


with open("data.1.30.update.csv", "r") as f:
	lines = f.readlines()

lines = lines[1:]
lines = [line.replace("\n", "").split(",") for line in lines]

with open("data.1.30.sql", "w") as f:
	for line in lines:
		edate = "2020." + line[0].replace("月", ".")
		etype = line[1]
		enum = line[2]
		eplace = line[3]
		efrom = line[4]
		eto = line[5]
		erefdate = line[6]
		ereference = line[7]
		f.write("insert into whinfo (id, edate, etype, enumber, eplace, efrom, eto, refurl, refdate) values(null, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');\n".format(edate, etype, enum, eplace, efrom, eto, ereference, erefdate))
