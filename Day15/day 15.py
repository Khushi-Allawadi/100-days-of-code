exit = "no"
while exit == "no":
  sound = input("What animal sound do you want to hear?")
  if sound == "cow":
    print("A cow goes moo.")
  elif sound == "pig":
    print("A pig goes oink.")
  elif sound == "duck":
    print("A duck goes quack.")
  else:
    print("I don't know that animal sound.")
    exit = input("Do you want to exit?")
      
  
