#!/usr/bin/env python3

import os
import re
import sys

# import name of cell, area, functionality.
# general list, generate a fornt end query that will take a cell name and give its leakage power and delay at specific condition
# add plotting capability.
import csv
os.environ["PYTHONUNBUFFERED"]="1"
cwd = os.getcwd()
upperLevelPath = os.path.dirname(cwd)
sys.path.append(upperLevelPath)
import libertyParser

################
# Main Process #
################
def main():
    libFile = './example.lib'
    print('')
    print('>>> Input file: ' + str(libFile))

    myLibertyParser = libertyParser.libertyParser(libFile)

    unitDic = myLibertyParser.getUnit()
    print('')
    print('>>> Unit:')
    print(unitDic)
    with open( "info.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        #for line in unitDic:
        writer.writerow(unitDic.keys())
        writer.writerow(unitDic.values())

    cellList = myLibertyParser.getCellList()
    print('')
    print('>>> Cell list:')
    print(cellList)

    with open( "info.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        #for line in unitDic:
        writer.writerow(unitDic.keys())
        writer.writerow(unitDic.values())
        writer.writerow(cellList)

    cellAreaDic = myLibertyParser.getCellArea()
    print('')
    print('>>> Cell area:')
    print(cellAreaDic)

    cellLeakagePowerDic = myLibertyParser.getCellLeakagePower()
    print('')
    print('>>> Cell leakage_power')
    print(cellLeakagePowerDic)
    with open("info.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        # for line in unitDic:
        writer.writerow(unitDic.keys())
        writer.writerow(unitDic.values())
        writer.writerow(cellList)
        writer.writerow(cellLeakagePowerDic.keys())
        writer.writerow(cellLeakagePowerDic.values())

    libPinDic = myLibertyParser.getLibPinInfo(cellList=['DFFX1'], pinList=['Q'])
    print('')
    print('>>> Lib pin info (cell="DFFX1", pin="Q"):')
    print(libPinDic)
    with open("info.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        # for line in unitDic:
        writer.writerow(unitDic.keys())
        writer.writerow(unitDic.values())
        writer.writerow(cellList)
        writer.writerow(cellLeakagePowerDic.keys())
        writer.writerow(cellLeakagePowerDic.values())
        writer.writerow(libPinDic.keys())
        writer.writerow(libPinDic.values())


if __name__ == '__main__':
    main()
