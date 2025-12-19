#neues Projekt um Datei einzulesen und Dinge wieder auszuspucken
#  1.einlesen
#  2. jede Zeile printen
# ein array ist eine unsortierte Liste oder Reihe
# sortet list ist ein dict

fileSnalesFlorenz=open("schnecken_florenz") #öffnet die Datei
fileSnalesHeidelberg=open("schnecken_heidelberg") 
fileSnalesFlorenzLines=fileSnalesFlorenz.readlines() #ließt einzelne Zeilen und packt sie in einen array
#  print(type(fileSnalesLines)) #spuckt Zeilen aus (ohne type)
lineNumbers=True 
print(type(lineNumbers))

#für jedes Element in diesem Array mache das folgende:
#print dieses Element
#und als nächstes nummerieren wir anhand der Variable i die einzelnen Elemente

i=1    #muss davor sein sonst erst ab danach gültig
for schnecke in fileSnalesFlorenzLines:
    schnecke=schnecke.strip()  #das hat den Umbruch nach jedem Element weggestript
    print(i, schnecke)
    i+=1
    
