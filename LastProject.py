import customtkinter as ctk
import tkinter as tk
from tkinter import Canvas, Label
import math
from PIL import Image, ImageTk
import cv2

class Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Projectile Motion Simulation")
        self.geometry("1280x720")
        self.config(bg="#000000")
        self.resizable(width=False, height=False)
        self._apply_appearance_mode("dark")
        # สร้างองค์ประกอบ
        self.create_widgets()
        self.place_widgets()
        self.input_value = InputValue(self)
        self.button = Button(self)
        self.calculator = Calculator(self)
        self.simulation = Simulation(self)
        self.video_label = ctk.CTkLabel(self,text="")
        self.video_capture = cv2.VideoCapture("img\G.mp4")
        self.video_label.place(x=0,y=0)
        self.update_frame()
        # เรียกใช้งานการอัพเดทวิดีโอ

    def create_widgets(self):
        # สร้างองค์ประกอบต่างๆ
        canvas_width = 730
        canvas_height = 400
        canvas1_height = 400
        canvas2_height = 267.5
        self.x1 = 0
        self.y1 = 0
        self.k1 = 0
        self.x2 = 0
        self.y2 = 0
        self.k2 = 0
        self.x3 = 0
        self.y3 = 0
        self.k3 = 0
        y1 = 350
        y2 = 260
        radius = 20
        self.canvas1 = Canvas(self, width=400, height=400, bg="black", highlightthickness=0)
        self.canvas1.create_arc(0, 0,radius*2, radius*2, start=90, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas1.create_arc(400-radius*2, 0, 400, radius*2, start=0, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas1.create_arc(0, 400-radius*2, radius*2, 400, start=180, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas1.create_arc(400-radius*2, 400-radius*2, 400, 400, start=270, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas1.create_rectangle(radius, 0, 400-radius, 400, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas1.create_rectangle(0, radius, 400, 400-radius, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas2 = Canvas(self, width=300, height=267.5, bg="black", highlightthickness=0)
        self.canvas2.create_arc(0, 0, radius*2, radius*2, start=90, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas2.create_arc(300-radius*2, 0, 300, radius*2, start=0, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas2.create_arc(0, 267.5-radius*2, radius*2, 267.5, start=180, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas2.create_arc(300-radius*2, 267.5-radius*2, 300, 267.5, start=270, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas2.create_rectangle(radius, 0, 300-radius, 267.5, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas2.create_rectangle(0, radius, 300, 267.5-radius, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas = Canvas(self, width=730, height=400, bg="black", highlightthickness=0)
        self.canvas.create_arc(0, 0, radius*2, radius*2, start=90, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas.create_arc(730-radius*2, 0, 730, radius*2, start=0, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas.create_arc(0, 400-radius*2, radius*2, 400, start=180, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas.create_arc(730-radius*2, 400-radius*2, 730, 400, start=270, extent=90, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas.create_rectangle(radius, 0, 730-radius, 400, fill='#2E2E2E', outline='#2E2E2E')
        self.canvas.create_rectangle(0, radius, 730, 400-radius, fill='#2E2E2E', outline='#2E2E2E')
        self.frame = ctk.CTkFrame(self,width=100,height=400,bg_color="black",fg_color="#2E2E2E",corner_radius=15)
        self.frame1 = ctk.CTkFrame(self,width=512.5,height=267.5,bg_color="black",fg_color="#2E2E2E",corner_radius=15)
        self.frame3 = ctk.CTkFrame(self,width=417.5,height=267.5,bg_color="black",fg_color="#2E2E2E",corner_radius=15)
        self.cl0 = ctk.CTkFrame(self,width=20,height=20,bg_color="#2E2E2E",fg_color="#C568DF",border_color="black",border_width=5,corner_radius=20)
        self.cl1 = ctk.CTkFrame(self,width=20,height=20,bg_color="#2E2E2E",fg_color="#018D4A",border_color="black",border_width=5,corner_radius=20)
        self.cl2 = ctk.CTkFrame(self,width=20,height=20,bg_color="#2E2E2E",fg_color="#BD2828",border_color="black",border_width=5,corner_radius=20)
        self.cl3 = ctk.CTkFrame(self,width=20,height=20,bg_color="#2E2E2E",fg_color="#E6CA58",border_color="black",border_width=5,corner_radius=20)
        self.fc1 = ctk.CTkFrame(self,width=20,height=20,bg_color="#2E2E2E",fg_color="#BD2828",border_color="black",border_width=5,corner_radius=20)
        self.fc2 = ctk.CTkFrame(self,width=20,height=20,bg_color="#2E2E2E",fg_color="Grey",border_color="black",border_width=5,corner_radius=20)#BD2828
        self.fc3 = ctk.CTkFrame(self,width=20,height=20,bg_color="#2E2E2E",fg_color="Grey",border_color="black",border_width=5,corner_radius=20)
        self.dis1 = ctk.CTkFrame(self,width=100,height=50,bg_color="#2E2E2E",fg_color="black",corner_radius=15)
        self.dis2 = ctk.CTkFrame(self,width=100,height=50,bg_color="#2E2E2E",fg_color="black",corner_radius=15)
        self.dis3 = ctk.CTkFrame(self,width=100,height=50,bg_color="#2E2E2E",fg_color="black",corner_radius=15)
        self.cal1 = ctk.CTkFrame(self,width=150,height=50,bg_color="#2E2E2E",fg_color="black",corner_radius=15)
        self.cal2 = ctk.CTkFrame(self,width=150,height=50,bg_color="#2E2E2E",fg_color="black",corner_radius=15)
        self.dis1cl = ctk.CTkFrame(self,width=15,height=40,bg_color="black",fg_color="#018D4A",corner_radius=15)
        self.dis2cl = ctk.CTkFrame(self,width=15,height=40,bg_color="black",fg_color="#BD2828",corner_radius=15)
        self.dis3cl = ctk.CTkFrame(self,width=15,height=40,bg_color="black",fg_color="#E6CA58",corner_radius=15)
        self.scale = ctk.CTkProgressBar(self,progress_color="#61FF00",fg_color="red",bg_color="#2E2E2E",border_color="black",border_width=5,width=300,height=15)
        self.hmch = self.canvas.create_line(40, 300, 720, 300,width=2,fill="orange",state='hidden')
        self.htb = self.canvas.create_line(40, 214.28571, 720, 214.28571,width=2,fill="orange",state='hidden')
        self.htg = self.canvas.create_line(40,  108.577196, 720,  108.577196,width=2,fill="orange",state='hidden')
        for i in range(0,15):
            y = 75 + (14-i) * (canvas_height - 100) / 14
            y2 -= 30
            self.canvas.create_line(40, y, 720, y,width=1,fill="Grey")
            self.canvas.create_text(25, y, text=str(10 * i),fill="white")
            print(y)
            if(i<=5):
                self.canvas2.create_line(60, y2, 250, y2,width=1,fill="Grey")
                self.canvas2.create_text(45, y2, text=str(10 * (5-i)),fill="white")
                self.canvas1.create_line(25, y1, 375, y1,width=1,fill="Grey")
                if(i<4):
                    self.canvas1.create_text(15, y1, text=str(10 * i),fill="white")
                    y1 -= 70 #7 pixel:1 cm
                else:
                    if(i==5):
                        self.canvas1.create_text(15, y1, text=str(45),fill="white")
                    else:
                        self.canvas1.create_text(15, y1, text=str(10*i),fill="white")
                    y1 -= 35
        self.hw = self.canvas.create_line(40,  246.42857, 720,  246.42857,width=2,fill="orange",state='hidden')
        self.canvas.create_line(50, 50, 50, canvas_height - 25, arrow=tk.FIRST,width=5,fill="white")
        triangle = self.canvas.create_polygon((85,375), (175,375), (175,300),fill="#398CC4") #แกนx ratio 2.25 pixel : 1 cm แกน y ratio 21.428571 pixel: 10 cm
        wall = self.canvas.create_rectangle(395, 246.42857, 405, 375, width=1, fill="#398CC4")
        target = self.canvas.create_rectangle(625, 108.577196, 630, 214.28571, width=1, fill="red")
        table = self.canvas.create_rectangle(625, 214.28571, 720, 375, width=1, fill="#398CC4")
        resolu = self.canvas.create_rectangle(290, 24,365, 51, width=1, fill="black")
        u_ball = self.canvas.create_rectangle(420, 24,495, 51, width=1, fill="black")
        v_ball = self.canvas.create_rectangle(570, 24, 645, 51, width=1, fill="black")
        self.maxtg = self.canvas.create_line(622.5,  0, 632.5,  0,width=3,fill="yellow",state='hidden')
        self.mintg = self.canvas.create_line(622.5, 0, 632.5,  0,width=3,fill="yellow",state='hidden')
        self.id_lx = self.canvas.create_line(50, canvas_height - 25, canvas_width , canvas_height - 25, arrow=tk.LAST,width=5,fill="white")
        x = -50
        x1 = 25
        x2 = 70
        for i in range(0, 6):
            x+=225
            self.canvas.create_line(x, canvas_height - 25, x, canvas_height - 15,width=5,fill="white")
            self.canvas.create_text(x, canvas_height - 7 , text=str(i),fill="white")
            self.canvas1.create_line(x1, canvas1_height - 40, x1, canvas1_height - 30,width=1,fill="Grey")
            self.canvas1.create_text(x1, canvas1_height - 20 , text=str(i*10),fill="white")
            self.canvas2.create_line(x2, 70, x2,240,width=1,fill="Grey")
            self.canvas2.create_text(x2, 55 , text=str(i*10),fill="white")
            x2+=30
            x1+=70
        target = self.canvas1.create_polygon((25,350),(400/2,46.89111),(375,350),fill="grey")
        self.pstgy = self.canvas1.create_line(25,  0, 375,  0,width=2,fill="orange",state='hidden')
        self.pstgx = self.canvas1.create_line(0, 50, 0,  360,width=2,fill="orange",state='hidden')
        self.liney = self.canvas2.create_line(70, 60, 70, canvas2_height - 25, arrow=tk.FIRST,width=5,fill="white")
        self.linex = self.canvas2.create_line(50, 80, 250 , 80, arrow=tk.LAST,width=5,fill="white")
        ctk.CTkLabel(self,text="Function",font=("Trebuchet MS", 18, "bold"),bg_color="#2E2E2E", fg_color="#2E2E2E").place(x=25, y=40)
        ctk.CTkLabel(self,text="Target",font=("Trebuchet MS", 18, "bold"),bg_color="#2E2E2E", fg_color="#2E2E2E").place(x=155, y=40)
        ctk.CTkLabel(self,text="Simulation",font=("Trebuchet MS", 18, "bold"),bg_color="white", fg_color="#2E2E2E").place(x=567.5, y=40)
        ctk.CTkLabel(self,text="Setup Target",bg_color="#000000",font=("Trebuchet MS", 20, "bold"), fg_color="#2E2E2E").place(x=40, y=450)
        ctk.CTkLabel(self,text="Position",bg_color="#000000",font=("Trebuchet MS", 20, "bold"), fg_color="#2E2E2E").place(x=567.5, y=450)
        ctk.CTkLabel(self,text="Dashboard ",bg_color="#000000",font=("Trebuchet MS", 20, "bold"), fg_color="#2E2E2E").place(x=880, y=450)
        ctk.CTkLabel(self,text="Resolution",bg_color="#2E2E2E",font=("Trebuchet MS", 15, "bold"), fg_color="#2E2E2E").place(x=1020, y=469)
        ctk.CTkLabel(self,text="1",bg_color="#2E2E2E",font=("Trebuchet MS", 15, "bold"), fg_color="#2E2E2E").place(x=380, y=445 )
        ctk.CTkLabel(self,text="2",bg_color="#2E2E2E",font=("Trebuchet MS", 15, "bold"), fg_color="#2E2E2E").place(x=430, y=445 )
        ctk.CTkLabel(self,text="3",bg_color="#2E2E2E",font=("Trebuchet MS", 15, "bold"), fg_color="#2E2E2E").place(x=480, y=445 )
        ctk.CTkLabel(self,text="x",bg_color="#000000",font=("Trebuchet MS", 15, "bold"), fg_color="#2E2E2E").place(x=1130, y=469)
        ctk.CTkLabel(self,text="x",bg_color="#000000",font=("Trebuchet MS", 15, "bold"), fg_color="#2E2E2E").place(x=790, y=480)
        ctk.CTkLabel(self,text="y",bg_color="#000000",font=("Trebuchet MS", 15, "bold"), fg_color="#2E2E2E").place(x=1175, y=469)
        ctk.CTkLabel(self,text="time",bg_color="#000000",font=("Trebuchet MS", 15, "bold"), fg_color="#2E2E2E").place(x=1225, y=469)
        ctk.CTkLabel(self,text="Calculator",bg_color="#000000",font=("Trebuchet MS", 20, "bold"), fg_color="#2E2E2E").place(x=880, y=575)
        ctk.CTkLabel(self,text="X-AXIS",bg_color="#000000",font=("Trebuchet MS", 20, "bold"), fg_color="#2E2E2E").place(x=40, y=505)
        ctk.CTkLabel(self,text="Y-AXIS",bg_color="#000000",font=("Trebuchet MS", 20, "bold"), fg_color="#2E2E2E").place(x=40, y=580)
        ctk.CTkLabel(self,text="K-Spring",bg_color="#000000",font=("Trebuchet MS", 20, "bold"), fg_color="#2E2E2E").place(x=290, y=505)
        ctk.CTkLabel(self,text="Cm",bg_color="#000000",font=("Trebuchet MS", 20, "bold"), fg_color="#2E2E2E").place(x=240, y=505)
        ctk.CTkLabel(self,text="Cm",bg_color="#000000",font=("Trebuchet MS", 20, "bold"), fg_color="#2E2E2E").place(x=240, y=580)
        ctk.CTkLabel(self,text="u-ball",bg_color="#2E2E2E",font=("Trebuchet MS", 16, "bold"), fg_color="#2E2E2E").place(x=910, y=42.5)
        ctk.CTkLabel(self,text="Velocity",bg_color="#2E2E2E",font=("Trebuchet MS", 16, "bold"), fg_color="#2E2E2E").place(x=1040, y=42.5)
        ctk.CTkLabel(self,text="Compression Distance",bg_color="#2E2E2E",font=("Trebuchet MS", 16, "bold"), fg_color="#2E2E2E").place(x=890, y=605)
        ctk.CTkLabel(self,text="Position x",bg_color="#2E2E2E",font=("Trebuchet MS", 16, "bold"), fg_color="#2E2E2E").place(x=1105, y=605)
        ctk.CTkLabel(self,text="Cm",bg_color="#000000",font=("Trebuchet MS", 18, "bold"), fg_color="black").place(x=1000.75, y=645)
        ctk.CTkLabel(self,text="Cm",bg_color="#000000",font=("Trebuchet MS", 18, "bold"), fg_color="black").place(x=1170.75, y=645)
        ctk.CTkLabel(self,text="m",bg_color="#000000",font=("Trebuchet MS", 18, "bold"), fg_color="black").place(x=975, y=510)
        ctk.CTkLabel(self,text="m",bg_color="#000000",font=("Trebuchet MS", 18, "bold"), fg_color="black").place(x=1087, y=510)
        ctk.CTkLabel(self,text="s",bg_color="#000000",font=("Trebuchet MS", 18, "bold"), fg_color="black").place(x=1215, y=510)
        ctk.CTkLabel(self,text="Resolution",bg_color="#2E2E2E",font=("Trebuchet MS", 15, "bold"), fg_color="#2E2E2E").place(x=750, y=44)
        ctk.CTkLabel(self,text="x",bg_color="#000000",font=("Trebuchet MS", 14, "bold"), fg_color="black").place(x=850, y=44 )
        ctk.CTkLabel(self,text="m/s",bg_color="#000000",font=("Trebuchet MS", 14, "bold"), fg_color="black").place(x=1005, y=44 )
        ctk.CTkLabel(self,text="m/s",bg_color="#000000",font=("Trebuchet MS", 14, "bold"), fg_color="black").place(x=1155, y=44 )
        self.value_label = ctk.CTkLabel(self.master, text=0, font=("Trebuchet MS", 18, "bold"), bg_color="black", fg_color="black")
        self.position_value = ctk.CTkLabel(self.master, text=0, font=("Trebuchet MS", 18, "bold"), bg_color="black", fg_color="black")
        self.ress = ctk.CTkLabel(self.master, text=1, font=("Trebuchet MS", 14, "bold"), bg_color="black", fg_color="black")
        self.u_ball = ctk.CTkLabel(self.master, text=0, font=("Trebuchet MS", 14, "bold"), bg_color="black", fg_color="black")
        self.velo = ctk.CTkLabel(self.master, text=0, font=("Trebuchet MS", 14, "bold"), bg_color="black", fg_color="black")
        self.hmt =  ctk.CTkLabel(self.canvas,text="",height=15,font=("Trebuchet MS", 12, "bold"),text_color='orange',bg_color="#2E2E2E", fg_color="#2E2E2E")
        self.htbt =  ctk.CTkLabel(self.canvas,text="",height=15,font=("Trebuchet MS", 12, "bold"),text_color='orange',bg_color="#2E2E2E", fg_color="#2E2E2E")
        self.htgt =  ctk.CTkLabel(self.canvas,text="",height=15,font=("Trebuchet MS", 12, "bold"),text_color='orange',bg_color="#2E2E2E", fg_color="#2E2E2E")
        self.hwt =  ctk.CTkLabel(self.canvas,text="",height=15,font=("Trebuchet MS", 12, "bold"),text_color='orange',bg_color="#2E2E2E", fg_color="#2E2E2E")
        self.mint =  ctk.CTkLabel(self.canvas,text="",height=15,font=("Trebuchet MS", 12, "bold"),text_color='orange',bg_color="#2E2E2E", fg_color="#2E2E2E")
        self.maxt =  ctk.CTkLabel(self.canvas,text="",height=15,font=("Trebuchet MS", 12, "bold"),text_color='orange',bg_color="#2E2E2E", fg_color="#2E2E2E")
        self.xt =  ctk.CTkLabel(self.canvas1,text="",height=15,font=("Trebuchet MS", 12, "bold"),text_color='orange',bg_color="#2E2E2E", fg_color="#2E2E2E")
        self.yt =  ctk.CTkLabel(self.canvas1,text="",height=15,font=("Trebuchet MS", 12, "bold"),text_color='orange',bg_color="#2E2E2E", fg_color="#2E2E2E")
        self.x = ctk.CTkLabel(self.master, text=0, font=("Trebuchet MS", 18, "bold"), bg_color="black", fg_color="black")
        self.y = ctk.CTkLabel(self.master, text=0, font=("Trebuchet MS", 18, "bold"), bg_color="black", fg_color="black")
        self.sl = ctk.CTkLabel(self.master, text=0, font=("Trebuchet MS", 18, "bold"), bg_color="black", fg_color="black")
        self.scale.set(0)   
        self.video_label = Label(self, bg="black")

    def place_widgets(self):
        # ตำแหน่งขององค์ประกอบ
        self.hmt.place(x=80, y=280)
        self.htbt.place(x=80, y=194.28571)
        self.htgt.place(x=80, y=90.35714)
        self.hwt.place(x=80, y=226.42857)
        self.mint.place(x=635,y=0)
        self.maxt.place(x=635,y=0)
        self.xt.place(x=0,y=375)
        self.yt.place(x=20,y=0)
        self.canvas1.place(x=125, y=20)
        self.canvas2.place(x=537.5, y=432.5)
        self.canvas.place(x=537.5, y=20)
        self.frame.place(x=12.5, y=20 )
        self.frame1.place(x=12.5, y=432.5 )
        self.frame3.place(x=850, y=432.5 )
        self.fc1.place(x=375, y=475 )
        self.fc2.place(x=425, y=475 )
        self.fc3.place(x=475, y=475 )
        self.cl0.place(x=995, y=475 )
        self.cl1.place(x=1100, y=475 )
        self.cl2.place(x=1150, y=475 )
        self.cl3.place(x=1200, y=475 )
        self.dis1.place(x=896.75, y=500 )
        self.dis2.place(x=1008.75, y=500 )
        self.dis3.place(x=1128.75, y=500 )
        self.dis1cl.place(x=900.75, y=505 )
        self.dis2cl.place(x=1012.75, y=505 )
        self.dis3cl.place(x=1132.75, y=505 )
        self.cal1.place(x=896.75, y=635 )
        self.cal2.place(x=1066.75, y=635 )
        self.scale.place(x=908.75, y=560)
        self.value_label.place(x=950.75, y=645 )
        self.position_value.place(x=1118.75, y=645)
        self.sl.place(x=1160, y=510 )
        self.x.place(x=918, y=510 )
        self.y.place(x=1030, y=510 )
        self.ress.place(x=860, y=44 )
        self.u_ball.place(x=965, y=44 )
        self.velo.place(x=1115, y=44 )
        self.video_label.pack()

    def update_frame(self):
        # อัพเดทวิดีโอจากไฟล์
        ret, frame = self.video_capture.read()
        if ret:
            frame = cv2.resize(frame, (1280, 720))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            image_tk = ImageTk.PhotoImage(image)
            self.video_label.configure(image=image_tk)
            self.video_label.image = image_tk
            self.after(3, self.update_frame)
        else:
            self.video_capture.release()
            self.after(2000, self.video_label.destroy())
class Button:
    def __init__(self, master):
        self.master = master
        self.master.f = 0
        self.master.hid = ctk.IntVar(value=0)
        self.master.ch = ctk.IntVar(value=0)
        self.master.state1 = 1
        self.master.state2 = 0
        self.master.state3 = 0
        self.mrr = self.process_image(r"img\mrr.png", 80, 65)
        self.rtll = self.process_image(r"img\rtl.png", 80, 65)
        self.rtrr = self.process_image(r"img\rtr.png", 80, 65)
        self.t1 = self.process_image(r"img\1.png", 80, 65)
        self.t2 = self.process_image(r"img\2.png", 80, 65)
        self.t3 = self.process_image(r"img\3.png", 80, 65)
        self.st = self.process_image(r"img\start.png", 115, 45)
        self.rs = self.process_image(r"img\reset.png", 115, 45)
        self.rsim = self.process_image(r"img\resim.png", 115, 45)
        self.opl = ctk.CTkSwitch(master,text='Line',font=("Trebuchet MS", 16, "bold"),onvalue=1,variable=self.master.hid,offvalue=0,bg_color='#2E2E2E',width=10,command=lambda:self.master.simulation.draw_line())
        self.choi = ctk.CTkCheckBox(master,text='All',font=("Trebuchet MS", 20, "bold"),border_width=5,  border_color='black',variable=self.master.ch,checkbox_width=30,onvalue=1,offvalue=0, checkbox_height=30,width=40,height=40,checkmark_color='#E6CA58',bg_color="#2E2E2E",hover_color='#E6CA58',fg_color='#E6CA58')
        self.master.res =  ctk.CTkSlider(master,progress_color="#0C1FCB",button_color='#C568DF',bg_color="#2E2E2E",fg_color="red",border_color="black",from_=0,to=2,width=150,height=15,corner_radius=2,command=self.event_slide)
        self.resim = tk.Button(master, image=self.rsim, font=("Trebuchet MS", 10, "bold"), width=110, height=45, bg="#2E2E2E", fg="black", relief="flat", compound="center", border=0, highlightthickness=0, command=self.rrsim)
        self.start = tk.Button(master, image=self.st, font=("Trebuchet MS", 10, "bold"), width=110, height=45, bg="#2E2E2E", fg="black", relief="flat", compound="center", border=0, highlightthickness=0, command=self.master.input_value.check_point)
        self.reset_def = tk.Button(master, image=self.rs, font=("Trebuchet MS", 10, "bold"), width=110, height=45, bg="#2E2E2E", fg="black", relief="flat", compound="center", border=0, highlightthickness=0, command=lambda: self.master.simulation.reset_to_default())
        self.mirr = tk.Button(master, image=self.mrr, font=("Trebuchet MS", 10, "bold"), width=60, height=45, bg="#2E2E2E", fg="#398CC4", relief="flat", compound="center", border=0, highlightthickness=0, command=self.mrr1)
        self.rtl = tk.Button(master, image=self.rtll, font=("Trebuchet MS", 10, "bold"), width=60, height=45, bg="#2E2E2E", fg="#398CC4", relief="flat", compound="center", border=0, highlightthickness=0, command=self.rtl1)
        self.rtr = tk.Button(master, image=self.rtrr, font=("Trebuchet MS", 10, "bold"), width=60, height=45, bg="#2E2E2E", fg="#398CC4", relief="flat", compound="center", border=0, highlightthickness=0, command=self.rtr1)
        self.tg1 = tk.Button(master, image=self.t1, font=("Trebuchet MS", 10, "bold"), width=60, height=45, bg="#2E2E2E", fg="#398CC4", relief="flat", compound="center", border=0, highlightthickness=0, command=self.sttg1)
        self.tg2 = tk.Button(master, image=self.t2, font=("Trebuchet MS", 10, "bold"), width=60, height=45, bg="#2E2E2E", fg="#398CC4", relief="flat", compound="center", border=0, highlightthickness=0, command=self.sttg2)
        self.tg3 = tk.Button(master, image=self.t3, font=("Trebuchet MS", 10, "bold"), width=60, height=45, bg="#2E2E2E", fg="#398CC4", relief="flat", compound="center", border=0, highlightthickness=0, command=self.sttg3)
        self.master.res.set(0)
        # Place buttons
        self.opl.place(x=1190,y=45)
        self.choi.place(x=460, y=637.5)
        self.master.res.place(x=1100,y=450)
        self.start.place(x=50, y=635)
        self.resim.place(x=195, y=635)
        self.reset_def.place(x=340, y=635)
        self.mirr.place(x=32.5, y=70)
        self.rtl.place(x=32.5, y=130)
        self.rtr.place(x=32.5, y=190)
        self.tg1.place(x=32.5, y=250)
        self.tg2.place(x=32.5, y=310)
        self.tg3.place(x=32.5, y=370)

    def process_image(self, path, x, y):
        image_path = path
        pil_image = Image.open(image_path)
        img_resized = pil_image.resize((x, y), Image.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(img_resized)
        pil_image.close()  # Close the image file
        return self.tk_image
    def event_slide(self,value):
        self.master.f = round(float(value),2)
        print(self.master.f)
        self.master.ress.configure(text=round(value+1,2))
    def rrsim(self):
        self.master.simulation.change_state()
        if self.master.state1 == 1:
            self.master.calculator.calculate(self.master.x1, self.master.y1, self.master.k1)
        elif self.master.state2 == 1:
            self.master.calculator.calculate(self.master.x2, self.master.y2, self.master.k2)
        elif self.master.state3 == 1:
            self.master.calculator.calculate(self.master.x3, self.master.y3, self.master.k3)

    def sttg1(self):
        self.master.state1 = 1
        self.master.state2 = 0
        self.master.state3 = 0
        self.master.fc1.configure(fg_color="#BD2828")
        self.master.fc2.configure(fg_color="Grey")
        self.master.fc3.configure(fg_color="Grey")
        self.master.simulation.reset_line()
        self.master.simulation.change_state()
        self.master.simulation.reset_focus()
        self.master.calculator.calculate(self.master.x1, self.master.y1, self.master.k1)
        self.master.simulation.draw_line()


    def sttg2(self):
        self.master.state2 = 1
        self.master.state1 = 0
        self.master.state3 = 0
        self.master.fc2.configure(fg_color="#BD2828")
        self.master.fc3.configure(fg_color="Grey")
        self.master.fc1.configure(fg_color="Grey")
        self.master.simulation.reset_line()
        self.master.simulation.change_state()
        self.master.simulation.reset_focus()
        self.master.calculator.calculate(self.master.x2, self.master.y2, self.master.k2)
        self.master.simulation.draw_line()


    def sttg3(self):
        self.master.state3 = 1
        self.master.state1 = 0
        self.master.state2 = 0
        self.master.fc3.configure(fg_color="#BD2828")
        self.master.fc2.configure(fg_color="Grey")
        self.master.fc1.configure(fg_color="Grey")
        self.master.simulation.reset_line()
        self.master.simulation.change_state()
        self.master.simulation.reset_focus()
        self.master.calculator.calculate(self.master.x3, self.master.y3, self.master.k3)
        self.master.simulation.draw_line()

    def mrr1(self):
        self.master.simulation.reset_alltg()
        self.master.simulation.reset_line()
        self.master.simulation.break_sim()
        self.master.simulation.reset_focus()
        x1 = self.master.x1
        x2 = self.master.x2
        x3 = self.master.x3
        if (x1 > 0):
            x_mir1 = (350/7) - x1
            self.master.x1 = x_mir1
            self.master.simulation.draw_circle(x_mir1, (self.master.y1))
            self.master.canvas1.delete(self.master.circle_id)
        if (x2 > 0):
            x_mir2 = (350/7) - x2
            self.master.x2 = x_mir2
            self.master.simulation.draw_circle(x_mir2, (self.master.y2))
            self.master.canvas1.delete(self.master.circle_id)
        if (x3 > 0):
            x_mir3 = (350/7) - x3
            self.master.x3 = x_mir3
            self.master.simulation.draw_circle(x_mir3, (self.master.y3))
            self.master.canvas1.delete(self.master.circle_id)
    def rtl1(self):
        self.master.simulation.reset_alltg()
        self.master.simulation.reset_line()
        print(self.master.x1 ,self.master.y1 )
        self.master.simulation.break_sim()
        self.master.simulation.reset_focus()
        x1 = self.master.x1
        x2 = self.master.x2
        x3 = self.master.x3
        y1 = self.master.y1
        y2 = self.master.y2
        y3 = self.master.y3
        if (x1 > 0 and y1 > 0):
            print(self.master.x1 ,self.master.y1 )
            x_rtl1 = x1 * math.cos(math.radians(120)) - y1 * math.sin(math.radians(120))
            y_rtl1 = x1 * math.sin(math.radians(120)) + y1 * math.cos(math.radians(120))
            self.master.x1 = 50+x_rtl1
            self.master.y1 = y_rtl1
            print(round(self.master.x1,2) ,round(self.master.y1,2) )
            self.master.simulation.draw_circle(self.master.x1, (self.master.y1))
            self.master.canvas1.delete(self.master.circle_id)
        if (x2 > 0 and y2 > 0):
            print(self.master.x2 ,self.master.y2 )
            x_rtl2 = x2 * math.cos(math.radians(120)) - y2 * math.sin(math.radians(120))
            y_rtl2 = x2 * math.sin(math.radians(120)) + y2 * math.cos(math.radians(120))
            self.master.x2 = 50+x_rtl2
            self.master.y2 = y_rtl2
            print(round(self.master.x2,2) ,round(self.master.y2,2) )
            self.master.simulation.draw_circle(self.master.x2, (self.master.y2))
            self.master.canvas1.delete(self.master.circle_id)
        if (x3 > 0 and y3 > 0):
            print(self.master.x3 ,self.master.y3 )
            x_rtl3 = x3 * math.cos(math.radians(120)) - y3 * math.sin(math.radians(120))
            y_rtl3 = x3 * math.sin(math.radians(120)) + y3 * math.cos(math.radians(120))
            self.master.x3 = 50+x_rtl3
            self.master.y3 = y_rtl3
            print(round(self.master.x3,2) ,round(self.master.y3,2) )
            self.master.simulation.draw_circle(self.master.x3, (self.master.y3))
            self.master.canvas1.delete(self.master.circle_id)
    def rtr1(self):
        self.master.simulation.reset_alltg()
        self.master.simulation.reset_line()
        print(self.master.x1 ,self.master.y1 )
        self.master.simulation.break_sim()
        self.master.simulation.reset_focus()
        x1 = self.master.x1
        x2 = self.master.x2
        x3 = self.master.x3
        y1 = self.master.y1
        y2 = self.master.y2
        y3 = self.master.y3
        if (x1 > 0 and y1 > 0):
            print(self.master.x1 ,self.master.y1 )
            x_rtl1 = (x1-50) * math.cos(math.radians(-120)) - y1 * math.sin(math.radians(-120))
            y_rtl1 = x1 * math.sin(math.radians(-120)) + y1 * math.cos(math.radians(-120))
            self.master.x1 = x_rtl1
            self.master.y1 = 43.3 + y_rtl1
            print(round(self.master.x1,5) ,round(self.master.y1,5) )
            self.master.simulation.draw_circle(self.master.x1, (self.master.y1))
            self.master.canvas1.delete(self.master.circle_id)
        if (x2 > 0 and y2 > 0):
            print(self.master.x2 ,self.master.y2 )
            x_rtl2 = (x2-50) * math.cos(math.radians(-120)) - y2 * math.sin(math.radians(-120))
            y_rtl2 = x2 * math.sin(math.radians(-120)) + y2 * math.cos(math.radians(-120))
            self.master.x2 = x_rtl2
            self.master.y2 = 43.3 + y_rtl2
            print(round(self.master.x2,5) ,round(self.master.y2,5) )
            self.master.simulation.draw_circle(self.master.x2, (self.master.y2))
            self.master.canvas1.delete(self.master.circle_id)
        if (x3 > 0 and y3 > 0):
            print(self.master.x3 ,self.master.y3 )
            x_rtl3 = (x3-50) * math.cos(math.radians(-120)) - y3 * math.sin(math.radians(-120))
            y_rtl3 = x3 * math.sin(math.radians(-120)) + y3 * math.cos(math.radians(-120))
            self.master.x3 = x_rtl3
            self.master.y3 = 43.3 + y_rtl3
            print(round(self.master.x3,5) ,round(self.master.y3,5) )
            self.master.simulation.draw_circle(self.master.x3, (self.master.y3))
            self.master.canvas1.delete(self.master.circle_id)
class InputValue:
    def __init__(self, master):
        self.master = master
        self.master.x_entry = ctk.CTkEntry(self.master, width=100, font=("Trebuchet MS", 15), bg_color="#2E2E2E")
        self.master.x_entry.place(x=125, y=505)
        self.master.y_entry = ctk.CTkEntry(self.master, width=100, font=("Trebuchet MS", 15), bg_color="#2E2E2E")
        self.master.y_entry.place(x=125, y=580)
        self.master.k_entry = ctk.CTkEntry(self.master, width=100, font=("Trebuchet MS", 15), bg_color="#2E2E2E")
        self.master.k_entry.place(x=400, y=505)
        self.err_entry = ctk.CTkEntry(self.master, width=100, font=("Trebuchet MS", 15), bg_color="#2E2E2E")
        # self.err_entry.place(x=400, y=580)
        self.master.x_entry.focus_set()
        self.master.bind("<Up>", lambda event: self.master.x_entry.focus_set())
        self.master.bind("<Down>", lambda event: self.master.y_entry.focus_set())

    def check_point(self):
        x_input = self.master.x_entry.get()
        y_input = self.master.y_entry.get()
        k_input = self.master.k_entry.get()

        x_input = float(x_input)
        y_input = float(y_input)
        k_input = float(k_input)
        self.master.simulation.reset_target()
        if self.master.state1 == 1:
            self.master.x1 = x_input
            self.master.y1 = y_input
            self.master.k1 = k_input
            print(f"x1 : {self.master.x1} y1 : {self.master.y1} k1 : {self.master.k1}")
            self.master.fc1.configure(fg_color="#BD2828")
            self.master.fc2.configure(fg_color="Grey")
            self.master.fc3.configure(fg_color="Grey")
            self.master.calculator.calculate(self.master.x1, self.master.y1, self.master.k1)
        elif self.master.state2 == 1:
            self.master.x2 = x_input
            self.master.y2 = y_input
            self.master.k2 = k_input
            print(f"x2 : {self.master.x2} y2 : {self.master.y2} k2 : {self.master.k2}")
            self.master.fc2.configure(fg_color="#BD2828")
            self.master.fc1.configure(fg_color="Grey")
            self.master.fc3.configure(fg_color="Grey")
            self.master.calculator.calculate(self.master.x2, self.master.y2, self.master.k2)
        elif self.master.state3 == 1:
            self.master.x3 = x_input
            self.master.y3 = y_input
            self.master.k3 = k_input
            print(f"x3 : {self.master.x3} y3 : {self.master.y3} k3 : {self.master.k3}")
            self.master.fc3.configure(fg_color="#BD2828")
            self.master.fc2.configure(fg_color="Grey")
            self.master.fc1.configure(fg_color="Grey")
            self.master.calculator.calculate(self.master.x3, self.master.y3, self.master.k3)
    def reset_entries(self):
        self.master.x_entry.delete(0, tk.END)
        self.master.y_entry.delete(0, tk.END)
        self.master.k_entry.delete(0, tk.END)
class Calculator:
    def __init__(self, master):
        self.master = master

    def calculate(self, x, y,k):
        self.master.x_entry.configure(placeholder_text=round(x,2))
        self.master.y_entry.configure(placeholder_text=round(y,2))
        self.master.k_entry.configure(placeholder_text=round(k,2))
        if (k!=0):
            e = 0.45
            base_machine = 12
            self.master.angle = 45
            self.master.gforce_value = 9.812
            self.master.v_ball = math.sqrt((4 * self.master.gforce_value) / (1.595 - float(y+2) / 100))
            self.master.time = 2 / ((self.master.v_ball) * (1.414 / 2))
            u_want  = 0.214/0.19 * self.master.v_ball
            c = -(0.095-(0.0106542*(1-e**2)))*u_want**2
            self.master.position = x-base_machine
            distance1 = (-(1.31804596*1.414-math.sqrt(1.73706-2*(k)*c))/k*100) -4.9 +2.3 #-preload+realdistance
            self.master.value_label.configure(text=round(distance1, 2))
            self.master.u_ball.configure(text=round(self.master.v_ball, 3))
            self.master.position_value.configure(text=round((float(x)-base_machine),2))
            self.master.simulation.draw_circle(x, y)
            self.master.simulation.draw_position()
            self.master.simulation.update_ball()
            self.master.simulation.draw_line()
            self.master.input_value.reset_entries()
        else:
            print("Error variable is not defind")
class Simulation:
    def __init__(self, master):
        self.master = master
        self.master.matg = 0
        self.master.mitg = 0
        self.master.pgy = 0
        self.master.pgx = 0
        self.master.timesim = 0
        self.master.circle_ids = []
        self.master.target1_ids = []
        self.master.target2_ids = []
        self.master.target3_ids = []
        self.master.position_ids = []
        self.ball_ids = []
        self.after_id = None
    def draw_circle(self, x, y):
        #แกนx ratio 2.25 pixel : 1 cm แกน y ratio 21.428571 pixel: 10 cm
        self.reset_focus()
        self.reset_sim()  
        self.master.timesim = 0
        radius = 6.85 * 7
        radius1 = 2 * 7
        self.master.realy = y
        self.master.realx = x
        self.master.realmatg = (y+77.5)+6.85
        self.master.realmitg = (y+77.5)-6.85
        self.master.matg = 375-((self.master.realmatg)/10 *21.428571)
        self.master.mitg = 375-((self.master.realmitg)/10 *21.428571)
        x = x * 7 + 25
        y = 350 - y * 7
        self.master.pgy = y
        self.master.pgx = x
        self.circle_id1 = self.master.canvas1.create_oval(x - radius, y - radius, x + radius, y + radius,
                                                           outline="#2E2E2E", fill="#2E2E2E")
        self.master.circle_id = self.master.canvas1.create_oval(x - radius1, y - radius1, x + radius1, y + radius1,
                                                                outline="red", fill="red")
        self.master.circle_ids.extend([self.master.circle_id])
        if self.master.x1 == self.master.realx and self.master.y1 == self.master.realy:
            self.master.target1_ids.extend([self.circle_id1])
            print(f"tg1 : {self.master.target1_ids}")
        elif self.master.x2 == self.master.realx and self.master.y2 == self.master.realy :
            self.master.target2_ids.extend([self.circle_id1])
            print(f"tg2 : {self.master.target2_ids}")
        elif self.master.x3 == self.master.realx and self.master.y3 == self.master.realy :
            self.master.target3_ids.extend([self.circle_id1])
            print(f"tg3 : {self.master.target3_ids}")
    def draw_position(self):
        if len(self.master.position_ids) > 0:
            self.reset_position()
        self.robot = self.master.canvas2.create_rectangle(self.master.position * 3 + 70, 80,
                                                          (self.master.position * 3 + 70) + 24 * 3,
                                                          40 * 3 + 80, width=1, fill="#398CC4")
        self.master.canvas2.lower(self.robot, self.master.linex)
        self.master.canvas2.lower(self.robot, self.master.liney)
        self.master.position_ids.extend([self.robot])
    def draw_line(self):
        if self.master.hid.get() ==1:
            self.master.canvas.itemconfigure(self.master.hmch,state = '')
            self.master.canvas.itemconfigure(self.master.htb,state = '')
            self.master.canvas.itemconfigure(self.master.htg,state = '')
            self.master.canvas.itemconfigure(self.master.hw,state = '')
            if self.master.pgy >0 or self.master.pgx >0 :
                self.master.canvas.itemconfigure(self.master.maxtg,state = '')
                self.master.canvas.itemconfigure(self.master.mintg,state = '')
                self.master.maxt.configure(text=round(self.master.realmatg,1))
                self.master.mint.configure(text=round(self.master.realmitg,1))
                self.master.xt.configure(text=round(self.master.realx,1))
                self.master.yt.configure(text=round(self.master.realy,1))
                self.master.maxt.place(y=self.master.matg-15 )
                self.master.mint.place(y=self.master.mitg-15 )
                self.master.xt.place(x=self.master.pgx)
                self.master.yt.place(y=self.master.pgy+5)
                self.master.canvas.coords(self.master.maxtg,622.5, self.master.matg, 632.5,  self.master.matg)
                self.master.canvas.coords(self.master.mintg,622.5, self.master.mitg, 632.5,  self.master.mitg)
                self.master.canvas1.itemconfigure(self.master.pstgy,state = '')
                self.master.canvas1.itemconfigure(self.master.pstgx,state = '')
                self.master.canvas1.coords(self.master.pstgy,25,self.master.pgy,375 ,self.master.pgy)
                self.master.canvas1.coords(self.master.pstgx,self.master.pgx,50,self.master.pgx,360)
            self.master.hmt.configure(text = '35')
            self.master.htbt.configure(text = '75.5')
            self.master.htgt.configure(text = '124')
            self.master.hwt.configure(text = '60')
        else:
            self.master.canvas.itemconfigure(self.master.maxtg,state = 'hidden')
            self.master.canvas.itemconfigure(self.master.mintg,state = 'hidden')
            self.master.canvas.itemconfigure(self.master.hmch,state = 'hidden')
            self.master.canvas.itemconfigure(self.master.htb,state = 'hidden')
            self.master.canvas.itemconfigure(self.master.htg,state = 'hidden')
            self.master.canvas.itemconfigure( self.master.hw,state = 'hidden')
            self.master.canvas1.itemconfigure(self.master.pstgy,state = 'hidden')
            self.master.canvas1.itemconfigure(self.master.pstgx,state = 'hidden')
            self.master.maxt.configure(text='')
            self.master.mint.configure(text='')
            self.master.xt.configure(text='')
            self.master.yt.configure(text='')
            self.master.hmt.configure(text = '')
            self.master.htbt.configure(text = '')
            self.master.htgt.configure(text = '')
            self.master.hwt.configure(text = '')
    def update_ball(self):
        x = 175 + (self.master.v_ball * 225) * math.cos(math.radians(self.master.angle)) * self.master.timesim
        y = 103.571429 + (self.master.v_ball * 2.1428571 * 100) * math.sin(
            math.radians(self.master.angle)) * self.master.timesim - 0.5 * (
                    9.81 * 2.1428571 * 100) * self.master.timesim ** 2
        vy = self.master.v_ball * 1.414 / 2 - self.master.gforce_value * self.master.timesim
        vx = self.master.v_ball * 1.414 / 2
        vvelo = math.sqrt((vx ** 2) + (vy ** 2))
        ball_radius = 5
        self.master.velo.configure(text=round(vvelo, 3))
        self.master.x.configure(text=f"{round((x - 175) / 225, 3)}")
        self.master.y.configure(text=f"{round(((y - 28.5714305)) / (2.1428571 * 100), 3)}")
        self.master.sl.configure(text=f"{round(self.master.timesim, 3)}")
        self.master.scale.set(self.master.timesim / self.master.time)
        self.ball = self.master.canvas.create_oval(x, 400 - y, x + ball_radius * 2, 400 - y + ball_radius * 2,
                                                   fill="White")
        self.ball_ids.append(self.ball)
        self.master.canvas.coords(self.ball, x, 400 - y, x + ball_radius * 2, 400 - y + ball_radius * 2)
        # print(float(3-self.master.f)/100)
        self.master.timesim +=  float(3-self.master.f)/100
        if y >= 0 and x <= 625:
            self.after_id = self.master.after(100, self.update_ball)
    def reset_position(self):
        for position_id in self.master.position_ids:
            self.master.canvas2.delete(position_id)
        self.master.position_ids = []
    def reset_alltg(self):
        for circle_id in self.master.target1_ids:
            self.master.canvas1.delete(circle_id)
        self.master.target1_ids = []
        for circle_id in self.master.target2_ids:
            self.master.canvas1.delete(circle_id)
        self.master.target2_ids = []
        for circle_id in self.master.target3_ids:
            self.master.canvas1.delete(circle_id)
        self.master.target3_ids = []  
    def reset_target(self):
        if self.master.state1 == 1:
            print("delete state 1")
            for circle_id in self.master.target1_ids:
                self.master.canvas1.delete(circle_id)
            self.master.target1_ids = []
        elif self.master.state2 == 1:
            print("delete state 2")
            for circle_id in self.master.target2_ids:
                self.master.canvas1.delete(circle_id)
            self.master.target2_ids = []
        elif self.master.state3 == 1:
            print("delete state 3")
            for circle_id in self.master.target3_ids:
                self.master.canvas1.delete(circle_id)
            self.master.target3_ids = []
    def reset_focus(self):
        for circle_id in self.master.circle_ids:
            self.master.canvas1.delete(circle_id)
        self.master.circle_ids = []
    def reset_sim(self):
        for ball_id in self.ball_ids:
            self.master.canvas.delete(ball_id)
        self.ball_ids = []
    def reset_dasboard(self):
        self.master.scale.set(0)
        self.master.value_label.configure(text=round(0, 3))
        self.master.position_value.configure(text=round((0), 2))
        self.master.u_ball.configure(text=f"{0}")
        self.master.velo.configure(text=f"{0}")
        self.master.x.configure(text=f"{0}")
        self.master.y.configure(text=f"{0}")
        self.master.sl.configure(text=f"{0}")
    def reset_entry(self):
        self.master.x_entry.configure(placeholder_text='')
        self.master.y_entry.configure(placeholder_text='')
        self.master.k_entry.configure(placeholder_text='')
        self.master.input_value.reset_entries()
    def reset_variable(self):
        self.master.timesim = 0
        self.master.matg = 0
        self.master.mitg = 0
        self.master.pgy = 0
        self.master.pgx = 0
        if self.master.ch.get() == 0:
            if self.master.state1 == 1:
                self.master.x1 = 0
                self.master.y1 = 0
                self.master.k1 = 0
            elif self.master.state2 == 1:
                self.master.x2 = 0
                self.master.y2 = 0
                self.master.k2 = 0
            elif self.master.state3 == 1:
                self.master.x3 = 0
                self.master.y3 = 0
                self.master.k3 = 0
        else:
            self.master.x1 = 0
            self.master.y1 = 0
            self.master.k1 = 0
            self.master.x2 = 0
            self.master.y2 = 0
            self.master.k2 = 0
            self.master.x3 = 0
            self.master.y3 = 0
            self.master.k3 = 0
    def reset_line(self):
        self.master.hid.set(0)
        self.draw_line()
    def reset_state(self):
        self.master.ress.configure(text=1)
        self.master.res.set(0)
        self.reset_line()
        self.master.f=0
        if self.master.ch.get() == 0:
            return
        else:
            self.master.state1 = 1
            self.master.state2 = 0
            self.master.state3 = 0
            self.master.fc1.configure(fg_color="#BD2828")
            self.master.fc2.configure(fg_color="Grey")
            self.master.fc3.configure(fg_color="Grey")   
    def break_sim(self):
        if self.after_id is not None:
            self.master.after_cancel(self.after_id)
    def change_state(self):
        self.break_sim()
        self.reset_dasboard()
        self.reset_entry()
        self.reset_position()
        self.reset_sim()
        self.master.timesim = 0
    def reset_to_default(self):
        self.reset_dasboard()
        self.reset_entry()
        self.reset_focus()
        self.reset_position()
        self.reset_sim()
        self.reset_target()
        if self.master.ch.get() == 1:
            self.reset_alltg()
        self.reset_variable()
        self.reset_state()
        self.break_sim()


if __name__ == "__main__":
    app = Window()
    app.mainloop()