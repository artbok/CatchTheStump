from tkinter import *
import random
import os

tk = Tk()
geometry = str(700) + "x" + str(900) + "+" + str((tk.winfo_screenwidth()//2) - 350) + "+" + str(tk.winfo_screenheight()-980)
tk.geometry(geometry)
tk.resizable(width=False, height=False)
tk.title("Побег от бревна")
tk.config(cursor="plus")
tk.iconbitmap("images\\icon.ico")
brevno_image = PhotoImage(file='images\\stump.png')
deaths_image = PhotoImage(file='images\\death.png')
coin_image = PhotoImage(file="images\\coin.png")
bomb_image = PhotoImage(file="images\\bomb.png")
cd_image = PhotoImage(file="images\\cooldown_unavailable.png")
nocd_image = PhotoImage(file="images\\cooldown_available.png")
pause_image = PhotoImage(file="images\\pause.png")
help_image = PhotoImage(file="images\\help.png")
rules_image = PhotoImage(file="images\\rules.png")
shop_image = PhotoImage(file="images\\shop.png")
continue_image = PhotoImage(file="images\\continue.png")
emotions = [" ", PhotoImage(file="images\\dislike.png"), PhotoImage(file="images\\like.png"), PhotoImage(file="images\\happy.png")]
shield_image = PhotoImage(file="images\\shield.png")
meterorit_image = PhotoImage(file="images\\meteorit.png")

class Player:
    x = 350 
    y = 840
    obj = None

class Brevno:
    x = 0
    y = 96
    status = False
    obj = None
    def initXY(self, player: Player):
        self.x = random.randint(player.x-150, player.x+150)
        if self.x < 100:
            self.x = 100
        if self.x > 600:
            self.x = 600
        self.y = 96

class Coins:
    x = []
    y = []
    obj = []

class Shield:
    x = random.randint(60, 660)
    x = x - x % 12
    y = random.randint(200, 600)
    y = y - y % 12
    status = False
    obj = None
# class Meteorit:
#     x = 0
#     y = 0
#     def gen_meteorite(self, player):
#         self.x = random.randint(player.x-200, player.x+200) 
#         self.x = meteorit_x - meteorit_x % 12
#         self.y = random.randint(player.y-200, player.y+200)
#         self.y = self.y - self.y % 12
#         y < 225:
#             meteorit_y = 225
#         if meteorit_y > 675:
#             meteorit_y = 675
#         if meteorit_x < 150:
#             meteorit_x = 150
#         if meteorit_x > 600:
#             meteorit_x = 600
#         killtime = random.randint(15, 30)
#         cnvs.moveto(meteorit_obj, meteorit_x-150, meteorit_y-150)
#         meteorit_timer()
#         tk.after(5000, meterorit) 


e = 0
h = 0

player = Player()
shield = Shield()
brevna = [Brevno(), Brevno()]
coins = Coins() 
w_cooldown = None
a_cooldown = None
d_cooldown = None
s_cooldown = None
jump_text_cooldown = False
jump_cooldown = None
game = True
help_status = False
nomoney_status = False
dislikes = [" ", " ", " "]
coins.obj = []
deaths = 0
coins_received = 0
balance = 0
number = None
def restart():
    global jump_cooldown, player, meteorit_obj, pause_image, continue_image, shield, rules_image, shield_image, help_image, shop_button, help_button, shop_image, pause_button, bombs_x, bombs_y, bombs_objs, bomb_image, brevna, cd_status_image, balance, cnvs, brevno_image, deaths_image, coin_image, cd_image, nocd_image, death_text, money_text, shop_lines, game, deaths, total_deaths, coins_received, coins
    game = True
    deaths = 0
    player = Player()
    shield = Shield()
    brevna = [Brevno(), Brevno()]
    coins = Coins() 
    bombs_x = []
    bombs_y = []
    bombs_objs = []
    jump_cooldown = None
    coins_received = 0
    brevna[0].status = False
    brevna[1].status = False
    shield.status = False
    open_settings = open('resources\\settings.txt', 'r')
    shop_lines = open_settings.readlines()
    open_settings.close()
    balance = int(shop_lines[0])
    total_deaths = int(shop_lines[1])
    open_colors = open('resources\\colors.txt', 'r')
    shop_lines = open_colors.readlines()
    color = shop_lines[0]
    color = color[:-1]
    open_colors.close()
    cnvs = Canvas(bg=color, highlightbackground=color)
    cnvs.place(anchor=NW, height=900, width=700)
    cnvs.create_rectangle(-5, 100, 705, 105, fill="black")
    cnvs.create_rectangle(-5, 800, 705, 805, fill="black")
    cnvs.create_image(640, 40, image=deaths_image)
    cnvs.create_image(540, 40, image=coin_image)
    shield.obj = cnvs.create_image(shield.x, shield.y, image=shield_image)
    meteorit_obj = cnvs.create_image(5000, 5000, image=meterorit_image)
    cd_status_image = cnvs.create_image(490, 40, image=nocd_image)
    death_text = cnvs.create_text(670, 40, text=deaths, font=("Impact", 25))
    money_text = cnvs.create_text(590, 40, text=balance, font=("Impact", 25))
    pause_button = cnvs.create_image(50, 50, image=pause_image)
    cnvs.tag_bind(pause_button, '<Button-1>', pause)
    help_button = cnvs.create_image(130, 50, image=help_image)
    cnvs.tag_bind(help_button, '<Button-1>', help)
    shop_button = cnvs.create_image(210, 50, image=shop_image)
    cnvs.tag_bind(shop_button, '<Button-1>', shop)
    player.obj = (cnvs.create_oval(330, 820, 370, 860, fill="black", width=3))
    gen_brevno()
    meterorit()
    gen_coins()
    bomba()
    check()

def press_w(event):
    global w_cooldown, player, shield
    if game == True and not w_cooldown:
        player.y = player.y - 12
        cnvs.move(player.obj, 0, -12)
        if shield.status == True:
            cnvs.move(shield.obj, 0, -12)
        check()
        w_cd()
def w_cd():
    global w_cooldown, player
    w_cooldown = 1 if not w_cooldown else w_cooldown + 1 
    if w_cooldown == 2:
        w_cooldown = None
        tk.after_cancel(w_cd)
        return
    tk.after(120, w_cd)


def press_s(event):
    global s_cooldown, player, shield
    if game == True and player.y < 770 and not s_cooldown:
        player.y = player.y + 12
        cnvs.move(player.obj, 0, 12)
        if shield.status == True:
            cnvs.move(shield.obj, 0, 12)
        check()
        s_cd()
def s_cd():
    global s_cooldown, player
    s_cooldown = 1 if not s_cooldown else s_cooldown + 1 
    if s_cooldown == 2:
        s_cooldown = None
        tk.after_cancel(s_cd)
        return
    tk.after(120, s_cd)


def press_a(event):
    global a_cooldown, player, shield
    if game == True and player.x > 30 and not a_cooldown:
        player.x = player.x - 12
        cnvs.move(player.obj, -12, 0)
        if shield.status == True:
            cnvs.move(shield.obj, -12, 0)
        check()
        a_cd()
def a_cd():
    global a_cooldown, player, shield
    a_cooldown = 1 if not a_cooldown else a_cooldown + 1 
    if a_cooldown == 2:
        a_cooldown = None
        tk.after_cancel(a_cd)
        return
    tk.after(120, a_cd)


def press_d(event):
    global d_cooldown, player, shield
    if game == True and player.x < 670 and not d_cooldown:
        player.x = player.x + 12
        cnvs.move(player.obj, 12, 0)
        if shield.status == True:
            cnvs.move(shield.obj, 12, 0)
        check()
        d_cd()
def d_cd():
    global d_cooldown, player
    d_cooldown = 1 if not d_cooldown else d_cooldown + 1 
    if d_cooldown == 2:
        d_cooldown = None
        tk.after_cancel(d_cd)
        return
    tk.after(120, d_cd)


def jump(event):
    global jump_cooldown, player, shop_lines, cnvs, game, balance, total_deaths, shield
    if game == True:
        if not jump_cooldown:
            player.y = player.y - 108
            cnvs.move(player.obj, 0,-108)
            if shield.status == True:
                    cnvs.move(shield.obj, 0, -108)
            check()
            cd2()
        else:
            if not jump_text_cooldown:
                wait_jump()
def cd2():
    global jump_cooldown, cd_status_image, cd_image, nocd_image, game
    if game == True:
        if not jump_cooldown:
            jump_cooldown = 0
        jump_cooldown += 1
        if jump_cooldown == 1:
            cnvs.delete(cd_status_image)
            cd_status_image = cnvs.create_image(490, 40, image=cd_image)
        if jump_cooldown == 80:
            jump_cooldown = None
            cnvs.delete(cd_status_image)
            cd_status_image = cnvs.create_image(490, 40, image=nocd_image)
            return
        else:
            tk.after(100, cd2)
def wait_jump():
    global jump_cooldown, jump_text, jump_text_cooldown
    if not jump_text_cooldown:
        jump_text_cooldown = 0
    jump_text_cooldown += 1
    if jump_text_cooldown == 2:
        cnvs.delete(jump_text)
        tk.after_cancel(wait_jump)
        jump_text_cooldown = None
        return
    jump_text = cnvs.create_text(350, 750, text=("Подождите " + str(8-(jump_cooldown//10)) + " сек. перед следующим использованием"), fill="red", font=("Impact", 15))
    tk.after(1000, wait_jump)

def gen_brevno():
    global brevna
    if game == True:
        if brevna[0].status == False:
            brevna[0].initXY(player)
            brevna[0].obj = (cnvs.create_image(brevna[0].x, 96, image=brevno_image))
            brevna[0].status = True
        if brevna[1].status == False and brevna[0].y >= 450:
            brevna[1].initXY(player)
            brevna[1].obj = (cnvs.create_image(brevna[1].x, 96, image=brevno_image))
            brevna[1].status = True
        for i in range(2):
            if brevna[i].status != False:
                if brevna[i].y < 800:
                    cnvs.move(brevna[i].obj, 0, 12)
                    brevna[i].y += 12
                    check()
                else:
                    cnvs.delete(brevna[i].obj)
                    brevna[i].obj = None
                    brevna[i].status = False
        tk.after(50, gen_brevno)
    else:
        tk.after_cancel(gen_brevno)

def check():
    global brevna, player, deaths, balance, coins, coins_received, player, shield, game
    if game == True:
        cnvs.itemconfig(death_text, text=deaths)
        cnvs.itemconfig(money_text, text=balance)
        if player.y < 100:
            balance += 10
            balance = balance - deaths // 2
            shop_lines = str(balance), "\n", str(deaths + total_deaths)
            save_settings = open('resources\\settings.txt', 'w')
            save_settings.writelines(shop_lines)
            save_settings.close()
            cnvs.delete("all")
            cnvs.delete(death_text)
            cnvs.delete(money_text)
            game = False
            menu()
        for s in range(0, len(coins.obj)):
            if coins.x[s-1]+24 >= player.x and coins.x[s-1]-24 <= player.x and coins.y[s-1]+24 >= player.y and coins.y[s-1]-24 <= player.y:
                cnvs.delete(coins.obj[s-1])
                coins.obj.pop(s-1)
                coins.x.pop(s-1)
                coins.y.pop(s-1)
                balance += 1
                coins_received += 1
        for e in range(0, len(bombs_objs)):
            if bombs_x[e-1]+60 >= player.x and bombs_x[e-1]-60 <= player.x and bombs_y[e-1]+60 >= player.y and bombs_y[e-1]-60 <= player.y:
                if shield.status == True:
                    shield.status = None
                    cnvs.delete(shield.obj)
                    cnvs.delete(bombs_objs[e-1])
                    bombs_objs.pop(e-1)
                    bombs_y.pop(e-1)
                    bombs_x.pop(e-1)
                else:
                    cnvs.delete(bombs_objs[e-1])
                    bombs_objs.pop(e-1)
                    bombs_y.pop(e-1)
                    bombs_x.pop(e-1)
                    deaths += 1
                    cnvs.delete(player.obj)
                    player.obj = (cnvs.create_oval(330, 820, 370, 860, fill="black", width=3))
                    player.x = 350
                    player.y = 840
        if shield.status == False and shield.x+60 >= player.x and shield.x-60 <= player.x and shield.y+60 >= player.y and shield.y-60 <= player.y:
            shield.status = True
            cnvs.delete(shield.obj)
            shield.obj = (cnvs.create_oval(player.x+30, player.y+30, player.x-30, player.y-30, outline="red", width=3))
        for i in range(2):
            if brevna[i].y == player.y and player.x >= brevna[i].x-100 and player.x <= brevna[i].x+100:
                if shield.status == True:
                    shield.status = None
                    cnvs.delete(shield.obj)
                    brevna[i].status = None
                elif shield.status != True and brevna[i].status:
                    deaths += 1
                    cnvs.delete(player.obj)
                    player.obj = (cnvs.create_oval(330, 820, 370, 860, fill="black", width=3))
                    player.x = 350
                    player.y = 840

def gen_coins():
    global coins
    for i in range(7):
        a = random.randint(40, 660)
        a = a - a % 12
        coins.x.append(a)
    for j in range(7):
        a = random.randint(160, 800)
        a = a - a % 12
        coins.y.append(a)
    for e in range(0, 7):
        coins.obj.append(cnvs.create_image(coins.x[e], coins.y[e], image=coin_image))
def bomba():
    global bombs_objs, bombs_x, bombs_y
    for i in range(2):
        a = random.randint(40, 660)
        a = a - a % 12
        bombs_x.append(a)
    for j in range(2):
        a = random.randint(200, 600)
        a = a - a % 12
        bombs_y.append(a)
    bombs_objs.append(cnvs.create_image(bombs_x[0], bombs_y[0], image=bomb_image))
    bombs_objs.append(cnvs.create_image(bombs_x[1], bombs_y[1], image=bomb_image))
def menu():
    global deaths, balance, coins_received, total_deaths
    total_deaths += deaths
    cnvs = Canvas(bg='lime')
    cnvs.place(anchor=NW, height=900, width=700)
    win_text = Label(text="Пройдено!", bg="lime", font=("Impact", 80))
    win_text.place(x=100, y=30)
    death_stats = Label(text=("Смеретей: " + str(deaths)), bg="lime", font=("Impact", 30))
    death_stats.place(x=20, y=320)
    total_deaths_stats = Label(text=("Всего смертей: " + str(total_deaths)), bg="lime", font=("Impact", 30))
    total_deaths_stats.place(x=20, y=370)
    coin_stats = Label(text=("Собрано монет: " + str(coins_received)), bg="lime", font=("Impact", 30))
    coin_stats.place(x=20, y=420)
    salary = Label(text=("Заработано всего:  " + str(coins_received+10-deaths//2)), bg="lime", font=("Impact", 30))
    salary.place(x=20, y=470)
    balance_stats = Label(text=("Текущий баланс: " + str(balance)), bg="lime", font=("Impact", 30))
    balance_stats.place(x=20, y=520)
    play_again = Button(text="Играть снова", bg="green", command=restart, font=("Impact", 30))
    play_again.place(x=220, y=700, width=260, height=70)
def shop(event):
    global balance, coin_image, color_status, Buttons, game
    if help_status == False:
        game = False
        cnvs = Canvas()
        cnvs.place(anchor=NW, height=900, width=700)
        cnvs.create_image(600, 60, image=coin_image)
        money_text = Label(text=balance, font=("Impact", 25))
        money_text.place(x=620, y=40)
        color_status = []
        open_colors = open('resources\\colors.txt', 'r')
        shop_lines = open_colors.readlines()
        open_colors.close()
        for i in range(len(shop_lines)):
            if shop_lines[i] == "yes\n":
                color_status.append("Выбрать")
            elif shop_lines[i] == "no\n" or shop_lines[i] == "no":
                color_status.append("Купить")
        selected = int(shop_lines[1])
        color_status[selected] = "Выбрано"
        text = Label(text="Магазин", font=("Impact", 50))
        text.place(x=10, y=20)
        play_button = Button(text="Назад", bg="red", command=restart, font=("Impact", 30))
        play_button.place(x=230, y=770, width=200, height=100)
        Buttons = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        Buttons[0] = Button(bg="sienna4", text=color_status[0], anchor=SW, command=lambda:(buy_color("sienna4", 0)), font=("Impact", 12))
        Buttons[0].place(x=20, y=120, width=100, height=100)
        Buttons[1] = Button(bg="coral", text=color_status[1], anchor=SW, command=lambda:(buy_color("coral", 1)), font=("Impact", 12))
        Buttons[1].place(x=20, y=240, width=100, height=100)
        Buttons[2] = Button(bg="orange", text=color_status[2], anchor=SW, command=lambda:(buy_color("orange", 2)), font=("Impact", 12))
        Buttons[2].place(x=20, y=360, width=100, height=100)
        Buttons[3] = Button(bg="gold", text=color_status[3], anchor=SW, command=lambda:(buy_color("gold", 3)), font=("Impact", 12))
        Buttons[3].place(x=20, y=480, width=100, height=100)
        Buttons[4] = Button(bg="yellow", text=color_status[4], anchor=SW, command=lambda:(buy_color("yellow", 4)), font=("Impact", 12))
        Buttons[4].place(x=20, y=600, width=100, height=100)
        Buttons[5] = Button(bg="green", text=color_status[5], anchor=SW, command=lambda:(buy_color("green", 5)), font=("Impact", 12))
        Buttons[5].place(x=140, y=120, width=100, height=100)
        Buttons[6] = Button(bg="lime", text=color_status[6], anchor=SW, command=lambda:(buy_color("lime", 6)), font=("Impact", 12))
        Buttons[6].place(x=140, y=240, width=100, height=100)
        Buttons[7] = Button(bg="cyan", text=color_status[7], anchor=SW, command=lambda:(buy_color("cyan", 7)), font=("Impact", 12))
        Buttons[7].place(x=140, y=360, width=100, height=100)
        Buttons[8] = Button(bg="turquoise", text=color_status[8], anchor=SW, command=lambda:(buy_color("turquoise", 8)), font=("Impact", 12))
        Buttons[8].place(x=140, y=480, width=100, height=100)
        Buttons[9] = Button(bg="blue", text=color_status[9], anchor=SW, command=lambda:(buy_color("blue", 9)), font=("Impact", 12))
        Buttons[9].place(x=140, y=600, width=100, height=100)
        Buttons[10] = Button(bg="SlateBlue2", text=color_status[10], anchor=SW, command=lambda:(buy_color("SlateBlue2", 10)), font=("Impact", 12))
        Buttons[10].place(x=260, y=120, width=100, height=100)
        Buttons[11] = Button(bg="Purple", text=color_status[11], anchor=SW, command=lambda:(buy_color("Purple", 11)), font=("Impact", 12))
        Buttons[11].place(x=260, y=240, width=100, height=100)
        Buttons[12] = Button(bg="DarkOrchid1", text=color_status[12], anchor=SW, command=lambda:(buy_color("DarkOrchid1", 12)), font=("Impact", 12))
        Buttons[12].place(x=260, y=360, width=100, height=100)
        Buttons[13] = Button(bg="Pink", text=color_status[13], anchor=SW, command=lambda:(buy_color("Pink", 13)), font=("Impact", 12))
        Buttons[13].place(x=260, y=480, width=100, height=100)
        Buttons[14] = Button(bg="White", text=color_status[14], anchor=SW, command=lambda:(buy_color("White", 14)), font=("Impact", 12))
        Buttons[14].place(x=260, y=600, width=100, height=100)
def meterorit():
    global meteorit_x, meteorit_y, killtime, player, meteorit_obj
    if game == True:
        meteorit_x = random.randint(player.x-200, player.x+200) 
        meteorit_x = meteorit_x - meteorit_x % 12
        meteorit_y = random.randint(player.y-200, player.y+200)
        meteorit_y = meteorit_y - meteorit_y % 12
        if meteorit_y < 225:
            meteorit_y = 225
        if meteorit_y > 675:
            meteorit_y = 675
        if meteorit_x < 150:
            meteorit_x = 150
        if meteorit_x > 600:
            meteorit_x = 600
        killtime = random.randint(15, 30)
        cnvs.moveto(meteorit_obj, meteorit_x-150, meteorit_y-150)
        meteorit_timer()
    tk.after(5000, meterorit)   

def meteorit_timer():
    global h, deaths, player, shield
    if game == True:
        h = h + 1
        if killtime == h:
            cnvs.moveto(meteorit_obj, 5000, 5000)
            if ((meteorit_x - player.x)**2 + (meteorit_y - player.y)**2)**0.5 <= 125 and killtime == h:
                if shield.status == True:
                    shield.status = False
                    cnvs.delete(shield.obj)
                else:
                    deaths += 1
                    cnvs.delete(player.obj)
                    player.obj = (cnvs.create_oval(330, 820, 370, 860, fill="black", width=3))
                    player.x = 350
                    player.y = 840
            h = 0
            tk.after_cancel(meteorit_timer)
            return
    tk.after(100, meteorit_timer)
def buy_color(color, position):
    global balance, nomoney_status, Buttons
    open_file = open('resources\\colors.txt', 'r')
    shop_lines = open_file.readlines()
    for i in range(len(shop_lines)):
        line = shop_lines[i]
        shop_lines[i] = line[:-1]
    if shop_lines[position+2] == "no":
        if balance >= 10:
            balance = balance - 10
            shop_lines[position+2] = "yes"
            for i in range(2, len(shop_lines)):
                line = shop_lines[i]
                shop_lines[i] = line + "\n"
            shop_lines[0] = color + "\n"
            shop_lines[1] = str(position) + "\n"
            shop_lines.append("\n")
            open_colors = open('resources\\colors.txt', 'w')
            open_colors.writelines(shop_lines)
            open_colors.close()
            shop_lines = [(str(balance) + "\n"),  (str(total_deaths) + "\n")]
            open_colors = open('resources\\settings.txt', 'w')
            open_colors.writelines(shop_lines)
            open_colors.close()
            cnvs.delete("all")
            for i in range(len(Buttons)):
                Buttons[i].destroy()
            shop("a")
        else:
            if nomoney_status == False:
                no_money()
                return
    else:
        open_colors = open('resources\\colors.txt', 'w')
        for i in range(2, len(shop_lines)):
            line = shop_lines[i]
            shop_lines[i] = line + "\n"
        shop_lines[0] = color + "\n"
        shop_lines[1] = str(position) + "\n"
        open_colors.writelines(shop_lines)
        open_colors.close()
        cnvs.delete("all")
        for i in range(len(Buttons)):
            Buttons[i].destroy()
        shop("a")
        
def no_money():
    global e, nomoney_text, nomoney_status, cnvs
    nomoney_status = True
    e = e+1
    if e == 2:
        nomoney_text.destroy()
        tk.after_cancel(no_money)
        nomoney_status = False
        e = 0
        return
    nomoney_text = Label(text="Недостаточно средств", fg="red", font=("Impact", 25))
    nomoney_text.place(x=150, y=730)
    tk.after(1000, no_money)
def pause(event):
    global game, pause_button, help_status
    if game == False and help_status == False:
        game = True
        cnvs.delete(pause_button)
        pause_button = cnvs.create_image(50, 50, image=pause_image)
        gen_brevno()
        check()
    elif game == True:
        game = False
        cnvs.delete(pause_button)
        pause_button = cnvs.create_image(50, 50, image=continue_image)
    cnvs.tag_bind(pause_button, '<Button-1>', pause)
def help(event):
    global game, cnvs2, rules_image, close_button, help_status
    if help_status == False:
        help_status = True
        game = False
        cnvs2 = Canvas(highlightbackground="black")
        cnvs2.place(x=150, y=150, height=600, width=400)
        cnvs2.create_image(200, 300, image=rules_image)
        close_button = Button(bg="Red", text="Ок", command=lambda:(cnvs2.destroy(), close_button.destroy(), close_help()), font=("Impact", 25))
        close_button.place(x=300, y=670, width=100, height=50)
def close_help():
    global game, help_status
    game = True
    gen_brevno()
    check()
    help_status = False
def key(event):
    if game == True:
        if event.keycode == 87 or event.keycode == 38:
            press_w(event)
        if event.keycode == 68 or event.keycode == 39:
            press_d(event)
        if event.keycode == 65 or event.keycode == 37:
            press_a(event)
        if event.keycode == 83 or event.keycode == 40:
            press_s(event)
        if event.keycode == 81:
            jump(event)
tk.bind('<Key>', key)
restart()
mainloop()
