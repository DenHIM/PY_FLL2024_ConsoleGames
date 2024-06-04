import random
import time
import sys
wooden_stick= '0'
egg = '0'
room= '1'
lighter = '0'
fire_stick= '0'
glass = '0'
rope = '0'
pillow = '0'
punching_bag = '0'
hammer = '0'
long_stick = '0'
key3= '0'
brick = '0'
bread= '0'
short_stick = '0'
broom = '0'
spider = '0'
dragon = '0'
sit1 = '0'
spidey = '0'
discovery = '0'
conversation = '0'
fate = '0'
life= 6
print('''
      
      
      Excape The Cow Prison 🤔 1st
      
      
      ''')
sleep=time.sleep
sleep(3)
print('''You are traped in a sell with 6 health points, a wooden door with a small lock (101) and with a painting on it (201).
An egg sits on the table(301). On the bed is a wooden stick (501) and there might be something under the bed (401).''')
while room == '1':
 if life < 1:
   print('''


🧨You did not survive🧨


''')
   sys.exit()
 pick = input('''
             
action: ''')

 if pick == '101':
    print('There is no way you could open that door without the right key.')
 elif pick == '201' and fire_stick == '1':
    print('Do you want to burn the painting (801) or not (901)')
 elif pick == '201':
    print('The painting does not seem to have a wooden back - Strange')
 elif pick == '301':
    print('You take the egg. It is realy warm (15).')
    egg = '1'
 elif pick == '401':
    print('Do you want to reach under (601)? Otherwise answer (701)')
 elif pick == '501':
    print('The stick is very dry, it must have bean here for a long time. You take the stick (10)')
    wooden_stick = '1'
 elif pick == '601':
    print('You stick your hand under the bed. Your hand wraps around a lighter (11).')
    lighter = '1'
 elif pick == '1011' and wooden_stick == '1' and lighter == '1':
    print('You light the stick and get a flaming stick. You do not have the lighter any more')
    fire_stick = '1'
 elif pick == '701':
    print('')
 elif pick == '801' and fire_stick == '1':
    print('You burn the painting and in the end the stick goes out of flame. Now you climb through.')
    room = '2'
 elif pick == '901':
    print('')
 else:
    print('You can not do that.')
print('''
      

      
In the next room there is a window (102). A door stands with no locks or windows (302) and a sign with something carved on it was placed right beside it (202).
A rope lays on the ground (402). There is a cilinder shaped pillow leaning against the wall (502). You do not have the flaming stick any more.
The painting grew back as soon as you came through.''')
while room == '2':
 if life < 1:
   print('''


🧨You did not survive🧨


''')
   sys.exit()
 pick = input('''
             
action: ''')
 if pick == '102':
   print('The window is to small to fit through. A piece of the glass looks loose. You pull gently and now have a piece of glass. It might be useful.')
   glass = '1'
 elif pick == '202':
   print('The sign says,"EGNUOL WOC With a mirror" - Strange')
 elif pick == '302':
   print('Do you want to open the door and look inside (602)? Otherwise (702).')
 elif pick == '402':
   print('You pick up the rope (45).')
   rope = '1'
 elif pick == '502':
   print('The pillow seems very strong. It has a hook at the end of it (24)')
   pillow = '1'
 elif pick == '602' and punching_bag == '1':
   print('You open the door and see cows wearing armor. You where prepared. The gaurds flea.')
   room = '3'
 elif pick == '602':
   print('You open the door and see cows wearing armor. But you did not expect this. You loose 4 health points.')
   life = life - 4 
   room = '3'
 elif pick == '702':
   print('')
 elif pick == '2445' and pillow == '1' and rope == '1':
   print('You attach the pillow to the rope and get a punching bag (13). You hang it up and punch it one hundred times and pack it up.')
   punching_bag = '1'
 else:
   print('You can not do that.')
print('''



The door locks as you go through. You are in a room with a long table (603) and 10 tall run down chairs (103). There is a couch in the back of the room (303).
A door with a lock stands to your left (203).Some hay is in the back crorner (503). There is a loose brick (403) in the wall and a short stick below it (703).
A spider web is in the far top corner of the room (803).
''')
while room == '3':
  if life < 1:
   print('''


🧨You did not survive🧨


''')
   sys.exit()
  if life > 6:
    life = 6
  pick = input('''

action: ''')

  if pick == '103' and hammer == '1':
    print('You swing the hammer at the chair and get a long stick (72) from one of the chair legs.')
    long_stick = '1'
  elif pick == '103':
    print('Nice Try - There is no time to sit and eat.')
  elif pick == '203' and key3 == '1':
    print('Do you want to unlock the door and step inside (903). Otherwise (113)')
  elif pick == '203':
    print('The door is locked.')
  elif pick == '303' and life < 6:
    print('Do you sit down (213). Otherwise (113).')
  elif pick == '303':
    print('Nice Try - There is not time to sit and rest.')
  elif pick == '403':
    print('You take the brick (16) out of the wall.')
    brick = '1'
  elif pick == '503':
    print('You take the hay (20).')
    hay = '1'
  elif pick == '603' and life > 5:
    print('You do not need any food')
  elif pick == '603':
    print('You take a lofe of bread (14)')
    bread = '1'
  elif pick == '703':
    print('You pick up the short stick (17)')
    short_stick = '1'
  elif pick == '803' and broom == '1':
    print('You use the broom to clean away the webs. You find a key (21).')
    key3 = '1'
  elif pick == '803':
    print('Do you want to reach in (313). Otherwise (113)')
  elif pick == '903' and key3 == '1':
    room = '4'
  elif pick == '113':
    print('')
  elif pick == '213' and life < 6 and sit1 == '0':
    print('You sit down and rest. You get one health point.')
    life = life + 1
    sit1 = '1'
  elif pick == '313':
    print('''You reach into the spider web. A spider jumps onto your arm and bites. Now you have a spider bite (59). Every time you loose
health points, you loose one extra health point. If you make the correct combonation, you might be able to heal it. You loose 2 health points''')
    life = life - 2
    spider = '1'
  elif pick == '1617' and short_stick == '1' and brick == '1':
    print('You stick the stick into a hole in the brick. You have a hammer (80)')
    hammer = '1'
  elif pick == '1520' and egg == '1' and hay == '1':
    print('You build a nest for the egg')
    time.sleep(1)
    print('You spot a crack')
    time.sleep(1)
    print('More cracks apear.')
    time.sleep(1)
    print('A wall of the egg falls off to reveal an eye.')
    time.sleep(1)
    print("The walls fall off and a red dragon (18) now stands in the nest. You have some hay still left. The dragon eats his's egg shell.")
    dragon = '1'
    egg = '0'
    hay = '1'
  elif pick == '80' and hammer == '1':
    print('Do you want to wack yourself with the hammer(412) Otherwise (113)')
  elif pick == '412' and hammer == '1' and spider == '1':
    print('You hit yourself with the hammer. You loose 5 lives')
    life = life - 5
  elif pick == '412' and hammer == '1':
    print(' You hit yourself with the hammer. You loose 4 lives')
    life = life - 4
  elif pick == '2072' and hay == '1' and long_stick == '1':
    print('You use the hay and stick to make a broom.')
    broom = '1'
  elif pick == '1859' and dragon == '1' and spider == '1':
    print('The dragon heals the bite magicaly.')
    spider = '0'
  elif pick == '14' and bread == '1':
    print('You eat the bread. You get 2 health points')
    life = life + 2
    bread = '0'
  else:
    print('You can not do that.')
if spider == '1':
  damage = '2 health points.'
  life = life - 2
else:
  damage = '1 health point.'
  life = life - 1
print('''



You enter a room with a large door. You get hit by an arrow. You loose''', damage,'''A cow head stands (104) but you umeadetly look away.
''')
while room == '4':
  if life < 1:
    print('''


🧨You did not survive🧨


''')
    sys.exit()
  if life > 6:
    life = 6
  pick = input('''

action: ''')
  if pick == '104':
    print('Do you want to touch it (204) Otherwise (304)')
  elif pick == '204':
    print('You put your hand on it and the jaw moves when you push it up and down. Do you want to play with it (404) Otherwise (304)')
    discovery = '1'
  elif pick == '304':
    print('The head shoots an arrow at you. You loose', damage,'')
    if spider == '1':
      life = life - 2
    else:
      life = life -1
  elif pick == '404' and discovery == '1':
    print('Do you want to make it say "I will kill you"(504),"I will open the door"(604),"Help"(704), or nothing at all(304)')
    conversation = '1'
  elif pick == '504' and conversation == '1':
    print('You move the mouth in a way that mouths "I will kill you". And just like that you die.')
    life = life - 6
  elif pick == '14' and bread == '1':
    print('You eat the bread. You get 2 health points')
    life = life + 2
    bread = '0'
  elif pick == '604' and conversation == '1':
    print('You move the mouth in a way that mouths "I will open the door". And just like that the door opens. You get through just in time before the door shuts')
    break
  elif pick == '704' and conversation == '1':
    print(' You move the mouth in a way that mouths "Help". And just like that guards come running and they kill you.')
    life = life - 6
  else:
    print('You can not do that')
print('''You are outside the prison. But it is not over. There is a big pit that you can't go around.''')
if life < 1:
  print('''


🧨You did not survive🧨


''')
  sys.exit()
if life > 6:
  life = 6
if dragon == '1':
  time.sleep(3)
  print('Your dragon has grown up to be an adult. He flies you to the other side.')
  time.sleep(3)
  print('''


          🐄🐄🐄🐄🐄

🎉You Excaped The Cow Prison🎉

''')
elif dragon == '0':
  if spider == '1':
    fate = '2 lives.'
    if life < 1:
      print('''


🧨You did not survive🧨


''')
      sys.exit()
  if spider == '0':
    fate = '1 life.'
    if life < 1:
      print('''


🧨You did not survive🧨


''')
      sys.exit()
  time.sleep(3)
  print('''
        
        
You spot a rope on the other side of the pit. You jump down and loose''', fate,'''Then you climb the rope out on the other side''')
  time.sleep(3)
  print('''


          🐄🐄🐄🐄🐄

🎉You Excaped The Cow Prison🎉

''')