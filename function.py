def countingWords():
    counting=input("ENTER A FILE NAME : ")
    numberofwords=0
    file=open(counting,'r')
    for line in file :
        word=line.split()
        numberofwords=numberofwords+len(word)
    print("Number Of Words = " )
    print(numberofwords)

countingWords()