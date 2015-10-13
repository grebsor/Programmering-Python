
'------------------------ Funktioner ------------------------'

def bubbleSortINT(a):
    'a=matris'
    u=len(a)
    try:
        while u:
            for x in range(u-1):
                if a[x][1]>a[x+1][1]:
                    a[x],a[x+1]=a[x+1],a[x]
            u-=1
    except ValueError:
        print "Ogiltigt värde för ålder i databasen, vänligen ändra till numeriskt värde."
        
def bubbleSortSTR(a):
    'a=matris'
    u=len(a)
    while u:
        for x in range(u-1):
            rensad1=a[x][0].lower().replace(" ","")
            rensad2=a[x+1][0].lower().replace(" ","")
            if rensad1==rensad2:
                a[x],a[x+1]=a[x+1],a[x]
            else:
                letter=0
                while rensad1[letter]==rensad2[letter]:
                    letter+=1
                if rensad1[letter]>rensad2[letter]:
                    a[x],a[x+1]=a[x+1],a[x]
        u-=1

def insertD(a):
    'a=matris'
    print "\n"
    a.append([raw_input("Namn person: "),int(raw_input("Ålder person:"))]) 

def printD(a):
    'a=matris'
    print "\n"
    i=0
    header="{0: ^6}{1: ^30}{2}".format("Index","Namn","Ålder")
    print header
    print "-"*len(header)
    for x in l:        
        print "{0: ^6}{1: ^30}{2}".format(i,x[0],x[1])
        i+=1
    print "\n"

def printI(i,a):
    'i=index'
    'a=matris'
    print "\nIndex %d:"%i,a[i],"\n"

def skapaD(b):
    'b=int'
    lista=[]
    for x in range(b):
        lista.append([raw_input("Namn person %d: "%(x+1)),int(raw_input("Ålder person %d:"%(x+1)))])
    return lista
        
'------------------------   Main     ------------------------'
b=True
while b:
    print "\nVälj vilket alternativ du vill göra \n"
    print "{0: <4}{1: <40}".format("1","Använd en färdig databas.")
    print "{0: <4}{1: <40}".format("2","Skapa en databas.")
    print "{0: <4}{1: <40}".format("3","Ta bort element ur databasen.")
    print "{0: <4}{1: <40}".format("4","Lägg till element till databasen.")
    print "{0: <4}{1: <40}".format("5","Ändra ett element i databasen.")
    print "{0: <4}{1: <40}".format("6","Sotera databasen efter namn.")
    print "{0: <4}{1: <40}".format("7","Sotera databasen efter ålder.")
    print "{0: <4}{1: <40}".format("8","Skriv ut alla namn ur databasen.")
    print "{0: <4}{1: <40}".format("9","Skriv ut alla åldrar ur databasen.")
    print "{0: <4}{1: <40}".format("10","Skriv ut hela listan.")
    print "{0: <4}{1: <40}".format("11","Skriv ut ett visst index ur databasen.\n\n")
##    try:
    val=int(raw_input("Ditt val 1-11: "))

    if val==1:
        l=[["Robin Rosberg", 29],["Eda Krodguldu", 19],["Stefan Falk", 49],["Knugen", 70],["Stina Svensson", 17]]
        print "\nHär är den förberedda databasen: "
        printD(l)
    elif val==2:
        antalStart=int(raw_input("\nHur många personer vill du att databasen ska innehålla? : "))
        l=skapaD(antalStart)
    elif val==3:
        printD(l)
        del l[int(raw_input("Vilket index vill du ta bort? : "))]
        print "\n"
    elif val==4:
        insertD(l)
    elif val==5:
        printD(l)
        index=int(raw_input("Vilket index vill du ändra? : "))
        printI(index,l)
        print "\n1. Ändra namn\n2. Ändra ålder\n3. Ändra både namn och ålder\n"
        na_al=int(raw_input("Vad vill du ändra? : "))
        if na_al==1:
            l[index][0]=raw_input("\nNamn person: ")
        elif na_al==2:
            l[index][1]=int(raw_input("Ålder person:"))
        elif na_al==3:
            l[index]=raw_input("\nNamn person: "),int(raw_input("Ålder person:"))
    elif val==6:
        bubbleSortSTR(l)
    elif val==7:
        bubbleSortINT(l)
    elif val==8:
        for x in l:
            print x[0]
    elif val==9:
        for x in l:
            print x[1]
    elif val==10:
        printD(l)
    elif val==11:
        printI(int(raw_input("\nVilket index vill du skriva ut? 0-%d: \n"%(len(l)-1))),l)
    else:
        print "Du har inte gjort ett giltigt val. \n"
    
            
    val2=str(raw_input("Vill du göra ett nytt val? (y/n): "))
    if val2=="n":
        b=False
##    except:
##        print "Försök igen \n"
        
