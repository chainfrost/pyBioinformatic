__author__ = 'Srkn'
# -*- coding: utf-8 -*-
import re


def menu():
    global secim
    if secim == "1":
        giris()
    elif secim == "2":
        sorgu()
    elif secim == "3":
        hizalama()
    else:
        secim = input("Yanlış Seçim Yaptınız - Seçim: ")
        menu()


print("\n", "------DNA_py Program Menüsü------", "\n", "[1] Tm Hesaplama & PCR Mix", "\n", "[2] Kodon Optimizasyonu",
      "\n", "[3] Dikey Hizalama", "\n")
secim = input("İşlem Seçimi: ")

# -------------- [1] Tm & PCR Mix ------------
def reak():
    rh = float(input("Reaksiyon Hacmi (ul) "))
    ka = float(input("Kalıp miktarı (ul): "))
    tp = float(input("Tüp Sayısı : "))



    # Reaksiyon Elemanları
    b = 5.0  # buffer
    d = 2.0  # dntp
    fp = 2.5  # Forward Primer
    rp = 2.5  # Reverse Primer
    e = 2 / 10  # Enzim
    h = (rh - (b + d + fp + rp + e + ka))

    print(" ")
    print("---------Reaksiyon-------------")
    print("            Reak.      Mix", "(", int(tp), ")")
    print("Psbuffer   " + str(b) + " uL", "  | ", str(b * tp) + " uL")
    print("dntp       " + str(d) + " uL", "  | ", str(d * tp) + " uL")
    print("Fprimer    " + str(fp) + " uL", "  | ", str(fp * tp) + " uL")
    print("Rprimer    " + str(rp) + " uL", "  | ", str(rp * tp) + " uL")
    print("Kalıp      " + str(ka) + " uL", "  | ", " --")
    print("Enzim      " + str(e) + " uL", "  | ", str(format((e * tp), '.3g')) + " uL")
    print("dH20       " + str(h) + " ul"  "  | ", str(format((h * tp), '.3g')) + " uL")
    print("")
    print("--------- Tarif ----------")
    print("Her tüpe " + str(b + d + fp + rp + e + h) + " uL mix ekleyip " + str(int(ka)) +
          "uL kalıp aktarılacaktır.", "\n")


def tm():
    print("\n", "-----Tm Hesaplama Aracı")
    Fdizi = input("İleri Primer Dizisi: ")
    Rdizi = input("Geri Primer Dizisi ")
    FpTm = ((Fdizi.count("G") + Fdizi.count("C")) * 3 + ((Fdizi.count("A") + Fdizi.count("T")) * 2))
    # print (Fdizi.count("G") , Fdizi.count("C") , Fdizi.count("A") , Fdizi.count("T"))
    # print ((Fdizi.count("G") + Fdizi.count("C")) * 3)
    # print ((Fdizi.count("A") + Fdizi.count("T")) * 2)
    RpTm = ((Rdizi.count("G") + Rdizi.count("C")) * 3 + ((Rdizi.count("A") + Rdizi.count("T")) * 2))
    print("İleri Primer Tm: ", FpTm, "C'", "\n", "Geri Primer Tm: ", RpTm, "C'")

    ReakTm = ((FpTm + RpTm) / 2) - 5
    print("Reaksiyon Tm :", ReakTm, "\n")


def sorgu():
    y = input("Primer Tm Hesaplama için [1], Menüye Dönmek için [2]'ye basın: ")
    if y == "1":
        tm()
    else:
        giris()


def giris():
    print("\n", "[1] :Tm Hesaplama ", "\n", "[2] :PCR Mix Hesaplama ", "\n")
    m = input("Seçim :")
    if m == "1":
        tm(), sorgu()
    elif m == "2":
        reak(), sorgu()
    elif m == "3":
        menu()
    else:
        print("yanlış seçim")


# ----------------------------- Kodon Optimize Başlangıç ------------------------------------

seq = ""
sozluk = {"ATT": "I", "ATC": "I",
              "ATA": "I", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L", "TTA": "L", "TTG": "L",
              "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
              "TTT": "F", "TTC": "F",
              "ATG": "M",
              "TGT": "C", "TGC": "C",
              "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
              "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
              "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
              "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
              "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
              "TAT": "Y", "TAC": "Y",
              "TGG": "W",
              "CAA": "Q", "CAG": "Q",
              "AAT": "N", "AAC": "N",
              "CAT": "H", "CAC": "H",
              "GAA": "E", "GAG": "E",
              "GAT": "D", "GAC": "D",
              "AAA": "K", "AAG": "K",
              "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
              "TAA": "*", "TAG": "*", "TGA": "*"}

optimize = {"M": "ATG", "A": "GCT", "C": "TGC", "D": "GAC", "E": "GAA", "F": "TTC", "G": "GGT", "H": "CAC",
                "I": "ATT", "K": "AAA", "L": "TTA", "N": "AAC", "P": "CCT", "Q": "CAA", "R": "AGA", "S": "TCT",
                "T": "ACT", "V": "GTT", "Y": "TAC", "W": "TGG", "*": "TGA"}

def DNA():
    global seq
    seq = input("DNA dizisini giriniz: ")
    seq = seq.upper()
    codons = [seq[i:i + 3] for i in range(0, len(seq), 3)]
    dizi = ''.join(str(sozluk.get(word, word)) for word in codons)
    seq = ''.join(str(sozluk.get(word, word)) for word in dizi)
    opt()
    cıktı()

def prot():
    global seq
    global sec
    seq = input("Protein dizisini giriniz :")
    seq = re.sub("[^A-Za-z]", "", seq)
    seq = seq.upper()
    opt()
    cıktı()

def opt():
    global optimizedizi
    optimizedizi = ''.join(str(optimize.get(word, word)) for word in seq)

def cıktı():
    print("\n")
    print('\x1b[0;30;43m' + "Kodon Optimize DNA: ", "5'", optimizedizi, "3'" + '\x1b[0m')
    print('\x1b[0;30;43m' + "Nükleotid Sayısı: ", str(len(optimizedizi)) + '\x1b[0m')
    print("----------------------")
    print('\x1b[0;30;42m' + "Protein Dizisi: ", seq + '\x1b[0m')
    print('\x1b[0;30;42m' + "Aminoasit Sayısı: ", str(len(seq)) + '\x1b[0m')
    sec = input("Yeni Bir Dizi Girmek İstiyor musunuz : Evet [1] - Hayır [2]: ")
    if sec == "1":
        sorgu()
    else:
        menu()

def sorgu():
    print("Gireceğiniz Dizinin Türünü Seçiniz: ", "\n", "[1] DNA Dizisi", "\n", "[2] Protein Dizisi", "\n",
          "[3] Optimizasyonda Seçilen Kodonları Görüntüle", "\n", "[4] Seçilen Kodonlarda Değişiklik Yap")
    tip = input("Seçim: ")
    if tip == "1":
        DNA()
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

# ------------------ Dikey Hizalama-------------------

def hizalama():
    from Bio import pairwise2
    from Bio.pairwise2 import format_alignment

    dizi1 = (input("1. DNA Dizisi: "))
    dizi2 = (input("2. DNA Dizisi: "))
    alignments = pairwise2.align.globalxx(dizi1, dizi2)
    print("\n", "Hizalama Sonucu", "\n")
    print(format_alignment(*alignments[0]))

# -------Ana Program ---------------------------------

menu()
