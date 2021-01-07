import csv
import math

x0t = []; x1t =[]; x2t =[]; x3t =[]; x4t =[]; x5t =[]; x6t = [];x7t = []; label = []#for train set
labeltest = []
train = csv.reader(open("Diabetes.csv")) #import Data Train

def distance(x0,x1,x2,x3,x4,x5,x6,x7,x0t,x1t,x2t,x3t,x4t,x5t,x6t,x7t): #rumus jarak
	root = (x0t-x0)**2+(x1t-x1)**2 + (x2t-x2)**2 + (x3t-x3)**2 + (x4t-x4)**2 + (x5t-x5)**2 +(x6t-x6)**2+(x7t-x7)**2
	return math.sqrt(root)

def voting(nol,satu):
    l_kategori=[]
    l_kategori.insert(0,nol)
    l_kategori.insert(1,satu)
    return (l_kategori)

#input K
nilai_k = int(input("Input nilai k: "))
#Pilih Dataset
dataset = "Pilih sorting:\n1.Baris ke-1 sampai baris ke-614 sebagai training set dan sisanya sebagai testing set\n2.Baris ke-1 sampai baris ke-461 ditambah baris ke-615 sampai 768 sebagai training set dan yang lain sebagai testing set\n3.Baris ke-1 sampai baris ke-307 ditambah baris ke-462 sampai 768 sebagai training set dan yang lain sebagai testing set\n4.Baris ke-1 sampai baris ke-154 ditambah baris ke-308 sampai 768 sebagai training set dan yang lain sebagai testing set\n5.Baris ke-155 sampai sampai 768 sebagai training set dan yang lain sebagai testing set\n\n Dataset yang dipilih adalah : "
data = input(dataset)
i = 0
x0 = []; x1 =[]; x2 =[]; x3 =[]; x4 =[]; x5 =[]; x6 = [];x7 = [] #for test set

#Pilih Dataset
if data == "1":
    for row in train:
        if i<=614 and i>0:#train
            x0t.append(row[0])
            x1t.append(row[1]) #Baca x1 dst
            x2t.append(row[2])
            x3t.append(row[3])
            x4t.append(row[4])
            x5t.append(row[5])
            x6t.append(row[6])
            x7t.append(row[7])
            label.append(row[8])
        elif i>614:#test
            x0.append(row[0])
            x1.append(row[1]) #Baca x1 dst
            x2.append(row[2])
            x3.append(row[3])
            x4.append(row[4])
            x5.append(row[5])
            x6.append(row[6])
            x7.append(row[7])
            labeltest.append(row[8])
        i = i +1

elif data=="2":
    for row in train:
        if i<=461 and i>0:#train
            x0t.append(row[0])
            x1t.append(row[1]) #Baca x1 dst
            x2t.append(row[2])
            x3t.append(row[3])
            x4t.append(row[4])
            x5t.append(row[5])
            x6t.append(row[6])
            x7t.append(row[7])
            label.append(row[8])
        elif i>=615 and i<=768:
            x0t.append(row[0])
            x1t.append(row[1]) #Baca x1 dst
            x2t.append(row[2])
            x3t.append(row[3])
            x4t.append(row[4])
            x5t.append(row[5])
            x6t.append(row[6])
            x7t.append(row[7])
            label.append(row[8])
        else:#test
            if i>0:
                x0.append(row[0])
                x1.append(row[1]) #Baca x1 dst
                x2.append(row[2])
                x3.append(row[3])
                x4.append(row[4])
                x5.append(row[5])
                x6.append(row[6])
                x7.append(row[7])
                labeltest.append(row[8])
        i = i +1

elif data=="3":
    for row in train:
        if i<=307 and i>0:#train
            x0t.append(row[0])
            x1t.append(row[1]) #Baca x1 dst
            x2t.append(row[2])
            x3t.append(row[3])
            x4t.append(row[4])
            x5t.append(row[5])
            x6t.append(row[6])
            x7t.append(row[7])
            label.append(row[8])
        elif i>=462 and i<=768:
            x0t.append(row[0])
            x1t.append(row[1]) #Baca x1 dst
            x2t.append(row[2])
            x3t.append(row[3])
            x4t.append(row[4])
            x5t.append(row[5])
            x6t.append(row[6])
            x7t.append(row[7])
            label.append(row[8])
        else:#test
            if i>0:
                x0.append(row[0])
                x1.append(row[1]) #Baca x1 dst
                x2.append(row[2])
                x3.append(row[3])
                x4.append(row[4])
                x5.append(row[5])
                x6.append(row[6])
                x7.append(row[7])
                labeltest.append(row[8])
        i = i +1

elif data=="4":
    for row in train:
        if i<=154 and i>0:#train
            x0t.append(row[0])
            x1t.append(row[1]) #Baca x1 dst
            x2t.append(row[2])
            x3t.append(row[3])
            x4t.append(row[4])
            x5t.append(row[5])
            x6t.append(row[6])
            x7t.append(row[7])
            label.append(row[8])
        elif i>=308 and i<=768:
            x0t.append(row[0])
            x1t.append(row[1]) #Baca x1 dst
            x2t.append(row[2])
            x3t.append(row[3])
            x4t.append(row[4])
            x5t.append(row[5])
            x6t.append(row[6])
            x7t.append(row[7])
            label.append(row[8])
        else:#test
            if i>0:
                x0.append(row[0])
                x1.append(row[1]) #Baca x1 dst
                x2.append(row[2])
                x3.append(row[3])
                x4.append(row[4])
                x5.append(row[5])
                x6.append(row[6])
                x7.append(row[7])
                labeltest.append(row[8])
        i = i +1

elif data=="5":
    for row in train:
        if i>=155 and i<768:#train
            x0t.append(row[0])
            x1t.append(row[1]) #Baca x1 dst
            x2t.append(row[2])
            x3t.append(row[3])
            x4t.append(row[4])
            x5t.append(row[5])
            x6t.append(row[6])
            x7t.append(row[7])
            label.append(row[8])
        else:#test
            if i>0:
                x0.append(row[0])
                x1.append(row[1]) #Baca x1 dst
                x2.append(row[2])
                x3.append(row[3])
                x4.append(row[4])
                x5.append(row[5])
                x6.append(row[6])
                x7.append(row[7])
                labeltest.append(row[8])
        i = i +1


n = 0    
x = []
sort = []
temp = []
urutkanjarak = []
dist =[]
kategori_akhir = []
while n<len(x0):
    c = 0
    while c < len(x0t):
        jarak = distance(float(x0[n]),float(x1[n]),float(x2[n]),float(x3[n]),float(x4[n]),float(x5[n]),float(x6[n]),float(x7[n]),float(x0t[c]),float(x1t[c]),float(x2t[c]),float(x3t[c]),float(x4t[c]),float(x5t[c]),float(x6t[c]),float(x7t[c]))
        urutkanjarak.insert(n,jarak)
        x.insert(c,jarak)
        x.extend(label[c])
        dist.extend(x)
        x.clear() #clear
        c = c+1
        #sort = sorted(x) #Sorting untuk mencari nilai jarak terdekat
    
    #Masukkan nilai K
    k = 0  
    sort = sorted(urutkanjarak)
    while k<nilai_k:   
        satu = 0
        nol = 0
        m =0
        while m< len(dist):
            if sort[k]==dist[m]:             
                m = m+1
                if dist[m]=='0':
                    nol = nol+1
                elif dist[m]=='1':
                    satu = satu+1
            else:
                m = m+1
        kategori=voting(nol,satu)
        k = k + 1
    if (kategori[1]==1):
        kategori_akhir.insert(n,1)
    else :
        kategori_akhir.insert(n,0)
   
    sort.clear()
    urutkanjarak.clear()
    dist.clear()
    n = n+1
#coba = []
pred = 0
l = 0


file = open('tebakan.csv', 'w') #eksport Data
with file:
    ws = csv.writer(file,lineterminator='\n')
    for val in kategori_akhir:
        ws.writerow([val])
print("Data sudah di output sebagai 'tebakan.csv'")

labelpred = []
tebakan = csv.reader(open("tebakan.csv")) #import Data Train
for row in tebakan:
    labelpred.append(row[0])


while l<len(kategori_akhir):
    if (labelpred[l]==labeltest[l]):
        pred = pred + 1
    else:
        pass
    l = l+1

prediksi = 0
print("Total Prediksi yang benar: ",pred,"/",len(labeltest),"data")
prediksi = pred/len(labeltest)
print("Akurasinya adalah : ","{:.0%}".format(prediksi))
#penampung 1 untuk sorting dan satu untuk dibandingkan dengan sorting agar diketahui dimana labelnya
#if xt0 == 1 then satu = satu+1
#bandingkan melalui k, mana yang lebih banyak 
#sorting
#pilih terdekat sesuai K (tetangga)
#pilih tetangga terbanyak label yang sama
