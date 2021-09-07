from flask import Flask, render_template
from replit import db
from PIL import Image, ImageDraw
from threading import Thread
import datetime as dt
from config import time_war

app = Flask('')
colors = {
    "1" : "red",
    "2" : "green",
	"3" : "blue"
}
con = 23.5

def update():
    image = Image.open('map.png')
    draw = ImageDraw.Draw(image)
    for y, i in enumerate(db["map"]):
        for x, j in enumerate(i, 1):
            if j != "*" and type(j) == str:
                draw.rectangle(((con * x + 1, con * y + 1),(con * (x + 1) + 1, con * (y + 1) + 1)), fill=colors[j])
            elif type(j) != str:
                ww = j.value
                if (dt.datetime.now() - dt.datetime.strptime(ww[2] , "%d/%m/%Y %H:%M:%S")) >  time_war:
                    draw.rectangle(((con * x + 1, con * y + 1),(con * (x + 1) + 1, con * (y + 1) + 1)), fill=colors[str(ww[0])])
                    db["map"][y][x - 1] = f"{ww[0]}"
                else:
                    draw.rectangle(((con * x + 1, con * y + 1),(con * (x + 0.5) + 1, con * (y + 1) + 1)), fill=colors[str(ww[0])])
                    draw.rectangle(((con * (x + 0.5) + 1, con * y + 1),(con * (x + 1) + 1, con * (y + 1) + 1)), fill=colors[str(ww[1])])
    image.save('map2.png')

@app.route('/')
def main():
    update()
    return render_template('index.html', map=db["map"], enumerate=enumerate, colors=colors, type=type, str=str)


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()