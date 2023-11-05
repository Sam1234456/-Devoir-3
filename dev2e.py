
#-----------------zyem pati -----------------

#1
n = 10 

lis_divizib = [x for x in range(n+1) if x % 2 == 0]

print(lis_divizib)


#2
lis_antye = [1, 2, 3, 4, 5]

lis_chenn = [str(x) for x in lis_antye]

print(lis_chenn)


#3
lis_miniskil = ["pom", "kiwi", "zoranj", "banan", "grenad"]

lis_majiskil = [mo.upper() for mo in lis_miniskil]

print(lis_majiskil)


#4
lis_orijinal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nouvo_lis = [eleman for i, eleman in enumerate(lis_orijinal) if i % 3 == 0]

print(nouvo_lis)


#5
lis_orijinal = [1, 2, 3, 4, 5, 6, 7, 8, 9]

nouvo_lis = [tuple(lis_orijinal[i:i+3]) for i in range(0, len(lis_orijinal), 3)]

print(nouvo_lis)


#6
lis_orijinal = [1, 2, 2, 3, 4, 4, 5, 5, 5]

lis_sans_doublon = []

[lis_sans_doublon.append(eleman) for eleman in lis_orijinal if eleman not in lis_sans_doublon]

print(lis_sans_doublon)


#7
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]

lis = [eleman for eleman in lis1 if eleman in lis2]

print(lis)


#8
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]

lis_distenksyon = [eleman for eleman in lis1 if eleman not in lis2] + [eleman for eleman in lis2 if eleman not in lis1]

print(lis_distenksyon)


#9
diksyone = {'kle1': 'valè1', 'kle2': 'valè2', 'kle3': 'valè3'}

lis_kle = list(diksyone.keys())

lis_valè = list(diksyone.values())

print("Liste kle:", lis_kle)
print("Liste valè:", lis_valè)


#10

lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis3 = [5, 6, 7, 8, 9]

lis_reyini = list(set(lis1) | set(lis2) | set(lis3))

print(lis_reyini)