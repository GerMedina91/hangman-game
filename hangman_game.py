import random
import os
import string
import re
from unicodedata import normalize


TITLE = """ ██░ ██  ▄▄▄       ███▄    █   ▄████  ▄▄▄       ███▄    █     ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▒████▄     ██ ▀█   █    ▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▒██  ▀█▄  ▓██  ▀█ ██▒   ▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓░██▄▄▄▄██ ▓██▒  ▐▌██▒   ▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒ ▓█   ▓██▒▒██░   ▓██░   ▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒    ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░   ▒   ▒▒ ░░ ░░   ░ ▒░   ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░   ░   ▒      ░   ░ ░    ░      ░     ░   ▒      ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░       ░  ░         ░           ░         ░  ░         ░ 
                                                                                             
                                                                                             
                                by German Medina
                           
"""

WIN = """██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
                                                      """

LOSE = """██╗   ██╗ ██████╗ ██╗   ██╗     █████╗ ██████╗ ███████╗    ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║
 ╚████╔╝ ██║   ██║██║   ██║    ███████║██████╔╝█████╗      ██║  ██║█████╗  ███████║   ██║   ███████║
  ╚██╔╝  ██║   ██║██║   ██║    ██╔══██║██╔══██╗██╔══╝      ██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║
   ██║   ╚██████╔╝╚██████╔╝    ██║  ██║██║  ██║███████╗    ██████╔╝███████╗██║  ██║   ██║   ██║  ██║
   ╚═╝    ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
                                                                                                    """


DEAD_0 = """
//===
    |
"""
DEAD_1 = """
//===
    |
    o
"""
DEAD_2 = """
//===
    |
 __ o 
"""
DEAD_3 = """
//===
    |
 __ o __
"""
DEAD_4 = """
//===
    |
 __ o __
    |
"""
DEAD_5 = """
//===
    |
 __ o __
    |
   / """


def getWord():
    with open("./data.txt", "r", encoding="utf-8") as words:
        return random.choice(list(words))


def deleteTildes(s):
    """
    It takes a string, normalizes it to NFD, removes all diacritics, then normalizes it back to NFC
    
    :param s: The string to be normalized
    :return: the normalized string.
    """
    s = re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
            normalize( "NFD", s), 0, re.I
        )

    return normalize( 'NFC', s)


def lifeCanvasFlow(l):
    if l == 6:
        print(DEAD_0)
    elif l == 5:
        print(DEAD_1)
    elif l == 4:
        print(DEAD_2)
    elif l == 3:
        print(DEAD_3)
    elif l == 2:
        print(DEAD_4)
    elif l == 1:
        print(DEAD_5)


def startGame(g):
    """
    It takes a dictionary as an argument, and if the life is 0, it returns, otherwise it checks if the
    final string is equal to the word, if it is, it sets the win key to true, otherwise it prints the
    life canvas and the result, then it asks for a letter, and if it's not in the word, it subtracts one
    from the life, and then it calls itself again
    
    :param g: is a dictionary that contains the following:
    :return: the value of the variable "g"
    """
    life = g.get("life")
    result = ''.join(g.get("result"))
    final = str(g.get("final")).replace(' ', '')
    word = g.get("word")
    wordindexs = g.get("wordindexs")

    if life == 0:
        os.system("cls")
        return 
    else:
        os.system("cls")
        if(final == word):
            g["win"] = True
            return 
        else:
            lifeCanvasFlow(life)
            print(result)

            char = input("Enter a letter: ").lower()
            while not char in string.ascii_lowercase:
                char = input("ERROR: Ingrese una letra: ")

            encontro = False
            for i, a in wordindexs:
                if char == a:
                    g["result"][i] = char + ' '
                    g["final"] = ''.join(g.get("result"))
                    encontro = True
            if(not encontro):
                g["life"] -= 1
            startGame(g)


def main():
    
    word = deleteTildes(getWord().strip())
    game = {
        "life": 6,
        "word": word,
        "wordindexs": list(enumerate(word)),
        "result": ["_ " for i in word],
        "final": '',
        "win": False,
    }


    os.system("cls")
    print(TITLE)
    input("                           Press enter to start")

    startGame(game)
    win = game["win"]
    if win:
        print(WIN)
    else:
        print(LOSE)


if __name__ == "__main__":
    main()