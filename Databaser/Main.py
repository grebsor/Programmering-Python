import os
#'------------------------ Funktioner ------------------------'

def bubbleSortINT(a):
    'a=matris'
    try:
        for u in range(len(a),1,-1):
            for x in range(u-1):
                if a[x][1]>a[x+1][1]:
                    a[x],a[x+1]=a[x+1],a[x]
    except ValueError:
        print "Ogiltigt varde for alder i databasen, vanligen andra till numeriskt varde."
        
def bubbleSortSTR(a):
    'a=matris'
    for u in range(len(a),1,-1):
        for x in range(u-1):
            rensad1=a[x][0].lower().replace(" ","")
            rensad2=a[x+1][0].lower().replace(" ","")
            if rensad1!=rensad2:
                letter=0
                while rensad1[letter]==rensad2[letter]:
                    letter+=1
                if rensad1[letter]>rensad2[letter]:
                    a[x],a[x+1]=a[x+1],a[x]

def insertD(a):
    'a=matris'
    print "\n"
    a.append([raw_input("Namn person: "),int(raw_input("Alder person:"))]) 

def printD(a):
    'a=matris'
    print "\n"
    i=0
    header="{0: ^6}{1: ^30}{2}".format("Index","Namn","Alder")
    print header
    print "-"*len(header)
    for x in l:        
        print "{0: ^6}{1: ^30}{2}".format(i,x[0],x[1])
        i+=1
    print "\n"

def printI(i,a):
    'i=index'
    'a=matris'
    print "\n"
    try:
        print "Index %d:"%i,a[i]
    except:
        for u in i:
            print "Index %d:"%u,a[u]
    print "\n"
    
def skapaD(b):
    'b=int'
    try:
        lista=[]
        for x in range(b):
            lista.append([raw_input("Namn person %d: "%(x+1)),int(raw_input("Alder person %d:"%(x+1)))])
        return lista
    except ValueError:
        print "\nOgiltig inmatning, databasen forkastas.\n"
        
def meny1():
    print "{0: <5}{1: <40}".format("\n1","Anvand en fardig databas.")
    print "{0: <4}{1: <40}".format("2","Skapa en databas.")
    print "{0: <4}{1: <40}".format("3","Oppna en databas fran fil")
    print "{0: <4}{1: <40}".format("4","Spara din databas till fil")
    print "{0: <4}{1: <40}".format("5","Avsluta.\n")
    T=raw_input("Vad vill du gora? : ")
    if str(T)=="1" or str(T)=="2" or str(T)=="3" or str(T)=="4" or str(T)=="5":
        return int(T)
    else:
        print "Fel val. Try again. \n"
        return meny1()

def meny2():
    print "\n{0: <5}{1: <40}".format("\n1","Ta bort element ur databasen.")
    print "{0: <4}{1: <40}".format("2","Lagg till element till databasen.")
    print "{0: <4}{1: <40}".format("3","andra ett element i databasen.")
    print "{0: <4}{1: <40}".format("4","Sotera databasen efter namn.")
    print "{0: <4}{1: <40}".format("5","Sotera databasen efter alder.")
    print "{0: <4}{1: <40}".format("6","Skriv ut hela databasen.")
    print "{0: <4}{1: <40}".format("7","Skriv ut ett visst index ur databasen.")
    print "{0: <4}{1: <40}".format("8","Soka namn ur databasen")
    print "{0: <4}{1: <40}".format("9","Soka alder ur databasen")
    print "{0: <4}{1: <40}".format("10","Backa till huvudmenyn.")
    print "{0: <4}{1: <40}".format("11","Avsluta programmet.\n\n")
    T=raw_input("Vad vill du gora? : ")
    if str(T)=="1" or str(T)=="2" or str(T)=="3" or str(T)=="4" or str(T)=="5" or str(T)=="6" or str(T)=="7" or str(T)=="8" or str(T)=="9" or str(T)=="10" or str(T)=="11" or str(T)=="12":
        return int(T)
    else:
        print "\nOgiltigt val. Try again. \n"
        return meny2()

def searchName(name,l):
    found=False
    hittatIndexLista=[]
    for item1 in l:
        if name.lower().replace(" ","") in item1[0].lower().replace(" ",""):
            found=True
            hittatIndexLista.append(l.index([item1[0],item1[1]]))
    if found==False:
        print "\nDoesn't exist.\n"
    return hittatIndexLista

"""

        searchNumber() tar tva argument(number,l)
        och returnerar en lista med alla index dar numret matchar
        number: Heltal.
        l: Lista av listor med minst tva element.
        found:Found ar false tills den hittar en matchning.
        hittatIndexLista:Lista med vardet pa alla index som matchar med number.
        item1: Varje lista i l
        
"""

def searchNumber(number,l):
    found=False
    hittatIndexLista=[]
    for item1 in l:
        if number==item1[1]:
            found=True
            hittatIndexLista.append(l.index([item1[0],item1[1]]))
    if found==False:
        print "\nDoesn't exist.\n"
    return hittatIndexLista

def readFile(name):
    l=[]
    with open(os.path.join('.',name),'r') as f:
        for a in f.readlines():
            namn,alder=a.strip().split("\t")
            l.append([namn,int(alder)])
    return l

def saveFile(name,l):
    with open(os.path.join('.',name),'w+') as f:
        for info in l:
            temp=info[0]+"\t"+str(info[1])+"\n"
            f.write(temp)
        
#---------------------------------------MAIN------------------------------------------------

#---------------------------------------MENY1-----------------------------------------------

l=[]

while a==True:    
    myDir=[]
    for fil in os.listdir('.'):
        if '.txt' in fil:
            myDir.append(fil)
    val=meny1()
    b=True
    if val==1:
        l=[["Robin Rosberg", 29],["Eda Krodguldu", 19],["Stefan Falk", 49],["Knugen", 70],["Stina Svensson", 17]]
        print "\nHar ar den forberedda databasen: "
        printD(l)
    elif val==2:
        try:
            antalPers=int(raw_input("\nHur manga personer vill du att databasen ska innehalla? : "))
            l=skapaD(antalPers)
        except ValueError:
            print "\nOgiltig inmatning\n"
            b=False
    elif val==3:
        print "\nNedan foljer en lista pa databaser som ar sparade:\n"
        for u in myDir:
            print u
        print "\n"
        try:
            l=readFile(raw_input("Namn pa filen du vill anvanda: "))
        except IOError:
            print "\nDet finns ingen fil vid det namnet."
            b=False
    elif val==4:
        c=True
        print "\nNedan foljer en lista pa databaser som ar sparade:\n"
        for u in myDir:
            print u
        try:        
            inputnamn=raw_input("\nSpara databas som(namn utan .txt): ")
            filnamn=inputnamn+".txt"
            for fil in myDir:
                if filnamn==fil:
                    c=False
            if c==False:
                if "y"==raw_input("\nDet finns redan en fil vid namn {}, \nvill du skriva over den?(y/n)".format(filnamn)):
                    saveFile(filnamn,l)
                    b=False
                else:
                    print "\nTry again from main menu."
                    b=False
            elif c==True:
                saveFile(filnamn,l)
                b=False
                print "\nSparat och klart"
        except:
            print "\nNagot gick fel, try again.\n"
            b=False
    elif val==5:
        a=False
        b=False
#---------------------------------------MENY2-------------------------------------
    if b==True:
        while b==True:
            val=meny2()
            if val==1:
                printD(l)
                del l[int(raw_input("Vilket index vill du ta bort? : "))]
                print "\n"
            elif val==2:
                insertD(l)
            elif val==3:
                printD(l)
                index=int(raw_input("Vilket index vill du andra? : "))
                printI(index,l)
                print "\n1. andra namn\n2. andra alder\n3. andra bade namn och alder\n"
                na_al=int(raw_input("Vad vill du andra? : "))
                if na_al==1:
                    l[index][0]=raw_input("\nNamn person: ")
                elif na_al==2:
                    l[index][1]=int(raw_input("alder person:"))
                elif na_al==3:
                    l[index]=raw_input("\nNamn person: "),int(raw_input("alder person:"))
            elif val==4:
                bubbleSortSTR(l)
            elif val==5:
                bubbleSortINT(l)
            elif val==6:
                printD(l)
            elif val==7:
                printI(int(raw_input("\nVilket index vill du skriva ut? 0-%d: \n"%(len(l)-1))),l)
            elif val==8:
                hittatIndexNamn=searchName(raw_input("\nSok efter namn eller del av namn i databasen: "),l)
                printI(hittatIndexNamn,l)
            elif val==9:
                hittatIndexNummer=searchNumber(int(raw_input("\nSok alla med en viss alder: ")),l)
                printI(hittatIndexNummer,l)
            elif val==10:
                b=False
            elif val==11:
                a=False
                b=False
            
            raw_input("\nTryck enter.")
            
            
