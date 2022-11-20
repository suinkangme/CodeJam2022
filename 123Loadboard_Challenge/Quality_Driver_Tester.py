import random
import math

# Fix Data set
#Initial_Speed = [94, 94, 70, 58, 57, 97, 74, 76, 80, 86]    # Good driver data set
#Final_Speed = [77, 81, 86, 74, 77, 80, 79, 83, 86, 88]

#Initial_Speed = [100, 57, 87, 69, 93, 65, 95, 50, 57, 70]     # Dangerous driver data set
#Final_Speed = [81, 90, 76, 84, 77, 80, 77, 85, 90, 82] 

#Initial_Speed = [69, 109, 97, 66, 120, 120, 110, 114, 115, 109]   # Hard Breaking driver data set
#Final_Speed = [77, 77, 90, 74, 83, 83, 86, 87, 92, 88]

Initial_Speed = [100, 91, 82, 75, 67, 50, 46, 42, 80, 86]  # Drowsy driver data set
Final_Speed = [92, 84, 76, 69, 61, 48, 44, 40, 86, 88]

print(" ")
acc_sample = 5  # Sampling acceleration every 5 seconds
iteration = 0       
warning_time = 1
counter = 0
drowsy_counter = 0
lenght_array = len(Initial_Speed)
tempv_init = []
tempv_final = []

while iteration < lenght_array:   # Looping over the lenght of the array dataset
    current_acc = abs((Final_Speed[counter] - Initial_Speed[counter]) / acc_sample) # Calculating acceleration
    v_init = Initial_Speed[counter]
    v_final = Final_Speed[counter]
    counter = counter + 1   # Incrementing array index for each successful iteration
    
    if v_init > v_final and v_init - v_final <= 10: # Checking for gradual deceleration and if
        drowsy_counter = drowsy_counter + 1        # the delta between samples is at least of 5
        tempv_init.append(v_init)   # Storing initial speed value in array when above condition is true
        tempv_final.append(v_final) # Storing final speed value in array when above condition is true
       
    if current_acc < 5: # checking for safe acceleration/deceleration
        print("Initial: " + str(v_init) + " km/h" + " - " + "Final: " + str(v_final) + " km/h")
        print(str(current_acc) + " m/s^2\n") 
        int(current_acc)
        tempv_init.append(v_init)   # Storing initial speed value in array when above condition is true
        tempv_final.append(v_final) # Storing final speed value in array when above condition is true

    if current_acc > 5: # checking for big acceleration/deceleration
        if v_init < v_final: # checking if speed increases
            print("Initial: " + str(v_init) + " km/h" + " - " + "Final: " + str(v_final) + " km/h")
            print(str(current_acc) + " m/s^2" + " - " + "Warning" + " " + str(warning_time) + " !!!" + "\n" + "You are accelerating too much!" + "\n")
            int(current_acc)
            int(warning_time)
            tempv_init.append(v_init)   # Storing initial speed value in array when above condition is true
            tempv_final.append(v_final) # Storing final speed value in array when above condition is true
            warning_time += 1
        elif v_init > v_final: # checking if speed decreases
            print("Initial: " + str(v_init) + " km/h" + " - " + "Final: " + str(v_final) + " km/h")
            print(str(current_acc) + " m/s^2" + " - " + "Warning" + " " + str(warning_time) + " !!!" + "\n" + "You are breaking too hard!" + "\n")
            int(current_acc)
            int(warning_time)
            tempv_init.append(v_init)   # Storing initial speed value in array when above condition is true
            tempv_final.append(v_final) # Storing final speed value in array when above condition is true
            warning_time += 1
        
    if warning_time == 3:
        if v_init < v_final:
            print("Initial: " + str(v_init) + " km/h" + " - " + "Final: " + str(v_final) + " km/h")
            print(str(current_acc) + " m/s^2" + " - " + "Warning" + " " + str(warning_time) + " !!!" + "\n" + "You are accelerating too much!" + "\n")
            print("You were warn 3 times.\nBe careful with the cargo or a fee will be applied to your account!\n")
            break
        elif v_init > v_final:
            print("Initial: " + str(v_init) + " km/h" + " - " + "Final: " + str(v_final) + " km/h")
            print(str(current_acc) + " m/s^2" + " - " + "Warning" + " " + str(warning_time) + " !!!" + "\n" + "You are breaking too hard!" + "\n")
            print("Stop Breaking so hard!\nYou might damage the cargo!\n")
            break
        
    iteration = iteration + 1

firstv_init = (tempv_init[0])
lastv_final = (tempv_final[4])

if drowsy_counter >= 5 and firstv_init > lastv_final: # Checking for a gradual deceleration (sample size is 5)
    print("You look a bit drowsy...\nI suggest pulling over and taking a nap.\n")

if warning_time != 3 and drowsy_counter < 5:
    print("Good job, you had no warnings. Keep up the good work!\n")
    
