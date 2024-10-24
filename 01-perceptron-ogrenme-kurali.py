x1 = [1, 2, 3, 4, 5, 6]
x2 = [2, 2, 3, 4, 5, 5]

hedef_cikti = [0, 0, 0, 1, 1, 1]
w = [4, 4]
eta = 1
teta = -1.5  

"""
AND KAPISI İÇİN DEĞERLER

x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
hedef_cikti = [0, 0, 0, 1] 

w = [0.25, -0.75]  
eta = 0.5  
teta = -0.5  
"""

def aktivasyon_fonksiyonu(x):
    return 1 if x >= 0 else 0

def cikti(i):
    return aktivasyon_fonksiyonu(w[0] * x1[i] + w[1] * x2[i] + teta)

def guncelle(i, cikti_degeri):
    global teta
    error = hedef_cikti[i] - cikti_degeri
    w[0] += eta * error * x1[i]
    w[1] += eta * error * x2[i]
    teta += eta * error


total_error = 1  
while total_error != 0:
    total_error = 0  
    for i in range(len(x1)):
        cikti_degeri = cikti(i)
        if cikti_degeri != hedef_cikti[i]:
            guncelle(i, cikti_degeri)
            total_error += 1  
    
    #print(f"Ağırlıklar [w1,w2]: {w}, Teta: {teta}, Total Errors: {total_error}")

# Optimum ağırlıklar ve teta değeri
print(f"Optimum değerler:\nw1 = {w[0]}\nw2 = {w[1]}\nteta = {teta}")
