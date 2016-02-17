# -*- coding: utf-8 -*-

passSuccessTimesStr = raw_input("input passSuccessTimes: ")

passSuccessTimes = float(passSuccessTimesStr)

passTimesStr = raw_input("input passTimes: ")

passTimes = float(passTimesStr)

passYardSumStr = raw_input("input passYardSum: ")

passYardSum = float(passYardSumStr)

interceptTimesStr = raw_input("input interceptTimes: ")

interceptTimes = float(interceptTimesStr)

C = (passSuccessTimes / passTimes * 100 - 30) / 20

Y = (passYardSum / passTimes - 3) / 4

T = C * 20

I = 2.375 - (interceptTimes - passTimes) * 35

print (C + Y + T + I) / 6 * 100
