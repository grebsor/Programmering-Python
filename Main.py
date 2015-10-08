
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
    print "Välj vilket alternativ du vill göra "
    print ""
    print "1. Använd en färdig databas."
    print "2. Skapa en databas."
    print "3. Ta bort element ur databasen."
    print "4. Lägg till element till databasen."
    print "5. Ändra ett element i databasen."
    print "6. Skriv ut alla namn ur databasen."
    print "7. Skriv ut alla åldrar ur databasen."
    print "8. Skriv ut hela listan"
    print "x. bla bla bla", "\n", "\n"
    try:
        val=int(raw_input("Ditt val 0-9: "))

        if val==1:
            l=[["Robin Rosberg", 29],["Eda Krodguldu", 19],["Stefan Falk", 49],["Knugen", 70],["Stina Svensson", 17]]
            print "Här är den förberedda listan:", "\n", "\n", l, "\n", "\n" 
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
        
        val2=str(raw_input("Vill du göra ett nytt val? (y/n): "))
        if val2=="n":
            b=False
        print "\n \n"
    except:
        print "Försök igen \n"
        
