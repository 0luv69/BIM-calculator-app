# this app is made to calculate the body mass index of person
import customtkinter as ctk
try:
    from ctypes import windll,byref,c_int,sizeof
except:
    pass

class window(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#50bfab")
        # window setup
        self.title("")#Body Mass Calculator
        self.geometry("380x350")
        self.resizable(False,False)
        try:
            self.iconbitmap("empty.ico")
        except Exception as error_c:
            print(error_c)
            print("The error could be of the icon file is Not found, \n Plz see the \"empty.ico\" file ")

        #change the title color
        self.title_bar_color_change()

        # datas
        self.metric_bool=ctk.BooleanVar(value=True)
        self.weight_value=ctk.DoubleVar(value=70)
        self.height_value= ctk.IntVar(value=170)
        self.bim_value_label= ctk.StringVar()
        self.calculator()

        #widgets
        self.first_part()
        self.second_part()
        self.third_part()
        
        #runner
        self.mainloop()

    def title_bar_color_change(self):
        try:    
            HWND= windll.user32.GetParent(self.winfo_id())
            title_bar_color= 0x00abbf50 # color start from 4th letter/digits which is inverted then the orginal one like it is first (blue,green,red)
            windll.dwmapi.DwmSetWindowAttribute(HWND,
                                        35,# 36= title nmae color
                                        byref(c_int(title_bar_color)),
                                        sizeof(c_int))
        except:    
            pass 

    def calculator(self):
        height_in_meter=self.height_value.get()/100
        weigth_in_kg= self.weight_value.get()
        bim_result= round(weigth_in_kg/ height_in_meter **2,2)
        self.bim_value_label.set(bim_result)


    def first_part(self):
        #first frame
        self.first_frame=ctk.CTkFrame(self,corner_radius=0,fg_color="#50bfab")
        self.first_frame.place(relx=0,rely=0,relheight=.5,relwidth=1)

        # the button in top right corner
        self.mertic_button=ctk.CTkButton(self.first_frame, text="metric", fg_color="#50bfab",
                                         text_color="Blue", hover=False, command=self.units_changer)
        self.mertic_button.place(relx=1,rely=0,anchor="ne",relwidth=.19)

        #the bim value
        self.bim__label=ctk.CTkLabel(self.first_frame,text="0", textvariable=self.bim_value_label,
                                     fg_color="#50bfab", font=ctk.CTkFont(family="comic sans ms",size=80,weight="bold"),
                                     text_color="#fff")
        self.bim__label.place(relx=.2,rely=.17,anchor="nw")
   
    def units_changer(self):
        if self.metric_bool.get():
            self.mertic_button.configure(text="imperial")
            #weight    
            pound,ounches=divmod((self.weight_value.get() *2.20462 *16),12)
            self.weight_var.set(f"{int(pound)}lb {int(ounches)}oz")

            #height
            feet,Inch_height=divmod(self.height_value.get()/2.54,12)
            self.height_label_var.set(f"{int(feet)}\'{int(Inch_height)}\"")

        else:
            self.mertic_button.configure(text="metric")
            #weight
            self.weight_var.set(f"{self.weight_value.get()}Kg")   

            #height
            self.height_label_var.set(f"{round(self.height_value.get()/100,2)}m")
        self.metric_bool.set(not self.metric_bool.get())    
        pass
    
    def second_part(self):
        #second frame
        self.second_frame=ctk.CTkFrame(self,corner_radius=15,fg_color="#fff")
        self.second_frame.place(relx=0.05,rely=0.5,relheight=.2,relwidth=0.89)
        
        # weigth entry

        self.weight_var=ctk.StringVar(value=f"{self.weight_value.get()}Kg")
        self.weight_label= ctk.CTkLabel(self.second_frame,textvariable=self.weight_var,
                                        text_color="#000",font=("classic",25))
        self.weight_label.place(relx=0.33,rely=.28) 

        def butttoonn():
            # left buttons
                # big button
            self.big_minus_btn=ctk.CTkButton(self.second_frame,text="-",font=("b",30),
                                            fg_color="#EEEEEE",text_color="#000",hover_color="light grey",command= lambda:self.minus_weight(1))
            self.big_minus_btn.place(relx=0.04,rely=0.14,relheight=.7,relwidth=.15)

                # small button
            self.big_minus_btn=ctk.CTkButton(self.second_frame,text="-",font=("b",30),
                                            fg_color="#EEEEEE",text_color="#000",hover_color="light grey",command= lambda:self.minus_weight(.1))
            self.big_minus_btn.place(relx=0.2,rely=0.24,relheight=.5,relwidth=.11)  


            # rigth buttons
                    # big button -5
            self.big_left_btn=ctk.CTkButton(self.second_frame,text="+",font=("b",30),
                                            fg_color="#EEEEEE",text_color="#000",hover_color="light grey",command= lambda:self.add_weight(1))
            self.big_left_btn.place(relx=0.81,rely=0.14,relheight=.7,relwidth=.15)

                # small button -1
            self.big_left_btn=ctk.CTkButton(self.second_frame,text="+",font=("b",30),
                                            fg_color="#EEEEEE",text_color="#000",hover_color="light grey",command= lambda:self.add_weight(.1))
            self.big_left_btn.place(relx=0.687,rely=0.24,relheight=.5,relwidth=.11)  
        butttoonn()
    def minus_weight(self,num):
        weigth_minus= round(self.weight_value.get() - float(num),2)
        self.weight_value.set(weigth_minus)
        if self.metric_bool.get():
            self.weight_var.set(f"{weigth_minus}Kg")
        else:
            pound,ounches=divmod((self.weight_value.get() *2.20462 *16),12)
            self.weight_var.set(f"{int(pound)}lb {int(ounches)}oz")
        self.calculator()
    def add_weight(self,num):
        weigth_add= round(self.weight_value.get() +float(num),2)
        self.weight_value.set(weigth_add)
        if self.metric_bool.get():
            self.weight_var.set(f"{weigth_add}Kg")
        else:
            pound,ounches=divmod((self.weight_value.get() *2.20462 *16),12)
            self.weight_var.set(f"{int(pound)}lb {int(ounches)}oz")    

        self.calculator()    
        

    def third_part(self):
        # third frame
        self.third_frame=ctk.CTkFrame(self,corner_radius=15,fg_color="#fff")
        self.third_frame.place(relx=0.05,rely=0.75,relheight=.2,relwidth=0.89)

        #slider
        self.slider0=ctk.CTkSlider(self.third_frame,orientation="horizontal",from_=100,to=250,button_color="#50bfab",
                                   variable=self.height_value,progress_color="#50bfab",fg_color="#F1F0E8",command=self.height_formula)
        self.slider0.place(relx=0.05,rely=0.38)

        #label for height input
        self.height_label_var=ctk.StringVar(value=f"{round(self.height_value.get()/100,2)}m")

        self.height_label= ctk.CTkLabel(self.third_frame,textvariable=self.height_label_var,
                                        text_color="#000",font=("ink free",37))
        self.height_label.place(relx=0.64,rely=.12)
    def height_formula(self,e):
        if self.metric_bool.get():    
                self.height_label_var.set(f"{round(self.height_value.get()/100,2)}m") 
        else:
            feet,Inch_height=divmod(self.height_value.get()/2.54,12)
            self.height_label_var.set(f"{int(feet)}\'{int(Inch_height)}\"")

        self.calculator()



if __name__=="__main__":
    window()



