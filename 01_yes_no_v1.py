# Ask the User if they have played before
show_instructions = input("have you played this game before?").lower()


# If they say yes, output 'program continues'
if show_instructions == "yes":
  print ("program continues")

elif show_instructions == "no":
  print("show instructions")

elif show_instructions == "y":
  print ("")

  # If they say no, output ('display instructions')
else:
  print ("display instructions")
  print("please answer yes / no")    