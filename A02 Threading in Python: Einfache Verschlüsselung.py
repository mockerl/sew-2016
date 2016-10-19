import threading, time


class encoding(threading.Thread):
    """
    Diese Klasse stellt einen Thread dar,
    welcher einen text ent bzw. verschlüsselt
    """


    def __init__(self, thread_number, von, bis,speicher_,t,tun):
        """
        Initialisiert die Superklasse und speichert
        die Parameter in die Instanzvariablen.
        :param thread_number: Nummer des neuen Threads
        :param von: Zahl, von welcher an der thread für den text zuständig ist
        :param bis: zahl, bis welche der thread für den text zuständig ist
        :param speicher_: ort an den das egebnis gespeichert werden soll
        :param t: der text
        :param tun: wenn 1 dann encoden wenn 0 dann decodens
        """
        threading.Thread.__init__(self)
        self.thread_number = thread_number
        self.von=von
        self.bis=bis
        self.speicher=speicher_
        self.text=t
        self.tun=tun


    def run(self):
        """
        addiert bzw subtrahier 3 von ascii wert des textes für den der thread zuständig ist,
        schreibt sie in einen string der am ende mit der threadnummer als key in ein dictionary geschrieben.

        :return: None
        """
        if self.tun==1:
            encoded_text =""
            for i in self.text[int(self.von):int(self.bis)]:
                encoded_text=encoded_text + chr(ord(i)+3)
                time.sleep(0.01)
            self.speicher[self.thread_number]=encoded_text
        elif self.tun==0:
            encoded_text =""
            for i in self.text[int(self.von):int(self.bis)]:
                encoded_text=encoded_text + chr(ord(i)-3)
                time.sleep(0.01)
            self.speicher[self.thread_number]=encoded_text







def en():
    print("bitte geben sie die zu verschlüsselde zeichen ein")
    rein = input()
    rein=rein.upper()
    print(
        "geben sie die anzahl der threads ein mit denen verschlüsselt werden soll.\ndie zahl der trads darf die zahl der zeichen nicht übersteigen\nund muss einen rest von null ergeben")
    thr_anz = input()
    thr_anz = int(thr_anz)
    if len(rein) < thr_anz or len(rein)%thr_anz != 0:
        print("falsche anzahl threads ausgewält es wird automatisch die maximale anzahl von %s gewählt" % (len(rein)))
        thr_anz = len(rein)

    speicher={}

    # Fünf Threads erstellen und in einer Liste speichern
    threads = []
    abst = len(rein)/thr_anz
    for i in range(0, thr_anz):

        thread = encoding(i, i*abst, i*abst+abst, speicher, rein,1)
        threads += [thread]
        # Thread gleich starten
        thread.start()



    # Auf die Terminierung aller Threads warten
    for x in threads:
        x.join()



    #unsortiertes dictionary sortieren und in einen string schreiben
    s = ""
    for key in sorted(speicher):
        s=s+speicher[key]


    #ausgeben und beändern
    print("encodete nachricht:")
    print(s)
    input("druecken sie eine belibige taste zum beenden!\n")


def de():
    print("bitte geben sie die zu entschlüsselden zeichen ein")
    rein = input()
    rein = rein.upper()
    print(
        "geben sie die anzahl der threads ein mit denen entschlüsselt werden soll.\ndie zahl der trads darf die zahl der zeichen nicht übersteigen\nund muss einen rest von null ergeben")
    thr_anz = input()
    thr_anz = int(thr_anz)
    if len(rein) < thr_anz or len(rein) % thr_anz != 0:
        print("falsche anzahl threads ausgewält es wird automatisch die maximale anzahl von %s gewählt" % (len(rein)))
        thr_anz = len(rein)

    speicher = {0: "q"}

    # Fünf Threads erstellen und in einer Liste speichern


    threads = []
    abst = len(rein) / thr_anz
    for i in range(0, thr_anz):
        thread = encoding(i, i * abst, i * abst + abst, speicher, rein,0)
        threads += [thread]
        # Thread gleich starten
        thread.start()

    # Auf die Terminierung aller Threads warten
    for x in threads:
        x.join()

    # unsortiertes dictionary sortieren und in einen string schreiben
    s = ""
    for key in sorted(speicher):
        s = s + speicher[key]

    print("encodete nachricht:")
    print(s)
    input("druecken sie eine belibige taste zum beenden!\n")


wahl=input("geben sie 1 ein wenn sie verschlüsseln wollen oder 0 wenn sie entschlüsseln wollen!")
if wahl == "1":
    en()
elif wahl == "0":
    de()
else:
    print("wie kann mann so dumm sein??????")
    input("druecken sie eine belibige taste zum beenden!\n")
