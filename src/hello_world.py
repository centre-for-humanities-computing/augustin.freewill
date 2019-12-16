#! /usr/bin/python3

import os

def hello_world():
    fpath = os.path.join("..", "dat", "hello_world.txt")
    with open(fpath, "r") as fobj:
        content = fobj.read()
    print(content)

if __name__ == "__main__":
    hello_world()
