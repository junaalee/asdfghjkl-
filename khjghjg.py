def main():
    list = []
    x = "hi"
    while x != "":
        x = input()
        list.append(x)
    list.sort()
    for i in range(0,len(list)):
        list[i] = piglatin(list[i])

def piglatin():
