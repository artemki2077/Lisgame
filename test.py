from replit import db
import datetime as dt

# db["map"][13][13] = [1, 2, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")]
print(*db["map"].value)