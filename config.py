import datetime as dt
import os

colors = {
    "Волки" : "#30324b",
    "Львы" : "orange",
	"Вороны" : "purple",
	"Артём" : "green"
}
TOKEN = os.environ['TOKEN']

time = dt.timedelta(hours=14)
time_war = dt.timedelta(minutes=8)