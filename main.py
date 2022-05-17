from tkinter import *
import random
import os
from tkinter import messagebox

tk = Tk()
geometry = str(700) + "x" + str(900) + "+" + str((tk.winfo_screenwidth()//2) - 350) + "+" + str(tk.winfo_screenheight()-980)
tk.geometry(geometry)
tk.resizable(width=False, height=False)
tk.title("            Temjik GAMES: CatchTheStump")
tk.config(cursor="plus")
#tk.iconbitmap("images/icon.ico")
brevno_image = PhotoImage(file='images/stump.png')
deaths_image = PhotoImage(file='images/death.png')
coin_image = PhotoImage(file="images/coin.png")
coin_counter_image = PhotoImage(file="images/coin_counter.png")
bomb_image = PhotoImage(file="images/bomb.png")
cd_image = PhotoImage(file="images/cooldown_unavailable.png")
nocd_image = PhotoImage(file="images/cooldown_available.png")
pause_image = PhotoImage(file="images/pause.png")
help_image = PhotoImage(file="images/help.png")
rules_image = PhotoImage(file="images/rules.png")
shop_image = PhotoImage(file="images/shop.png")
continue_image = PhotoImage(file="images/continue.png")
shield_image = PhotoImage(file="images/shield.png")
meterorit_image = PhotoImage(file="images/meteorit.png")
settings_image = PhotoImage(file="images/settings.png")
def restart():
    class Player:
        x = 350 
        y = 840
        obj = None
    player = Player()

    class Shield:
        x = random.randint(60, 660)
        x = x - x % 12
        y = random.randint(200, 600)
        y = y - y % 12
        status = False
        obj = None
    shield = Shield()

    def shop(event):
        print("Тех. работы")

    class New_game:
        def __init__(self):
            self.files()
            self.status = False
            self.deaths = 0
            self.help_status = False
            self.cnvs = Canvas(bg=self.color, highlightbackground=self.color)
            self.cnvs.place(anchor=NW, height=900, width=700)
            self.cnvs.create_rectangle(-5, 100, 705, 105, fill="black")
            self.cnvs.create_rectangle(-5, 800, 705, 805, fill="black")
            self.cnvs.create_image(620, 50, image=deaths_image)
            self.cnvs.create_image(480, 50, image=coin_counter_image)
            self.cd_status_image = self.cnvs.create_image(420, 50, image=nocd_image)   
            self.death_text = self.cnvs.create_text(670, 50, text=self.deaths, font=("Impact", 40))
            self.money_text = self.cnvs.create_text(555, 50, text=self.balance, font=("Impact", 40))
            self.settings_button = self.cnvs.create_image(50, 50, image=settings_image)
            self.cnvs.tag_bind(self.settings_button, '<Button-1>', self.setup)
            self.pause_button = self.cnvs.create_image(130, 50, image=pause_image)
            self.cnvs.tag_bind(self.pause_button, '<Button-1>', self.pause)
            self.help_button = self.cnvs.create_image(210, 50, image=help_image)
            self.cnvs.tag_bind(self.help_button, '<Button-1>', self.help)
            self.shop_button = self.cnvs.create_image(290, 50, image=shop_image)
            self.cnvs.tag_bind(self.shop_button, '<Button-1>', shop)           
        def files(self):
            self.open_file = open('resources/settings.yaml', 'r')
            self.settings_lines = self.open_file.readlines()
            self.open_file.close()
            self.balance = int(self.settings_lines[0])
            self.total_deaths = int(self.settings_lines[1])
            self.n_breven = int(self.settings_lines[2])
            self.n_bombs = int(self.settings_lines[3])
            self.n_coins = int(self.settings_lines[4])
            self.meteorit_interval = int(self.settings_lines[5])
            self.open_file = open('resources/colors.txt', 'r')
            self.lines = self.open_file.readlines()
            self.color = self.lines[0]
            self.color = self.color[:-1]
            self.open_file.close()  
        def pause(self, event):
            if self.status == False and self.help_status == False:
                self.status = True
                self.cnvs.delete(self.pause_button)
                self.pause_button = self.cnvs.create_image(130, 50, image=pause_image)
                self.cnvs.tag_bind(self.pause_button, '<Button-1>', self.pause)
                brevna.gen_brevno()
                meteorit.gen_meteorit()
            elif self.status == True:
                self.status = False
                self.cnvs.delete(self.pause_button)
                self.pause_button = game.cnvs.create_image(130, 50, image=continue_image)
                self.cnvs.tag_bind(self.pause_button, '<Button-1>', self.pause)
        def help(self, event):
            if self.help_status == False:
                self.help_status = True
                self.status = False
                self.cnvs2 = Canvas(highlightbackground="black")
                self.cnvs2.place(x=150, y=150, height=600, width=400)
                self.cnvs2.create_image(200, 300, image=rules_image)
                self.close_button = Button(bg="Red", text="Ок", command=lambda:(self.cnvs2.destroy(), self.close_button.destroy(), self.close_help()), font=("Impact", 25))
                self.close_button.place(x=300, y=670, width=100, height=50)
        def close_help(self):
            self.status = True
            self.help_status = False
            brevna.gen_brevno()
            #meteorit.gen_meteorit()
        def save(self): 
            self.settings_lines[2] = str(self.scales[0].get()) + "\n"
            self.settings_lines[3] = str(self.scales[1].get()) + "\n"
            self.settings_lines[4] = str(self.scales[2].get()) + "\n"
            self.settings_lines[5] = str(self.scales[3].get()) + "\n"
            open_file = open('resources/settings.yaml', 'w')
            open_file.writelines(game.settings_lines)
            open_file.close()
            restart()
        def reset_settings(self):
            self.scales[0].set(2)
            self.scales[1].set(2)
            self.scales[2].set(7)
            self.scales[3].set(5)
        def setup(self, event):
            self.status = False
            self.cnvs = Canvas(bg="grey25", highlightbackground="grey25")
            self.cnvs.place(anchor=NW, height=900, width=700)
            self.cnvs.create_text(90, 60, text="Конфигурация игры", fill="red", anchor=W, font=("Impact", 45))
            self.cnvs.create_text(50, 150, text="Количество брёвен:", fill="white", anchor=W, font=("Impact", 30))
            self.cnvs.create_text(50, 300, text="Количество бомб:", fill="white", anchor=W, font=("Impact", 30))
            self.cnvs.create_text(50, 450, text="Количество монет:", fill="white", anchor=W, font=("Impact", 30))
            self.cnvs.create_text(50, 600, text="Интервал метеоритов:", fill="white", anchor=W, font=("Impact", 30))
            self.scales = [Scale(self.cnvs, orient='horizontal', fg="white", highlightbackground="grey25", troughcolor="grey50", showvalue=0, font=('Times New Roman', 15), bg="grey25", from_=0, to=5, tickinterval=1, resolution=1), Scale(self.cnvs, orient='horizontal', fg="white", highlightbackground="grey25", troughcolor="grey50", showvalue=0, font=('Times New Roman', 15), bg="grey25", from_=0, to=10, tickinterval=1, resolution=1), Scale(self.cnvs, orient='horizontal', fg="white", highlightbackground="grey25", troughcolor="grey50", showvalue=0, font=('Times New Roman', 15), bg="grey25", from_=0, to=10, tickinterval=1, resolution=1), Scale(self.cnvs, orient='horizontal', fg="white", highlightbackground="grey25", troughcolor="grey50", showvalue=0, font=('Times New Roman', 15), bg="grey25", from_=0, to=10, tickinterval=1, resolution=1)]
            self.scale = [self.cnvs.create_window(50, 230, window=self.scales[0], height=80, anchor=W, width=500), self.cnvs.create_window(50, 380, window=self.scales[1], height=80, anchor=W, width=500), self.cnvs.create_window(50, 530, window=self.scales[2], height=80, anchor=W, width=500), self.cnvs.create_window(50, 680, window=self.scales[3], height=80, anchor=W, width=500)]
            self.scales[0].set(game.n_breven)
            self.scales[1].set(game.n_bombs)
            self.scales[2].set(game.n_coins)
            self.scales[3].set(game.meteorit_interval)
            self.close_button = Button(bg="black", text="Сохранить", command=lambda:(self.save()), fg="white", font=("Impact", 25))
            self.close_button.place(x=100, y=780, width=200, height=80)          
            self.reset_button = Button(bg="black", text="Сбросить", command=lambda:(self.reset_settings()), fg="white", font=("Impact", 25))
            self.reset_button.place(x=400, y=780, width=200, height=80) 
        def menu(self):
            self.reward = self.n_breven * 3 + self.n_bombs * 2 - self.deaths
            self.total_deaths += self.deaths
            self.cnvs = Canvas(bg='lime')
            self.cnvs.place(anchor=NW, height=900, width=700)
            self.win_text = Label(text="Пройдено!", bg="lime", font=("Impact", 80))
            self.win_text.place(x=100, y=30)
            self.death_stats = Label(text=("Смеретей: " + str(self.deaths)), bg="lime", font=("Impact", 30))
            self.death_stats.place(x=20, y=320)
            self.total_deaths_stats = Label(text=("Всего смертей: " + str(self.total_deaths)), bg="lime", font=("Impact", 30))
            self.total_deaths_stats.place(x=20, y=370)
            self.salary = Label(text=("Заработано всего:  " + str(self.reward)), bg="lime", font=("Impact", 30))
            self.salary.place(x=20, y=470)
            self.balance_stats = Label(text=("Текущий баланс: " + str(balance)), bg="lime", font=("Impact", 30))
            self.balance_stats.place(x=20, y=520)
            self.play_again = Button(text="Играть снова", bg="green", font=("Impact", 30))
            self.play_again.place(x=220, y=700, width=260, height=70)
    game = New_game()      
    class Brevno:
        x = []
        y = []
        status = []
        obj = []
        for i in range(game.n_breven):
            x.append(None)
            y.append(96)
            status.append(False)
            obj.append(None)
        def initXY(self, player: Player, i):
            self.x[i] = (random.randint(player.x-150, player.x+150))
            if self.x[i] < 100:
                self.x[i] = 100
            if self.x[i] > 600:
                self.x[i] = 600
        def gen_brevno(self):
            if game.status == True and game.n_breven != 0:
                if not self.x[0]:
                    self.initXY(player, 0)
                    self.obj[0] = game.cnvs.create_image(self.x[0], self.y[0], image=brevno_image)
                    self.status[0] = True  
                for self.i in range(game.n_breven):
                    if not self.x[self.i] and self.y[0] >= (700 // game.n_breven)*self.i +100:
                        self.initXY(player, self.i)
                        self.obj[self.i] = game.cnvs.create_image(self.x[self.i], self.y[self.i], image=brevno_image)
                        self.status[self.i] = True                
                    if self.status[self.i] != False:
                        if self.y[self.i] < 805:
                            game.cnvs.move(self.obj[self.i], 0, 12)
                            self.y[self.i] += 12
                            if game.status == True:
                                game.cnvs.itemconfig(game.death_text, text=game.deaths)
                                game.cnvs.itemconfig(game.money_text, text=game.balance)
                                if brevna.y[self.i] == player.y and player.x >= brevna.x[self.i]-100 and player.x <= brevna.x[self.i]+100:
                                    if shield.status == True:
                                        shield.status = None
                                        game.cnvs.delete(shield.obj)
                                        brevna.status[self.i] = None
                                    elif shield.status != True and brevna.status[self.i]:
                                        game.deaths += 1
                                        game.cnvs.delete(player.obj)
                                        player.x = 350
                                        player.y = 840   
                                        player.obj = game.cnvs.create_oval(330, 820, 370, 860, fill="black", width=3)        
                        else:
                            game.cnvs.delete(self.obj[self.i])
                            self.obj[self.i] = None
                            self.y[self.i] = 96
                            self.x[self.i] = None
                            self.status[self.i] = False  
                tk.after(50, self.gen_brevno)   
            else:
                tk.after_cancel(self.gen_brevno)
    class Meteorit:
        x = 0
        y = 0
        obj = None
        h = 0
        def gen_meteorit(self):
            if game.status == True and game.meteorit_interval != 0:
                self.x = random.randint(player.x-200, player.x+200) 
                self.x = self.x - self.x % 12
                self.y = random.randint(player.y-200, player.y+200)
                self.y = self.y - self.y % 12
                if self.y < 225:
                    self.y = 225
                if self.y > 675:
                    self.y = 675
                if self.x < 150:
                    self.x = 150
                if self.x > 600:
                    self.x = 600
                self.killtime = random.randint(game.meteorit_interval * 5, game.meteorit_interval * 8)
                print(self.killtime)
                game.cnvs.moveto(self.obj, self.x-125, self.y-125)
                self.meteorit_timer()
            tk.after((game.meteorit_interval*1000), self.gen_meteorit) 
        def meteorit_timer(self):
            if game.status == True and game.meteorit_interval != 0:
                self.h = self.h + 1
                if self.killtime == self.h:
                    if ((self.x - player.x)**2 + (self.y - player.y)**2)**0.5 <= 125:
                        if shield.status == True:
                            shield.status = False
                            game.cnvs.delete(shield.obj)
                        else:
                            game.deaths += 1
                            game.cnvs.delete(player.obj)
                            player.obj = (game.cnvs.create_oval(330, 820, 370, 860, fill="black", width=3))
                            player.x = 350
                            player.y = 840
                    game.cnvs.moveto(self.obj, 5000, 5000)
                    self.h = 0
                    tk.after_cancel(self.meteorit_timer)
                    return
                tk.after(100, self.meteorit_timer)
            else:
                tk.after_cancel(self.meteorit_timer)  
    class Bomba:
        x = []
        y = []
        obj = []
        def __init__(self):
            for self.i in range(game.n_bombs):
                self.a = random.randint(40, 660)
                self.a = self.a - self.a % 12
                self.x.append(self.a)
            for self.i in range(game.n_bombs):
                self.a = random.randint(200, 600)
                self.a = self.a - self.a % 12
                self.y.append(self.a)
            for self.i in range(0, game.n_bombs):
                self.obj.append(game.cnvs.create_image(self.x[self.i], self.y[self.i], image=bomb_image))

    class Coins:
        x = []
        y = []
        obj = []
        def __init__(self):
            for self.i in range(game.n_coins):
                self.a = random.randint(40, 640)
                self.a = self.a - self.a % 12
                self.x.append(self.a)
            for self.i in range(game.n_coins):
                self.a = random.randint(160, 800)
                self.a = self.a - self.a % 12
                self.y.append(self.a)
            for self.i in range(0, game.n_coins):
                self.obj.append(game.cnvs.create_image(self.x[self.i], self.y[self.i], image=coin_image))
    class Move:
        cooldown = None
        time = 120
        def moveto(self, x, y, s, border):
            if game.status == True and not self.cooldown:
                if x == 0:
                    if border == 841 and player.y < border:
                        player.y = player.y + y
                    elif border == 100 and player.y > border:
                        player.y = player.y + y
                    elif border == 100 and player.y > border:
                            game.cnvs.delete("all")
                            game.status = False
                            game.menu()
                    else: 
                        x = 0
                        y = 0
                elif y == 0:
                    if border == 670 and player.x < border:
                        player.x = player.x + x
                    elif border == 30 and player.x > border:
                        player.x = player.x + x
                    else: 
                        x = 0
                        y = 0
                game.cnvs.move(player.obj, x, y)
                if shield.status == True:
                    game.cnvs.move(shield.obj, x, y)
                for i in range(game.n_breven):
                    if brevna.y[i] == player.y and player.x >= brevna.x[i]-100 and player.x <= brevna.x[i]+100:
                        if shield.status == True:
                            shield.status = None
                            game.cnvs.delete(shield.obj)
                            brevna.status[i] = None
                        elif shield.status != True and brevna.status[i]:
                            game.deaths += 1
                            game.cnvs.delete(player.obj)
                            player.x = 350
                            player.y = 840   
                            player.obj = game.cnvs.create_oval(330, 820, 370, 860, fill="black", width=3)   
                for i in range(len(coins.obj)):
                    if coins.x[i]+36 >= player.x and coins.x[i]-36 <= player.x and coins.y[i]+36 >= player.y and coins.y[i]-36 <= player.y:
                        game.cnvs.delete(coins.obj[i])
                        coins.obj.pop(i)
                        coins.x.pop(i)
                        coins.y.pop(i)
                        game.balance += 1
                        break
                for i in range(len(bombs.obj)):
                    if bombs.x[i]+60 >= player.x and bombs.x[i]-60 <= player.x and bombs.y[i]+60 >= player.y and bombs.y[i]-60 <= player.y:
                        if shield.status == True:
                            shield.status = None
                            game.cnvs.delete(shield.obj)
                            game.cnvs.delete(bombs.obj[i])
                            bombs.obj.pop(i)
                            bombs.x.pop(i)
                            bombs.y.pop(i)
                        else:
                            game.cnvs.delete(bombs.obj[i])
                            bombs.obj.pop(i)
                            bombs.x.pop(i)
                            bombs.y.pop(i)
                            game.deaths += 1
                            game.cnvs.delete(player.obj)
                            player.obj = (game.cnvs.create_oval(330, 820, 370, 860, fill="black", width=3))
                            player.x = 350
                            player.y = 840
                        break
                if shield.status == False and shield.x+60 >= player.x and shield.x-60 <= player.x and shield.y+60 >= player.y and shield.y-60 <= player.y:
                    shield.status = True
                    game.cnvs.delete(shield.obj)
                    shield.obj = (game.cnvs.create_oval(player.x+30, player.y+30, player.x-30, player.y-30, outline="red", width=3))
                self.time = s
                if y == -108:
                    game.cnvs.delete(game.cd_status_image)
                    game.cd_status_image = game.cnvs.create_image(420, 50, image=cd_image)
                game.cnvs.itemconfig(game.death_text, text=game.deaths)
                game.cnvs.itemconfig(game.money_text, text=game.balance)
                self.cd()
        def cd(self):
            if game.status == True:
                self.cooldown = 1 if not self.cooldown else self.cooldown + 1 
                if self.cooldown == 2:
                    if self.time == 8000:
                        game.cnvs.delete(game.cd_status_image)
                        game.cd_status_image = game.cnvs.create_image(420, 50, image=nocd_image)
                    self.cooldown = None
                    tk.after_cancel(self.cd)
                    return
                tk.after(self.time, self.cd)
            else:
                tk.after_cancel(self.cd)
    def start():
        global brevna, meteorit, bombs, coins, move
        game.status = True
        brevna = Brevno()
        meteorit = Meteorit()
        meteorit.obj = game.cnvs.create_image(5000, 5000, image=meterorit_image)
        player.obj = game.cnvs.create_oval(330, 820, 370, 860, fill="black", width=3)
        shield.obj = game.cnvs.create_image(shield.x, shield.y, image=shield_image)
        brevna.gen_brevno()
        meteorit.gen_meteorit()
        bombs = Bomba()
        coins = Coins()
        move = [Move(), Move(), Move(), Move(), Move()]
    def key(event):
        if game.status == True:
            if event.keycode == 87 or event.keycode == 38:
                move[0].moveto(0, -12, 120, 100)
            if event.keycode == 68 or event.keycode == 39:
                move[1].moveto(12, 0, 120, 670)
            if event.keycode == 65 or event.keycode == 37:
                move[2].moveto(-12, 0, 120, 30)
            if event.keycode == 83 or event.keycode == 40:
                move[3].moveto(0, 12, 120, 841)
            if event.keycode == 81:
                move[4].moveto(0, -108, 8000, 100)
    def shop(event):
        if game.help_status == False:
            game = False
            cnvs = Canvas()
            cnvs.place(anchor=NW, height=900, width=700)
            cnvs.create_image(600, 60, image=coin_image)
            money_text = Label(text=game.balance, font=("Impact", 25))
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
        def buy_color(color, position):
            open_file = open('resources/colors.txt', 'r')
            lines = open_file.readlines()
            for i in range(len(lines)):
                line = lines[i]
                lines[i] = line[:-1]
            if lines[position+2] == "no":
                if balance >= 10:
                    balance = balance - 10
                    lines[position+2] = "yes"
                    for i in range(2, len(lines)):
                        line = lines[i]
                        lines[i] = line + "\n"
                    lines[0] = color + "\n"
                    lines[1] = str(position) + "\n"
                    lines.append("\n")
                    open_file = open('resources/colors.txt', 'w')
                    open_file.writelines(lines)
                    open_file.close()
                    lines = [(str(balance) + "\n"),  (str(total_deaths) + "\n")]
                    open_file = open('resources/settings.yaml', 'w')
                    open_file.writelines(lines)
                    open_file.close()
                    cnvs.delete("all")
                    for i in range(len(Buttons)):
                        Buttons[i].destroy()
                    shop("a")
                else:
                    if nomoney_status == False:
                        no_money()
                        return
            else:
                open_file = open('resources/colors.txt', 'w')
                for i in range(2, len(lines)):
                    line = lines[i]
                    lines[i] = line + "\n"
                lines[0] = color + "\n"
                lines[1] = str(position) + "\n"
                open_file.writelines(lines)
                open_file.close()
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
    tk.bind('<Key>', key)
    start()
restart()
tk.mainloop()
