import streamlit as st
score= 0

st.title("Python Quiz-Kapitel 1!")

if "score" not in st.session_state:
    st.session_state.score = 0

def berechne_score():
    st.session_state.score = 0



#Fragen Operatoren
st.subheader("Welcher Operator gibt den ganzzahligen Anteil einer Division zurück?")
antwort1 = st.multiselect("Wähle eine Antwort", ["/", "//", "%", "**"], default=[])
# Score initialisieren, falls nicht vorhanden
if "score" not in st.session_state:   #if "score" not in st.session_state:	Initialisierung, falls noch nicht vorhanden
    st.session_state.score = 0
# Richtige Antwort prüfen
if "//" in antwort1 and len(antwort1) == 1:  #if "/" in antwort1	Prüft, ob richtige Antwort gewählt
    st.session_state.score += 1              #len(antwort1) == 1	Stellt sicher, dass nur eine Antwort gegeben wurde
    st.success("Richtig!")                   #Meldung das die Frage richtig beantwortet wurde
elif len(antwort1) > 0:
    st.error("Falsch. Richtige Antwort: //")  #Anzeige das die Antwort Falsch ist und zeigt die richtige Antwort


st.subheader("Welche Aussage ist Falsch?:")
antwort2 = st.multiselect("Wähle eine Antwort",["5<10 ist True","4== 4 ist True","5!=6 ist True","3>=3 ist True"],key="antwort2",default=[])
if "5<10 ist True" in antwort2 and len(antwort2) == 1:
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort2) > 0:
    st.error("Falsch. Richtige Antwort: 5<10 ist True")

st.subheader("Was gibt 2*3 zurück?:")
antwort3 = st.text_input("Deine Antwort",key= "frage3") #jedes Streamlit-Element wie st.txt_input,/st.radio/st.checkbox braucht einen eindeutigen key, wenn du den gleichen text mehrfach verwendest.
if "6" in antwort3 and len(antwort3) == 1:
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort3) > 0:
    st.error("Falsch. Richtige Antwort: 6")


st.subheader("Welche Eingabe ergibt bei int(input(Zahl: + 5 das Ergebnis 15?")
antwort4 = st.multiselect("Wähle eine Antwort",["5","10","fünf"],key="antwort4",default=[])
if "10" in antwort4 and len(antwort4) == 1:
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort4) > 0:
    st.error("Falsch. Richtige Antwort: 10")


st.subheader("Was bewirkt der Operator !=?")
antwort5 = st.multiselect("Wähle eine Antwort",["Er prüft, ob zwei Werte gleich sind","Er prüft, ob zwei Werte unterschiedlich sind","Er gibt den Rest einer Divison wieder","Er wandelt einen String in Integer um"],key="antwort5",default=[])
if "Er prüft ob zwei Werte unterschiedlich sind" in antwort5 and len(antwort5) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort5) > 0:
    st.error("Falsch. Richtige Antwort: Er prüft ob zwei Werte unterschiedlich sind")


st.subheader("Was ergibt bool(0)?:")
antwort6 = st.multiselect("Wähle eine Antwort",["True","False","none","0"],key="antwort6",default=[])
if "False" in antwort6 and len(antwort6) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort6) > 0:
    st.error("Falsch. Richtige Antwort: False")

#Fragen Kontrollstrukturen

st.subheader("Wofür wird eine If-Anweisung verwendet?")
antwort7 = st.text_input("Deine Antwort",key="frage7")
if "Für die wenn dann Logik" in antwort7 and len(antwort7) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort7) > 0:
    st.error("Falsch. Richtige Antwort: Für die wenn dann Logik")

st.subheader("Was passiert, wenn die Bedingung in einer if Anweisung nicht erfüllt ist?")
antwort8 = st.multiselect("Wähle eine Antwort",["Der code im if_Block wird trotzdem ausgeführt","Das Programm stürzt sofort ab","Der Code im if-Block wird übersprungen und das Programm läuft normal weiter","Python wählt zufällig einen anderen Block aus, den es stattdessen ausführt"],key="antwort8",default=[])
if "Der Code im if Block wird übersprungen und das Programm läuft normal weiter" in antwort8 and len(antwort8) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort8) > 0:
    st.error("Falsch. Richtige Antwort Der Code im if Block wird übersprungen und das Programm läuft normal weiter")


st.subheader("Wie viele elif-Blöcke kann man in einer verzweigung verwenden?")
antwort9 = st.text_input("Deine Antwort",key="frage9")
if "So viele, wie man möchte" in antwort9 and len(antwort9) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort9) > 0:
    st.error("Falsch. Richtige Antwort: So viele, wie man möchte")


st.subheader("Kann man eine if-Anweisung ohne else schreiben?")
antwort10 = st.multiselect("Wähle eine Antwort",["JA!","Nein!"],key="antwort10",default=[])
if "JA!" in antwort10 and len(antwort10) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort10) > 0:
     st.error("Falsch. Richtige Antwort: JA!")


st.subheader("Was bedeutet == in Python?:")
antwort11 = st.text_input("Deine Antwort",key="frage11")
if "gleich" in antwort11 and len(antwort11) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort11) > 0:
    st.error("Falsch. Richtig Antwort: gleich")


st.subheader("Welcher Code prüft, ob eine Zahl größer als 100 ist?")
antwort12 = st.multiselect("Wähle eine Antwort",["If zahl >= 100","if zahl == 100","if zahl > 100","if 100 < zahl"],key="antwort12",default=[])
if "if zahl > 100" in antwort12 and len(antwort12) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort12) > 0:
    st.error("Falsch. Richtige Antwort: If zahl > 100 ")


st.subheader("Was prüft folgender Code? if x ==10 print x ist gleich 10")
antwort13 = st.multiselect("Wähle eine Antwort",["Ob x kleiner als 10 ist","Ob x ungleich 10 ist","Ob x gleich 10 ist","Ob x größer als 10 ist"],key="antwort13",default=[])
if "Ob x kleiner als 10 ist" in antwort13 and len(antwort13) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort13) > 0:
    st.error("Falsch. Richtige Antwort: Ob x kleiner als 10 ist")


st.subheader("Was ist korrekt bei if,elif und else?")
antwort14 = st.multiselect("Wähle eine Antwort",["Es darf nur if verwendet werden","Jedes if muss ein else haben","Elif kann nur einmal vorkommen","if,elif und else sind optional, aber if is Vorraussetzung"],key="antwort14",default=[])
if "if,elif und else sind optional, aber if is Vorraussetzung" in antwort14 and len(antwort14) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort14) > 0:
    st.error("Falsch. Richtige Antwort: if,elif und else sind optional, aber if ist Vorraussetzung")


#Fragen zu Funktionen / Wiederverwendbarkeit

st.subheader("Wie startet man eine Funktion in Python?")
antwort15 = st.text_input("Deine Antwort",key="frage15")
if "def funktion()" in  antwort15 and len(antwort15) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort15) > 0:
    st.error("Falsch. Richtige Antwort: def funktion()")


st.subheader("Welche Funktion hat zwei Parameter?")
antwort16 = st.multiselect("Wähle eine Antwort",["def sagen():","def rechnen(a):","def vergleichen(a, b)","def_hallo(nico)"],key="antwort16",default=[])
if "def vergleichen(a, b)" in antwort16 and len(antwort16) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort16) > 0:
    st.error("Falsch. Richtige Antwort: def vergleichen(a, b)")


st.subheader("Was ist eine Funktion in Python?")
antwort17 = st.multiselect("Wähle eine Antwort",["Eine Schleife,die unendlich oft läuft","Eine Art variabe für Zahlen","Ein wiederverwendbarer Codeblock mit einem Namen","Eine spezielle Art von Kommentar"],key="antwort17",default=[])
if "Ein wiederverwendbarer Codeblock mit einem Namen" in antwort17 and len(antwort17) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort17) > 0:
    st.error("Falsch. Richtige Antwort: Ein wiederverwendbarer Codeblock mit einem Namen")


st.subheader("Welche der Zeilen ruft ene Funktion namens begrüßung aus")
antwort18 = st.multiselect("Wähle eine Antwort",["def begrüßung","call begrüßung","begrüßung()","return begrüßung"],key="antwort18",default=[])
if "begrüßung()" in  antwort18 and len(antwort18) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort18) > 0:
    st.error("Falsch. Richtige Antwort: begrüßung()")


st.subheader("Was ist der Hauptvorteil von Funktionen?")
antwort19 = st.multiselect("Wähle eine Antwort",["Sie machen den Code länger","Sie speichern Daten","Sie helfen, den Code wiederzuverweden"],key="antwort19",default=[])
if "Sie helfen, den Code wiederzuverweden" in antwort19 and len(antwort19) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort19) > 0:
    st.error("Falsch. Richtige Antwort: Sie helfen, den Code wiederzuverweden")



st.subheader("Was sind Parameter?")
antwort20 = st.multiselect("Wähle eine Antwort",["Eine Fehlermeldung","Ein anderer Name für print","Ein Wert, den du einer Funktion übergibst","Der Titel eines Codes"],key="antwort20",default=[])
if "Ein Wert, den du einer Funktion übergibst" in antwort20 and len(antwort20) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort20) > 0:
    st.error("Falsch. Richtige Antwort: Ein Wert, den du einer Funktion übergibst")

st.subheader("Wie viele Parameter kann eine Funktion haben?")
antwort21 = st.text_input("Deine Antwort",key="frage21")
if "unbegrenzt" in  antwort21 and len(antwort21) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort21) > 0:
    st.error("Falsch. Richtige Antwort: unbegrenzt")

#Listen,Tuple,Set & Dictionaries

st.subheader("Wie greifst du auf den Wert im Dictionary zu ?")
antwort22 = st.multiselect("Wähle eine Antwort",["person.get(alter)","person.alter","person[alter]"],key="antwort22",default=[])
if "person.get(alter)" in  antwort22 and len(antwort22) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort22) > 0:
    st.error("Falsch. Richtige Antwort: person.get(alter)")


st.subheader("Welche Methode entfernt ein Element aus einer Liste")
antwort23 = st.multiselect("Wähle eine Antwort",[".delete",".remove",".cut",".destroy"],key="antwort23",default=[])
if ".remove" in antwort23 and len(antwort23) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort23) > 0:
    st.error("Falsch. Richtige Antwort: remove")


st.subheader("welche Struktur erlaubt keine doppelten Werte?")
antwort24 = st.multiselect("Wähle eine Antwort",["List","Tuple","Dictionary","Set"],key="antwort24",default=[])
if "Set" in antwort24 and len(antwort24) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort24) > 0:
    st.error("Falsch. Richtige Antwort: Set")


st.subheader("Wofür ist.append() zuständig?")
antwort25 = st.multiselect("Wähle eine Antwort",["Einen Wert zu einem Dictionary hinzufügen","Einen Wert am Ende einer Liste hinzufügen","Einen Wert aus einem Set entfernen", "Einen Wert aus einem Tupel entfernen"],key="antwort25",default=[])
if "Einen Wert am Ende einer Liste hinzuzufügen" in antwort25 and len(antwort25) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort25) > 0:
    st.error("Falsch. Richtige Antwort: Einen Wert am Ende einer Liste hinzuzufügen")



st.subheader("Welchen Datentypen sind nicht veränderbar?")
antwort26 = st.multiselect("Wähle eine Antwort",["List","Tuple","Dictionary","Set"],key="antwort26",default=[])
if "Tuple" in antwort26 and len(antwort26) == 1 :
    st.session_state.score = score + 1
    st.success("Richtig!")
elif len(antwort26) > 0:
    st.error("Falsch. Richtige Antwort: Tuple")



if st.button("Punkte anzeigen"):
    st.session_state.score = berechne_score()
st.markdown("-----")
st.subheader(f"Dein aktueller Punktestand: {st.session_state.score}")
