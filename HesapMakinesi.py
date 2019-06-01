from tkinter import *


########## MAIN ##########
root = Tk()
root.title("Hesap Makinesi")
root.geometry("235x200")
root.resizable(FALSE,FALSE)
root.config(bg="#171717")
root.iconbitmap("images/sdsad.ico")
#########################
main_number = ''
memory_number = ''
cold_blue = "#68FFF2"
mavi = "#4F9EFF"
last_time = 0



def cik():
     sys.exit()


def hane_sil(event=None):
    global main_number
    a =main_number[len(main_number)-1]
    x = str(a)
    jh = main_number.replace(a, "", 1)
    main_number = jh
    screen()
    yazi()


def clean(event=None):
    global main_number
    main_number = ' '
    screen()
    sil_text = Label(text="                                                      ", fg="#171717", bg="#171717")
    sil_text.pack()
    sil_text.place(x=20, y=40)

    return main_number

def memory_arti(event=None):
    global  main_number
    global memory_number
    global last_time
    sayisal_veri = eval(main_number)
    virtual_number  = str(sayisal_veri)
    memory_number=virtual_number
    if(memory_number==virtual_number )and(last_time == 0):
        viasd = "M1 = " + memory_number
        label = Label(text=viasd, bg="#171717", fg="white", font="Arial 8")
        label.pack()
        label.place(x=185, y=33)
        last_time = last_time+1

    elif(last_time>= 1):
        m2 = "M2 = " + memory_number
        label = Label(text=m2, bg="#171717", fg="white", font="Arial 8")
        label.pack()
        label.place(x=185, y=50)
        last_time = last_time + 1



def memory_clear(event=None):
    global memory_number
    global last_time
    memory_number = ''
    label = Label(text="                \n                ", bg="#171717", fg="white", font="Arial 8")
    label.pack()
    label.place(x=185, y=33)
    last_time = 0


def hesapla(event=None):
    a = eval(main_number)
    ab = str(a)
    text_yazi = ("Sonuç  :   " + ab)
    cikti = Label(text=text_yazi,fg="red",bg="#171717")
    cikti.pack()
    cikti.place(x=20, y=40)

def yazi():
    label = Label(text=main_number,bg="white",fg="black")
    label.pack()
    label.place(x=26, y=10)

def fonk_sifir(event=None):
    global main_number
    main_number += '0'
    yazi()
    return main_number

def fonk_bir(event=None):
    global main_number
    main_number+= '1'
    yazi()
    return main_number

def fonk_iki(event=None):
    global main_number
    main_number+= '2'
    yazi()
    return main_number

def fonk_uc(event=None):
    global main_number
    main_number+= '3'
    yazi()
    return main_number

def fonk_dort(event=None):
    global main_number
    main_number+= '4'
    yazi()
    return main_number

def fonk_bes(event=None):
    global main_number
    main_number+= '5'
    yazi()
    return main_number

def fonk_alti(event=None):
    global main_number
    main_number+= '6'
    yazi()
    return main_number

def fonk_yedi(event=None):
    global main_number
    main_number+= '7'
    yazi()
    return main_number

def fonk_sekiz(event=None):
    global main_number
    main_number+= '8'
    yazi()
    return main_number

def fonk_dokuz(event=None):
    global main_number
    main_number+= '9'
    yazi()
    return main_number
#####################

def fonk_topla(event=None):
    global main_number
    main_number+= '+'
    yazi()
    return main_number

def fonk_cikar(event=None):
    global main_number
    main_number+= '-'
    yazi()
    return main_number

def fonk_carp(event=None):
        global main_number
        main_number+= '*'
        yazi()
        return main_number

def fonk_bol(event=None):
    global main_number
    main_number+= '/'
    yazi()
    return main_number



def screen():
     screen = Label(text="                                                           ", bg="white")
     screen.pack()
     screen.place(x=26, y=10)

screen()



bitir = Button(text="Hesapla",command=hesapla,bg="#7975FF")
bitir.pack()
bitir.place(x=180,y=170)

sil = Button(text="      Sil    ", command=clean,bg="#7975FF")
sil.pack()
sil.place(x=180, y=80)

m_arti = Button(text="    M+    ",bg="#3F62FF",command=memory_arti)
m_arti.pack()
m_arti.place(x=180,y=140)

mrc = Button(text="   MRC   ",bg="#3F62FF",command=memory_clear)
mrc.pack()
mrc.place(x=180,y=110)

cizgi_yatay = Label(text="-----------------------------------------------",bg="#171717", fg="#19C485")
cizgi_yatay.pack()
cizgi_yatay.place(x=0,y=59)

cizgi = Label(text="|\n|\n|\n|\n|\n|\n|\n|\n",bg="#171717", fg="#19C485")
cizgi.pack()
cizgi.place(x=105,y=75)





#######

bol = Button(text = "       /       ",command=fonk_bol,bg=mavi)
bol.pack()
bol.place(x=120,y=170)

carp = Button(text="       *       ",command=fonk_carp,bg=mavi)
carp.pack()
carp.place(x=120, y=140)

cikar = Button(text="       -       ",command=fonk_cikar,bg=mavi)
cikar.pack()
cikar.place(x=120, y=110)

topla = Button(text="       +      ",command=fonk_topla,bg=mavi)
topla.pack()
topla.place(x=120, y=80)



#########       RAKAMLAR   ############
sifir = Button(text="             0             ",command=fonk_sifir,bg=cold_blue)
sifir.pack()
sifir.place(x=10, y=170)

bir = Button(text="  1  ",command=fonk_bir,bg=cold_blue)
bir.pack()
bir.place(x=10,y=140)

iki = Button(text="  2  ",command=fonk_iki,bg=cold_blue)
iki.pack()
iki.place(x=42, y=140)

uc = Button(text="  3  ",command=fonk_uc,bg=cold_blue)
uc.pack()
uc.place(x=75, y=140)

dort = Button(text="  4  ",command=fonk_dort,bg=cold_blue)
dort.pack()
dort.place(x=10, y=110)

bes = Button(text="  5  ",command=fonk_bes,bg=cold_blue)
bes.pack()
bes.place(x=42, y=110)

alti = Button(text="  6  ",command=fonk_alti,bg=cold_blue)
alti.pack()
alti.place(x=75, y=110)

yedi = Button(text="  7  ",command=fonk_yedi,bg=cold_blue)
yedi.pack()
yedi.place(x=10, y=80)

sekiz = Button(text="  8  ",command=fonk_sekiz,bg=cold_blue)
sekiz.pack()
sekiz.place(x=42, y=80)

dokuz = Button(text="  9  ",command=fonk_dokuz,bg=cold_blue)
dokuz.pack()
dokuz.place(x=75, y=80)
##############################

root.bind("<Delete>",clean)
root.bind("<Escape>", sys.exit)
root.bind("0",fonk_sifir)
root.bind("1",fonk_bir)
root.bind("2",fonk_iki)
root.bind("3",fonk_uc)
root.bind("4",fonk_dort)
root.bind("5",fonk_bes)
root.bind("6",fonk_alti)
root.bind("7",fonk_yedi)
root.bind("8",fonk_sekiz)
root.bind("9",fonk_dokuz)

root.bind("+",fonk_topla)
root.bind("-",fonk_cikar)
root.bind("*",fonk_carp)
root.bind("/",fonk_bol)

root.bind("<BackSpace>",hane_sil)
root.bind("<Return>",hesapla)
root.bind("<End>",memory_clear)
root.bind("<Insert>",memory_arti)

mainloop()
