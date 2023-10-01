
import os

if __name__ == '__main__':
    print("welcome to RoboSpeaker 1.1 created by Bilal")
    while True:
        x = input("Enter what you want to speak: ")
        if x == "stop":
            os.system("say 'bye bye friend'")
            break
        if x == "good robot":
            os.system("say 'thanks chad'")
            break
        command = f"say {x}"
        os.system(command)






