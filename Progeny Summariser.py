from itertools import islice
from itertools import product
import string
from collections import Counter 
import pandas
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format
import sys
alphabets = list(string.ascii_lowercase)
capalphabets = list(string.ascii_uppercase)
y = []
capy = []
lts = []
gamete = []
newgamete = []
indexlist = []
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
lghjk = []
perc = []
init(strip=not sys.stdout.isatty())
cprint(figlet_format('Progeny Summary', font='epic'),'red', attrs=['bold'])
x = int(input("Enter Number of Traits :- "))
if((x <= 26)):
    for i in range(0, x, +1):
        if i not in y:
            y.append(alphabets[i])
        if i not in capy:
            capy.append(capalphabets[i])
    l1 = sorted(capy+y, key= str.casefold)
    for j in range(0, len(l1)//2, +1):
        lts.append(2)
    inputnew = iter(l1)
    output = [list(islice(inputnew,ele)) for ele in lts]
    gamete = (list(product(*output)))
    for e in gamete:
        l5.append(list(e))
    for k in range(0, len(gamete), +1):
        for l in range(0, len(gamete), +1):
            newgamete.append(gamete[k] + gamete[l])
    for f in newgamete:
        l6.append(list(f))
    printchoice = int(input("Enter 1 to see all offsprings, else Enter 2 to skip to summary: "))
    print(' ')
    if printchoice==1:
        interfaceinput = int(input("Which Interface would you want? For line by line, enter 1 and for single line, enter 2 :- "))
        if(interfaceinput == 1):
            print("Offsprings are of the form")
            for ele in newgamete:
                ele = sorted(ele, key = lambda u: u.lower())
                ele = [''.join(ele)]
                print(str(ele[0]))
        elif(interfaceinput == 2):
            print("Offsprings are of the form")    
            for ele in newgamete:
                ele = sorted(ele, key = lambda u: u.lower())
                ele = [''.join(ele)]
                print(str(ele[0]), end = " ")
            print("\n")
    print("Offsprings are", len(newgamete), "in number")
    for element in newgamete:
        l2.append(list(element))
    l3 = list(map(sorted, l2))
    for elem in l3:
        if elem not in l4:
            l4.append(elem)
    for z in range(0, len(l4), +1):
        indexlist.append(" ")
    dict = Counter([tuple(sorted(z, key = lambda v: v.lower())) for z in l3])
    p = list(dict.keys())
    for i in p:
        s = ''.join(list(i))
        lghjk.append(s)
    no = len(newgamete)
    occ = list(dict.values())
    for i in occ:
        c = int(i)
        percc = (c*100)/no
        perc.append(str(percc)+'%')
    Output = pandas.DataFrame(data ={'Genotype': lghjk, 'Occurence': occ, 'Percentage': perc}, index = list(indexlist))
    pandas.set_option( "display.max_rows", None, "display.max_columns", None) 
    ra = list(dict.values())
    ra1 = []
    for ele in ra:
      ra1.append(str(ele))
    s = ':'.join(ra1)  
    print("Genotypes are as follows")
    print(Output)
    print("Genotypic Ratio is")
    print(s)
else:
    print("Not possible in this program due to availability of only 26 alphabets")
end = input("Enter Anything to End")