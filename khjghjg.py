def main():
    list = []
    x = "hi"
    while x != "":
        x = input()
        list.append(x)
    for i in range(0,len(list)):
        list[i] = piglatin(list[i])
    list.sort()
    for i in list:
        print(i)

staticmethodfs

def piglatin(word):
    list=[]
    for i in word:
        list.append[i]
    if list[0] not in "aeiouAEIOU":
        list.append[list[0]]
        list.remove[list[0]]
    for i in "ay":
        list.append[i]
    string=""
    for i in list:
        string+=i
    return string