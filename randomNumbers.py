##################################################################
# Author: Shea McNeely
# Date: 2/19/2024
# Program Name: RandomNumbers.py
# Description: A microservice to generate 6 random numbers open request.
##################################################################

import random
import time

ran = [-1, -1, -1, -1, -1, -1]

def checkForDuplicates(temp, ran):
    for j in range(6):
        while temp == ran[j]:
            temp = random.randrange(0, 1025)
            checkForDuplicates(temp, ran)
    return temp

while True:
    StartFile = open("run.txt", 'r', encoding="utf-8")  # change 'run.txt' with other file name to change
    temp = ""

    while temp != "run":  # change "run" to whatever command you want to start the service. Must be encoded in utf-8 (plain text)
        time.sleep(.25)  # this can be removed if desired. In theory just keeps the thread from being clogged with while loop
        temp = StartFile.read()

    StartFile.close()
    StartFile = open('run.txt', 'w').close()  # change 'run.txt' with other file name to change

    print("Opening output file...")
    OutFile = open('outputfile.txt', 'w', encoding="utf-8")  # change 'OutputFile.txt' with other file name to change
    print("Opened output file successfully")


    print("Writing Random Numbers to output file...")
    for i in range(6):
        temp2 = random.randint(0, 1025)  # change end value to # of possible pokemon. Inclusive
        temp2 = checkForDuplicates(temp2, ran)
        ran[i] = temp2
        OutFile.write(str(ran[i])+" ")
    print("Random numbers written successfully")

    print("Closing output file...")
    OutFile.close()
    print("Output file closed successfully")

