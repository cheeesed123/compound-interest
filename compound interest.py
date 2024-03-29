global help_
global no_years
help_ = 0
def Long_text():
        print("Compound Formula: \nA = p(1+r/n)^(nt)")
        print("Variables have notes ABOVE them when answering them.\n")
class Solve:
    def Solve():
        global help_
        if help_ == 1:
            print ("The principle is the amount you start with.")
            print ("The rate is the amount of change over each period.")
        while True:
            principle = input("Principle:")
            rate = input("Rate (percent form no %):")
            n = input("Number of times per year:")
            years = input("Years:")
            try:
                principle = float(principle)
                rate = float(rate)/100
                n = int(n)
                years = int(years)
            except ValueError:
                print ("Unrecognized choice, restarting")
                continue
            else:
                break
        answer = principle * (1+(rate/n))**(n * years)
        return answer
        
class Find:
    def Find():
        global help_
        print ("_________________")
        print ("Find mode enabled")
        if help_ == 1:
            print ("The target value is what decides how long it'll\ntake for that much money.")
            print ("This will spit out cycles it takes to pass that goal.")
            print ("Please remember to keep money value in __.__")
            print ("(Whole numbers do not have to be 2 long.)")
        iterations = 0
        while True:
            target = input("Target Value:")
            principle = input("Principle:")
            rate = input("Rate (percent form no %):")
            try:
                target = float(target)
                principle = float(principle)
                rate = float(rate)/100
            except ValueError:
                print ("Unrecognized choice, restarting")
                continue
            else:
                break
        while iterations < target:
            if (principle * (1+(rate))**(iterations)) < target:
                iterations += 1
                continue
            else:
                break
        if iterations == 1:
            answer = str(iterations) + " iteration to reach/pass $" + str(target)
        else:
            answer = str(iterations) + " iterations to reach/pass $" + str(target)
        return answer


def Start():
    Long_text()
    choice = ""
    global help_
    global no_years
    while True:
        print("Welcome to the Compund Formula solver!\n Mode:\n [S]olve   [F]ind   [C]redits    [H]elp notes?")
        choice = input("Choice:").strip().lower()
        if choice in ["find", "f"]:
            no_years = 1
            print("It took", Find.Find(),)
            input("Press enter to continue")
            Long_text()
        elif choice in ["solve", "s"]:
            print ("__________________")
            print ("Solve mode enabled")
            no_years = 0
            print("Answer:", "$" + str(round(Solve.Solve(), 2)))
            input("Press enter to continue")
            Long_text()
        elif choice in ["credits", "credit", "c"]:
            print ("\nEverything - Chief guy.\nMake sure to check out my Itch for new content!")
            print ("\nAlso make sure to check out my Youtube at:\nhttps://www.youtube.com/@Awesomechiefguy")
            input("Enter to continue")
            Start()
        elif choice in ["help notes", "h"]:
            if help_ == 0:
                help_ = 1
                print ("Help notes enabled.")
            else:
                help_ = 0
                print ("Help notes disabled.")
            continue
        else:
            print ("Unrecognized choice, restarting")
            continue
Start()