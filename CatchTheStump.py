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
objects = ["", "", "", ""]
x1 = 350 
y1 = 850
h1 = 0
h2 = 0
h3 = 0 
h4 = 0
e = 0
q = 0
c = 0
b2 = 0
b3 = 0
b1 = 0
v1 = []
v2 = []
w_cooldown = False
a_cooldown = False
d_cooldown = False
s_cooldown = False
wait_status = False
game = True
nomoney_status = False
time = 0
monetka = []
deaths = 0
coins_received = 0
balance = 0
cooldown2 = False
def restart():
    global cooldown, cooldown2, bombs1, bombs2, bomba, bomba_image, brevno_status1, brevno_status2, brevno_status3, cd_status_image, balance, cnvs, brevno_image, deaths_image, coin_image, cd_image, nocd_image, death_text, money_text, objects, lines, game, deaths, total_deaths, x1, y1, monetka, coins_received, v1, v2
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
    сooldown = False
    cooldown2 = False
    coins_received = 0
    brevno_status1 = False
    brevno_status2 = False
    brevno_status3 = False
    open_settings = open('resources\\settings.txt', 'r')
    lines = open_settings.readlines()
    open_settings.close()
    balance = int(lines[0])
    total_deaths = int(lines[1])
    open_colors = open('resources\\colors.txt', 'r')
    lines = open_colors.readlines()
    color = lines[0]
    color = color[:-1]
    open_colors.close()
    if balance > 999:
        balance = 999
    cnvs = Canvas(bg=color)
    cnvs.place(anchor=NW, height=900, width=700)
    cnvs.create_rectangle(-5, 100, 705, 105, fill="black")
    cnvs.create_rectangle(-5, 800, 705, 805, fill="black")
    brevno_image = PhotoImage(file='images\\stump.png')
    deaths_image = PhotoImage(file='images\\death.png')
    coin_image = PhotoImage(file="images\\coin.png")
    bomba_image = PhotoImage(file="images\\bomb.png")
    cd_image = PhotoImage(file="images\\cooldown_unavailable.png")
    nocd_image = PhotoImage(file="images\\cooldown_available.png")
    cnvs.create_image(640, 40, image=deaths_image)
    cnvs.create_image(540, 40, image=coin_image)
    cd_status_image = cnvs.create_image(490, 40, image=nocd_image)
    death_text = Label(text=deaths, bg=color, font=("Impact", 25))
    death_text.place(x=660, y=20)
    money_text = Label(text=balance, bg=color, font=("Impact", 25))
    money_text.place(x=560, y=20)
    objects[0] = (cnvs.create_oval(330, 820, 370, 860, fill="blue", width=3))
    brevno1()
    brevno2()
    brevno3()
    coins()
    gen_bomba()
    check()
def press_w(event):
    global w_cooldown, x1, y1, lines, cnvs, game, balance, total_deaths
    if game == True:
        if y1 < 100:
            balance += 10
            balance = balance - deaths // 2
            lines = str(balance), "\n", str(deaths + total_deaths)
            save_settings = open('settings.txt', 'w')
            save_settings.writelines(lines)
            save_settings.close()
            cnvs.delete("all")
            death_text.destroy()
            money_text.destroy()
            game = False
            menu()
        if w_cooldown == False:
            y1 = y1 - 12
            cnvs.move(objects[0], 0, -12)
            w_cd()
def press_s(event):
    global s_cooldown, x1, y1
    if game == True:
        if y1 < 770:
            if s_cooldown == False:
                y1 = y1 + 12
                cnvs.move(objects[0], 0, 12)
                s_cd()
def press_a(event):
    global a_cooldown, x1, y1
    if game == True:
        if x1 > 30:   
            if a_cooldown == False:
                x1 = x1 - 12
                cnvs.move(objects[0], -12, 0)
                a_cd()
def press_d(event):
    global d_cooldown, x1, y1
    if game == True:
        if x1 < 670:
            if d_cooldown == False:
                x1 = x1 + 12
                cnvs.move(objects[0], 12, 0)
                d_cd()
def cheat(event):
    global cooldown2, x1, y1, lines, cnvs, game, balance, total_deaths
    if game == True:
        if cooldown2 == False:
            y1 = y1 - 108
            cnvs.move(objects[0], 0,-108)
            cd2()
            if y1 < 100:
                balance += 10
                balance = balance - deaths // 2
                lines = str(balance), "\n", str(deaths + total_deaths)
                save_settings = open('settings.txt', 'w')
                save_settings.writelines(lines)
                save_settings.close()
                cnvs.delete("all")
                death_text.destroy()
                money_text.destroy()
                game = False
                menu()
        else:
            if wait_status == False:
                wait()
def cd2():
    global cooldown2, q, cd_status_image, cd_image, nocd_image, game
    if game == True:
        cooldown2 = True
        q = q + 1
        if q == 1:
            cnvs.delete(cd_status_image)
            cd_status_image = cnvs.create_image(490, 40, image=cd_image)
        if q == 100:
            cooldown2 = False
            q = 0
            cnvs.delete(cd_status_image)
            cd_status_image = cnvs.create_image(490, 40, image=nocd_image)
            return
        else:
            tk.after(100, cd2)
def wait():
    global q, c, wait_text, wait_status
    wait_status = True
    c = c+1
    if c == 2:
        cnvs.delete(wait_text)
        tk.after_cancel(wait)
        wait_status = False
        c = 0
        return
    wait_text = cnvs.create_text(350, 750, text=("Подождите " + str(10-(q//10)) + " сек. перед следующим использованием"), fill="red", font=("Impact", 15))
    tk.after(1000, wait)
def w_cd():
    global w_cooldown, h1, x1, y1
    w_cooldown = True
    h1 = h1 + 1
    if h1 == 2:
        w_cooldown = False
        tk.after_cancel(w_cd)
        h1 = 0
        return
    tk.after(120, w_cd)
def a_cd():
    global a_cooldown, h2, x1, y1
    a_cooldown = True
    h2 = h2 + 1
    if h2 == 2:
        a_cooldown = False
        tk.after_cancel(a_cd)
        h2 = 0
        return
    tk.after(80, a_cd)
def s_cd():
    global s_cooldown, h3, x1, y1
    s_cooldown = True
    h3 = h3 + 1
    if h3 == 2:
        s_cooldown = False
        tk.after_cancel(s_cd)
        h3 = 0
        return
    tk.after(80, s_cd)
def d_cd():
    global d_cooldown, h4, x1, y1
    d_cooldown = True
    h4 = h4 + 1
    if h4 == 2:
        d_cooldown = False
        tk.after_cancel(d_cd)
        h4 = 0
        return
    tk.after(80, d_cd)
def brevno1():
    global brevno_status1, brevno_status2, brevno_status3, a1, a2, a3, b1, b2, b3, x1, y1
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
            else:
                cnvs.delete(objects[1])
                objects[1] = "" 
                brevno_status1 = False
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
            else:
                cnvs.delete(objects[2])
                objects[2] = "" 
                brevno_status2 = False
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
            else:
                cnvs.delete(objects[3])
                objects[3] = "" 
                brevno_status3 = False 
        tk.after(60, brevno3)
    else:
        tk.after_cancel(brevno3)

def check():
    global brevno_status1, brevno_status2, brevno_status3, a1, a2, a3, b1, b2, b3, x1, y1, deaths, monetka, balance, v1, v2, time, coins_received
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
            if bombs2[e-1]+60 >= x1 and bombs2[e-1]-60 <= x1 and bombs1[e-1]+60 >= y1 and bombs1[e-1]-60 <= y1:
                cnvs.delete(bomba[e-1])
                bomba.pop(e-1)
                bombs2.pop(e-1)
                bombs1.pop(e-1)
                deaths += 1
                cnvs.delete(objects[0])
                objects[0] = (cnvs.create_oval(330, 820, 370, 860, fill="blue", width=3))
                x1 = 350
                y1 = 840
        if b3 == y1 and x1 >= a3-100 and x1 <= a3+100:
            deaths += 1
            cnvs.delete(objects[0])
            objects[0] = (cnvs.create_oval(330, 820, 370, 860, fill="blue", width=3))
            x1 = 350
            y1 = 840
        if b2 == y1 and x1 >= a2-100 and x1 <= a2+100:
            deaths += 1
            cnvs.delete(objects[0])
            objects[0] = (cnvs.create_oval(330, 820, 370, 860, fill="blue", width=3))
            x1 = 350
            y1 = 840
        if b1 == y1 and x1 >= a1-100 and x1 <= a1+100:
            deaths += 1
            cnvs.delete(objects[0])
            objects[0] = (cnvs.create_oval(330, 820, 370, 860, fill="blue", width=3))
            x1 = 350
            y1 = 840
        tk.after(1, check)
    else:
        tk.after_cancel(check)
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
        a = random.randint(300, 800)
        a = a - a % 20 - 10
        bombs1.append(a)
    for j in range(2):
        a = random.randint(40, 660)
        a = a - a % 20 - 10
        bombs2.append(a)
    bomba.append(cnvs.create_image(bombs2[0], bombs1[0], image=bomba_image))
    bomba.append(cnvs.create_image(bombs2[1], bombs1[1], image=bomba_image))
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
def shop():
    global color_change, balance, color, coin_image, color_status, Buttons
    cnvs = Canvas()
    cnvs.place(anchor=NW, height=900, width=700)
    cnvs.create_image(600, 60, image=coin_image)
    money_text = Label(text=balance, font=("Impact", 25))
    money_text.place(x=620, y=40)
    color_status = []
    open_colors = open('colors.txt', 'r')
    lines = open_colors.readlines()
    open_colors.close()
    for i in range(len(lines)):
        if lines[i] == "yes\n":
            color_status.append("Выбрать")
        elif lines[i] == "no\n" or lines[i] == "no":
            color_status.append("Купить")
    selected = int(lines[1])
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
def buy_color(color, position):
    global balance, nomoney_status, Buttons
    open_colors = open('resources\\colors.txt', 'r')
    lines = open_colors.readlines()
    open_colors.close()
    for i in range(2, len(lines)):
        line = lines[i]
        lines[i] = line[:-1]
    if lines[position+2] == "no":
        if balance >= 10:
            balance = balance - 10
            lines[position+2] = "yes"
            for i in range(2, len(lines)):
                line = lines[i]
                lines[i] = line + "\n"
            lines.append("\n")
            open_colors = open('resources\\colors.txt', 'w')
            open_colors.writelines(lines)
            open_colors.close()
            open_colors = open('resources\\settings.txt', 'r')
            lines = open_colors.readlines()
            open_colors.close()
            lines[0] = str(balance) + "\n"
            open_colors = open('resources\\settings.txt', 'w')
            open_colors.writelines(lines)
            open_colors.close()
            open_colors = open('resources\\colors.txt', 'r')
            lines = open_colors.readlines()
            open_colors.close()
            open_colors = open('resources\\colors.txt', 'w')
            lines[0] = color + "\n"
            lines[1] = str(position) + "\n"
            open_colors.writelines(lines)
            open_colors.close()
            cnvs.delete("all")
            for i in range(len(Buttons)):
                Buttons[i].destroy()
            shop()
        else:
            if nomoney_status == False:
                no_money()
                return
    else:
        open_colors = open('resources\\colors.txt', 'r')
        lines = open_colors.readlines()
        open_colors.close()
        open_colors = open('resources\\colors.txt', 'w')
        lines[0] = color + "\n"
        lines[1] = str(position) + "\n"
        open_colors.writelines(lines)
        open_colors.close()
        cnvs.delete("all")
        for i in range(len(Buttons)):
            Buttons[i].destroy()
        shop()
        
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
def x(event):
    global game
    cnvs.delete("all")
    game = False
    shop()
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
            cheat(event)
    if event.keycode == 88:
            x(event)
    
tk.bind('<Key>', key)
tk.bind('<Key>', key)
tk.bind('<Key>', key)
tk.bind('<Key>', key)
tk.bind('<Key>', key)
tk.bind('<Key>', key)
restart()
mainloop()



