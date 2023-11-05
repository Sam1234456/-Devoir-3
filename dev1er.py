
#1
karakte = ['A', 'B', 'C', 'D', 'E']

miniskil_karakte = [k.lower() for k in karakte]

print(miniskil_karakte)


#2
chen_karakte = "Sa se yon ekzanp "

lis  = chen_karakte.split()

print(lis)


#3
chen_karakte = " Yon ekzanp nan yon fraz ak plizyè mo."

lis_mò = chen_karakte.split()

lis_mò_majiskil = [mo.capitalize() for mo in lis_mò]

chen_majiskil = ' '.join(lis_mò_majiskil)

print(chen_majiskil)
 
 
 #4
chen_karakte = "sa se yon ekzanp nan yon fraz ak plizyè mo."

lis_mò = chen_karakte.split()

inisyal  = [mo[0] for mo in lis_mò]

chen_inisyal = ''.join(inisyal)

print(chen_inisyal)


#6
chen_anvan = "anvan"
chen_apre = "dapre"

nouvo_chenn = chen_anvan + chen_apre

nouvo_chenn_majiskil = nouvo_chenn.capitalize()

print(nouvo_chenn_majiskil)



#5

chen_karakte = " fraz sa ak plizyè lòt mo ki gen karaktè a."

chen_ranplase = chen_karakte.replace("a", "@")

print(chen_ranplase)


#7
chen_karakte = "fraz sa ak plizyè lòt karaktè yo."

endeks = chen_karakte.find("a")

if endeks != -1:
    print("Endeks premye karaktè 'a':", endeks)
else:
    print("Pa gen karaktè 'a' nan chenn sa a.")


#8

chen_karakte = " Plizyè lòt mo ki gen karaktè A ak a."

endeks_list = [i for i, char in enumerate(chen_karakte) if char in 'Aa']

if endeks_list:
    print("Total tout endeks karaktè 'a':", len(endeks_list))
    print("Endeks yo:", endeks_list)
else:
    print("Pa gen karaktè 'a' nan chenn sa a.")


#9
chen_karakte = "fraz sa ka rete ak plizyè lòt mo ki gen karaktè A ak a."

endeks_list = [i for i, char in enumerate(chen_karakte) if char == 'a']

if endeks_list:
    print("Endeks tout karaktè 'a' a miniskil:", endeks_list)
else:
    print("Pa gen karaktè 'a' a miniskil nan chenn sa a.")



#10
chen_karakte = "fraz sa ak plizyè lòt mo yo ki gen menm karaktè a."

chen_san_espas = chen_karakte.replace(" ", "")

kantite_karakte = len(chen_san_espas)

print("Chenn san espas:", chen_san_espas)
print("Kantite karaktè:", kantite_karakte)



