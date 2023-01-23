import tkinter as tk
from PIL import ImageTk, Image

dash=tk.Tk()
dash.title('TRELLA')
dash.geometry('1920x1080')
dash.minsize(1920, 1080)

#----------------  Titlebar Icon   -----------------------
icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/llogo.png')
dash .iconphoto(True, icon)

#-------------------  Theme  -----------------------------
            
lth_clr='#A0B6E9'
dth_clr='#4C6195'
btn_bg='#637EC2'

lfnt=lth_clr
dfnt=dth_clr

#----------------------------------------------------------
def dash_frontend():
#------------------  HEADER BAR ---------------------------

    header= tk.Frame(dash , bg=lth_clr)
    header.place(x=400, y=0, width=1550, height=150)   

#------------------  SIDEBAR  ---------------------------
    sidebar =tk.Frame(dash ,bg=dth_clr)    
    sidebar.place(x=0, y=0, width=400, height=1080)
#----------------  Dashboard Heading  -------------------
    heading =tk.Label(header , text='Dashboard',font=('yu gothic ui', 44, 'bold'),bg=lth_clr, fg=dfnt)
    heading.place(x=600, y=30)
        
#----------------  Logo Frame  -------------------
    
    lframe =tk.Frame(sidebar ,bg=dth_clr)    
    lframe.place(x=50, y=50, width=300, height=250)

    #----------------  Logo Image -------------------
    
    dash_logo=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/llogo.png'))
    logo_lbl=tk.Label(lframe, image=dash_logo, bg= dth_clr)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='top') 
    
    #----------------  Logo Label -------------------

    logo_lbl=tk.Label(lframe, text='Hello Haseena', bg= dth_clr, font=('yu gothic ui', 25, 'bold'), fg=lfnt)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='bottom') 

# ====================  Button Labels  ========================
    #-----------------Checklist--------------------------
    btn_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/dash_btn.png')
    
    chk_btn_lbl=tk.Label(sidebar, image=btn_img, bg=dth_clr)
    chk_btn_lbl.image=btn_img
    chk_btn_lbl.place(x=15, y=370)


# ====================  Buttons  ========================
    #-----------------Checklist--------------------------
    chk_btn=tk.Button(chk_btn_lbl, text='CHECKLIST',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg, bd=0,highlightthickness=0 )
    chk_btn.place(x=15, y=10)

dash_frontend()

dash.mainloop()