
'------------------------ Funktioner ------------------------'

def bubbleSortINT(a):
    'a=matris'

def bubbleSortSTR(a):
    'a=matris'
    i=0
    for x in a:
        if x[0][0].lower()<x[i+1][0].lower():
            x[i],x[i+1]=x[i+1],x[i]
        i+=1

'------------------------   Main     ------------------------'
b=True
while b:
    print "V�lj vilket alternativ du vill g�ra "
    print ""
    print "1. Anv�nd en f�rdig databas."
    print "2. Skapa en databas."
    print "3. Ta bort element ur databasen."
    print "4. L�gg till element till databasen."
    print "5. �ndra ett element i databasen."
    print "6. Skriv ut alla namn ur databasen."
    print "7. Skriv ut alla �ldrar ur databasen."
    print "8. Skriv ut hela listan"
    print "x. bla bla bla", "\n", "\n"
    try:
        val=int(raw_input("Ditt val 0-9: "))

        if val==1:
            l=[["Robin Rosberg", 29],["Eda Krodguldu", 19],["Stefan Falk", 49],["Knugen", 70],["Stina Svensson", 17]]
            print "H�r �r den f�rberedda listan:", "\n", "\n", l, "\n", "\n" 
        elif val==6:
            for x in l:
                print x[0]
        elif val==7:
            for x in l:
                print x[1]
        elif val==8:
            for x in l:
                print x[0],"   ",x[1]
        else:
            print "Du har inte gjort ett giltigt val. \n"
        
        val2=str(raw_input("Vill du g�ra ett nytt val? (y/n): "))
        if val2=="n":
            b=False
        print "\n \n"
    except:
        print "F�rs�k igen \n"
        
