import random
knife = 11
box = 15
ca = 7
rando = (random.randrange(3,6))
blue = (random.randrange(0,5))
hp = 20


zadamage = [3,4,5,6]
zareturn = [1,2,3,4]





def he():
   print ("You can only buy an apple now, which heals 3 hp. Do you want to buy it?")
   option = input()
   if option == "YES":
    print ("That will be 7 gold coins, do you want to buy it?: YES or NO")  
    option = input ()
    if option == "YES":
      print (f"You have got an ....apple? and now have {co- ca} gold coins")
      print ("Do you want to continue searching?: YES or NO")
      return co - ca
  


def apple():
   print ("You can only buy an apple now, which heals 3 hp. Do you want to buy it?")
   option = input()
   if option == "YES":
    print ("That will be 7 gold coins, do you want to buy it?: YES or NO")  
    option = input ()
    if option == "YES":
      print (f"You have got an apple and now have {co- ca} gold coins")
      print ("Do you want to continue searching?: YES or NO")
      return co - ca
   
def cowfight():
   if rando == 3:
        print ("You punch Blugorhorn on his horn damaging him and removing 3 hp, it wasn't very effective")
        print (f"Blugorhorn now has {blugorhorn - 3} hp")
        
   elif rando == 4:
        print ("You punch Blugorhorn in the stomach damaging him and removing 4 hp, it was an okay attack")    
        print (f"Blugorhorn now has {blugorhorn - 4} hp")
        return blugorhorn - 4
   elif rando == 5:
        print ("You kick Blugorhorn in the stomach damaging him and removing 5 hp, it was an effective attack") 
        print (f"Blugorhorn now has {blugorhorn - 5} hp") 
        return blugorhorn - 5
   elif rando == 6:
        print ("You kick Blugorhorn in the neck damaging him and removing 6 hp, it was a very effective attack")  
        print (f"Blugorhorn now has {blugorhorn - 6} hp")  
        return blugorhorn - 6  

def cowfightback():
   print ("Blugorhorn prepares to fight back")
   if blue == 1:
      print ("Blugorhorn UDDERS a curse, you trip and fall, but not to hard")
      print (f"You now have {hp - 1} hp")
   elif blue == 2:
      print ("Bluegorhorn spits in your eye, a painful nussance")
      print (f"You now have {hp - 2} hp")
   elif blue == 3:
      print ("Blugorhorn charges at you and boops you with her snout, hard enough for yuo to fall over")
      print (f"You now have {hp - 3} hp")
   elif blue == 4:
      print ("Blugorhorn charges at you and kicks you, you trip")
      print (f"You now have{hp - 4} hp")
   elif blue == 0:
      print ("Blugorhorn charges at you, but she trips and misses you")
      print ("You are unharmed")
   elif blue == 5:
      print ("Blugorhorn kicks dust to you, but it gets into her eyes instead")
      print ("You are unharmed")


def underling(co):
 print ("That will be 11 gold coins, do you want to buy it?: YES or NO")  
 option = input ()
 if option == "YES":
  print (f"You have got a plastic knife and you now have {co - knife } gold coins")
  print ("Do you want to continue searching?: YES or NO")
  return co - knife

def nonono():
   print ("What do you want to buy: an apple, heals 3 hp or a cardboard box, def +4")
   whatever = input()
   if whatever == "a cardboard box":
    print ("That will be 15 gold coins, do you want to buy it?: YES or NO")
    okay = input()
    if okay == "YES":
          print (f"You have got a cardboard box and you now have {co - box} gold coins")
          print ("Do you want to continue searching?: YES or NO")
          return co - box
      

def under(co):
 print ("That will be 15 gold coins, do you want to buy it?: YES or NO")  
 option = input ()
 if option == "YES":
  print (f"You have got a cardboard box and you now have {co - box  } gold coins")
  print ("Do you want to continue searching?: YES or NO")
  return co - box

def yesyes():
   print ("What do you want to buy: an apple, heals 3 hp or a plastic knife, +3 attack ")
   whatever = input()
   if whatever == "a plastic knife":
    print ("That will be 11 gold coins, do you want to buy it?: YES or NO")
    okay = input()
    if okay == "YES":
          print (f"You have got a cardboard box and you now have {co - knife} gold coins")
          print ("Do you want to continue searching?: YES or NO")
          return co - knife

def repeat(co):
    print ("That will be 7 gold coins, do you want to buy it?: YES or NO")
    option = input ()
    if option == "YES":
     print (f"You have got an apple and you now have {co - ca} gold coins")
     print ("Do you want to continue searching?: YES or NO")
     return co - ca 
     
    

def bored():
     print ("What do you want to buy: an apple, heals 3 hp, a plastic knife, +3 attack, a cardboard box, def +4")
     whatever = input()
     if whatever == "an apple":
      print ("That will be 7 gold coins, do you want to buy it?: YES or NO")
      okay = input()
      if okay == "YES":
       print (f"You have got an apple and you now have {co- ca} gold coins")
       print ("Do you want to continue searching?: YES or NO")
       return co - ca
      
def bore():
     print ("What do you want to buy: an apple, heals 3 hp, a plastic knife, +3 attack, a cardboard box, def +4")
     whatever = input()
     if whatever == "an apple":
      print ("That will be 7 gold coins, do you want to buy it?: YES or NO")
      okay = input()
      if okay == "YES":
       print (f"You have got an......apple?. Now you have {co- ca} gold coins")
       print ("Do you want to continue searching?: YES or NO")
       return co - ca



def oshoot():
    print("oh, you're in dept, yet you still want an apple for completey free. OH NO NO NO. Things don't work like this here")
    print("ARE YOU TRYING TO STEAL FROM ME!!!,: tip: type in all caps and you may not die")
    life = input()
    if life == ("YES"):
     print("OH so you are trying to steal from me. You have humored me.")
     print ("I gave you a plastic apple for trying to steal from me") 
     print ("well I will let you go for now< but if you show your face here again... well, you will what will happen")
     print ("")
     print ("YOU ARE NO LONGER ABBLE TO VISIT GANGORE'S SHOP, however someone may have an interest with your plastic apple somewhere")
    else:
       print ("SO YOU PICKED TO BE A COWARD, I HATE PEOPLE LIKE YOU")
       print (" you know, instead of killing you, I want you to help me with something")
       print ("I have wanted to add something to my shop for a very long time, and I also want to make an example to others, you will do quite nicely")
       print (" What I want to sell is ....... YOuR BOdy")
       print (".....")
       print (".....")
       print ("HELLO we are selling a new item... a hanged body, do you want to buy it?")
       print ("GREAT it will be delivered to your doorstep for 30 gold, have a very nice day")
       print ("")
       print ("")
       print("Blood ouzzes from a peircing from the man's stomach, a hook is through the man's body, driven through his heart. What a LOVELY piece of decoration")
       print("HANGEDMAN ENDIND")
       print (" tip; try not to annoy Mr. Gangore")
       print ("")

    

co = 40
blugorhorn = 3
tin = 4


print("""There is a dark tower that looms in front of you, the doors open to greet you.You may get wealth from the tower.Do you enter: YES or NO""")
enter = input ()

if enter== "YES":
    print ("You enter the tower.It isn't too dark in the tower, but there is a torch nearby.Do you want to use the torch: YES or NO")
    light = input ()
    if light == "YES":
        print ("You light the torch, somehow, and find 3 doors (the one that got illuminated by the torch is 3.) Do you enter door number 1, 2, or 3 ")
        inside = input ()

        if inside == "3":
         print ('You find a shop for goods."You only have 4 tin coins, lemme give you 40 GOLD coins."')
         print ('What do you want to buy: an apple, heals 3 hp, a plastic knife, +3 attack, a cardboard box, def +4,')
         whatever = input()

         if whatever == "an apple":
              repeat(40)
              co = co - ca
              sigh = input()
              if sigh =="YES":
               bored()
               co = co - ca
               sigh = input()
               if sigh =="YES":
                bored()
                co = co - ca
                sigh = input()
                if sigh =="YES":
                 bored()
                 co = co - ca
                 sigh = input()
                 if sigh =="YES":
                  bored()
                  co = co - ca
                  sigh = input()
                  if sigh =="YES":
                   bored()
                   co = co - ca
                   sigh = input()
                   if sigh =="YES":
                    bore()
                    co = co - ca
                    sigh = input()
                    if sigh =="YES":
                     oshoot()
                     print ("")
                     print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
                                  
                         
                         
                         
                          
         elif whatever == "a plastic knife":
            underling(40)
            co = co - knife
            option = input()
            if option == "YES":
             nonono()
             co = co - box
             option = input()
             if option == "YES":
              apple()
              co = co - ca
              option = input()
              if option == "YES":
               apple()
               co = co - ca
               option = input()
               if option == "YES":
                apple()
                option = input()
                if option == "YES":
                 he()
                 co = co - ca
                 sigh = input()
                 if sigh == "YES":
                  oshoot()
             
             
               



             
            
            
            
                
         else:
          under(40)
          co = co - box
          option = input()
          if option == "YES":
           yesyes()
           co = co - box
           option = input()
           if option == "YES":
            apple()
            co = co - ca
            option = input()
            if option == "YES":
             apple()
             co = co - ca
             option = input()
             if option == "YES":
              apple()
              option = input()
              if option == "YES":
               he()
               co = co - ca
               sigh = input()
               if sigh == "YES":
                oshoot()
        
        elif inside == "2":
            print ("You encouter a blugorhorn amd engage in combat")
            print ("what do you do: ATTACK, DEFEND, ITEM, OTHER")
            option = input()
            if option == "ATTACK":   
                print ("You prepare to fight this cow")
                cowfight()
                cowfightback()
                print ("Blugorhorn has fallen and vanished in a wisp of smoke")
                print ("You got 5XP and 4 gold coins")
                print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
            elif option == "OTHER":
              print ("MILK, RUN AWAY")
              qwerty = input()
              if qwerty == "MILK":
                print ("You milk blugorhorn, and it runs away")
                print ("You got 5XP and 4 gold coins")
                print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
              elif qwerty == "RUN AWAY":
                print ("YOU run away unscathed. You were lucky, other monsters would have tried to stop you")
                print ("You got 0XP and no gold coins")
                print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
        
        elif inside == "1":
            print ("You encouter a blugorhorn amd engage in combat")
            print ("what do you do: ATTACK, DEFEND, ITEM, OTHER")
            option = input()
            if option == "ATTACK":   
                print ("You prepare to fight this cow")
                cowfight()
                cowfightback()
                print ("Blugorhorn has fallen and vanished in a wisp of smoke")
                print ("You got 5XP and 4 gold coins")
                print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
            elif option == "OTHER":
              print ("MILK, RUN AWAY")
              qwerty = input()
              if qwerty == "MILK":
                print ("You milk blugorhorn, and it runs away")
                print ("You got 5XP and 4 gold coins")
                print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
              elif qwerty == "RUN AWAY":
                print ("YOU run away unscathed. You were lucky, other monsters would have tried to stop you")
                print ("You got 0XP and no gold coins")
                print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
        


    else:
       print ("You leave the torch alone. There are 2 doors. Do you enter door number 1 or 2")   
       inside = input ()
       if inside == "2":
           print ("You encouter a blugorhorn amd engage in combat")
           print ("what do you do: ATTACK, DEFEND, ITEM, OTHER")
           option = input()
           if option == "ATTACK":   
             print ("You prepare to fight this cow")  
             cowfight()
             cowfightback()
             print ("Blugorhorn has fallen and vanished in a wisp of smoke")
             print ("You got 5XP and 4 gold coins")
             print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
           elif option == "OTHER":
              print ("MILK, RUN AWAY")
              qwerty = input()
              if qwerty == "MILK":
                print ("You milk blugorhorn, and it runs away")
                print ("You got 5XP and 4 tin coins")
                print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
              elif qwerty == "RUN AWAY":
                print ("YOU run away unscathed. You were lucky, other monsters would have tried to stop you")
                print ("You got 0XP and no gold coins")
                print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")

       elif inside == "1":
            print ("You encouter a blugorhorn amd engage in combat")
            print ("what do you do: ATTACK, DEFEND, ITEM, OTHER")
            option = input()
            if option == "ATTACK":   
                print ("You prepare to fight this cow")
                cowfight()
                cowfightback()
                print ("Blugorhorn has fallen and vanished in a wisp of smoke")
                print ("You got 5XP and 4 tin coins")
                print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
            elif option == "OTHER":
              print ("MILK, RUN AWAY")
              qwerty = input()
              if qwerty == "MILK":
                print ("You milk blugorhorn, and it runs away")
                print ("You got 5XP and 4 tin coins")
                print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
              elif qwerty == "RUN AWAY":
                print ("YOU run away unscathed. You were lucky, other monsters would have tried to stop you")
                print ("You got 0XP and no gold coins")
                print ("THAANK YOU FOR PLAYING MY DEMO, THE FULL GAME IS COMING OUT SOON FOR JUST 24$. THAK YOU")
        
      
           

    
elif enter== "NO":
    print ("You go home to your family. Since you don't have any money to buy food, you and your family starve..........Lazy Ending")

else:
    print("You stay there standing in the open. A meteorite hits your head......... YOU DIED") 
