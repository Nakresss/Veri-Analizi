import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

#basit doğrusal regresyon (bağımlı ve bağımsız değişken arasındaki ilişkiyi ifade eden doğrusal fonksiyonu bulmak.)
veriseti = input("lütfen veri setini gösterin(Bu set programla aynı dosyada olmalı):")
ad = pd.read_csv(veriseti)
df = ad.copy()
df = df.iloc[:,1:len(df)]
df.head()
#Veri işlemleri
print("veriseti infosu=",df.info())
print("veriseti betimsel istatistik ve transpozon",df.describe().T)
print("verinin eksik gözlemi=",df.isnull().values.any())
print("değişkenlerin dağılımı ve korolasyonu=",df.corr())
print("Veri grafiği",sns.pairplot(df,kind ="reg"))
istek = input("odaklanmak istediğiniz bir yer var mı? Y/N")
if istek =="N":
    pass
elif istek=="Y":
    s = input("ilkini yazınız.")
    e = input("ikincisini yazınız")
    print("istediğiniz odaklanılan yerler",sns.joinplot(x="s",y="e",data = df,kind = "reg"))
else:
    pass
#Statsmodels ile modelleme
istek1 = input("Statsmodels kullanmak istermisiniz? Y/N")
if istek1 == "N":
    pass
elif istek1 == "Y":
    r = input("Lütfen istediğiniz statın adını giriniz")
    x = df[["r"]]
    print("istediğiniz stat sıralanmıştır.",x[0:5])
    #Matris işlemi
    a=input("matris halini görmek ister misin? Y/N")
    if a == "Y":
        x =sm.add_constant(x)
        print("verinin matris hali:",x[0:5])
    else:
        pass

else:
    pass

#Model kurma işlemi
k = input("Model kurmak ister misinz? Y/N")
if k == "Y":
    lm = sm.OLMS(y,X)
    model = lm.fit()
    print(model)
    n = input("Modelde statlara bakmak ister misiniz? Y/N")
    if n == "Y":
        c = input("lütfen birinci statı girin:")
        e = input("lütfen ikinci statı girin:")
        lm = smf.ols(c,e,df)
        model= lm.fit()
        print(model.params)
        print(model.summary().tables[1])
        print(model.conf_int())
        print(model.f_pvalue)
        print("f_pvalue:","%.3f" %model.f_value)
        print("fvalue:","%.2f" %model.fvalue)
        print("tvalues:","%.3f" %model.tvalues[0:1])
        print("model hatası sonuçları",model.mse_model)
        print("Açıklanabilirlik oranı:",model.rsquared_adj)
        g = sns.regplot(df[c],df[e],ci=None,scatter_kws={"color":"red","s":9})
        g.set_title("Model Denklemi")
        g.set_ylabel()
        g.set_xlabel()
        plt.xlim(-10,310)
        plt.ylim(bottom=0); 
    else:
        pass
else:
    pass


