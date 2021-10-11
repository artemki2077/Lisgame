import datetime as dt
import os

colors = {
    "Волки" : "#30324b",
    "Львы" : "orange",
	"Вороны" : "purple",
	"угроза" : "#31814b",
	"трава" : "#31814b"
}
TOKEN = os.environ['TOKEN']

time = dt.timedelta(hours=14)
time_war = dt.timedelta(minutes=8)