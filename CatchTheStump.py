from tkinter import *
import random
import os
tk = Tk()
geometry = str(700) + "x" + str(900) + "+" + str((tk.winfo_screenwidth()//2) - 350) + "+" + str(tk.winfo_screenheight()-1000)
tk.geometry(geometry)
tk.resizable(width=False, height=False)
tk.title("Убеги от пенька")
tk.config(cursor="plus")
tk.iconbitmap("images\\icon.ico")
objects = [" ", " ", " ", " "]
e = 0
b2 = 0
b3 = 0
b1 = 0
v1 = []
v2 = []
w_cooldown = None
a_cooldown = None
d_cooldown = None
s_cooldown = None
jump_text_cooldown = False
jump_cooldown = None
game = True
help_status = False
nomoney_status = False
time = 0
dislikes = [" ", " ", " "]
monetka = []
deaths = 0
coins_received = 0
balance = 0
number = None
def restart():
    global jump_cooldown, player, dislike_image, pause_image, continue_image, shield_status, shield_pos, rules_image, shield_image, help_image, shop_button, help_button, shop_image, pause_button, bombs1, bombs2, bomba, bomba_image, brevno_status1, brevno_status2, brevno_status3, cd_status_image, balance, cnvs, brevno_image, deaths_image, coin_image, cd_image, nocd_image, death_text, money_text, objects, shop_lines, game, deaths, total_deaths, x1, y1, monetka, coins_received, v1, v2
    game = True
    deaths = 0
    monetka = []
    x1 = 350 
    y1 = 840
    v1 = []
    v2 = []
    bombs1 = []
    bombs2 = []
    bomba = []
    shield_pos = []
    jump_cooldown = None
    coins_received = 0
    brevno_status1 = False
    brevno_status2 = False
    brevno_status3 = False
    shield_status = False
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
    if balance > 999:
        balance = 999
    cnvs = Canvas(bg=color, highlightbackground=color)
    cnvs.place(anchor=NW, height=900, width=700)
    cnvs.create_rectangle(-5, 100, 705, 105, fill="black")
    cnvs.create_rectangle(-5, 800, 705, 805, fill="black")
    brevno_image = PhotoImage(file='images\\stump.png')
    deaths_image = PhotoImage(file='images\\death.png')
    coin_image = PhotoImage(file="images\\coin.png")
    bomba_image = PhotoImage(file="images\\bomb.png")
    cd_image = PhotoImage(file="images\\cooldown_unavailable.png")
    nocd_image = PhotoImage(file="images\\cooldown_available.png")
    pause_image = PhotoImage(file="images\\pause.png")
    help_image = PhotoImage(file="images\\help.png")
    rules_image = PhotoImage(file="images\\rules.png")
    shop_image = PhotoImage(file="images\\shop.png")
    continue_image = PhotoImage(file="images\\continue.png")
    dislike_image = PhotoImage(file="images\\dislike.png")
    shield_image = PhotoImage(file="images\\shield.png")
    cnvs.create_image(640, 40, image=deaths_image)
    cnvs.create_image(540, 40, image=coin_image)
    cd_status_image = cnvs.create_image(490, 40, image=nocd_image)
    death_text = Label(text=deaths, bg=color, font=("Impact", 25))
    death_text.place(x=660, y=20)
    money_text = Label(text=balance, bg=color, font=("Impact", 25))
    money_text.place(x=560, y=20)
    pause_button = cnvs.create_image(50, 50, image=pause_image)
    cnvs.tag_bind(pause_button, '<Button-1>', pause)
    help_button = cnvs.create_image(130, 50, image=help_image)
    cnvs.tag_bind(help_button, '<Button-1>', help)
    shop_button = cnvs.create_image(210, 50, image=shop_image)
    cnvs.tag_bind(shop_button, '<Button-1>', shop)
    player = (cnvs.create_oval(330, 820, 370, 860, fill="black", width=3))
    brevno1()
    brevno2()
    brevno3()
    shield()
    coins()
    gen_bomba()
    check()
def press_w(event):
    global w_cooldown, x1, y1, shop_lines, cnvs, game, balance, total_deaths, shield_object
    if game == True:
        if y1 < 100:
            balance += 10
            balance = balance - deaths // 2
            shop_lines = str(balance), "\n", str(deaths + total_deaths)
            save_settings = open('resources\\settings.txt', 'w')
            save_settings.writelines(shop_lines)
            save_settings.close()
            cnvs.delete("all")
            death_text.destroy()
            money_text.destroy()
            game = False
            menu()
        if not w_cooldown:
            y1 = y1 - 12
            cnvs.move(player, 0, -12)
            if shield_status == True:
                print(shield_status)
                cnvs.move(shield_object, 0, -12)
            w_cd()

def press_s(event):
    global s_cooldown, x1, y1
    if game == True:
        if y1 < 770:
            if not s_cooldown:
                y1 = y1 + 12
                cnvs.move(player, 0, 12)
                if shield_status == True:
                    cnvs.move(shield_object, 0, 12)
                s_cd()
def press_a(event):
    global a_cooldown, x1, y1
    if game == True:
        if x1 > 30:   
            if not a_cooldown:
                x1 = x1 - 12
                cnvs.move(player, -12, 0)
                if shield_status == True:
                    cnvs.move(shield_object, -12, 0)
                a_cd()
def press_d(event):
    global d_cooldown, x1, y1
    if game == True:
        if x1 < 670:
            if not d_cooldown:
                x1 = x1 + 12
                cnvs.move(player, 12, 0)
                if shield_status == True:
                    cnvs.move(shield_object, 12, 0)
                d_cd()
def jump(event):
    global jump_cooldown, x1, y1, shop_lines, cnvs, game, balance, total_deaths
    if game == True:
        if not jump_cooldown:
            y1 = y1 - 108
            cnvs.move(player, 0,-108)
            if shield_status == True:
                    cnvs.move(shield_object, 0, -108)
            if y1 < 100:
                balance += 10
                balance = balance - deaths // 2
                shop_lines = str(balance), "\n", str(deaths + total_deaths)
                save_settings = open('resources\\settings.txt', 'w')
                save_settings.writelines(shop_lines)
                save_settings.close()
                cnvs.delete("all")
                death_text.destroy()
                money_text.destroy()
                game = False
                menu()
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
def w_cd():
    global w_cooldown, x1, y1
    w_cooldown = 1 if not w_cooldown else w_cooldown + 1 
    if w_cooldown == 2:
        w_cooldown = None
        tk.after_cancel(w_cd)
        return
    tk.after(120, w_cd)
def a_cd():
    global a_cooldown, x1, y1
    a_cooldown = 1 if not a_cooldown else a_cooldown + 1 
    if a_cooldown == 2:
        a_cooldown = None
        tk.after_cancel(a_cd)
        return
    tk.after(120, a_cd)
def s_cd():
    global s_cooldown, x1, y1
    s_cooldown = 1 if not s_cooldown else s_cooldown + 1 
    if s_cooldown == 2:
        s_cooldown = None
        tk.after_cancel(s_cd)
        return
    tk.after(120, s_cd)
def d_cd():
    global d_cooldown, x1, y1
    d_cooldown = 1 if not d_cooldown else d_cooldown + 1 
    if d_cooldown == 2:
        d_cooldown = None
        tk.after_cancel(d_cd)
        return
    tk.after(120, d_cd)
def brevno1():
    global brevno_status1, brevno_status2, brevno_status3, a1, a2, a3, b1, b2, b3, x1, y1, number, dislikes
    if game == True:
        if brevno_status1 == False:
            a1 = random.randint(x1-200, x1+200)
            if a1 < 100:
                a1 = 100
            if a1 > 600:
                a1 = 600
            b1 = 96
            brevno_status1 = True
            objects[1] = (cnvs.create_image(a1, 96, image=brevno_image))
        elif brevno_status1 == True:
            if b1 < 800: 
                cnvs.move(objects[1], 0, 12)
                b1 += 12
                if number == 0:
                    cnvs.move(dislikes[0], 0, 12)
            else:
                cnvs.delete(objects[1])
                objects[1] = "" 
                brevno_status1 = False
                if number == 0:
                    cnvs.delete(dislikes[0])
                    dislikes[0] = " "
        tk.after(60, brevno1)
    else:
        tk.after_cancel(brevno1)
def brevno2():
    global brevno_status1, brevno_status2, brevno_status3, a1, a2, a3, b1, b2, b3, x1, y1
    if game == True:
        if brevno_status2 == False and b1 >= 350:
            a2 = random.randint(x1-200, x1+200)
            b2 = 96
            if a2 < 100:
                a2 = 100
            if a2 > 600:
                a2 = 600
            brevno_status2 = True
            objects[2] = (cnvs.create_image(a2, 96, image=brevno_image))
        elif brevno_status2 == True:
            if b2 < 800: 
                cnvs.move(objects[2], 0, 12)
                b2 += 12
                if number == 1:
                    cnvs.move(dislikes[1], 0, 12)
            else:
                cnvs.delete(objects[2])
                objects[2] = "" 
                brevno_status2 = False
                if number == 1:
                    cnvs.delete(dislikes[1])
                    dislikes[1] = " "
        tk.after(60, brevno2)
    else:
        tk.after_cancel(brevno2)
def brevno3():
    global brevno_status1, brevno_status2, brevno_status3, a1, a2, a3, b1, b2, b3, x1, y1
    if game == True:
        if brevno_status3 == False and b1 >= 590:
            a3 = random.randint(x1-200, x1+200)
            b3 = 96
            if a3 < 100:
                a3 = 100
            if a3 > 600:
                a3 = 600
            brevno_status3 = True
            objects[3] = (cnvs.create_image(a3, 96, image=brevno_image))
        elif brevno_status3 == True:
            if b3 < 800: 
                cnvs.move(objects[3], 0, 12)
                b3 += 12  
                if number == 2:
                    cnvs.move(dislikes[2], 0, 12)
            else:
                cnvs.delete(objects[3])
                objects[3] = "" 
                brevno_status3 = False 
                if number == 2:
                    cnvs.delete(dislikes[2])
                    dislikes[2] = " "
        tk.after(60, brevno3)
    else:
        tk.after_cancel(brevno3)

def check():
    global brevno_status1, brevno_status2, brevno_status3, a1, a2, a3, b1, b2, b3, x1, y1, deaths, monetka, balance, v1, v2, time, coins_received, player, shield_status, shield_object, shield_pos
    if game == True:
        death_text.configure(text=deaths)
        money_text.configure(text=balance)
        time += 1
        for s in range(0, len(monetka)):
            if v2[s-1]+24 >= x1 and v2[s-1]-24 <= x1 and v1[s-1]+24 >= y1 and v1[s-1]-24 <= y1:
                cnvs.delete(monetka[s-1])
                monetka.pop(s-1)
                v2.pop(s-1)
                v1.pop(s-1)
                balance += 1
                coins_received += 1
        for e in range(0, len(bomba)):
            if bombs1[e-1]+60 >= x1 and bombs1[e-1]-60 <= x1 and bombs2[e-1]+60 >= y1 and bombs2[e-1]-60 <= y1:
                if shield_status == True:
                    shield_status = False
                    cnvs.delete(shield_object)
                    bomba.pop(e-1)
                    bombs2.pop(e-1)
                    bombs1.pop(e-1)
                else:
                    cnvs.delete(bomba[e-1])
                    bomba.pop(e-1)
                    bombs2.pop(e-1)
                    bombs1.pop(e-1)
                    deaths += 1
                    cnvs.delete(player)
                    player = (cnvs.create_oval(330, 820, 370, 860, fill="black", width=3))
                    x1 = 350
                    y1 = 840
        if shield_pos[0]+60 >= x1 and shield_pos[0]-60 <= x1 and shield_pos[1]+60 >= y1 and shield_pos[1]-60 <= y1:
            shield_status = True
            shield_pos = [5000, 50000]
            cnvs.delete(shield_object)
            shield_object = (cnvs.create_oval(x1+30, y1+30, x1-30, y1-30, outline="light blue", width=2))
        if b3 == y1 and x1 >= a3-100 and x1 <= a3+100:
            if shield_status == True:
                shield_status = False
                cnvs.delete(shield_object)
            else:
                deaths += 1
                cnvs.delete(player)
                player = (cnvs.create_oval(330, 820, 370, 860, fill="black", width=3))
                x1 = 350
                y1 = 840
                dis(2, a3, b3)
        if b2 == y1 and x1 >= a2-100 and x1 <= a2+100:
            if shield_status == True:
                shield_status = False
                cnvs.delete(shield_object)
            else:
                deaths += 1
                cnvs.delete(player)
                player = (cnvs.create_oval(330, 820, 370, 860, fill="black", width=3))
                x1 = 350
                y1 = 840
                dis(1, a2, b2)
        if b1 == y1 and x1 >= a1-100 and x1 <= a1+100:
            if shield_status == True:
                shield_status = False
                cnvs.delete(shield_object)
            else:
                deaths += 1
                cnvs.delete(player)
                player = (cnvs.create_oval(330, 820, 370, 860, fill="black", width=3))
                x1 = 350
                y1 = 840
                dis(0, a1, b1)
        tk.after(60, check)
    else:
        tk.after_cancel(check)
def dis(numb, x, y):
    global dislikes, number
    if dislikes[numb] == " ":
        dislikes[numb] = cnvs.create_image(x+60, y-55, image=dislike_image)
        number = numb
def coins():
    global monetka, v1, v2
    for i in range(7):
        a = random.randint(160, 800)
        a = a - a % 20 - 10
        v1.append(a)
    for j in range(7):
        a = random.randint(40, 660)
        a = a - a % 20 - 10
        v2.append(a)
    for e in range(0, 7):
        monetka.append(cnvs.create_image(v2[e], v1[e], image=coin_image))
def gen_bomba():
    global bomba, bombs1, bombs2
    for i in range(2):
        a = random.randint(40, 660)
        a = a - a % 12
        bombs1.append(a)
    for j in range(2):
        a = random.randint(200, 600)
        a = a - a % 12
        bombs2.append(a)
    bomba.append(cnvs.create_image(bombs1[0], bombs2[0], image=bomba_image))
    bomba.append(cnvs.create_image(bombs1[1], bombs2[1], image=bomba_image))
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
def shield():
    global shield_pos, shield_object
    shield_pos = []
    a = random.randint(60, 660)
    a = a - a % 12
    shield_pos.append(a)
    a = random.randint(200, 600)
    a = a - a % 12
    shield_pos.append(a)
    shield_object = cnvs.create_image(shield_pos[0], shield_pos[1], image=shield_image)
    
def buy_color(color, position):
    global balance, nomoney_status, Buttons
    open_file = open('resources\\colors.txt', 'r')
    shop_lines = open_file.readlines()
    print(shop_lines)
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
        brevno1()
        brevno2()
        brevno3()
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
    brevno1()
    brevno2()
    brevno3()
    check()
    help_status = False
def key(event):
    if game == True:
        if event.keycode == 87:
            press_w(event)
        if event.keycode == 68:
            press_d(event)
        if event.keycode == 65:
            press_a(event)
        if event.keycode == 83:
            press_s(event)
        if event.keycode == 81:
            jump(event)
tk.bind('<Key>', key)
restart()
mainloop()
