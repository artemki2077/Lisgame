from replit import db
import datetime as dt
import random as r

# db["map"][13][13] = [1, 2, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
# print(*db["map"].value)
def jjj(x, y, z):
	db["map"][25 - y][x - 1] = z	
# db["stat"] = [[type, who, step, success or not, time, [x, y], user]]
# db["stat"] = [[type, who, for who,symbol, success or not, time, [x, y], user]]
# for x in range(1, 26):
# 	for y in range(1, 26):
# 		jjj(x,  y, "*")
# x = r.randint(1, 25)
# y = r.randint(1, 25)
# jjj(x, y, "Вороны")
db["stat"] = []
# db["map"][0][24] = "*"
# db["map"][0][23] = "*"
# db["map"][5][0] = "2"