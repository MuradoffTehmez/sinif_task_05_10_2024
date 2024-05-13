class Kitab:
    def __init__(self, ad, muellif, janr, nesr_ili):
        self.ad = ad
        self.muellif = muellif
        self.janr = janr
        self.nesr_ili = nesr_ili
        self.movcuddur = True

    def __str__(self):
        return f"{self.ad} ({self.nesr_ili}) - {self.muellif}, Janr: {self.janr}"

class Kitabxana:
    def __init__(self, ad):
        self.ad = ad
        self.kitablar = []

    def kitab_elave_et(self, kitab):
        self.kitablar.append(kitab)
        return f"'{kitab.ad}' kitabı {self.ad} kitabxanasına əlavə edildi."

    def movcud_kitablari_goster(self):
        if self.kitablar:
            movcud_kitablar = [str(kitab) for kitab in self.kitablar if kitab.movcuddur]
            if movcud_kitablar:
                return f"{self.ad} Kitabxanasının Mövcud Kitabları:\n" + "\n".join(movcud_kitablar)
            else:
                return f"{self.ad} kitabxanasında mövcud kitab yoxdur."
        else:
            return f"{self.ad} kitabxanasında kitab yoxdur."

    def kitab_gotur(self, kitab_adi):
        for kitab in self.kitablar:
            if kitab.ad == kitab_adi and kitab.movcuddur:
                kitab.movcuddur = False
                return f"'{kitab.ad}' kitabı {self.ad} kitabxanasından götürüldü."
        return f"'{kitab_adi}' kitabı ya götürülüb, ya da {self.ad} kitabxanasında mövcud deyil."

    def kitab_qaytar(self, kitab_adi):
        for kitab in self.kitablar:
            if kitab.ad == kitab_adi and not kitab.movcuddur:
                kitab.movcuddur = True
                return f"'{kitab.adi}' kitabı {self.ad} kitabxanasına qaytarıldı."
        return f"'{kitab_adi}' kitabı götürülməyib və ya {self.ad} kitabxanasında mövcud deyil."

    def goturulmus_kitablari_goster(self):
        goturulmus_kitablar = [str(kitab) for kitab in self.kitablar if not kitab.movcuddur]
        if goturulmus_kitablar:
            return f"{self.ad} Kitabxanasının Götürülmüş Kitabları:\n" + "\n".join(goturulmus_kitablar)
        else:
            return f"{self.ad} kitabxanasından hazırda götürülmüş kitab yoxdur."

    def kitablari_jansina_gore_goster(self, janr):
        janra_uygun_kitablar = [str(kitab) for kitab in self.kitablar if kitab.janr.lower() == janr.lower()]
        if janra_uygun_kitablar:
            return f"{self.ad} Kitabxanasının '{janr}' janrına aid Kitabları:\n" + "\n".join(janra_uygun_kitablar)
        else:
            return f"{self.ad} kitabxanasında '{janr}' janrına aid kitab yoxdur."

    def muellif_adina_gore_axtar(self, muellif_adi):
        tapilan_kitablar = [str(kitab) for kitab in self.kitablar if muellif_adi.lower() in kitab.muellif.lower()]
        if tapilan_kitablar:
            return f"{self.ad} Kitabxanasında '{muellif_adi}' müəllifinə aid Kitablar:\n" + "\n".join(tapilan_kitablar)
        else:
            return f"{self.ad} kitabxanasında '{muellif_adi}' müəllifinə aid kitab yoxdur."

# Kitabxana obyektinin yaradılması
milli_kitabxana = Kitabxana("Milli Kitabxana")

# Kitabların əlavə edilməsi
kitab1 = Kitab("Xosrov və Şirin", "Nizami Gəncəvi", "Dram", 1197)
kitab2 = Kitab("Qaçaq Nəbi", "Süleyman Rəhimov", "Roman", 1938)
kitab3 = Kitab("Ölülər", "Cəfər Cabbarlı", "Dram", 1923)
kitab4 = Kitab("Kəndçi qızı", "Mirzə Cəlil", "Povestlər", 1926)

milli_kitabxana.kitab_elave_et(kitab1)
milli_kitabxana.kitab_elave_et(kitab2)
milli_kitabxana.kitab_elave_et(kitab3)
milli_kitabxana.kitab_elave_et(kitab4)

# Mövcud kitabların göstərilməsi
print(milli_kitabxana.movcud_kitablari_goster())

# Kitab götürülməsi
print(milli_kitabxana.kitab_gotur("Qaçaq Nəbi"))
print(milli_kitabxana.kitab_gotur("Ölülər"))

# Götürülmüş kitabların göstərilməsi
print(milli_kitabxana.goturulmus_kitablari_goster())

# Kitabların janrına görə göstərilməsi
print(milli_kitabxana.kitablari_jansina_gore_goster("Dram"))

# Müəllif adına görə kitab axtarışı
print(milli_kitabxana.muellif_adina_gore_axtar("Mirzə Cəlil"))

# Kitab qaytarılması
print(milli_kitabxana.kitab_qaytar("Ölülər"))