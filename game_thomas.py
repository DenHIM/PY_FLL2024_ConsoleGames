my_cloths = 'ragged robes'
my_armor = 'no armor'
my_money = 'no money'
my_weapons = 'none'

end1 = "you get your head chopped off"
end2 = "you go home with nothing you your spouse and four kids starve"
print ("you find yourself in an old abandoned sawmill")
print ("all you smell is sawdust and rusting metal")
print ("you see a movement in the eerie shadows of the sawmill")
print ("you have no armor or no money so you either go home, go towards the movement or look for food")

ch1 = input ("which option (123)")
if ch1 == "1":
    print ("you go home with no food, you your spouse and 4 kids starve (death)")
if ch1 == "2":
    print ("you go towards the movement soon you see it is your best friend")
    print ("you say hi but he falls to the ground then you see there is a meat hook through his heart")
    print ("after seeing your friend die you can scream in horror, or ignore it (4,5)")
if ch1 == "3":
    print ("you turn and start walking... a saw falls on your head (death)")
ch1 = input("do you choose option 4 or 5")
if ch1 == "4":
    print ("your screaming attracted some rabid raccons (death)")
if ch1 == "5":

    print ("you step over the body and keep walking then you realize it is not just a sawmill it is also a slaughterhouse")
    print ("you see a conveyer where the cows died so you can walk past it, press the ON button or get in it (6,7,8)")
    ch1 = input("which one do you choose")
if ch1 == "6":
    print ("you walk past the conveyer... you are attacked by killer hornets (death)")
if ch1 == "7":
    print ("you press ON the machine whirrs then stops then the whole building explodes(death)")
if ch1 == "8":
    print ("you start crawling in the conveyer, then you fall.")
    print ("next thing you know you are climbing out of a manhole on to street level (WINNER!!?!!)")