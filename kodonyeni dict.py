import re

seq = ""
sozluk = dict(ATT="I", ATC="I", ATA="I", CTT="L", CTC="L", CTA="L", CTG="L", TTA="L", TTG="L", GTT="V", GTC="V",
              GTA="V", GTG="V", TTT="F", TTC="F", ATG="M", TGT="C", TGC="C", GCT="A", GCC="A", GCA="A", GCG="A",
              GGT="G", GGC="G", GGA="G", GGG="G", CCT="P", CCC="P", CCA="P", CCG="P", ACT="T", ACC="T", ACA="T",
              ACG="T", TCT="S", TCC="S", TCA="S", TCG="S", AGT="S", AGC="S", TAT="Y", TAC="Y", TGG="W", CAA="Q",
              CAG="Q", AAT="N", AAC="N", CAT="H", CAC="H", GAA="E", GAG="E", GAT="D", GAC="D", AAA="K", AAG="K",
              CGT="R", CGC="R", CGA="R", CGG="R", AGA="R", AGG="R", TAA="*", TAG="*", TGA="*")

optimize = dict(A="GCT", L="TTA", W="TGG", R="AGA", P="CCT", G="GGT", D="GAC", F="TTC", V="GTT", N="AAC", Q="CAA",
                H="CAC", C="TGC", S="TCT", E="GAA", Y="TAC", T="ACT", K="AAA", I="ATT", M="ATG")

def dna():
    global seq
    seq = input("DNA dizisini giriniz: ")
    seq = seq.upper()
    codons = [seq[i:i + 3] for i in range(0, len(seq), 3)]
    dizi = ''.join(str(sozluk.get(word, word)) for word in codons)
    seq = ''.join(str(sozluk.get(word, word)) for word in dizi)
    opt()
    sonuc()

def prot():
    global seq
    global sec
    seq = input("Protein dizisini giriniz :")
    seq = re.sub("[^A-Za-z]", "", seq)
    seq = seq.upper()
    opt()
    sonuc()

def opt():
    global optdizi
    optdizi = ''.join(str(optimize.get(word, word)) for word in seq)

def sonuc():
    print("\n")
    print('\x1b[0;30;43m' + "Kodon Optimize DNA: ", "5'", optdizi, "3'" + '\x1b[0m')
    print('\x1b[0;30;43m' + "Nükleotid Sayısı: ", str(len(optdizi)) + '\x1b[0m')
    print("----------------------")
    print('\x1b[0;30;42m' + "Protein Dizisi: ", seq + '\x1b[0m')
    print('\x1b[0;30;42m' + "Aminoasit Sayısı: ", str(len(seq)) + '\x1b[0m')
    secim = input("Yeni Bir Dizi Girmek İstiyor musunuz : Evet [1] - Hayır [2]: ")
    if secim == "1":
        sorgu()

def sorgu():
    print("Gireceğiniz Dizinin Türünü Seçiniz: ", "\n", "[1] DNA Dizisi", "\n", "[2] Protein Dizisi", "\n",
          "[3] Optimizasyonda Seçilen Kodonları Görüntüle", "\n", "[4] Seçilen Kodonlarda Değişiklik Yap")
    tip = input("Seçim: ")
    if tip == "1":
        dna()
    elif tip == "2":
        prot()
        opt()
    elif tip == "3":
        print("\n", "Kodon & Aminoasit Tablosu")
        for key, value in optimize.items():
            print(key, value)
        print("\n")
        secim = input("Menüye Dönmek İstiyor musunuz : Evet [1] - Hayır [2]: ")
        if secim == "1":
            sorgu()
    elif tip == "4":
        print("çalışıyor")
        sorgu()

    else:
        print("Yanlış Seçim Yaptınız: (", tip, ")")
        sorgu()

sorgu()
