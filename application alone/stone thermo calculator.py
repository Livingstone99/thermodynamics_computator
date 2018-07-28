from tkinter import *
from tkinter import ttk

# from tkFileDialog   import askopenfilename
import math

root = Tk()
# master = Tk()
root.title("STONE'S THERMODYNAMICS APP")
root.geometry("1200x600")
#root.resizable(False, False)
root.iconbitmap('Custom-Icon-Design-Flatastic-4-Hot.ico')



# noinspection PyUnresolvedReferences
class window_widgets:
    def __init__(self, master):
        #self.master = master
        #self.MASS = None
        ### The menu widgets
        self.menu1 = Menu(master, tearoff=0)


        root.configure(menu=self.menu1)
        self.sbmenu = Menu(self.menu1)
        self.menu1.add_cascade(label='BASIC THEORY AND LAWS', font='times 20 bold', menu=self.sbmenu)
        self.sbmenu.add_command(label='What is thermodynamics?')
        self.sbmenu.add_command(label='Laws of thermodynamics')
        self.sbmenu.add_command(label='Recommended textbook to deepen your knowledge')
        ## SECOND MENU
        self.menu2 = Menu(self.menu1)
        self.menu1.add_cascade(label='SOLVE PROBLEMS', font=('times', '60'), menu=self.menu2)
        self.menu2.add_command(label="About...", command = self.about_us)
        self.menu2.add_command(label='Real Gas situation')
        self.menu2.add_command(label='Idea Gas situation')
        ##THIRD MENU
        self.menu3 = Menu(self.menu1)
        self.menu1.add_cascade(label='NUMBER OF STATES', font=('times', '60'), menu=self.menu3)
        self.menu3.add_radiobutton(label='state 1')
        self.menu3.add_radiobutton(label='state 2')
        self.menu3.add_radiobutton(label='state 3')

        self.left = Frame(master, width=500, height=720, bg='#ffcd9b')
        self.left.pack(side=LEFT)
        self.right = Frame(master, width=900, height=720, bg='#ffcd9b')
        self.right.pack(side=RIGHT)
        self.left.bind("<Button-1>",self.callback1)
        self.right.bind("<Button-1>",self.callback2)
        self.heading = Label(self.left, text='Compute problems in thermodynamics...',
                             font=('Bradley Hand ITC', '15', 'bold'), fg='#773c00', bd=5, bg='#ffcd9b')
        self.heading.place(x=0, y=0)
        self.instruct = Label(self.left,
                              text='Enter given value, type "?" without the qoutes for a parameter you want to compute',
                              font=('Bradley Hand ITC', '15', 'bold'), fg='#773c00', bd=5, bg='#ffcd9b')
        self.instruct.place(x=0, y=25)
        self.instruct = Label(self.right, text=' for a parameter you want to compute',
                              font=('Bradley Hand ITC', '15', 'bold'), fg='#773c00', bd=5, bg='#ffcd9b')
        self.instruct.place(x=0, y=25)
        self.heading = Label(self.right, text='computation details',
                             font=('Lucida Calligraphy', '15', 'bold', 'underline'), fg='#773c00', bd=5, bg='#ffcd9b')
        self.heading.place(x=30, y=60)
        self.graph_heading = Label(self.right, text='GRAPHS', font=('Lucida Calligraphy', '15', 'bold', 'underline'),
                                   fg='#773c00', bd=5, bg='#ffcd9b')
        self.graph_heading.place(x=600, y=0)

        # labels for widgets
        initial_volume = Label(self.left, text='INITIAL VOLUME', fg='#96216d', bd=5)
        initial_volume.place(x=0, y=60)

        final_volume = Label(self.left, text='FINAL VOLUME', fg='#96216d', bd=5)
        final_volume.place(x=0, y=100)
        initial_temp = Label(self.left, text='INITIAL TEMPERATURE', fg='#96216d', bd=5)
        initial_temp.place(x=0, y=140)
        final_Temp = Label(self.left, text='FINAL TEMPERATURE', fg='#96216d', bd=5)
        final_Temp.place(x=0, y=180)
        initial_pressure = Label(self.left, text='INITIAL PRESSURE', fg='#96216d', bd=5)
        initial_pressure.place(x=0, y=220)

        Final_pressure = Label(self.left, text='FINAL PRESSURE', fg='#96216d', bd=5)
        Final_pressure.place(x=0, y=260)
        WORKDONE = Label(self.left, text='WORKDONE', fg='#96216d', bd=5)
        WORKDONE.place(x=0, y=300)
        POLYTROPIC_INDEX = Label(self.left, text='POLYTROPIC INDEX', fg='#96216d', bd=5)
        POLYTROPIC_INDEX.place(x=0, y=340)
        MASS = Label(self.left, text='MASS', fg='#96216d', bd=5)
        MASS.place(x=0, y=380)
        Internal_energy = Label(self.left, text='INTERNAL ENERGY', fg='#96216d', bd=5)
        Internal_energy.place(x=0, y=420)
        heat_transferred = Label(self.left, text='HEAT TRANSFERRED', fg='#96216d', bd=5)
        heat_transferred.place(x=0, y=460)
        Polytropic_workdone = Label(self.left, text='POLYTROPIC WORK', fg='#96216d', bd=5)
        Polytropic_workdone.place(x=0, y=500)
        units = ("m3", "m3", "k","k","N/m3","N/m3","kj/kg","","kg","kj/kg","kj/kg","kj/kg")
        z = 20
        for i in units:
            z += 40
            Label(self.left, text = i,fg='#96216d', bd=5).place(x = 220, y = z)


        # #Entry widgets

        ## this code permits specific key validation
        vcmd = (self.left.register(self.validate_float), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        # Variable for reset
        self.clear_Widgets_v1= StringVar()
        self.clear_Widgets_v2= StringVar()
        self.clear_Widgets_t1 = StringVar()
        self.clear_Widgets_t2 = StringVar()
        self.clear_Widgets_p1 = StringVar()
        self.clear_Widgets_p2 = StringVar()
        self.clear_Widgets_wd = StringVar()
        self.clear_Widgets_pi = StringVar()
        self.clear_Widgets_m= StringVar()
        self.clear_Widgets_ie = StringVar()
        self.clear_Widgets_ht = StringVar()
        self.clear_Widgets_pw = StringVar()
        self.V1 = Entry(self.left,  textvariable = self.clear_Widgets_v1, width=10)#validate="all", validatecommand=vcmd,
        self.V1.place(x=150, y=60)
        self.V2 = Entry(self.left,textvariable = self.clear_Widgets_v2,width=10) # validate="all", validatecommand=vcmd,
        self.V2.place(x=150, y=100)
        self.T1 = Entry(self.left, textvariable = self.clear_Widgets_t1, width=10)# validate="all", validatecommand=vcmd,
        self.T1.place(x=150, y=140)
        self.T2 = Entry(self.left, textvariable = self.clear_Widgets_t2,width=10)#validate="all", validatecommand=vcmd,
        self.T2.place(x=150, y=180)
        self.P1 = Entry(self.left,textvariable = self.clear_Widgets_p1, width=10)# validate="all", validatecommand=vcmd,
        self.P1.place(x=150, y=220)
        self.P2 = Entry(self.left,textvariable = self.clear_Widgets_p2,width=10)#  validate="all", validatecommand=vcmd,
        self.P2.place(x=150, y=260)

        self.W = Entry(self.left, textvariable = self.clear_Widgets_wd,  width=10)#validate="all", validatecommand=vcmd,
        self.W.place(x=150, y=300)
        self.n = Entry(self.left,textvariable = self.clear_Widgets_pi,validate="all", validatecommand=vcmd , width=10)#,

        self.n.place(x=150, y=340)
        self.mss = Entry(self.left, textvariable = self.clear_Widgets_m,validate="all", validatecommand=vcmd,width=10)# ,
        self.mss.place(x=150, y=380)
        self.it = Entry(self.left,textvariable = self.clear_Widgets_ie,width=10)#  validate="all", validatecommand=vcmd,
        self.it.place(x=150, y=420)
        self.Q = Entry(self.left,textvariable = self.clear_Widgets_ht, width=10)# validate="all", validatecommand=vcmd,
        self.Q.place(x=150, y=460)
        self.PW = Entry(self.left,textvariable = self.clear_Widgets_pw,width=10)#  validate="all", validatecommand=vcmd,
        self.PW.place(x=150, y=500)
        self.V1.focus()


        # Radiobuttons

        self.v = StringVar()
        self.v.set("polytropic process")

        self.isotherm = Radiobutton(root, text='Isothermal process', variable=1, value=1, font='times 13', fg='#744862',
                                    bg='#ffcd9b')
        self.isotherm.place(x=280, y=60)
        self.polytropics = Radiobutton(root, text='Polytropic process', variable=1, value=2, font='times 13',
                                       fg='#744862', bg='#ffcd9b')
        self.polytropics.place(x=280, y=100)

        self.insulated = Radiobutton(root, text='Perfectly insulated', variable=3, value=3, font='times 13',
                                     fg='#744862', bg='#ffcd9b')
        self.insulated.place(x=280, y=140)
        self.rigid = Radiobutton(root, text='Rigid container', variable=6, value=4, font='times 13', fg='#744862',
                                 bg='#ffcd9b')
        self.rigid.place(x=280, y=180)
        self.isochoric = Radiobutton(root, text='Isochoric process', variable=6, value=5, font='times 13', fg='#744862',
                                     bg='#ffcd9b')
        self.isochoric.place(x=280, y=220)
        self.isobaric = Radiobutton(root, text='Isobaric', variable=6, value=6, font='times 13', fg='#744862',
                                    bg='#ffcd9b')
        self.isobaric.place(x=280, y=260)
        self.isentropic = Radiobutton(root, text='isentropic process', variable=1, value=7, font='times 13',
                                      fg='#744862', bg='#ffcd9b')
        self.isentropic.place(x=280, y=300)

        ##Buttons
        self.compute = Button(self.left, text='compute', cursor='target', command=self.loop, font='Georgia 12 bold',fg='#764741')
        self.compute.place(x=200, y=540)
        self.Resetbutt = Button(self.left, text='Reset', cursor='target', command=self.clearData, font='Georgia 12 bold',
                                fg='#764741')
        self.Resetbutt.place(x=300, y=540)
        self.compute.bind("<Return>" ,self.loop)


    def validate_float(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        # action=1 -> insert
        if (action == '1'):
            if text in '0123456789.-+':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True
     ## The call back functions helps me to know the exact location where i am /
    ##in the window app. this helps for better placement of widgets
    def callback1(self,event):
        print ("clicked at left frame", event.x, event.y)
    def callback2(self,event):
         print ("clicked at right frame", event.x, event.y)
    def clearData(self):
        #self.clear_Widgets.set("")
        self.clear_Widgets_v1.set("")
        self.clear_Widgets_v2.set("")
        self.clear_Widgets_t1.set("")
        self.clear_Widgets_t2.set("")
        self.clear_Widgets_p1.set("")
        self.clear_Widgets_p2.set("")
        self.clear_Widgets_wd.set("")
        self.clear_Widgets_pi.set("")
        self.clear_Widgets_m.set("")
        self.clear_Widgets_ie.set("")
        self.clear_Widgets_ht.set("")
        self.clear_Widgets_pw.set("")

    def MASS(self):
        p11 = float(self.P1.get())
        v11 = float(self.V1.get())
        t11 = float(self.T1.get())

        R = 0.287
        M = p11 * v11 / (t11 * R)
        m = DoubleVar()
        m.set(M)
        # ["text"] = ("The sum is:", M)
        Label(root, text="%s" % (M) + 'kg').place(x= 170, y = 300)

    def Initial_Volume(self):
        R = 0.287
        mss1 = float(self.mss.get())
        p11 = float(self.P1.get())
        t11 = float(self.T1.get())
        V = (mss1 * t11 * R / p11)
        v = DoubleVar()
        v.set(V)
        Label(root, text="%s" % (V) + 'm3').place(x= 170, y = 300)

    def about_us(self):
        text_file = open("C:\\Users\stone's\Desktop\\thrmo text.txt")
        text1 = text_file.read()
        Label(text="%s" % (text1), font=('Chiller', '18'), fg='#edc9e3', bg='#408080').place(x= 30, y = 100)

    def Polytropic_Workdone(self):
        T11 = float(self.T1.get())
        T22 = float(self.T2.get())
        p11 = float(self.P1.get())
        v11 = float(self.V1.get())
        nn = float(self.n.get())
        p22 = float(self.P2.get())
        v22 = float(self.V2.get())
        Poly_w = ((p22 * v22 ** nn) - (p11 * v11 ** nn)) / (1 - nn)
        v = DoubleVar()
        v.set(Poly_w)
        Label(root, text="Polytropic workdone for the system is : "+"%s" % (Poly_w) + 'Kj/kg').place(x= 170, y = 300)

    def temperature_polytropic(self):
        p11 = float(self.P1.get())
        v11 = float(self.V1.get())
        nn = float(self.n.get())
        p22 = float(self.P2.get())
        v22 = float(self.V2.get())
        if self.T2.get() == "?":
            T11 = float(self.T1.get())
            TT2 = T11 * (v11 / v22) ** (nn - 1)
            v = DoubleVar()
            v.set(TT2)
            Label(root, text="%s" % (TT2) + 'K').place(x= 170, y = 300)
            return
        elif self.T1.get() == "?":
            T22 = float(self.T2.get())
            TT1 = T22 * (v22 / v11) ** (nn - 1)
            # TT1 = T22 * (v22 / v11) ** (nn - 1)
            v = DoubleVar()
            v.set(TT1)
            Label(root, text="%s" % (TT1) + 'K').place(x= 170, y = 300)
            return

    def HeatTransfer_InternalEnergy_workdone(self):

        if self.HT.get() == "?":
            # HeatTrans = float(HT.get())
            InterEnerg = float(self.IT.get())
            WorkD = float(self.W.get())
            HeatT = InterEnerg + WorkD
            v = DoubleVar()
            v.set(HeatT)
            Label(root, text="Quantity of heat transferred = " + "%s" % (HeatT) + 'Kj/kg').place(x= 170, y = 300)

        elif W.get() == "?":
            InterEnerg = float(IT.get())
            HeatTrans = float(HT.get())
            # WorkD = foat(W.get())
            workD = HeatTrans + InterEnerg
            v = DoubleVar()
            v.set(workD)
            Label(root, text='Workdone by system = ' + "%s" % (workD) + 'Kj/kg').place(x= 170, y = 300)
        elif IT.get() == "?":
            # InterEnerg = float(IT.get())
            HeatTrans = float(HT.get())
            WorkD = float(W.get())
            InterEneg = HeatTrans - WorkD
            v = DoubleVar()
            v.set(InterEneg)
            Label(root, text='Internal Energy of the system = '"%s" % (InterEneg) + 'Kj/kg').place(x= 170, y = 300)
    def IntEntry(self):
        if inp.idgits():
            return true
        elif inp is "":
            return True
        else:
            return False
    def workdoneconstPressure(self):
        P11 = self.P1.get()
        V11 = self.V1.get()
        V22 = self.V2.get()
        work_CP = P11*(V11 - V22)
        v = DoubleVar()
        v.set(work_CP)
        Label(root, text='Workdone at constant pressure = '"%s" % (work_CP) + 'Kj/kg').place(x=170, y=300)
    def AllWorkdone(self):

         if  self.P2.get()=="?":
             print(workdoneconstPressure())
         else:
            print(HeatTransfer_InternalEnergy_workdone())

    def loop(self):
        if self.mss.get() == "?":
            print(self.MASS())
        elif self.V1.get() == "?":
            print(self.Initial_Volume())
        elif self.PW.get() == "?":
            print(self.Polytropic_Workdone())

        elif self.HT.get() == "?" or self.IT.get() == "?":
            print(self.HeatTransfer_InternalEnergy_workdone())
        elif  self.W.get() == "?":
            print(AllWorkdone())

        else:
            print("Enter a valid parameter")

        while 1:
                try:
                        Mass() and Initial_Volume()
                        break
                except ValueError:
                        print('Enter a valid number, click compute!')

    '''def Mass(self):
        p11 = float(self.P1.get())
        v11 = float(self.V1.get())
        t11 = float(self.T1.get())

        R = 0.287
        M = p11 * v11 / (t11 * R)
        m = DoubleVar()
        m.set(M)
        # ["text"] = ("The sum is:", M)
        self.LL = Label(root, text="%s" % (M) + 'kg')
        self.LL.place(x=170, y=380)

    def Initial_Volume(self):
            R = 0.287
            mss1 = float(mss.get())
            p11 = float(P1.get())
            t11 = float(T1.get())
            V = (mss1*t11*R/p11)
            v = DoubleVar()
            v.set(V) 
            Label(root, text = "%s" %(V)+'m3').place(x = 170, y = 60)
    def loop(self):
            if mss.get() =="?":
                    print(Mass())

            elif T22.get() =="?":
                    print(Polytropic_Workdone())'''


## ALGORITHMS AND COMPUTATION LOOPS
# x = window_widgets(master = None)
# Entry widgets




'''def Mass(massWidget):
    #global my_global
    #my_global = [V1,T1,P1]
    #global x
    p11 = float(massWidget.P1.get())
    v11 = float(massWidget.V1.get())
    t11 = float(massWidget.T1.get())

    R = 0.287
    M = p11 * v11/(t11*R)
    m = DoubleVar()
    m.set(M)
    #["text"] = ("The sum is:", M)
    Label(root,  text = "%s" %(M)+'kg' ).place(x = 170, y = 380)
def Initial_Volume():
    R = 0.287
    mss1 = float(mss.get())
    p11 = float(P1.get())
    t11 = float(T1.get())
    V = (mss1*t11*R/p11)
    v = DoubleVar()
    v.set(V) 
    Label(root, text = "%s" %(V)+'m3').place(x = 170, y = 60)
def about_us():
    text_file = open("C:\\Users\stone's\Desktop\\thrmo text.txt")
    text1 = text_file.read()
    Label(text = "%s" %(text1),font = ('Chiller', '18'), fg = '#edc9e3', bg = '#408080').grid(row = 0, column = 0, rowspan = 4,columnspan = 5)


def Polytropic_Workdone():
        T11 = float(T1.get())
        T22 = float(T2.get())
        p11 = float(P1.get())
        v11 = float(V1.get())
        nn = float(n.get())
        p22 = float(P2.get())
        v22 = float(V2.get())
        Poly_w = ((p22*v22**nn)-(p11*v11**nn))/(1 - nn)
        v = DoubleVar()
        v.set(Poly_w) 
        Label(root, text = "%s" %(Poly_w)+'Kj/kg').place(x= 170, y = 300)


def temperature_polytropic(Polytropic_Workdone):

        if T22 == "?":
                TT2 = T11*(v11/v22)**(nn-1)
        elif T11 =="":
                T11 = T22*(v22/v11)**(nn-1)

        v = DoubleVar()
        v.set(TT2)
        Label(root, text = "%s" %(TT2)+'K').grid(row = 6, column = 1)
#class_instance = window_widgets("")
#class_instance.Mass()'''
root.option_add('*font', ('Constantia', 10))
b = window_widgets(root)
root.mainloop()
