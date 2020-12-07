attendance = float(input("Please enter in the percentage of which the pupil attended school.\nFor example, if they attended 83%, type in 83. \n"))
if attendance >= 90:
    print("Student has completed the course! Now their marks.")
    mark = int(input("Please enter the pupil's mark: ")) 
    while mark != 999: 
        if mark >= 81 and mark <= 100: 
            print("Pass! :-) ")
            uwu = "\nThe pupil scored an A *, their specific grade was: " + str(mark)
            f = open("mark.txt", "a")
            f.write(uwu)
            f.close()
            print("This has been saved to mark.txt.")
        elif mark >= 70: 
            print("Pass! :-) ")
            uwu = "\nThe pupil scored an A , their specific grade was: " + str(mark)
            f = open("mark.txt", "a")
            f.write(uwu)
            f.close()
            print("This has been saved to mark.txt.")
        elif mark >= 57: 
            print("Pass! :-) ")
            uwu = "\nThe pupil scored an B , their specific grade was: " + str(mark)
            f = open("mark.txt", "a")
            f.write(uwu)
            f.close()
            print("This has been saved to mark.txt.")
        elif mark >= 45: 
            if mark >= 50:
                print("Pass! :-) ")
            else:
                print("Fail.")
            uwu = "\nThe pupil scored an C , their specific grade was: " + str(mark)
            f = open("mark.txt", "a")
            f.write(uwu)
            f.close()
            print("This has been saved to mark.txt.")
        elif mark >= 32: 
            print("Fail.")
            uwu = "\nThe pupil scored an D , their specific grade was: " + str(mark)
            f = open("mark.txt", "a")
            f.write(uwu)
            f.close()
            print("This has been saved to mark.txt.")
        elif mark >= 20: 
            print("Fail.")
            uwu = "\nThe pupil scored an E , their specific grade was: " + str(mark)
            f = open("mark.txt", "a")
            f.write(uwu)
            f.close()
            print("This has been saved to mark.txt.")
        elif mark >= 0: 
            print("Fail. ")
            uwu = "\nThe pupil scored an F , their specific grade was: " + str(mark)
            f = open("mark.txt", "a")
            f.write(uwu)
            f.close()
            print("This has been saved to mark.txt.")
        elif mark > 100:
            print("This pupil cheated, reporting to OCR.")
        else: 
            print("You entered a grade in wrong. Please try again you worthless heap of crap")
        mark = int(input("Please enter the pupil's mark: ")) 

    
else:
    print("The student has failed due to a lack of attendance.")
