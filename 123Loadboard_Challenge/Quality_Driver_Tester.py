import random
import math

#Fix Data set
Initial_Speed = [94, 94, 70, 58, 57, 97, 74, 76, 80, 86]    #Good driver data set
Final_Speed = [77, 81, 86, 74, 77, 80, 79, 83, 86, 88]

#Initial_Speed = [100, 57, 87, 69, 93, 65, 95, 50, 57, 70]   #Dangerous driver data set
#Final_Speed = [81, 90, 76, 84, 77, 80, 77, 85, 90, 82] 

#Initial_Speed = [69, 109, 97, 66, 120, 120, 110, 114, 115, 109]    #Hard Breaking driver data set
#Final_Speed = [77, 77, 90, 74, 83, 83, 86, 87, 92, 88]

#Initial_Speed = [94, 94, 70, 58, 54, 50, 46, 42, 80, 86]    #Drowsy driver data set
#Final_Speed = [77, 81, 86, 56, 52, 48, 44, 40, 86, 88]

print(" ")
acc_sample = 5      # Sampling acceleration every 5 seconds
iteration = 0       
warning_time = 1
counter = 0
drowsy_counter = 0

while iteration < 10:   #10 samples for testing purposes
    #num1 = random.randint(48, 120)  #Random speed from 48km/h to 120km/h
    #num2 = random.randint(74, 90)  #Random speed from 74km/h to 90km/h
    #v_init = num1
    #v_final = num2
    #current_acc = abs((v_final - v_init) / acc_sample)   #Acceleration in m/s^2

    current_acc = abs((Final_Speed[counter] - Initial_Speed[counter]) / acc_sample)
    v_init = Initial_Speed[counter]
    v_final = Final_Speed[counter]
    counter = counter + 1
    
    if v_init > v_final and v_init - v_final == 2:
        drowsy_counter = drowsy_counter + 1
    
    if drowsy_counter == 5:
        print("You look a bit drowsy...\nI suggest pulling over and taking a nap.\n")
        break

    if current_acc < 5:
        print("Initial: " + str(v_init) + " km/h" + " - " + "Final: " + str(v_final) + " km/h")
        print(str(current_acc) + " m/s^2\n") 
        int(current_acc)

    if current_acc > 5:
        if v_init < v_final:
            print("Initial: " + str(v_init) + " km/h" + " - " + "Final: " + str(v_final) + " km/h")
            print(str(current_acc) + " m/s^2" + " - " + "Warning" + " " + str(warning_time) + " !!!" + "\n" + "Dangerous Driving" + "\n")
            int(current_acc)
            int(warning_time)
            warning_time += 1
        elif v_init > v_final:
            print("Initial: " + str(v_init) + " km/h" + " - " + "Final: " + str(v_final) + " km/h")
            print(str(current_acc) + " m/s^2" + " - " + "Warning" + " " + str(warning_time) + " !!!" + "\n" + "Wake Up !!!" + "\n")
            int(current_acc)
            int(warning_time)
            warning_time += 1
        
    if warning_time == 3:
        if v_init < v_final:
            print("Initial: " + str(v_init) + " km/h" + " - " + "Final: " + str(v_final) + " km/h")
            print(str(current_acc) + " m/s^2" + " - " + "Warning" + " " + str(warning_time) + " !!!" + "\n" + "Dangerous Driving" + "\n")
            print("You were warn 3 times.\nBe careful with the cargo or a fee will be applied to your account!\n")
            break
        elif v_init > v_final:
            print("Initial: " + str(v_init) + " km/h" + " - " + "Final: " + str(v_final) + " km/h")
            print(str(current_acc) + " m/s^2" + " - " + "Warning" + " " + str(warning_time) + " !!!" + "\n" + "Wake Up !!!" + "\n")
            print("Stop Breaking so hard!\nYou might damage the cargo!\n")
            break
        

    iteration = iteration + 1
