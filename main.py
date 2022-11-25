from src.CFG2CNF import *
from src.CYK import *
from src.simplifierFA import *
from src.tokenizer import *
import src.tokenizer
import argparse
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("file", nargs="?",  default="N#AN#A", type=str)
args = parser.parse_args()

if (args.file == "N#AN#A") :
    print("No file specified")
    print("Usage: python main.py <path-of-file>")
    exit(0)

else :
    if (os.path.isfile(args.file)) :
        path = args.file

        CNFdict = CFGtoCNF("./Grammar/CFG.txt")

        simplifiedInput, valid = tokenize(path)

        startTime = time.time()
        if valid:
            # nanti jangan lupa dihapus
            print("Tokenizing done!")
            print(simplifiedInput)
            #for k, v in CNFdict.items():
            #    print(k, v)
            if len(simplifiedInput) == 0:
                print("File accepted")
            elif checkCYK(simplifiedInput, CNFdict):
                print("File accepted")
            else:
                print("Syntax Error (CYK)")
        else:
            print("Syntax Error (Token)")

        finishTime = time.time() - startTime
        print("Relative length : ", len(simplifiedInput))
        print(finishTime)
    else :
        print("File not found")