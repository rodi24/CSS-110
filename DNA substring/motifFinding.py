#motifFinding.py
#Rodas T Gebreslassie
#This program will open a data file of motifFinding.txt and output
#the index of each occurrence of the sub string T within the
# main string S.


def count(b,c):
    count = 0
    for i in range(len(b)):
        if b[i:].startswith(c):
            count = count + 1
    return count


def finder(b,c):
    l = len(c)
    p = []

    for i in range(len(b)):
        if b[i:i + l] == c:
            p.append(i)
    return p
def output(b):
    a = "The sub-string t occurs within the string s at starting positions indexed at "
    c = str(b[0])
    for i in b[1:]:
        c = c +", " + str(i)
    print(a + c + ".")





def main():
    fob = open("motifFinding.txt","r")
    line = fob.read()


    a = line.split("\n")
    S = a[0]
    T = a[1]
    c = count(S,T)
    f = finder(S,T)
    output(f)

    fob.close()
main()
