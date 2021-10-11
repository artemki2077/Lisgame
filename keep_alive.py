from flask import Flask, request,render_template, jsonify
from replit import db
from PIL import Image, ImageDraw
from threading import Thread
import datetime as dt
from config import time_war, colors

app = Flask('')
con = 23.5


def update():
    image = Image.open('map.png')
    draw = ImageDraw.Draw(image)
    for y, i in enumerate(db["map"]):
        for x, j in enumerate(i, 1):
            if j != "*" and type(j) == str:
                draw.rectangle(((con * x + 1, con * y + 1),
                                (con * (x + 1) + 1, con * (y + 1) + 1)),
                               fill=colors[j])
            elif type(j) != str:
                ww = j.value
                if (dt.datetime.now() - dt.datetime.strptime(
                        ww[2], "%d/%m/%Y %H:%M:%S")) > time_war:
                    draw.rectangle(((con * x + 1, con * y + 1),
                                    (con * (x + 1) + 1, con * (y + 1) + 1)),
                                   fill=colors[str(ww[0])])
                    db["map"][y][x - 1] = f"{ww[0]}"
                else:
                    draw.rectangle(((con * x + 1, con * y + 1),
                                    (con * (x + 0.5) + 1, con * (y + 1) + 1)),
                                   fill=colors[str(ww[0])])
                    draw.rectangle(((con * (x + 0.5) + 1, con * y + 1),
                                    (con * (x + 1) + 1, con * (y + 1) + 1)),
                                   fill=colors[str(ww[1])])
    image.save('map2.png')


def threated():
    n = db["n"]
    b = False
    # mat = [[0] * n for i in range(n)]
    for x in range(n - 1, -1, -1):
        for y in range(n):
            if db["map"][x][y] != "трава":
                db["map"][x][y] = "трава"
                b = True
                break
        if b:
            break
    if b == False:
        # db["n"] += 1
		# return threated()
        db["n"] += 1
        return threated()
    return {"ANSWER": b}


def activ():
    d = {}
    for i in db["stat"]:
        if i[-1] in d:
            d[i[-1]] += 1
        else:
            d[i[-1]] = 1
    return d


def useful():
    d = {}
    for i in db["stat"]:
        if i[0] == "step":
            j = i[3]
        else:
            j = i[4]
        if j:
            if i[-1] in d:
                d[i[-1]] += 1
            else:
                d[i[-1]] = 1
    return d


def winteam():
    t = {}
    for i in db["map"]:
        for j in i:
            if type(j) == str and j != "*":
                if j in t:
                    t[j] += 1
                else:
                    t[j] = 1
    bestt = sorted(t, key=lambda x: t[x], reverse=True)
    return bestt, t


@app.route('/threat')
def threat():
    return jsonify(threated())

# @app.route('/update', methods=['GET', 'POST'])
# def updt():
# 	update()
# 	# data = request.args.get('myLuckyNumber')
# 	# return jsonify(data)
# 	h = list(map(list, db["map"].value))
# 	return jsonify(h)


@app.route('/')
def main():
    update()
    use = useful()
    st, bestt = winteam()
    su = sorted(use, key=lambda x: use[x], reverse=True)
    return render_template('index.html',
                           bt=bestt,
                           st=st,
                           use=use,
                           map=db["map"],
                           enumerate=enumerate,
                           colors=colors,
                           type=type,
                           str=str,
                           su=su)


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()
