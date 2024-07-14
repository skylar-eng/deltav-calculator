#!/usr/bin/env python

###############################################################################
# Delta-V Calculator - calculate change in velocity for a single stage rocket.
# You can use any units you'd like, as long as you are consistent.
# Copyright(C) 2024 Skylar Grace, under the terms of the 3-clause BSD license.
###############################################################################

import math

ProgramName = "Delta-V Calculator"
FillerSpace = "###############################################################################"
CopyrightMessage = "Copyright(C) 2024 Skylar Grace. Under the terms of the BSD 3-clause license."

def PrintInitMessages(): # This function only serves to print my intial messages on screen.
  print(FillerSpace)
  print(ProgramName)
  print(CopyrightMessage)
  print(FillerSpace)

def ComputeDeltaV(): # This is the main function that contains all of the calculator code, and file operation code.
  try:
    NetMass = float(input("\nWhat is the full net mass of your vehicle: ")) # Ask the user some information about their vehicle, starting with net mass
    DryMass = float(input("What is the dry mass of your vehicle: ")) # then dry mass
    Impulse = float(input("What is the specific impulse of your engines: ")) # and finally specific impulse in Isp

    DeltaV = Impulse * float(9.8) * math.log(float(NetMass/DryMass)) # This runs the Delta V calculation on the inputs given to us by the user.
    print("Your total Delta-V is: ", DeltaV) # and this prints the output of that calcualtion

    YesNoQuestion = input("\nWould you like to continue(yes/no)?  ") # ask the user if they'd like to continue

    if YesNoQuestion.lower() == "yes": # if so we just restart the program from the ComputeDeltaV function
      ComputeDeltaV()

    elif YesNoQuestion.lower() == "no": # if not we write our data to an output file, inform the user of what we've done, and gracefully exit'
      UserFile = input("Please enter a name for your output file: ") # Ask the user what name they want for the output file
      file = open(UserFile, 'w') # Open a new file to store our calculator output.
      FileWriteOutput = ("Net Mass = ", str(NetMass), "\n", "Dry Mass = ", str(DryMass), "\n", "Specific Impulse = ", str(Impulse), "\n", "Total Delta-V = ", str(DeltaV), "\n") # Convert all output values into strings.
      FileWriteString = "".join(FileWriteOutput) # Join the strings together into one.
      file.write(FileWriteString) # Write that string into our file.
      print("The results of your last calculation have been saved to the text file", UserFile)
      print("Goodbye!")
      print(FillerSpace)
      exit()

  except ValueError: # Sometimes, users will try to enter garbage vaules into the program.
    print("You need to enter a number!") # so we tell them to enter an actual number instead.
    ComputeDeltaV()


PrintInitMessages()
ComputeDeltaV()
