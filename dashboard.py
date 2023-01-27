import tkinter as tk
from PIL import ImageTk, Image

dash=tk.Tk()
dash.title('TRELLA')
dash.geometry('1920x1080')
dash.minsize(1920, 1080)

icon=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/llogo.png')
dash .iconphoto(True, icon)

#========================  INDICATOR FUNCTION  ======================================

def hchk_indicate():
    chk_btn.config(fg=lfnt)
    rem_btn.config(fg=lfnt)
    st_btn.config(fg=lfnt)
    
def schk_indicate(ind):
    hchk_indicate()
    ind.config(fg='white')

#========================  FRONT END  ======================================
#-------------------  Theme  -----------------------------
            
lth_clr='#97C1EC'
dth_clr='#2A5F7F'
btn_bg='#5B90B4'

lfnt=lth_clr
dfnt=dth_clr

#----------------------------------------------------------
def chk_frontend(user_data:dict):
    dashfr=tk.Frame(dash, width=1230, height=746)
    dashfr.place(x=535, y=300)
    
    dashfr_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/dash_bg.jpg'))
    dash_bg=tk.Label(dash, image=dashfr_img)
    dash_bg.image=dashfr_img
    dash_bg.pack(fill='both', expand='yes')

#------------------  SIDEBAR  ---------------------------
    sidebar =tk.Frame(dash ,bg=dth_clr)    
    sidebar.place(x=30, y=70, width=400, height=800)
#----------------  Dashboard Heading  -------------------
    heading =tk.Label(dash , text='Dashboard',font=('yu gothic ui', 44, 'bold'),bg=lth_clr, fg=dfnt)
    heading.place(x=950, y=35)
        
#----------------  Logo Frame  -------------------
    
    lframe =tk.Frame(sidebar ,bg=dth_clr)    
    lframe.place(x=50, y=50, width=300, height=250)

    #----------------  Logo Image -------------------
    
    dash_logo=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/llogo.png'))
    logo_lbl=tk.Label(lframe, image=dash_logo, bg= dth_clr)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='top') 
    
    #----------------  Logo Label -------------------

    logo_lbl=tk.Label(lframe, text='Hello '+user_data["username"], bg= dth_clr, font=('yu gothic ui', 25, 'bold'), fg=lfnt)
    logo_lbl.image=dash_logo
    logo_lbl.pack(side='bottom') 

# ====================  Button Labels  =======================================================================
    #-----------------Checklist--------------------------
    btn_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/DASH_BTN.png')
    
    
    chk_btn_lbl=tk.Label(sidebar, image=btn_img, bg=dth_clr)
    chk_btn_lbl.image=btn_img
    chk_btn_lbl.place(x=15, y=370)

    #-----------------  REMINDER  --------------------------
    
    rem_btn_lbl=tk.Label(sidebar, image=btn_img, bg=dth_clr)
    rem_btn_lbl.image=btn_img
    rem_btn_lbl.place(x=15, y=460)

    #-----------------  sticky notes  --------------------------
    
    st_btn_lbl=tk.Label(sidebar, image=btn_img, bg=dth_clr)
    st_btn_lbl.image=btn_img
    st_btn_lbl.place(x=15, y=550)

# ====================  Buttons  ================================================================================
    #-----------------  Checklist  --------------------------
    chk_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/check-list.png'))
    chk_img.image=chk_img
    global chk_btn
    chk_btn=tk.Button(chk_btn_lbl, text='          CHECKLIST',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg,activeforeground='white', bd=0,highlightthickness=0, command=lambda:schk_indicate(chk_btn))
    chk_btn.place(x=30, y=7)

    chk_img_lbl=tk.Label(chk_btn, image=chk_img, bg=btn_bg)
    chk_img_lbl.place(x=10, y=10)
    
    #-----------------  reminder  --------------------------
    
    rem_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/reminder.png'))
    rem_img.image=rem_img
    global rem_btn
    rem_btn=tk.Button(rem_btn_lbl, text='          REMINDER',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg, activeforeground='white',bd=0,highlightthickness=0, command=lambda:schk_indicate(rem_btn) )
    rem_btn.place(x=30, y=10)

    rem_img_lbl=tk.Label(rem_btn, image=rem_img, bg=btn_bg)
    rem_img_lbl.place(x=10, y=10)

    #-----------------  sticky notes --------------------------
    
    st_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/reminder.png'))
    st_img.image=st_img
    global st_btn
    st_btn=tk.Button(st_btn_lbl, text='       STICKY NOTES',font=('yu gothic ui', 25, 'bold'), bg=btn_bg, fg=lfnt, cursor='hand2', activebackground=btn_bg,activeforeground='white' , bd=0,highlightthickness=0, command=lambda:schk_indicate(st_btn) )
    st_btn.place(x=30, y=10)

    st_img_lbl=tk.Label(st_btn, image=st_img, bg=btn_bg)
    st_img_lbl.place(x=10, y=10)

#-----------------  Logout Button  --------------------------

    lcircle_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/L_BTN.png')
    lcircle_img.image=lcircle_img
    lcircle_lbl=tk.Label(sidebar, image=lcircle_img, bg=dth_clr)
    lcircle_lbl.place(x=145, y=660)

    lbtn_img=tk.PhotoImage(file='/home/wae/Documents/giri raj sir/Trella/Images/logout.png')
    lbtn_img.image=lbtn_img
    lbtn=tk.Button(lcircle_lbl, image=lbtn_img, bg=btn_bg, activebackground=btn_bg, cursor='hand2', highlightthickness=0, bd=0)
    lbtn.place(x=19, y=15)

#-----------------  Inner Frame  --------------------------
    iframe =tk.Frame(dash ,bg=dth_clr)    
    iframe.place(x=520, y=140, width=1300, height=811)

    trans_img=ImageTk.PhotoImage(Image.open('/home/wae/Documents/giri raj sir/Trella/Images/h.png'))
    trans=tk.Label(iframe, image=trans_img, bd=0, highlightthickness=0)
    trans.image=trans_img
    trans.place(x=0, y=0)

if __name__=="__main__":
    chk_frontend()

def run_dashboard(user_data:dict):
    chk_frontend(user_data)
    dash.mainloop()