import datetime

casy_odjezdu_pracovni_den = [
    "04:28", "04:58",
    "05:16", "05:28", "05:38", "05:44", "05:58",
    "06:08", "06:16", "06:28", "06:38", "06:44", "06:58",
    "07:08", "07:16", "07:28", "07:38", "07:44", "07:58",
    "08:08", "08:16", "08:28", "08:38", "08:44", "08:58",
    "09:08", "09:16", "09:28", "09:44", "09:58",
    "10:16", "10:28", "10:44", "10:58",
    "11:16", "11:28", "11:44", "11:58",
    "12:16", "12:28", "12:44", "12:58",
    "13:16", "13:28", "13:44", "13:58",
    "14:16", "14:28", "14:38", "14:44", "14:58",
    "15:08", "15:16", "15:28", "15:38", "15:44", "15:58",
    "16:08", "16:16", "16:28", "16:38", "16:44", "16:58",
    "17:08", "17:16", "17:28", "17:38", "17:44", "17:58",
    "18:08", "18:16", "18:28", "18:38", "18:44", "18:58",
    "19:08", "19:16", "19:28", "19:38", "19:44", "19:58",
    "20:14", "20:28", "20:44", "20:58",
    "21:14", "21:28", "21:44", "21:58",
    "22:28", "22:58",
    "23:35", "23:54"
]
casy_odjezdu_vikend = [
    "04:28", "04:58",
    "05:28", "05:58",
    "06:28", "06:44", "06:58",
    "07:28", "07:44", "07:58",
    "08:28", "08:44", "08:58",
    "09:28", "09:44", "09:58",
    "10:28", "10:44", "10:58",
    "11:28", "11:44", "11:58",
    "12:28", "12:44", "12:58",
    "13:28", "13:44", "13:58",
    "14:28", "14:44", "14:58",
    "15:28", "15:44", "15:58",
    "16:28", "16:44", "16:58",
    "17:28", "17:44", "17:58",
    "18:28", "18:44", "18:58",
    "19:28", "19:44", "19:58",
    "20:28", "20:44", "20:58",
    "21:28", "21:44", "21:58",
    "22:28", "22:58",
    "23:35", "23:54"
]

def ziskej_casy_odjezdu():
    dnes = datetime.datetime.now()
    je_vikend = dnes.weekday() >= 5  
    if je_vikend:
        return casy_odjezdu_vikend
    else:
        return casy_odjezdu_pracovni_den

def najdi_nejblizsi_vlak(casy_odjezdu):
    ted = datetime.datetime.now().time()
    cas_nyni = datetime.datetime.strptime(str(ted)[:5], "%H:%M")

    nejblizsi_vlak = None

    for odjezd in casy_odjezdu:
        odjezd_objekt = datetime.datetime.strptime(odjezd, "%H:%M")
        if odjezd_objekt > cas_nyni:
            nejblizsi_vlak = odjezd
            break

    if nejblizsi_vlak:
        return f"Nejbližší vlak jede v {nejblizsi_vlak}."
    else:
        return "Žádný vlak už dnes neodjede."

def najdi_vlak_pro_prijezd(casy_odjezdu, cas_prijezdu):
    cas_prijezdu_objekt = datetime.datetime.strptime(cas_prijezdu, "%H:%M")
    nejpozdejsi_vlak = None

    for odjezd in casy_odjezdu:
        hodina, minuta = map(int, odjezd.split(":"))
        odjezd_objekt = datetime.datetime.strptime(odjezd, "%H:%M")

        if minuta == 44:
            doba_cesty = datetime.timedelta(minutes=16)
        else:
            doba_cesty = datetime.timedelta(minutes=14)

        cas_prijezdu_z_vlaku = odjezd_objekt + doba_cesty

        if cas_prijezdu_z_vlaku <= cas_prijezdu_objekt:
            nejpozdejsi_vlak = odjezd

    if nejpozdejsi_vlak:
        return f"Nejpozdější vlak, kterým se stihneš dostat, je v {nejpozdejsi_vlak}."
    else:
        return "Není žádný vlak, který by tě stihl na čas."

def main():
    casy_odjezdu = ziskej_casy_odjezdu()

    volba = input("Chceš zadat čas příjezdu? (ano/ne): ").strip().lower()

    if volba == "ne":
        print(najdi_nejblizsi_vlak(casy_odjezdu))
    elif volba == "ano":
        cas_prijezdu = input("Zadej čas příjezdu (HH:MM): ")
        print(najdi_vlak_pro_prijezd(casy_odjezdu, cas_prijezdu))
    else:
        print("Neplatná volba.")

if __name__ == "__main__":
    main()