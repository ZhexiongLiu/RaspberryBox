import os
printer_name = "HP_LaserJet_1020_1"
os.system("lpr -o page-left=60 -o page-right=100 -o page-top=60 -o page-bottom=100 -P {} output.txt".format(printer_name)

