from tkinter import *
import tkinter.messagebox
win = Tk()
win.geometry('600x480+450+150')
win.configure(background='#1C2951')
win.title("BMI")
win.resizable(width=False,height=False)

# ⁡⁢⁣⁣advice⁡ #
Uweigth = "Less weight than normal is not good. If you are very tall\nbut weigh too little There may be a risk of not getting\nenough nutrients or not getting enough energy.\nthe body is easily fatigued. eating enough And exercise\nto strengthen muscles can help increase your BMI\nto the normal range."
Normal  = "Suitable weight for Thai people is a BMI between 18.5-24\nis considered normal. far away from obesity And with\nthe lowest risk of developing various diseases, you\nshould try to keep your BMI at this level for as long as\npossible. And should have a health check every year."
Obese   = "Obese to some extent Even though they are\nnot considered very obese, they are still at risk of\ndeveloping diseasesthat come with obesity.\nboth diabetes and high blood pressure You should\nadjust your eating habits, exercise,\nand check your health."
Exobese = "Quite dangerous There is a risk of serious diseases\nassociated with obesity if the BMI is at this level.\nwill have to adjust eating behavior and should\nstart exercising And if the number is higher than 40\nit indicates more obesity. should go for a health check\nand consult a doctor."
# ⁡⁢⁣⁣advice⁡ #

# ⁡⁣⁢⁣Photo⁡ #
Venus = PhotoImage(file="venus.png")
Mercury = PhotoImage(file="mercury.png")
Earth = PhotoImage(file="Earth.png")
Moon = PhotoImage(file="moon.png")
Mars = PhotoImage(file="mars.png")
Jupiter = PhotoImage(file="jupiter.png")
Saturn = PhotoImage(file="saturn.png")
Uranus = PhotoImage(file="uranus.png")
Neptune = PhotoImage(file="neptune.png")
Sun = PhotoImage(file="sun.png")
# ⁡⁣⁢⁣Photo⁡ #

# ⁡⁢⁢⁢icon⁡ #
win.iconphoto(False,Earth)
# ⁡⁢⁢⁢icon⁡ #

# Page1
def put_WH():
    c2 = Canvas(c1,height=500,width=600,bg='#1C2951')
    Label(c2,text=('Your weight (kg)'),font=('arial',20,'bold'),fg='#50C878',bg='#1C2951',width=17).place(relx=0.255,rely=0.175)
    weight = IntVar()
    weight.set(1)
    Entry(c2,textvariable=weight,font=('arial',20),width=20).place(relx=0.25,rely=0.275)
    Label(c2,text=('Your height (cm)'),font=('arial',20,'bold'),fg='#50C878',bg='#1C2951',width=17).place(relx=0.255,rely=0.4)
    height = IntVar()
    height.set(1)
    Entry(c2,textvariable=height,font=('arial',20),width=20).place(relx=0.25,rely=0.5)

    # Page2 
    def get_WH():
        c3 = Canvas(c2,height=500,width=600,bg="#1c2951")

        # ⁡⁣⁢⁣Select The Planet⁡ #
        name = StringVar()
        name.set("Earth")
        # ⁡⁢⁣⁢Planet⁡ #        
        def Turn_right():
            Name = name.get()
            if Name == "Earth":
                name.set("Moon")
                Name = name.get()
                Label(c3,image=Moon,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Moon":
                name.set("Mars")
                Name = name.get()
                Label(c3,image=Mars,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Mars":
                name.set("Jupiter")
                Name = name.get()
                Label(c3,image=Jupiter,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Jupiter":
                name.set("Saturn")
                Name = name.get()
                Label(c3,image=Saturn,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Saturn":
                name.set("Uranus")
                Name = name.get()
                Label(c3,image=Uranus,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Uranus":
                name.set("Neptune")
                Name = name.get()
                Label(c3,image=Neptune,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Neptune":
                name.set("Sun")
                Name = name.get()
                Label(c3,image=Sun,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Sun":
                name.set("Venus")
                Name = name.get()
                Label(c3,image=Venus,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Venus":
                name.set("Mercury")
                Name = name.get()
                Label(c3,image=Mercury,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Mercury":
                name.set("Earth")
                Name = name.get()
                Label(c3,image=Earth,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            Label(c3,text=f'Your planet : {Name}',bg='#1C2951',fg='white',font=('arial',30,'bold'),width=23).place(relx=0.035,rely=0.075)

        def Turn_left():
            Name = name.get()
            if Name == "Moon":
                name.set("Earth")
                Name = name.get()
                Label(c3,image=Earth,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Mars":
                name.set("Moon")
                Name = name.get()
                Label(c3,image=Moon,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Jupiter":
                name.set("Mars")
                Name = name.get()
                Label(c3,image=Mars,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Saturn":
                name.set("Jupiter")
                Name = name.get()
                Label(c3,image=Jupiter,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Uranus":
                name.set("Saturn")
                Name = name.get()
                Label(c3,image=Saturn,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Neptune":
                name.set("Uranus")
                Name = name.get()
                Label(c3,image=Uranus,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Sun":
                name.set("Neptune")
                Name = name.get()
                Label(c3,image=Neptune,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Venus":
                name.set("Sun")
                Name = name.get()
                Label(c3,image=Sun,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Mercury":
                name.set("Venus")
                Name = name.get()
                Label(c3,image=Venus,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            elif Name == "Earth":
                name.set("Mercury")
                Name = name.get()
                Label(c3,image=Mercury,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
            Label(c3,text=f'Your planet : {Name}',bg='#1C2951',fg='white',font=('arial',30,'bold'),width=23).place(relx=0.035,rely=0.075)
        # ⁡⁢⁣⁢Planet⁡ #

        Name = name.get()
        Label(c3,image=Earth,width=250,height=250,bg="#1C2951").place(relx=0.28,rely=0.225)
        # ⁡⁣⁢⁣Select The Planet⁡ #

        # ⁡⁢⁣⁣BMI⁡ #
        def CalBMI(g,Name):
            w = weight.get()
            h = height.get()
            Calwin = Canvas(c3,height=500,width=600,bg="#1c2951")
            
            hm = h/100
            w*=g
            
            Label(Calwin,text=(f'your weight in {Name} is {w:.2f} kg'),font=('arial',20,'bold'),bg='#1c2951',fg='white',width=31).place(relx=0.055,rely=0.1)
            
            BMI = w/(hm*hm)

            if Name == "Sun":
                Label(Calwin,text=f'Dead',font=('arial',100,'bold'),bg='#1c2951',fg='#111111').place(relx=0.225,rely=0.275)
            else:
                if BMI < 18.5 :
                    crit = 'underweight'
                    Label(Calwin,text=f'Adviessce in {Name}',font=('arial',16,'bold'),bg='#1c2951',fg='#79CDCD',width=41).place(relx=0.05,rely=0.375)
                    Label(Calwin,text=Uweigth,font=('arial',16),bg='#1c2951',fg='#79CDCD',width=44).place(relx=0.055,rely=0.45)
                elif BMI >= 18.5 and BMI < 25  :
                    crit = 'normal'
                    Label(Calwin,text=f'Advice in {Name}',font=('arial',16,'bold'),bg='#1c2951',fg='#4CAF50',width=41).place(relx=0.05,rely=0.375)
                    Label(Calwin,text=Normal,font=('arial',16),bg='#1c2951',fg='#4CAF50',width=44).place(relx=0.055,rely=0.45)
                elif BMI >= 25 and BMI < 30 :
                    crit = 'obese'
                    Label(Calwin,text=f'Advice in {Name}',font=('arial',16,'bold'),bg='#1c2951',fg='#FFC300',width=41).place(relx=0.05,rely=0.375)
                    Label(Calwin,text=Obese,font=('arial',16),bg='#1c2951',fg='#FFC300',width=44).place(relx=0.055,rely=0.45)
                elif BMI >= 30 :
                    crit = 'extremly obese'
                    Label(Calwin,text=f'Advice in {Name}',font=('arial',16,'bold'),bg='#1c2951',fg='#FF5733',width=41).place(relx=0.05,rely=0.375)
                    Label(Calwin,text=Exobese,font=('arial',16),bg='#1c2951',fg='#FF5733',width=44).place(relx=0.055,rely=0.45)
                
                Label(Calwin,text=(f'your BMI in {Name} is {BMI:.2f}'),font=('arial',20,'bold'),bg='#1c2951',fg='white',width=31).place(relx=0.055,rely=0.175)
                Label(Calwin,text=(f'it falls with in the {crit} range '),font=('arial',20,'bold'),bg='#1c2951',fg='white',width=31).place(relx=0.055,rely=0.25)
              
            def back():
                Calwin.destroy()
            Button(Calwin,text='Back',width=12,font=('arial',12,'bold'),command=back).place(relx=0.39,rely=0.8)

            Calwin.place(relx=0,rely=0)
        # ----------------------------------------------------------------------------
        def Next():
            Name = name.get()
            if Name == "Earth":
                CalBMI(1,Name)
            elif Name == "Moon":
                CalBMI(0.16,Name)
            elif Name == "Mars":
                CalBMI(0.38,Name)
            elif Name == "Jupiter":
                CalBMI(2.5,Name)
            elif Name == "Saturn":
                CalBMI(1.05,Name)
            elif Name == "Uranus":
                CalBMI(0.92,Name)
            elif Name == "Neptune":
                CalBMI(1.12,Name)
            elif Name == "Sun":
                CalBMI(0,Name)
            elif Name == "Mercury":
                CalBMI(0.38,Name)
            elif Name == "Venus":
                CalBMI(0.91,Name)
        # ⁡⁢⁣⁣BMI⁡ #

        Label(c3,text=f'Your planet : Earth',bg='#1C2951',fg='white',font=('arial',30,'bold'),width=23).place(relx=0.035,rely=0.075)

        # ⁡⁢⁣⁣BUTTON⁡ #⁡⁡⁡
        Button(c3,text='>',font=('arial',18),width=2,height=3,bg='#E1BEE7',command=Turn_right).place(relx=0.75,rely=0.375)

        Button(c3,text='<',font=('arial',18),width=2,height=3,bg='#E1BEE7',command=Turn_left).place(relx=0.175,rely=0.375)
        # ⁡⁢⁣⁣BUTTON⁡ #

        def Bput():
            c3.destroy()

        Button(c3,text='CONTINUE',width=12,font=('arial',12,'bold'),command=Next).place(relx=0.39,rely=0.775)
        Button(c3,text='Back',width=12,font=('arial',12,'bold'),command=Bput).place(relx=0.39,rely=0.85)
        
        c3.place(relx=0,rely=0)
    # Page2

    def BKH():
        c2.destroy()
    Button(c2,text="Back",bd=0,width=13,fg='#FFF176',bg='#1C2951',font=('atial',15),activebackground="#FFF176",command=BKH).place(relx=0.25,rely=0.65)
    Button(c2,text='Next',bd=0,width=13,fg='#FFF176',bg='#1C2951',font=('arial',15),activebackground="#FFF176",command=get_WH).place(relx=0.5,rely=0.65)

    c2.place(relx=0,rely=0)
# Page1

c1 = Canvas(win,height=500,width=600,bg='#1C2951')
p1 = PhotoImage(file='BG.png')
c1.create_image(0, 0, image=p1, anchor=NW)

Button(c1,text='>>START<<',font=('arial',16,'bold'),fg='#FFF176',bg='#1C2951',command=put_WH,borderwidth=0).place(relx=0.385, rely=0.63)

def about():
    tkinter.messagebox.showinfo("credit",'Prject for T.Pailin\n team members have Phai(coder), Mum, Polar, Punn')
def exit():
    info = tkinter.messagebox.askquestion('exit ','you want to exit?')
    if info == 'yes' or info == 'ใช่':
        win.destroy()
    else :
        pass 

Button(c1,text='credit',font=('arial',16,'bold'),width=10,fg='#FFF176',bg='#1C2951',command=about,borderwidth=0).place(relx=0.385, rely=0.73)
Button(c1,text='exit',font=('arial',16,'bold'),width=10,fg='#FFF176',bg='#1C2951',command=exit,borderwidth=0).place(relx=0.385, rely=0.83)
c1.pack()
win.mainloop()