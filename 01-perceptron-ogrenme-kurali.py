x1 = [1, 2, 3, 4, 5, 6]
x2 = [2, 2, 3, 4, 5, 5]

hedef_cikti = [0, 0, 0, 1, 1, 1]
w = [4, 4]
eta = 1
teta = -1.5  

def aktivasyon_fonksiyonu(x):
    if x < 0:
        return 0
    else:
        return 1

def cikti(i):
    return aktivasyon_fonksiyonu(w[0] * x1[i] + w[1] * x2[i] + teta)

def guncelle(i, cikti_degeri):
    global teta  
    w[0] = w[0] + eta * (hedef_cikti[i] - cikti_degeri) * x1[i]
    w[1] = w[1] + eta * (hedef_cikti[i] - cikti_degeri) * x2[i]
    teta = teta + eta * (hedef_cikti[i] - cikti_degeri)  

for i in range(len(x1)):  
    cikti_degeri = cikti(i) 
#    print(f"cikti({i}): {cikti_degeri}")
    if cikti_degeri != hedef_cikti[i]:
#        print("Hata var")
        guncelle(i, cikti_degeri)  
#        print(f"Güncellendi\nw: {w}\nteta: {teta}\n") 
    else:
        continue

if w[0] == 0:
    print(f"Optimum değerler:\nw1 = {w[0]}\nw2 = {w[1]}\nteta = {teta}\ny = aktivasyon_fonksiyonu({w[1]}*x2{teta})")
elif w[1] == 0:
    print(f"Optimum değerler:\nw1 = {w[0]}\nw2 = {w[1]}\nteta = {teta}\ny = aktivasyon_fonksiyonu({w[0]}*x1{teta})")
elif teta == 0:
    print(f"Optimum değerler:\nw1 = {w[0]}\nw2 = {w[1]}\nteta = {teta}\ny = aktivasyon_fonksiyonu({w[0]}*x1 +{w[1]}*x2)")

