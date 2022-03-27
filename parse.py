import json
with open("./wordlist.txt","r") as fd:
    lines = fd.read().split("\n")
    with open("wordlist.json","w") as fd2:
        json.dump(lines,fd2)