from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' #to not get pygame 2.6... and other prompts

import random #for generating random numbers
import time #for timer
import sys #clear screen
import os #clear screen
from textwrap import wrap #for changing str --> int
from rich.tree import Tree #for styled tree stucture

from rich import print #should be imported as rprint I think but like I don't wanna change every print now so... #for colorfull texts

from rich.progress import track #timer progress bar
from pygame import mixer #for music that u can't stop listening to


print("\n[bold #00FFF7]Welcome to NumCog Game!!![/bold #00FFF7]")

def rules(x, y, skipSpell):
    tree = Tree("\n[bold italic red]RULES:[/bold italic red]", guide_style="italic bright_green")

    rule1 = tree.add(f"You will have [bold cyan]x[/bold cyan] digits of integer. (currently it's [bold cyan]{x}[/bold cyan] digits)")

    rule2 = tree.add(f"You have to add [bold cyan]y[/bold cyan] in each digit. (currently by [bold cyan]{y}[/bold cyan])")
    rule2.add("i.e. [bold cyan]1 2 3 4[/bold cyan] [italic red]==>[/italic red] [bold cyan]2 3 4 5[/bold cyan]")
    
    rule3 = tree.add("if number after addition is in [bold cyan]2[/bold cyan] digits, only provide unit [italic cyan]Digit[/italic cyan]. And forget the rest. Do not carry it like normal addition.")
    rule3.add("i.e [bold cyan]1 9 0 9[/bold cyan] [italic red]==(addition by 2)==>[/italic red] [bold cyan]3 1 2 1[/bold cyan]")

    rule4 = tree.add("[bold cyan]x[/bold cyan] [italic red]+[/italic red] [bold cyan]n[/bold cyan] [italic red]-[/italic red] [bold cyan]4[/bold cyan] [italic red]=[/italic red] [bold cyan]Ex Time[/bold cyan], [bold cyan]y[/bold cyan] [italic red]+[/italic red] [bold cyan]n[/bold cyan] [italic red]-[/italic red] [bold cyan]1[/bold cyan] [italic red]=[/italic red] [bold cyan]Ex Time/2[bold cyan]")

    rule4.add("[bold cyan]5[/bold cyan] digits then [italic red]+[/italic red][bold cyan]1[/bold cyan][magenta]s[/magenta] and/or addition by [bold cyan]2[bold cyan] then [italic red]+[/italic red][bold cyan]0.5[/bold cyan][magenta]s[/magenta]")

    tree.add(f"[magenta]a[/magenta]: skip ([bold cyan]{skipSpell}[/bold cyan] left), [magenta]b[/magenta]: exit, [magenta]c[/magenta]: change Stats, [magenta]v[/magenta]: view Stats [magenta]r[/magenta]: rules")
    print(tree)

    print()

def stats(x, y, multi):
    a = x
    b = y
    try:
        print(f"Enter the number of digits (currently it's [bold cyan]{x}[/bold cyan] digits): ", end=None)
        x = int(input())
        if (x<a):
            print("Can only change stats ⬆️")
            x = a
    except Exception:
        x = a

    try:
        print(f"addition by (currently by [bold cyan]{y}[/bold cyan]): ", end=None)
        y = int(input())
        if (y<b):
            print("Can only change stats ⬆️")
            y = b
    except Exception:
        y = b
    
    if (x<4 or y<1):
        x = a
        y = b

    if (x>4 or y>1):
        multi = round(1 + (x - 4) * 0.5 + (y - 1) * 0.25, 2)

    else:
        multi = 1

    if(multi<1):
        multi = 1

    # i = x - 4
    # j = y - 1
    # k = i + (j/2)

    # t = t + k

    # if (t<5):
    #     t = 5

    print()
    return x, y, multi


def resultedScore(newNum, addNum, score, multi, run):
    if (newNum == addNum):
            score += (1 * multi)
            print("[italic bright_red]Correct[/italic bright_red]")
            print(f"[italic light_green]Score[/italic light_green]: [bold cyan]", score)
            print()
            run = True
            return score, run
    else:
        print("oops, better luck next time")
        print("Correct answer: ", addNum, end=None)
        print("Your score: ", score)
        run = False
        return score, run

def timer():
    for i in track(range(t), description="timer..."):
        time.sleep(1)  

def viewStats():
    print(f"No. of digits: {x} and Addition by {y}")

x = 4 # digit on which addition will have Sorry for bad var names 
y = 1 # addition by
t = 5 #timer
n = 0 #total run


skipSpell = 3 #can skip 3 times

multi = 1 #mutiplier for score

rules(x, y, skipSpell)

x, y, multi = stats(x, y, multi)

run = True
score = 0

while run:
    ogNum = []
    addNum = []

    print("Num: ", end=None)
    for i in range(x):
        z = random.randint(0, 9)
        print(z, " ", end="")
        ogNum.append(z)
        if ((z+y) >= 10):
            i = (z+y) % 10
            addNum.append(i)
        else:
            addNum.append(z+y)
    
    print()
    timer()

    for i in range(3): #to clear the screen 
        sys.stdout.write("\033[F")  #move cursor up one line
        sys.stdout.write("\033[K")  #clear line

    print()
    
    print(f"[bold blue]Multi[/bold blue]: [bold cyan]{multi}[/bold cyan][bold red]\U0001D465[/bold red]") #\u... is for math... x symbol
    newNum = input("Your answer: ") #don't take as int otherwise rules won't work 
    os.system("cls")

    if(newNum == "69"): #easter egg check
        print("[bold red]Congratulations!!![/bold red]")
        print("May the divinity of [italic cornflower_blue]6[/italic cornflower_blue][italic deep_pink3]9[/italic deep_pink3] blossom in your life 🤞")



    def check(newNum, x, y): #check whether input is Ans or options
        if (type(newNum) is str):
            match (newNum):
                case "a":
                    return "continue"
                case "b":
                    return "break"
                case "c":
                    return "reset"
                case "r":
                    rules(x, y, skipSpell)
                    return check(newNum = input("Your answer: "), x=x, y=y)
                case "v":
                    print(f"No. of digits: [bold cyan]{x}[/bold cyan], Addition by [bold cyan]{y}[/bold cyan], Multi: [bold cyan]{multi}[/bold cyan][bold red]\U0001D465[/bold red], skip: [bold cyan]{skipSpell}[/bold cyan]")
                    return check(newNum = input("Your answer: "), x=x, y=y)
                case _:
                    pass
    
    if(newNum == 69):
        out == "easter"
    else:
        out = check(newNum, x, y) #winners win, losers lose 

    if (out == "continue"): #used skipSpell
        if (skipSpell > 0):
            skipSpell -= 1
            continue
        elif (skipSpell == 0):
            print("Oh NO you ran out of skips")
            check(newNum = input("Your answer: "), x=x, y=y)
    elif (out == "break"): #exit
        print(f"Your Score: {score}")
        run = False
        break
    elif (out == "reset"): #change stat
        x, y, multi = stats(x, y, multi)
        print(f"New stats: [bold cyan]{x}[/bold cyan] digits, addition by [bold cyan]{y}[/bold cyan]")
        continue
    elif (out == "easter"):#easter egg
        run = False
        break
    else:
        pass

    if(newNum == '69'):
        pass
    elif (len(newNum) != x or not all(i.isdigit() for i in newNum)): #now checking for valid/invalid num
        #print("Error: Invalid input")
        run = False

    if(newNum == '69'):
        score = "[bold deep_pink3]Eternal Love💘[/bold deep_pink3]"
        print(f"[italic light_green]Score[/italic light_green]: {score}")
        run = False
        break
    elif (newNum not in ("a", "b", "r")):

        newNum = wrap(newNum, 1)

        try:
            for i in range(x): #changing the type of num
                newNum[i] = int(newNum[i])
        except Exception:
            print("Error: Invalid input")

        print()

        score, run = resultedScore(newNum, addNum, score, multi, run)  #score I mean do I need to write this THIS here, lol
        
        n += 1 #run

        if (run == True): 
            if (n%3 == 0):
                x += 1
                y += 1
                n = 0
                multi = round(1 + (x - 4) * 0.5 + (y - 1) * 0.25, 2)
                print(f"[bold cyan]{x}[/bold cyan] digits, addition by [bold cyan]{y}[/bold cyan]")

    else:#Boo Hoo loser
        print(f"Your Score: {score}")
        run = False
        break

print()
try:
    if(newNum == '69'):
        mixer.init()
        mixer.music.load("NeverGonnaGiveYouUp.MP3")  
        mixer.music.play(-1)  #loop forever
except Exception as e:
    print("Can't play song because of error: ", e)
    print()
    print("So here just read this and sing ALONG: ")
    print("""
**🎷🎸🎹🎺
We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinkin' of
You wouldn't get this from any other guy

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up, never gonna let you down
Never gonna run around and desert you
Never gonna make you cry, never gonna say goodbye
Never gonna tell a lie and hurt you
🎧 🎚️  🎙️  🎛️""")

gameExit = input("Press any key to exit...") #to stop terminal from exiting

# Created by Me, defau1tuser0
#Thanks for playing my Game 🤛