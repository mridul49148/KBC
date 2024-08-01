from tkinter import *
import random as rd
import time as t
from ankita import *
from krishna import *
from Vishal import *
import random
root=Tk()
scoreimg0=PhotoImage(file='Image\\Picture0.png')
scoreimg1=PhotoImage(file='Image\\Picture1.png')
scoreimg2=PhotoImage(file='Image\\Picture2.png')
scoreimg3=PhotoImage(file='Image\\Picture3.png')
scoreimg4=PhotoImage(file='Image\\Picture4.png')
scoreimg5=PhotoImage(file='Image\\Picture5.png')
scoreimg6=PhotoImage(file='Image\\Picture6.png')
scoreimg7=PhotoImage(file='Image\\Picture7.png')
scoreimg8=PhotoImage(file='Image\\Picture8.png')
scoreimg9=PhotoImage(file='Image\\Picture9.png')
scoreimg10=PhotoImage(file='Image\\Picture10.png')
scoreimg11=PhotoImage(file='Image\\Picture11.png')
scoreimg12=PhotoImage(file='Image\\Picture12.png')
scoreimg13=PhotoImage(file='Image\\Picture13.png')
scoreimg14=PhotoImage(file='Image\\Picture14.png')
scoreimg15=PhotoImage(file='Image\\Picture15.png')

imgcongo=PhotoImage(file='congo.png')
lifeline50img=PhotoImage(file='Image\\d250-50.png')
lifeline50button_crossimg=PhotoImage(file='Image\\d2cross50-50.png')

layout=PhotoImage(file='lay.png')

flipTQimg=PhotoImage(file='Image\\flipTQ.png')
flipTQbutton_crossimg=PhotoImage(file='Image\\flipTQcross.png')

DDimg=PhotoImage(file='Image\\DD.png')
DDbutton_crossimg=PhotoImage(file='Image\\DDcross.png')

centerimg=PhotoImage(file='Image\\center.png')


dd='deactivated'
root.config(bg='black')



def work():
    questions=questions_kid
    options_A=options_A_kid
    options_B=options_B_kid
    options_C=options_C_kid
    options_D=options_D_kid
    answers=answers_kid

    global click
    click=True
    kidbutton.destroy()
   
    def fifty_fifty():
        flag=1
        quest_find=Textarea.get(1.0, "end-1c")
        quest_index=questions.index(quest_find)

        anscopy=answers
        OA=options_A
        OB=options_B
        OC=options_C
        OD=options_D
        tr=''
        if anscopy[quest_index]==OA[quest_index]:
            tr=1
        elif anscopy[quest_index]==OB[quest_index]:
            tr=2
        elif anscopy[quest_index]==OC[quest_index]:
            tr=3
        elif anscopy[quest_index]==OD[quest_index]:
            tr=4
        listr=[1,2,3,4]
        listr.remove(tr)
        for k in range(2):
            removeop=rd.choice(listr)
            listr.remove(removeop)
            if removeop==1:
                optionAbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
            elif removeop==2:
                optionbbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
            elif removeop==3:
                optioncbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
            elif removeop==4:
                optionDbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
        lifeline50button.config(command=0,relief='sunken',image=lifeline50button_crossimg)

    def flip():
        
        flip_quest=random.choice(extra_question_kids)
        # Textarea.delete(1.0,END)
        # Textarea.insert(END,flip_quest)
        # answers_kid.pop(i)
        # flip_oA=extra_optionA_kids[extra_question_kids.index(flip_quest)]
        # flip_oB=extra_optionB_kids[extra_question_kids.index(flip_quest)]
        # flip_oC=extra_optionC_kids[extra_question_kids.index(flip_quest)]
        # flip_oD=extra_optionD_kids[extra_question_kids.index(flip_quest)]
        # flip_ans=extra_answers_kids[extra_question_kids.index(flip_quest)]
        
        # answers_kid.insert(i,flip_ans)

        # optionAbutton.config(text=flip_oA)
        # optionbbutton.config(text=flip_oB)
        # optioncbutton.config(text=flip_oC)
        # optionDbutton.config(text=flip_oD)

        
        flipa='active'




        flipTQbutton.config(command=0,relief='sunken',image=flipTQbutton_crossimg)


    def DD():
        global dd
        dd='activated'
        print(dd)

        DDbutton.config(command=0,relief='sunken',image=DDbutton_crossimg)


    def select(event):
        global dd

        def fifty_fifty():
            flag=1
            quest_find=Textarea.get(1.0, "end-1c")
            quest_index=questions.index(quest_find)

            anscopy=answers
            OA=options_A
            OB=options_B
            OC=options_C
            OD=options_D
            tr=''
            if anscopy[quest_index]==OA[quest_index]:
                tr=1
            elif anscopy[quest_index]==OB[quest_index]:
                tr=2
            elif anscopy[quest_index]==OC[quest_index]:
                tr=3
            elif anscopy[quest_index]==OD[quest_index]:
                tr=4
            listr=[1,2,3,4]
            listr.remove(tr)
            for k in range(2):
                removeop=rd.choice(listr)
                listr.remove(removeop)
                if removeop==1:
                    optionAbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
                elif removeop==2:
                    optionbbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
                elif removeop==3:
                    optioncbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
                elif removeop==4:
                    optionDbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
            lifeline50button.config(command=0,relief='sunken',image=lifeline50button_crossimg)


        leftframe=Frame(root,bg='black',padx=30,pady=15)
        leftframe.grid(row=0,column=0)

        topframe=Frame(leftframe,bg='black')
        topframe.grid()

        centerframe=Frame(leftframe,bg='black')
        centerframe.grid(row=1,column=0)

        bottomframe=Frame(leftframe,bg='black')
        bottomframe.grid(row=2,column=0)
        bottomframe.place()

        rightframe=Frame(root,bg='black',pady=25,padx=50)
        rightframe.grid(row=0,column=1)

        
        
        lifeline50button=Button(topframe,image=lifeline50img,bg='black',bd=0,activebackground='black',width=180,height=80,command=fifty_fifty)   
        lifeline50button.grid(row=0,column=0)

        
        DDbutton=Button(topframe,image=DDimg,bg='black',bd=0,activebackground='black',width=180,height=80,command=DD)   
        DDbutton.grid(row=0,column=1)

        
        flipTQbutton=Button(topframe,image=flipTQimg,bg='black',bd=0,activebackground='black',width=180,height=80,command=flip)   
        flipTQbutton.grid(row=0,column=2)

        
        centerlabel=Label(centerframe,image=centerimg,bg='black',width=300,height=200)
        centerlabel.grid(row=0,column=0)


        scoreimg=[scoreimg0,scoreimg1,scoreimg2,scoreimg3,scoreimg4,scoreimg5,scoreimg6,scoreimg7,scoreimg8,scoreimg9,scoreimg10,scoreimg11,scoreimg12,scoreimg13,scoreimg14,scoreimg15]




        scorelabel=Label(rightframe,image=scoreimg[0],bg='black')
        scorelabel.grid(row=0,column=0)
                

        
        laylabel=Label(bottomframe,image=layout,bg='black')
        laylabel.grid(row=0,column=0)

        Textarea=Text(bottomframe,wrap='word',cursor='arrow',font=('arial',18,'bold'),width=42,height=2,fg='white',bd=0,bg='black',state='normal')
        Textarea.place(x=75,y=15)
        Textarea.bind("<Key>", lambda e: "break")
        Textarea.insert(END,questions[0])

        optionlabelA=Label(bottomframe,text='A:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
        optionlabelA.place(x=60,y=110+20)

        optionAbutton=Button(bottomframe,text=options_A[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2')
        optionAbutton.place(x=100,y=100+20)

        optionlabelB=Label(bottomframe,text='B:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
        optionlabelB.place(x=380,y=110+20)

        optionbbutton=Button(bottomframe,text=options_B[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2')
        optionbbutton.place(x=370+40,y=100+20)

        optionlabelc=Label(bottomframe,text='C:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
        optionlabelc.place(x=60,y=230)

        optioncbutton=Button(bottomframe,text=options_C[0],activebackground='black',font=('arial',18,'bold'),fg='white',bg='black',bd=0,activeforeground='white',cursor='hand2',anchor='sw')
        optioncbutton.place(x=90,y=220-5)

        optionlabeld=Label(bottomframe,text='D:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
        optionlabeld.place(x=330+50,y=190+40)

        optionDbutton=Button(bottomframe,text=options_D[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2',anchor='sw')
        optionDbutton.place(x=370+40,y=180+35)
        
        b=event.widget
        value=b['text']
        value2=b['image']
        f=1
        flag=0

        for i in range(15):
            if value==answers[i]:
                
                if answers[i]==answers[14]:
                    def dis():
                        root.destroy()
                    
                    Textarea.delete(1.0,END)
                    optionAbutton.config(text='')
                    optionbbutton.config(text='')
                    optioncbutton.config(text='')
                    optionDbutton.config(text='')
                    

                    root3=Toplevel()
                    root3.overrideredirect(True)
                    root3.config(bg='black')
                    root3.geometry('1000x300+140+200')
                    root3.title('You WON')

                    congolabel=Label(root3,image=imgcongo,height=200,bg='black')
                    congolabel.pack()
                    
                    dis=Button(root3,text='ENTER',font=('arial',20,'bold'),bg='black',activeforeground='white',activebackground='black',fg='white',bd=0,command=dis)
                    dis.place(x=600-150,y=250)
                    
                else:
                    Textarea.delete(1.0,END)
                    Textarea.insert(END,questions[i+1])
                    
                    
                    optionAbutton.config(text=options_A[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    optionbbutton.config(text=options_B[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    optioncbutton.config(text=options_C[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    optionDbutton.config(text=options_D[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    scorelabel.config(image=scoreimg[i+1])

            if value not in answers:
                if dd=='activated':
                    dd='deactivated'
                    
                else:
                    def closep():
                        root2.destroy()
                        root.destroy()
                    def tryp():
                        root2.destroy()
                        Textarea.delete(1.0,END)

                        Textarea.insert(END,questions[0])

                        optionAbutton.config(text=options_A[0])
                        optionbbutton.config(text=options_B[0])
                        optioncbutton.config(text=options_C[0])
                        optionDbutton.config(text=options_D[0])

                        scorelabel.config(image=scoreimg[0])





                    root2=Toplevel()
                    root2.overrideredirect(True)
            
                    root2.config(bg='black')
                    root2.geometry('287x400+250+70')
                    frame=Frame(root2,highlightbackground='blue',highlightthickness='5',height=500,width=400,bg='black')
                    frame.pack()
                    root2.title('You lose')

                    imglabel=Label(frame,image=centerimg,bd=0)
                    imglabel.pack(pady=30)

                    loselabel=Label(frame,text='You lose',font=('arial',40,'bold'),bg='black',fg='white')
                    loselabel.pack()

                    tryagain=Button(frame,text='Try again',font=('arial',20,'bold'),bg='black',activeforeground='white',activebackground='black',fg='white',bd=0,command=tryp)
                    tryagain.pack()

                    close=Button(frame,text='close',font=('arial',20,'bold'),bg='black',activeforeground='white',activebackground='black',fg='white',bd=0,command=closep)
                    close.pack()

                    root2.mainloop()
                    break




    
    

    leftframe=Frame(root,bg='black',padx=30,pady=15)
    leftframe.grid(row=0,column=0)

    topframe=Frame(leftframe,bg='black')
    topframe.grid()

    centerframe=Frame(leftframe,bg='black')
    centerframe.grid(row=1,column=0)

    bottomframe=Frame(leftframe,bg='black')
    bottomframe.grid(row=2,column=0)
    bottomframe.place()

    rightframe=Frame(root,bg='black',pady=25,padx=50)
    rightframe.grid(row=0,column=1)

    
    
    lifeline50button=Button(topframe,image=lifeline50img,bg='black',bd=0,activebackground='black',width=180,height=80,command=fifty_fifty)   
    lifeline50button.grid(row=0,column=0)

    
    DDbutton=Button(topframe,image=DDimg,bg='black',bd=0,activebackground='black',width=180,height=80,command=DD)   
    DDbutton.grid(row=0,column=1)

    
    flipTQbutton=Button(topframe,image=flipTQimg,bg='black',bd=0,activebackground='black',width=180,height=80,command=flip)   
    flipTQbutton.grid(row=0,column=2)

    
    centerlabel=Label(centerframe,image=centerimg,bg='black',width=300,height=200)
    centerlabel.grid(row=0,column=0)


    scoreimg=[scoreimg0,scoreimg1,scoreimg2,scoreimg3,scoreimg4,scoreimg5,scoreimg6,scoreimg7,scoreimg8,scoreimg9,scoreimg10,scoreimg11,scoreimg12,scoreimg13,scoreimg14,scoreimg15]




    scorelabel=Label(rightframe,image=scoreimg[0],bg='black')
    scorelabel.grid(row=0,column=0)
            

    
    laylabel=Label(bottomframe,image=layout,bg='black')
    laylabel.grid(row=0,column=0)

    Textarea=Text(bottomframe,wrap='word',cursor='arrow',font=('arial',18,'bold'),width=42,height=2,fg='white',bd=0,bg='black',state='normal')
    Textarea.place(x=75,y=15)
    Textarea.bind("<Key>", lambda e: "break")
    Textarea.insert(END,questions[0])

    optionlabelA=Label(bottomframe,text='A:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabelA.place(x=60,y=110+20)

    optionAbutton=Button(bottomframe,text=options_A[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2')
    optionAbutton.place(x=100,y=100+20)

    optionlabelB=Label(bottomframe,text='B:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabelB.place(x=380,y=110+20)

    optionbbutton=Button(bottomframe,text=options_B[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2')
    optionbbutton.place(x=370+40,y=100+20)

    optionlabelc=Label(bottomframe,text='C:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabelc.place(x=60,y=230)

    optioncbutton=Button(bottomframe,text=options_C[0],activebackground='black',font=('arial',18,'bold'),fg='white',bg='black',bd=0,activeforeground='white',cursor='hand2',anchor='sw')
    optioncbutton.place(x=90,y=220-5)

    optionlabeld=Label(bottomframe,text='D:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabeld.place(x=330+50,y=190+40)

    optionDbutton=Button(bottomframe,text=options_D[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2',anchor='sw')
    optionDbutton.place(x=370+40,y=180+35)  


    optionAbutton.bind('<Button-1>',select)
    optionbbutton.bind('<Button-1>',select)
    optioncbutton.bind('<Button-1>',select)
    optionDbutton.bind('<Button-1>',select)
    # lifeline50button.bind('<Button-1>',fifty_fifty)
        
def work2():
    questions=questions_adult
    options_A=options_A_adult
    options_B=options_B_adult
    options_C=options_C_adult
    options_D=options_D_adult
    answers=answers_adult

    global click
    click=True
    kidbutton.destroy()
    def fifty_fifty():
        flag=1
        quest_find=Textarea.get(1.0, "end-1c")
        quest_index=questions.index(quest_find)

        anscopy=answers
        OA=options_A
        OB=options_B
        OC=options_C
        OD=options_D
        tr=''
        if anscopy[quest_index]==OA[quest_index]:
            tr=1
        elif anscopy[quest_index]==OB[quest_index]:
            tr=2
        elif anscopy[quest_index]==OC[quest_index]:
            tr=3
        elif anscopy[quest_index]==OD[quest_index]:
            tr=4
        listr=[1,2,3,4]
        listr.remove(tr)
        for k in range(2):
            removeop=rd.choice(listr)
            listr.remove(removeop)
            if removeop==1:
                optionAbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
            elif removeop==2:
                optionbbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
            elif removeop==3:
                optioncbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
            elif removeop==4:
                optionDbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
        lifeline50button.config(command=0,relief='sunken',image=lifeline50button_crossimg)
    def flip():
        flipTQbutton.config(command=0,relief='sunken',image=flipTQbutton_crossimg)
    def DD():
        DDbutton.config(command=0,relief='sunken',image=DDbutton_crossimg)

    def select(event):
        b=event.widget
        value=b['text']
        value2=b['image']
        f=1
        flag=0

        for i in range(15):

            if value==answers[i]:
                
                if answers[i]==answers[14]:
                    def dis():
                        root.destroy()
                    
                    Textarea.delete(1.0,END)
                    optionAbutton.config(text='')
                    optionbbutton.config(text='')
                    optioncbutton.config(text='')
                    optionDbutton.config(text='')
                    

                    root3=Toplevel()
                    root3.overrideredirect(True)
                    root3.config(bg='black')
                    root3.geometry('1000x300+140+200')
                    root3.title('You WON')

                    congolabel=Label(root3,image=imgcongo,height=200,bg='black')
                    congolabel.pack()
                    
                    dis=Button(root3,text='ENTER',font=('arial',20,'bold'),bg='black',activeforeground='white',activebackground='black',fg='white',bd=0,command=dis)
                    dis.place(x=600-150,y=250)
                    
                else:
                    Textarea.delete(1.0,END)
                    Textarea.insert(END,questions[i+1])
                    
                    
                    optionAbutton.config(text=options_A[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    optionbbutton.config(text=options_B[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    optioncbutton.config(text=options_C[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    optionDbutton.config(text=options_D[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    scorelabel.config(image=scoreimg[i+1])
        
                

                

            if value not in answers:
                def closep():
                    root2.destroy()
                    root.destroy()
                def tryp():
                    root2.destroy()
                    Textarea.delete(1.0,END)

                    Textarea.insert(END,questions[0])

                    optionAbutton.config(text=options_A[0])
                    optionbbutton.config(text=options_B[0])
                    optioncbutton.config(text=options_C[0])
                    optionDbutton.config(text=options_D[0])

                    scorelabel.config(image=scoreimg[0])





                root2=Toplevel()
                root2.overrideredirect(True)
        
                root2.config(bg='black')
                root2.geometry('287x400+250+70')
                frame=Frame(root2,highlightbackground='blue',highlightthickness='5',height=500,width=400,bg='black')
                frame.pack()
                root2.title('You lose')

                imglabel=Label(frame,image=centerimg,bd=0)
                imglabel.pack(pady=30)

                loselabel=Label(frame,text='You lose',font=('arial',40,'bold'),bg='black',fg='white')
                loselabel.pack()

                tryagain=Button(frame,text='Try again',font=('arial',20,'bold'),bg='black',activeforeground='white',activebackground='black',fg='white',bd=0,command=tryp)
                tryagain.pack()

                close=Button(frame,text='close',font=('arial',20,'bold'),bg='black',activeforeground='white',activebackground='black',fg='white',bd=0,command=closep)
                close.pack()

                root2.mainloop()
                break




    
    

    leftframe=Frame(root,bg='black',padx=30,pady=15)
    leftframe.grid(row=0,column=0)

    topframe=Frame(leftframe,bg='black')
    topframe.grid()

    centerframe=Frame(leftframe,bg='black')
    centerframe.grid(row=1,column=0)

    bottomframe=Frame(leftframe,bg='black')
    bottomframe.grid(row=2,column=0)
    bottomframe.place()

    rightframe=Frame(root,bg='black',pady=25,padx=50)
    rightframe.grid(row=0,column=1)

    
    
    lifeline50button=Button(topframe,image=lifeline50img,bg='black',bd=0,activebackground='black',width=180,height=80,command=fifty_fifty)   
    lifeline50button.grid(row=0,column=0)

    
    DDbutton=Button(topframe,image=DDimg,bg='black',bd=0,activebackground='black',width=180,height=80,command=DD)   
    DDbutton.grid(row=0,column=1)

    
    flipTQbutton=Button(topframe,image=flipTQimg,bg='black',bd=0,activebackground='black',width=180,height=80,command=flip)   
    flipTQbutton.grid(row=0,column=2)

    
    centerlabel=Label(centerframe,image=centerimg,bg='black',width=300,height=200)
    centerlabel.grid(row=0,column=0)


    scoreimg=[scoreimg0,scoreimg1,scoreimg2,scoreimg3,scoreimg4,scoreimg5,scoreimg6,scoreimg7,scoreimg8,scoreimg9,scoreimg10,scoreimg11,scoreimg12,scoreimg13,scoreimg14,scoreimg15]




    scorelabel=Label(rightframe,image=scoreimg[0],bg='black')
    scorelabel.grid(row=0,column=0)
            

    
    laylabel=Label(bottomframe,image=layout,bg='black')
    laylabel.grid(row=0,column=0)

    Textarea=Text(bottomframe,wrap='word',cursor='arrow',font=('arial',18,'bold'),width=42,height=2,fg='white',bd=0,bg='black',state='normal')
    Textarea.place(x=75,y=15)
    Textarea.bind("<Key>", lambda e: "break")
    Textarea.insert(END,questions[0])

    optionlabelA=Label(bottomframe,text='A:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabelA.place(x=60,y=110+20)

    optionAbutton=Button(bottomframe,text=options_A[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2')
    optionAbutton.place(x=100,y=100+20)

    optionlabelB=Label(bottomframe,text='B:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabelB.place(x=380,y=110+20)

    optionbbutton=Button(bottomframe,text=options_B[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2')
    optionbbutton.place(x=370+40,y=100+20)

    optionlabelc=Label(bottomframe,text='C:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabelc.place(x=60,y=230)

    optioncbutton=Button(bottomframe,text=options_C[0],activebackground='black',font=('arial',18,'bold'),fg='white',bg='black',bd=0,activeforeground='white',cursor='hand2',anchor='sw')
    optioncbutton.place(x=90,y=220-5)

    optionlabeld=Label(bottomframe,text='D:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabeld.place(x=330+50,y=190+40)

    optionDbutton=Button(bottomframe,text=options_D[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2',anchor='sw')
    optionDbutton.place(x=370+40,y=180+35)  


    optionAbutton.bind('<Button-1>',select)
    optionbbutton.bind('<Button-1>',select)
    optioncbutton.bind('<Button-1>',select)
    optionDbutton.bind('<Button-1>',select)
    lifeline50button.bind('<Button-1>',fifty_fifty)
    
def work3():
    questions=questions_Teen
    options_A=options_A_Teen
    options_B=options_B_Teen
    options_C=options_C_Teen
    options_D=options_D_Teen
    answers=answers_Teen
    global click
    click=True
    kidbutton.destroy()
    def fifty_fifty():
        flag=1
        quest_find=Textarea.get(1.0, "end-1c")
        quest_index=questions.index(quest_find)

        anscopy=answers
        OA=options_A
        OB=options_B
        OC=options_C
        OD=options_D
        tr=''
        if anscopy[quest_index]==OA[quest_index]:
            tr=1
        elif anscopy[quest_index]==OB[quest_index]:
            tr=2
        elif anscopy[quest_index]==OC[quest_index]:
            tr=3
        elif anscopy[quest_index]==OD[quest_index]:
            tr=4
        listr=[1,2,3,4]
        listr.remove(tr)
        for k in range(2):
            removeop=rd.choice(listr)
            listr.remove(removeop)
            if removeop==1:
                optionAbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
            elif removeop==2:
                optionbbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
            elif removeop==3:
                optioncbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
            elif removeop==4:
                optionDbutton.config(text='',command=0,highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white')
        lifeline50button.config(command=0,relief='sunken',image=lifeline50button_crossimg)
    def flip():
        flipTQbutton.config(command=0,relief='sunken',image=flipTQbutton_crossimg)
    def DD():
        DDbutton.config(command=0,relief='sunken',image=DDbutton_crossimg)

    def select(event):
        b=event.widget
        value=b['text']
        value2=b['image']
        f=1
        flag=0

        for i in range(15):

            if value==answers[i]:
                
                if answers[i]==answers[14]:
                    def dis():
                        root.destroy()
                    
                    Textarea.delete(1.0,END)
                    optionAbutton.config(text='')
                    optionbbutton.config(text='')
                    optioncbutton.config(text='')
                    optionDbutton.config(text='')
                    

                    root3=Toplevel()
                    root3.overrideredirect(True)
                    root3.config(bg='black')
                    root3.geometry('1000x300+140+200')
                    root3.title('You WON')

                    congolabel=Label(root3,image=imgcongo,height=200,bg='black')
                    congolabel.pack()
                    
                    dis=Button(root3,text='ENTER',font=('arial',20,'bold'),bg='black',activeforeground='white',activebackground='black',fg='white',bd=0,command=dis)
                    dis.place(x=600-150,y=250)
                    
                else:
                    Textarea.delete(1.0,END)
                    Textarea.insert(END,questions[i+1])
                    
                    
                    optionAbutton.config(text=options_A[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    optionbbutton.config(text=options_B[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    optioncbutton.config(text=options_C[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    optionDbutton.config(text=options_D[i+1],highlightbackground='white',activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',state=NORMAL)
                    scorelabel.config(image=scoreimg[i+1])
        
                

                

            if value not in answers:
                def closep():
                    root2.destroy()
                    root.destroy()
                def tryp():
                    root2.destroy()
                    Textarea.delete(1.0,END)

                    Textarea.insert(END,questions[0])

                    optionAbutton.config(text=options_A[0])
                    optionbbutton.config(text=options_B[0])
                    optioncbutton.config(text=options_C[0])
                    optionDbutton.config(text=options_D[0])

                    scorelabel.config(image=scoreimg[0])





                root2=Toplevel()
                root2.overrideredirect(True)
        
                root2.config(bg='black')
                root2.geometry('287x400+250+70')
                frame=Frame(root2,highlightbackground='blue',highlightthickness='5',height=500,width=400,bg='black')
                frame.pack()
                root2.title('You lose')

                imglabel=Label(frame,image=centerimg,bd=0)
                imglabel.pack(pady=30)

                loselabel=Label(frame,text='You lose',font=('arial',40,'bold'),bg='black',fg='white')
                loselabel.pack()

                tryagain=Button(frame,text='Try again',font=('arial',20,'bold'),bg='black',activeforeground='white',activebackground='black',fg='white',bd=0,command=tryp)
                tryagain.pack()

                close=Button(frame,text='close',font=('arial',20,'bold'),bg='black',activeforeground='white',activebackground='black',fg='white',bd=0,command=closep)
                close.pack()

                root2.mainloop()
                break




    
    

    leftframe=Frame(root,bg='black',padx=30,pady=15)
    leftframe.grid(row=0,column=0)

    topframe=Frame(leftframe,bg='black')
    topframe.grid()

    centerframe=Frame(leftframe,bg='black')
    centerframe.grid(row=1,column=0)

    bottomframe=Frame(leftframe,bg='black')
    bottomframe.grid(row=2,column=0)
    bottomframe.place()

    rightframe=Frame(root,bg='black',pady=25,padx=50)
    rightframe.grid(row=0,column=1)

    
    
    lifeline50button=Button(topframe,image=lifeline50img,bg='black',bd=0,activebackground='black',width=180,height=80,command=fifty_fifty)   
    lifeline50button.grid(row=0,column=0)

    
    DDbutton=Button(topframe,image=DDimg,bg='black',bd=0,activebackground='black',width=180,height=80,command=DD)   
    DDbutton.grid(row=0,column=1)

    
    flipTQbutton=Button(topframe,image=flipTQimg,bg='black',bd=0,activebackground='black',width=180,height=80,command=flip)   
    flipTQbutton.grid(row=0,column=2)
    
    centerlabel=Label(centerframe,image=centerimg,bg='black',width=300,height=200)
    centerlabel.grid(row=0,column=0)


    scoreimg=[scoreimg0,scoreimg1,scoreimg2,scoreimg3,scoreimg4,scoreimg5,scoreimg6,scoreimg7,scoreimg8,scoreimg9,scoreimg10,scoreimg11,scoreimg12,scoreimg13,scoreimg14,scoreimg15]




    scorelabel=Label(rightframe,image=scoreimg[0],bg='black')
    scorelabel.grid(row=0,column=0)
            

    
    laylabel=Label(bottomframe,image=layout,bg='black')
    laylabel.grid(row=0,column=0)

    Textarea=Text(bottomframe,wrap='word',cursor='arrow',font=('arial',18,'bold'),width=42,height=2,fg='white',bd=0,bg='black',state='normal')
    Textarea.place(x=75,y=15)
    Textarea.bind("<Key>", lambda e: "break")
    Textarea.insert(END,questions[0])

    optionlabelA=Label(bottomframe,text='A:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabelA.place(x=60,y=110+20)

    optionAbutton=Button(bottomframe,text=options_A[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2')
    optionAbutton.place(x=100,y=100+20)

    optionlabelB=Label(bottomframe,text='B:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabelB.place(x=380,y=110+20)

    optionbbutton=Button(bottomframe,text=options_B[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2')
    optionbbutton.place(x=370+40,y=100+20)

    optionlabelc=Label(bottomframe,text='C:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabelc.place(x=60,y=230)

    optioncbutton=Button(bottomframe,text=options_C[0],activebackground='black',font=('arial',18,'bold'),fg='white',bg='black',bd=0,activeforeground='white',cursor='hand2',anchor='sw')
    optioncbutton.place(x=90,y=220-5)

    optionlabeld=Label(bottomframe,text='D:',font=('arial',18,'bold'),bg='black',fg='white',bd=0)
    optionlabeld.place(x=330+50,y=190+40)

    optionDbutton=Button(bottomframe,text=options_D[0],activebackground='black',font=('arial',18,'bold'),bg='black',fg='white',bd=0,activeforeground='white',cursor='hand2',anchor='sw')
    optionDbutton.place(x=370+40,y=180+35)  


    optionAbutton.bind('<Button-1>',select)
    optionbbutton.bind('<Button-1>',select)
    optioncbutton.bind('<Button-1>',select)
    optionDbutton.bind('<Button-1>',select)
    lifeline50button.bind('<Button-1>',fifty_fifty)

      

click=False
root.geometry('1270x652+0+0')
root.title('KBC')

kidbutton=Button(root,text='KID',activebackground='blue',font=('arial',18,'bold'),bg='blue',fg='white',bd=0,activeforeground='white',cursor='hand2',command=work)
kidbutton.place(x=200,y=330)

adultbutton=Button(root,text='ADULT',activebackground='blue',font=('arial',18,'bold'),bg='blue',fg='white',bd=0,activeforeground='white',cursor='hand2',command=work2)
adultbutton.place(x=1000,y=330)
teenbutton=Button(root,text='TEEN',activebackground='blue',font=('arial',18,'bold'),bg='blue',fg='white',bd=0,activeforeground='white',cursor='hand2',command=work3)
teenbutton.place(x=600,y=330)



    



root.mainloop()
t.sleep(5)
