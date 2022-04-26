#from tkinter.constants import FALSE, RIGHT
#from typing import Counter
#hiiiiiiiiiii
from guizero import *
from tksheet import Sheet
import tkinter as tk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
app = App(title= "hello",width=1920,height=1080,bg = "#012443")
app.tk.state('zoomed')
app.text_color = "#FF6B6B"
app.text_size = 30
###############################
def calculate_values():
    s = dna_a_nkl.value
    dna_a_nkl.value = s.upper()
    def calculate_dna_b():
        b = ""
        for i in s:
            if(i == "a" or i == "t" or i==  "c" or i=="g" or i=="A" or i=="T" or i=="C" or i=="G"):
                if(i == "a" or i=="A"):
                     b+= "T"
                elif(i=="c" or i=="C"):
                     b+="G"
                elif(i=="g"or i=="G"):
                     b+="C"
                elif(i=="t"or i=="T"):
                    b+="A"         
            else:
                error("hi","قيمة خاطئة في تسلسل الحمض النووي")
                b = ""
                return ""
            dna_b_nkl.value = b
            codon.value = (int(len(dna_a_nkl.value)) // 3) -2
            ramez.value = int(codon.value) + 2
            if int(codon.value) < 0:
                codon.value = "0"
            if int(ramez.value) < 0:
                ramez.value = "0"
    def calculate_mrna():
        mrna = ""
        for i in s:
            if(i == "a" or i == "t" or i==  "c" or i=="g" or i=="A" or i=="T" or i=="C" or i=="G"):
                if(i == "a" or i=="A"):
                     mrna+= "U"
                elif(i=="c" or i=="C"):
                     mrna+="G"
                elif(i=="g"or i=="G"):
                     mrna+="C"
                elif(i=="t"or i=="T"):
                    mrna+="A"             
            else:
                error("hi","قيمة خاطئة في تسلسل الحمض النووي")
                mrna = ""
                return ""            
        mrna_nkl.value = mrna
    def calculate_trna():
        s = mrna_nkl.value
        trna = ""
        Counter =0
        for i in s:
            if(i == "a" or i == "u" or i==  "c" or i=="g" or i=="A" or i=="U" or i=="C" or i=="G"):
                if(i == "a" or i=="A"):
                     trna+= "U"
                elif(i=="c" or i=="C"):
                     trna+="G"
                elif(i=="g"or i=="G"):
                     trna+="C"
                elif(i=="u"or i=="U"):
                    trna+="A"  
                Counter+=1
                if Counter == 3:
                    trna+="-"
                    Counter=0              
            else:
                error("hi","قيمة خاطئة في تسلسل الحمض النووي")
                trna = ""
                return ""
        if trna != "":
            if trna [-1] == "-":                    
                trna_nkl.value = trna[:-1]
            else:
                info("hi","هناك رامز معاكس ناقص الرجاء وضع سلسلة ابوية عدد النيوكلوتيدات فيها يقبل القسمة على 3")
                trna_nkl.value = trna           
    calculate_dna_b()              
    calculate_mrna()
    calculate_trna()
def calculate_diff_values():
    counter =0 
    s1 = st_dna_nkl.value
    s2 = nd_dna_nkl.value
    if(int(len(s1))>int(len(s2))):
        end = int(len(s2))
    else:
        end = int(len(s1))    
    for i in range(0,end,1):
        if (s1[i]!=s2[i]):
            counter +=1
    percent = 100*(counter + abs(int(len(s1)) - int(len(s2))))/end 
    percent  = int(percent)
    simlar_percent = 100 - percent
    if percent > 100:
        percent = 100
        simlar_percent = 0
    diff_percent.value = str(percent) + "%"  
    sim_percent.value =  str(simlar_percent) + "%"   
def calculate__values():
    a1 = 0
    t1 = 0
    c1 = 0 
    g1 = 0
    a2,t2,c2,g2 = 0
    s = st_dna.value
    for i in s:
        if(i == "a" or i=="A"):
            a1+=1
        elif(i=="c" or i=="C"):
            c1+=1
        elif(i=="g"or i=="G"):
            g1+=1
        elif(i=="t"or i=="T"):
            t1+=1 
    s = nd_dna.value         
    for i in s:
        if(i == "a" or i=="A"):
            a2+=1
        elif(i=="c" or i=="C"):
            c2+=1
        elif(i=="g"or i=="G"):
            g2+=1
        elif(i=="t"or i=="T"):
            t2+=1    

def show_calcu():
    basic_io.show()
    diffrence_box.hide()
    about_box.hide()   
def show_diff():
    basic_io.hide()    
    diffrence_box.show() 
    about_box.hide()   
def show_about():
    about_box.show()
    basic_io.hide()
    diffrence_box.hide()

###############################
Box(app,align="top",height= 15)
control = Box(app,align = "Top",width="fill",height=130)
Box(control,align="left",width= 70)
calcu_bt = PushButton(control,align="left",width=20,text = "الالة الحاسبة",command = show_calcu)
diffrence_bt = PushButton(control,align="left",width=20,text = "نسبة الاختلاف",command = show_diff)
about_bt = PushButton(control,align="left",width=20,text = "حــول",command = show_about)
#main_title = Text(app,"برنامج حاسبة الحموض النووية",align= "top")
#main_title.text_size = 40
#main_title.text_color = "#FFAB4C"
###################################################
diffrence_box = Box(app,align="top",width="fill")
diffrence_box.hide()
Box(diffrence_box,height=30,align="top")
st_dna = Box(diffrence_box,align="top",width="fill")
Text(st_dna,text = "    السلسلة الاولى ",align="right")
st_dna_nkl = TextBox(st_dna,align="right",width=60)
st_dna_nkl.bg = "#3F3351"
st_dna_nkl.text_color = "#E9A6A6"
Box(diffrence_box,height=30,align="top")
###
nd_dna = Box(diffrence_box,align="top",width="fill")
Text(nd_dna,text = "     السلسلة الثانية ",align="right")
nd_dna_nkl = TextBox(nd_dna,align="right",width=60)
nd_dna_nkl.bg = "#3F3351"
nd_dna_nkl.text_color = "#E9A6A6"
###
Box(diffrence_box,height=30,align="top")
##########
diff_result_box = Box(diffrence_box,align="top")
Text(diff_result_box,align= "left",text = "نسبة الاختلاف = ",size = 40,color = "#FFAB4C")
diff_percent = Text(diff_result_box,align= "left",text = "0",size = 40,color = "#FFAB4C")
Text(diff_result_box,align= "left",text = "             ",size = 40,color = "#FFAB4C")
Text(diff_result_box,align= "left",text = "نسبة التشابه = ",size = 40,color = "#FFAB4C")
sim_percent = Text(diff_result_box,align= "left",text = "0",size = 40,color = "#FFAB4C")
##########
Box(diffrence_box,height=30,align="top")
calculate_diff = PushButton(diffrence_box,align="top",text = "احــــســـــب",command = calculate_diff_values)
calculate_diff.bg = "#4A3933"
calculate_diff.text_color = "#F0A500"
calculate_diff.text_size = 25
calculate_diff.width = 30
###################################################
about_box = Box(app,align="top",width="fill")
about_box.hide()
Box(about_box,height=230,align="top")
Text(about_box,text = "تمت برمجته بواسطة الطالب اسامة بريمان",align="middle",color = "#FFAB4C",size = 40)
Box(about_box,height=30,align="top")
Text(about_box,text = "مدرسة العلوم الانسة سعاد طحان",align="middle",color = "#FFAB4C",size = 40)
Box(about_box,height=30,align="top")
Text(about_box,text = "ثانوية الباسل للمتفوقين  الفصل الاول عام 2021",align="middle",color = "#FFAB4C",size = 40)
Box(about_box,height=30,align="top")
Text(about_box,text = "الصف الحادي عشر شعبة 2",align="middle",color = "#FFAB4C",size = 40)

###################################################
basic_io = Box(app,align="top",width="fill")
Box(basic_io,height=30,align="top")
#
dna_a = Box(basic_io,align="top",width="fill")
Text(dna_a,text = "    السلسلة الابوية ",align="right")
dna_a_nkl = TextBox(dna_a,align="right",width=60)
dna_a_nkl.bg = "#3F3351"
dna_a_nkl.text_color = "#E9A6A6"
#
Box(basic_io,height=20,align="top")
#
dna_b = Box(basic_io,align="top",width="fill")
Text(dna_b,text = "   السلسلة المتممة ",align="right")
dna_b_nkl = TextBox(dna_b,align="right",width=60)
dna_b_nkl.bg = "#3F3351"
dna_b_nkl.text_color = "#E9A6A6"
#
Box(basic_io,height=20,align="top")
#
mrna = Box(basic_io,align="top",width="fill")
Text(mrna,text = "   مرسال RNA ",align="right")
mrna_nkl = TextBox(mrna,align="left",width=60)
mrna_nkl.bg = "#3F3351"
mrna_nkl.text_color = "#E9A6A6"
#
#
Box(basic_io,height=20,align="top")
#
trna = Box(basic_io,align="top",width="fill")
Text(trna,text = "   ناقل RNA ",align="right")
trna_nkl = TextBox(trna,align="left",width=60)
trna_nkl.bg = "#3F3351"
trna_nkl.text_color = "#E9A6A6"
#
Box(basic_io,height=50,align="top")
#####
tst = Box(basic_io,align="top",width="fill")
codon_box = Box(tst,align="left")
Text(codon_box,align= "left",text = " عدد الروامز المعاكسة = ",size = 40,color = "#FFAB4C")
codon = Text(codon_box,align= "left",text = "0",size = 40,color = "#FFAB4C")
Text(codon_box,align="left",text = "            ")
Text(codon_box,align= "left",text = " عدد الروامز = ",size = 40,color = "#FFAB4C")
ramez = Text(codon_box,align= "left",text = "0",size = 40,color = "#FFAB4C")
#
Box(basic_io,height=20,align="top")
#
calculate = PushButton(basic_io,align="top",text = "احــــســـــب",command = calculate_values)
calculate.bg = "#4A3933"
calculate.text_color = "#F0A500"
calculate.text_size = 25
calculate.width = 30



app.display()
