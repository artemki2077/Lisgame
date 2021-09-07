import discord
from PIL import Image, ImageDraw 
from discord.ext import commands
from replit import db
from config import time, time_war, colors
import config
import keep_alive
import random 
import datetime as dt

r = random.Random()

intents = discord.Intents.default()
client = commands.Bot(command_prefix=f".", intents=intents)
client.remove_command("help")

game = {
    "к" : "н",
    "н" : "б",
    "б" : "к"
}


con = 23.5
roles = {
    "855561052549021696": "1",
    "855561104985030717": "2",
    "855561141634990101": "3"
}

# db["map"] = [["*"] * 25] * 25
# db["map"][0][0] = "1"
# db["map"][24][0] = "2"
# db["map"][0][24] = "3"
# b = db["map"]
# db["map"][25 - 3][3 - 1] = "*"
# db["map"][25 - 6][6 - 1] = "*"
# for y, i in enumerate(b):
#     for x, j in enumerate(i):
#         if j == "*":
#             if b[y][x + 1 if x + 1 != 25 else x] != "*" or b[y][
#                     x - 1 if x -
#                     1 >= 0 else x] != "*" or b[y + 1 if y + 1 != 25 else y][
#                         x] != "*" or b[y - 1 if y - 1 >= 0 else y][x] != "*":
#                 print(f"|*|", end="")
#             else:
#                 print(f"|_|", end="")
#         else:
#             print(f"|{j}|", end="")
#     print()



def kkk(x, y):
    return db["map"][25 - y][x - 1]

def jjj(x, y, z):
	db["map"][25 - y][x - 1] = z

def war(x, y, uf, ut, s):
    db["map"][25 - y][x - 1] = [uf, ut, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), s]



@client.command(pass_context=True)
async def help(ctx: commands.Context):
    await ctx.send(" \
	в этой игре для того, чтобы")


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
    file = discord.File("map2.png")
    return file

@client.command(pass_context=True)
async def map(ctx: commands.Context):
    # b = db["map"]
    # answ = ""
    # for y, i in enumerate(b):
    #     for x, j in enumerate(i):
    #         if j == "*":
    #             if b[y][x + 1 if x + 1 != 25 else x] != "*" or b[y][
    #                     x - 1 if x - 1 >= 0 else x] != "*" or b[
    #                         y + 1 if y + 1 != 25 else y][x] != "*" or b[
    #                             y - 1 if y - 1 >= 0 else y][x] != "*":
    #                 answ += f"[-]"
    #             else:
    #                 answ += f"[ ]"
    #         else:
    #             answ += f"[{j}]"
    #     answ += "\n"
    # await ctx.send(f"{answ}")
    await ctx.send(file=update())



@client.command()
async def step(ctx=commands.Context, *args):
    if len(args) >= 4 or len(args) == 1:
        ctx.send(embed=discord.Embed(description=f".step <x> <y>",
                                     color=0xff4542).set_author(name="Ошибка"))
    else:
        # print(ctx.author.name)
        update()
        role = [i for i in ctx.author.roles if str(i.id) in roles.keys()]
        x = int(args[0])
        y = int(args[1])
        rol = roles[str(role[0].id)]

        if kkk(x, y) == rol:
            await ctx.send(embed=discord.Embed(description=f"поле уже занято",
                                     color=0xff4542).set_author(name="Ошибка"))
        elif not (0 < x <= 25) or not (0 < y <= 25):
            await ctx.send(embed=discord.Embed(description=f"так нельзя",
                                     color=0xff4542).set_author(name="Ошибка"))                              
       
        elif not role:
            await ctx.send(embed=discord.Embed(description=f"у тебя нет роли",
                                     color=0xff4542).set_author(name="Ошибка"))
        elif type(kkk(x, y)) != str:
            if len(args) != 3:
                await ctx.send(embed=discord.Embed(description=f".step <x> <y> <'к', 'н' или 'б'>",
                                     color=0xff4542).set_author(name="Ошибка"))
            elif kkk(x, y)[0] == rol or kkk(x, y)[1] != rol:
                await ctx.send(embed=discord.Embed(description=f"так нельзя",
                                     color=0xff4542).set_author(name="Ошибка"))
            else:
                if game[args[2]] == kkk(x, y)[3] or args[2] == kkk(x, y)[3]:
                    db["stat"].append(["answ", rol, kkk(x, y)[0], args[2], True, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), [x, y], ctx.author.name])
					# db["stat"].append([1, rol, ])
                    await ctx.send(embed=discord.Embed(description=f"succes",
                                                color=0x49ff42).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                    jjj(x, y, rol)
                else:
                    db["stat"].append(["answ", rol, kkk(x, y)[0], args[2], False, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), [x, y], ctx.author.name])
                    await ctx.send(embed=discord.Embed(description=f"ты проиграл",
                                     color=0xff4542).set_author(name="Ошибка"))
                    jjj(x, y, kkk(x, y)[0])
        elif kkk(x, y) != "*" and kkk(x, y) != rol and type(kkk(x, y)) == str:
            if len(args) != 3:
                await ctx.send(embed=discord.Embed(description=f"выберите 'к', 'н' или 'б'",
                                     color=0xff4542).set_author(name="Ошибка"))
            elif args[2] != "к" and args[2] != "н" and args[2] != "б":
                await ctx.send(embed=discord.Embed(description=f"неправильный набран знак войны",
                                     color=0xff4542).set_author(name="Ошибка"))
            elif r.randint(0, 10) > 7:
                await ctx.send(embed=discord.Embed(description=f"не повизло",
                                     color=0xff4542).set_author(name="Ошибка"))
                db["stat"].append(["war", rol, kkk(x, y), args[2], False, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), [x, y], ctx.author.name])
                db[str(ctx.author.id)] = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            else:
                if (kkk(x, y - 1 if y - 1 > 0 else y) == rol or kkk(x + 1 if x + 1 < 24 else x, y) == rol or kkk(x, y + 1 if y + 1 < 24 else y) == rol or kkk(x - 1 if x - 1 > 0 else x, y) == rol):
                    if str(ctx.author.id) not in db:
                        db["stat"].append(["war", rol, kkk(x, y), args[2], True, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), [x, y], ctx.author.name])
                        await ctx.send(embed=discord.Embed(description=f"succes",
                                                color=0x49ff42).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                        war(x, y, rol, kkk(x, y), args[2])
                        db[str(ctx.author.id)] = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    else:
                        delta = dt.datetime.now() - dt.datetime.strptime(db[str(ctx.author.id)] , "%d/%m/%Y %H:%M:%S")
                        if delta > time:
                            await ctx.send(embed=discord.Embed(description="succes",
                                                color=0x49ff42).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                            war(x, y, rol, kkk(x, y), args[2])
                            db[str(ctx.author.id)] = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                            db["stat"].append(["war", rol, kkk(x, y), args[2], True, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), [x, y], ctx.author.name])
                        else:
                            tt = time - delta
                            hour, remainder = divmod(tt.seconds, 3600)
                            minute, seconds = divmod(remainder, 60)
                            if hour >= 1:
                                await ctx.send(embed=discord.Embed(description=f"вам надо подождать в течении {hour} часов и {minute} минут",
                                                color=0xff4542).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                            else:
                                await ctx.send(embed=discord.Embed(description=f"вам надо подождать в течении {minute} минут и {seconds} секунд",
                                                color=0xff4542).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
        elif r.randint(0, 10) > 8:
            await ctx.send(embed=discord.Embed(description=f"не повизло",
                                     color=0xff4542).set_author(name="Ошибка"))
            db["stat"].append(["step", rol, [x, y], False, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), [x, y], ctx.author.name])
            db[str(ctx.author.id)] = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        elif (kkk(x, y - 1 if y - 1 > 0 else y) == rol or kkk(x + 1 if x + 1 <= 25 else x, y) == rol or kkk(x, y + 1 if y + 1 <= 25 else y) == rol or kkk(x - 1 if x - 1 > 0 else x, y) == rol):
            if str(ctx.author.id) not in db:
                await ctx.send(embed=discord.Embed(description=f"succes",
                                        color=0x49ff42).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                jjj(x, y, rol)
                db["stat"].append(["step", rol, [x, y], True, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), [x, y], ctx.author.name])
                db[str(ctx.author.id)] = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            else:
                delta = dt.datetime.now() - dt.datetime.strptime(db[str(ctx.author.id)] , "%d/%m/%Y %H:%M:%S")
                if delta > time:
                    await ctx.send(embed=discord.Embed(description="succes",
                                        color=0x49ff42).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                    jjj(x, y, rol)
                    db["stat"].append(["step", rol, [x, y], True, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), [x, y], ctx.author.name])
                    db[str(ctx.author.id)] = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                else:
                    tt = time - delta
                    hour, remainder = divmod(tt.seconds, 3600)
                    minute, seconds = divmod(remainder, 60)
                    if hour >= 1:
                        await ctx.send(embed=discord.Embed(description=f"вам надо подождать в течении {hour} часов и {minute} минут",
                                        color=0xff4542).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
                    else:
                        await ctx.send(embed=discord.Embed(description=f"вам надо подождать в течении {minute} минут и {seconds} секунд",
                                        color=0xff4542).set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url))
        else:
            await ctx.send(embed=discord.Embed(description=f"error",
                                     color=0xff4542).set_author(name="Ошибка"))
            db["stat"].append(["step", rol, [x, y], False, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), [x, y], ctx.author.name])

keep_alive.keep_alive()
client.run(config.TOKEN)
