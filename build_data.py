import json, math, random, os
from pathlib import Path
ROOT=Path('/mnt/data/zp10_eesa_website')
DATA=ROOT/'data'; DATA.mkdir(exist_ok=True)

THEMES=[
 {'id':'zahlen','name':'Zahlen & Rechnen','icon':'123','desc':'Zahlvorstellung, Brüche, Dezimalzahlen, negative Zahlen und Grundrechenarten'},
 {'id':'groessen','name':'Größen & Einheiten','icon':'↔','desc':'Länge, Fläche, Volumen, Masse, Zeit und Umrechnungen'},
 {'id':'prozent','name':'Prozent- & Zinsrechnung','icon':'%','desc':'Prozentwert, Grundwert, Prozentsatz, Rabatt und einfache Zinsen'},
 {'id':'terme','name':'Terme & Gleichungen','icon':'x','desc':'Terme einsetzen, vereinfachen, Gleichungen lösen und Fehler erkennen'},
 {'id':'funktionen','name':'Funktionen & Zuordnungen','icon':'↗','desc':'Proportionale und lineare Zuordnungen, Tabellen, Graphen und Wachstum'},
 {'id':'geometrie','name':'Geometrie','icon':'△','desc':'Flächen, Winkel, Symmetrie, Maßstab und Satz des Pythagoras'},
 {'id':'koerper','name':'Körper & Messen','icon':'◼','desc':'Volumen, Oberfläche und Sachaufgaben zu Würfel, Quader, Prisma, Zylinder und Kugel'},
 {'id':'daten','name':'Daten & Wahrscheinlichkeit','icon':'▥','desc':'Diagramme, Mittelwert, Median, Spannweite, Schätzen und Wahrscheinlichkeit'}
]
json.dump(THEMES, open(DATA/'themes.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)

FLASH={
'zahlen':[
('natürliche Zahl','Eine Zahl aus 0, 1, 2, 3, …'),('ganze Zahl','Natürliche Zahlen, ihre Gegenzahlen und 0.'),('Bruch','Darstellung eines Anteils mit Zähler und Nenner.'),('Zähler','Zahl oberhalb des Bruchstrichs.'),('Nenner','Zahl unterhalb des Bruchstrichs.'),('Dezimalzahl','Zahl mit Komma, die Stellenwerte wie Zehntel oder Hundertstel enthält.'),('Betrag','Abstand einer Zahl von 0 auf der Zahlengeraden.'),('Kehrwert','Bruch, der durch Vertauschen von Zähler und Nenner entsteht.'),('Potenz','Kurzschreibweise für wiederholte Multiplikation gleicher Faktoren.'),('Quadratzahl','Zahl, die als Produkt einer natürlichen Zahl mit sich selbst entsteht.')],
'groessen':[
('Länge','Größe zur Beschreibung einer Strecke, z. B. in m oder km.'),('Fläche','Größe einer zweidimensionalen Figur, z. B. in m².'),('Volumen','Rauminhalt eines Körpers, z. B. in cm³ oder l.'),('Masse','Größe für die Menge an Materie, z. B. in g oder kg.'),('Zeitspanne','Dauer zwischen zwei Zeitpunkten.'),('Maßstab','Verhältnis von Länge in einer Darstellung zur Länge in Wirklichkeit.'),('Quadratmeter','Flächeneinheit; 1 m² = 100 dm².'),('Kubikdezimeter','Volumeneinheit; 1 dm³ = 1 l.'),('Milliliter','Volumeneinheit; 1 ml = 1 cm³.'),('Tonne','Masseneinheit; 1 t = 1000 kg.')],
'prozent':[
('Grundwert','Die gesamte Bezugsgröße; entspricht 100 %.'),('Prozentwert','Der Anteil des Grundwertes, der zu einem Prozentsatz gehört.'),('Prozentsatz','Gibt an, wie viele Hundertstel des Grundwertes gemeint sind.'),('Rabatt','Preisnachlass, meist in Prozent angegeben.'),('Zinsen','Entgelt für geliehenes oder angelegtes Geld.'),('Kapital','Geldbetrag, auf den Zinsen berechnet werden.'),('Zinssatz','Prozentsatz, mit dem Zinsen berechnet werden.'),('Zinsfaktor','Faktor q für eine prozentuale Zu- oder Abnahme.'),('Mehrwertsteuer','Prozentualer Steueranteil auf Waren und Dienstleistungen.'),('relative Änderung','Änderung im Verhältnis zum Ausgangswert, häufig in Prozent.')],
'terme':[
('Term','Mathematischer Rechenausdruck ohne Gleichheitszeichen.'),('Variable','Platzhalter für eine Zahl, meist mit einem Buchstaben bezeichnet.'),('Gleichung','Mathematische Aussage, dass zwei Terme gleich sind.'),('Lösung einer Gleichung','Wert der Variablen, für den die Gleichung wahr ist.'),('Äquivalenzumformung','Umformung, die die Lösungsmenge einer Gleichung nicht verändert.'),('Klammerregel','Regel: Zuerst werden Rechnungen in Klammern ausgeführt.'),('Punkt-vor-Strich','Multiplikation und Division werden vor Addition und Subtraktion ausgeführt.'),('Einsetzen','Eine Variable durch einen konkreten Zahlenwert ersetzen.'),('Ausmultiplizieren','Klammern mithilfe des Distributivgesetzes auflösen.'),('Zusammenfassen','Gleichartige Terme addieren oder subtrahieren.')],
'funktionen':[
('Funktion','Eindeutige Zuordnung: Jedem x-Wert wird genau ein y-Wert zugeordnet.'),('Wertetabelle','Tabelle mit zusammengehörigen x- und y-Werten.'),('Graph','Grafische Darstellung einer Funktion im Koordinatensystem.'),('lineare Funktion','Funktion mit einer Geraden als Graph, meist y = m·x + n.'),('Steigung','Gibt an, um wie viel y sich ändert, wenn x um 1 steigt.'),('y-Achsenabschnitt','y-Wert, an dem eine Gerade die y-Achse schneidet.'),('proportionale Zuordnung','Zuordnung mit konstantem Quotienten y/x und Graph durch den Ursprung.'),('antiproportionale Zuordnung','Zuordnung mit konstantem Produkt x·y.'),('Wachstumsfaktor','Faktor q, mit dem ein Wert in jedem Schritt multipliziert wird.'),('exponentielles Wachstum','Wachstum, bei dem in gleichen Zeitabständen mit demselben Faktor multipliziert wird.')],
'geometrie':[
('Umfang','Länge des Randes einer ebenen Figur.'),('Flächeninhalt','Größe der Fläche einer ebenen Figur.'),('Radius','Strecke vom Mittelpunkt eines Kreises zum Rand.'),('Durchmesser','Doppelte Länge des Radius; verläuft durch den Kreismittelpunkt.'),('Symmetrieachse','Gerade, an der eine Figur gespiegelt werden kann und gleich aussieht.'),('rechter Winkel','Winkel mit 90°.'),('Hypotenuse','Längste Seite im rechtwinkligen Dreieck, gegenüber dem rechten Winkel.'),('Kathete','Eine der beiden Seiten, die im rechtwinkligen Dreieck den rechten Winkel bilden.'),('Satz des Pythagoras','Im rechtwinkligen Dreieck gilt a² + b² = c².'),('Maßstab 1:n','1 Längeneinheit in der Zeichnung entspricht n Längeneinheiten in Wirklichkeit.')],
'koerper':[
('Grundfläche','Fläche, auf der ein Körper steht bzw. die bei Prisma/Zylinder parallel verschoben wird.'),('Mantelfläche','Seitenfläche eines Körpers ohne Grund- und Deckfläche.'),('Oberfläche','Summe aller Begrenzungsflächen eines Körpers.'),('Volumen','Rauminhalt eines Körpers.'),('Prisma','Körper mit zwei kongruenten parallelen Grundflächen.'),('Zylinder','Körper mit zwei parallelen Kreisflächen als Grund- und Deckfläche.'),('Pyramide','Körper mit einer Grundfläche und dreieckigen Seitenflächen, die sich in einer Spitze treffen.'),('Kegel','Körper mit Kreis als Grundfläche und einer Spitze.'),('Kugel','Körper, dessen Oberflächenpunkte alle denselben Abstand vom Mittelpunkt haben.'),('Kantenlänge','Länge einer Kante eines Körpers.')],
'daten':[
('arithmetisches Mittel','Summe aller Werte geteilt durch die Anzahl der Werte.'),('Median','Mittlerer Wert einer der Größe nach geordneten Datenliste.'),('Spannweite','Differenz aus größtem und kleinstem Wert.'),('Säulendiagramm','Diagramm mit senkrechten Säulen zur Darstellung von Werten.'),('Kreisdiagramm','Diagramm zur Darstellung von Anteilen eines Ganzen.'),('absolute Häufigkeit','Anzahl, wie oft ein Ereignis oder Wert vorkommt.'),('relative Häufigkeit','Anteil einer Häufigkeit an der Gesamtzahl.'),('Wahrscheinlichkeit','Zahl zwischen 0 und 1 bzw. 0 % und 100 %, die die Chance eines Ereignisses beschreibt.'),('Laplace-Experiment','Zufallsexperiment, bei dem alle Elementarereignisse gleich wahrscheinlich sind.'),('Schätzen','Näherungsweises Bestimmen eines Wertes mit begründeter Vorgehensweise.')]
}
for t in THEMES:
    cards=[]
    # 20 cards per theme by adding application cards
    base=FLASH[t['id']]
    for i,(term,definition) in enumerate(base):
        cards.append({'id':f"{t['id']}-c{i+1}",'term':term,'definition':definition})
    extras=[]
    if t['id']=='zahlen': extras=[('Gegenzahl','Zahl mit gleichem Betrag und umgekehrtem Vorzeichen.'),('Zahlengerade','Gerade, auf der Zahlen geordnet dargestellt werden.'),('Dezimalbruch','Bruch mit Nenner 10, 100, 1000, …'),('Runden','Ersetzen einer Zahl durch einen nahegelegenen Wert mit weniger Stellen.'),('Überschlag','Grobe Rechnung mit gerundeten Zahlen zur Kontrolle eines Ergebnisses.'),('Primzahl','Natürliche Zahl größer als 1 mit genau zwei Teilern.'),('Teiler','Zahl, durch die eine andere Zahl ohne Rest teilbar ist.'),('Vielfaches','Produkt einer Zahl mit einer natürlichen Zahl.'),('Wurzel','Umkehrung des Quadrierens.'),('Vorzeichen','Plus oder Minus vor einer Zahl.')]
    elif t['id']=='groessen': extras=[('Sekunde','Basiseinheit der Zeit.'),('Minute','60 Sekunden.'),('Stunde','60 Minuten.'),('Kilometer','1000 Meter.'),('Dezimeter','Ein Zehntel Meter.'),('Zentimeter','Ein Hundertstel Meter.'),('Gramm','Ein Tausendstel Kilogramm.'),('Liter','Volumeneinheit; 1 l = 1 dm³.'),('Quadratzentimeter','Flächeneinheit; 100 cm² = 1 dm².'),('Kubikzentimeter','Volumeneinheit; 1000 cm³ = 1 dm³.')]
    elif t['id']=='prozent': extras=[('100 %','Der gesamte Grundwert.'),('50 %','Die Hälfte.'),('25 %','Ein Viertel.'),('10 %','Ein Zehntel.'),('1 %','Ein Hundertstel.'),('Preisnachlass','Betrag, der vom ursprünglichen Preis abgezogen wird.'),('Preissteigerung','Erhöhung eines Ausgangspreises.'),('Brutto','Preis oder Betrag inklusive Steuer.'),('Netto','Preis oder Betrag ohne Steuer.'),('Zinseszins','Zinsen, die auch auf bereits gutgeschriebene Zinsen berechnet werden.')]
    elif t['id']=='terme': extras=[('linke Seite','Term links vom Gleichheitszeichen.'),('rechte Seite','Term rechts vom Gleichheitszeichen.'),('Probe','Einsetzen der Lösung zur Überprüfung einer Gleichung.'),('Distributivgesetz','a·(b+c)=a·b+a·c.'),('Kommutativgesetz','Reihenfolge beim Addieren oder Multiplizieren darf vertauscht werden.'),('Assoziativgesetz','Klammern bei Addition oder Multiplikation dürfen umgruppiert werden.'),('Koeffizient','Zahlfaktor vor einer Variablen.'),('Konstante','Zahl ohne Variable.'),('Ungleichung','Vergleich zweier Terme mit <, >, ≤ oder ≥.'),('Formel','Allgemeine mathematische Beziehung zwischen Größen.')]
    elif t['id']=='funktionen': extras=[('Nullstelle','x-Wert, bei dem y=0 ist.'),('Koordinatensystem','System aus x- und y-Achse zur Darstellung von Punkten und Graphen.'),('Punktkoordinate','Schreibweise (x|y) für die Lage eines Punktes.'),('Ursprung','Punkt (0|0).'),('steigende Gerade','Gerade mit positiver Steigung.'),('fallende Gerade','Gerade mit negativer Steigung.'),('konstante Funktion','Funktion mit waagerechtem Graphen.'),('Startwert','Wert zu Beginn eines Wachstumsprozesses.'),('prozentuale Zunahme','Wachstum um einen festen Prozentsatz je Schritt.'),('prozentuale Abnahme','Abnahme um einen festen Prozentsatz je Schritt.')]
    elif t['id']=='geometrie': extras=[('Quadrat','Viereck mit vier gleich langen Seiten und vier rechten Winkeln.'),('Rechteck','Viereck mit vier rechten Winkeln.'),('Dreieck','Figur mit drei Seiten.'),('Parallelogramm','Viereck mit paarweise parallelen Gegenseiten.'),('Trapez','Viereck mit mindestens einem Paar paralleler Seiten.'),('Kreis','Menge aller Punkte mit gleichem Abstand zum Mittelpunkt.'),('Kreisbogen','Teil des Kreisumfangs.'),('Kreissektor','Teil einer Kreisfläche zwischen zwei Radien und einem Kreisbogen.'),('parallel','Geraden, die sich nicht schneiden.'),('senkrecht','Geraden, die einen rechten Winkel bilden.')]
    elif t['id']=='koerper': extras=[('Würfel','Quader mit sechs kongruenten quadratischen Flächen.'),('Quader','Körper mit sechs rechteckigen Flächen.'),('Netz','Ebene Darstellung aller Flächen eines Körpers zum Zusammenfalten.'),('Körperhöhe','Senkrechter Abstand zwischen Grund- und Deckfläche bzw. Grundfläche und Spitze.'),('Mantellinie','Schräge Seitenlinie eines Kegels.'),('Raumdiagonale','Verbindung zweier gegenüberliegender Ecken im Raum.'),('Deckfläche','Zur Grundfläche parallele kongruente Fläche bei Prisma oder Zylinder.'),('Kubikmeter','Volumeneinheit; 1 m³ = 1000 dm³.'),('Oberflächeninhalt','Flächeninhalt der gesamten Oberfläche eines Körpers.'),('Hohlkörper','Körper mit einem inneren, leeren Raum.')]
    else: extras=[('Minimum','Kleinster Wert einer Datenmenge.'),('Maximum','Größter Wert einer Datenmenge.'),('Stichprobe','Teilmenge, die untersucht wird.'),('Grundgesamtheit','Gesamtheit aller interessierenden Objekte.'),('Zufallsexperiment','Vorgang mit nicht sicher vorhersagbarem Ergebnis.'),('Ergebnis','Möglicher Ausgang eines Zufallsexperiments.'),('Ereignis','Menge von Ergebnissen eines Zufallsexperiments.'),('Baumdiagramm','Darstellung mehrstufiger Zufallsexperimente mit Ästen.'),('Balkendiagramm','Diagramm mit waagerechten Balken.'),('Piktogramm','Diagramm, das Mengen durch wiederholte Symbole darstellt.')]
    for j,(term,definition) in enumerate(extras): cards.append({'id':f"{t['id']}-c{len(base)+j+1}",'term':term,'definition':definition})
    json.dump(cards, open(DATA/f'flashcards_{t["id"]}.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)


def q(id,theme,diff,prompt,answer,solution,h1='',h2='',choices=None,qtype='input',source=None,unit=None,tolerance=1e-6):
    return {'id':id,'theme':theme,'difficulty':diff,'prompt':prompt,'answer':answer,'solution':solution,'hint1':h1,'hint2':h2,'choices':choices or [],'type':qtype,'source':source,'unit':unit,'tolerance':tolerance}

def de(x, digits=None):
    if digits is not None: s=f"{x:.{digits}f}"
    else: s=(f"{x:.8f}").rstrip('0').rstrip('.')
    return s.replace('.',',')

def make_theme(theme):
    r=random.Random({'zahlen':11,'groessen':12,'prozent':13,'terme':14,'funktionen':15,'geometrie':16,'koerper':17,'daten':18}[theme])
    arr=[]
    i=1
    def add(*args,**kwargs):
        nonlocal i
        arr.append(q(f'{theme}-{i:03d}',theme,*args,**kwargs)); i+=1
    if theme=='zahlen':
        # 10 structural families x 10 varied contexts/number patterns
        for k in range(10):
            vals=[r.randint(-80,-1)/10,r.randint(-20,20)/10,r.randint(1,90)/10,r.randint(-90,-1)/10]
            order=sorted(vals)
            add('leicht',f"Ordne die Zahlen der Größe nach (kleinste zuerst): {', '.join(de(v,1) for v in vals)}",";".join(de(v,1) for v in order),"Auf der Zahlengeraden liegen kleinere Zahlen weiter links. Ergebnis: "+" < ".join(de(v,1) for v in order),'Achte besonders auf negative Zahlen.','Bei negativen Zahlen ist die Zahl mit dem größeren Betrag kleiner.')
        for k in range(10):
            a=r.randint(20,90); b=r.choice([4,5,10,20,25,50,100]); frac=a/b; d=round(frac,3)
            add('leicht',f"Schreibe den Bruch {a}/{b} als Dezimalzahl.",de(d),f"Teile {a} durch {b}: {a}:{b}={de(d)}.",'Ein Bruchstrich bedeutet Division.','Rechne Zähler : Nenner.')
        for k in range(10):
            a=r.randint(120,999); b=r.randint(20,99)
            op=r.choice(['+','-'])
            ans=a+b if op=='+' else a-b
            add('leicht',f"Berechne {a} {op} {b}.",str(ans),f"{a} {op} {b} = {ans}",'Rechne stellenweise.','Kontrolliere mit einem Überschlag.')
        for k in range(10):
            a=r.randint(12,49); b=r.randint(3,12); ans=a*b
            add('leicht',f"Berechne {a} · {b}.",str(ans),f"{a}·{b}={ans}",'Zerlege einen Faktor.','Nutze z. B. das Distributivgesetz.')
        for k in range(10):
            b=r.randint(3,15); ans=r.randint(12,60); a=b*ans
            add('leicht',f"Berechne {a} : {b}.",str(ans),f"{a}:{b}={ans}",'Suche den passenden Faktor.','Welche Zahl mal '+str(b)+' ergibt '+str(a)+'?')
        for k in range(10):
            a=r.randint(2,12); b=r.randint(2,12); c=r.randint(1,15); ans=a*b+c
            add('mittel',f"Berechne unter Beachtung von Punkt-vor-Strich: {a} · {b} + {c}.",str(ans),f"Zuerst {a}·{b}={a*b}, dann +{c}={ans}.",'Multipliziere zuerst.','Punktrechnung vor Strichrechnung.')
        for k in range(10):
            n=r.randint(2,15); ans=n*n
            add('mittel',f"Welche Zahl ist {n}²?",str(ans),f"{n}²={n}·{n}={ans}.",'Quadrat bedeutet mal sich selbst.','Multipliziere '+str(n)+' mit '+str(n)+'.')
        for k in range(10):
            n=r.randint(4,20); sq=n*n
            add('mittel',f"Bestimme √{sq}.",str(n),f"Weil {n}²={sq}, gilt √{sq}={n}.",'Gesucht ist die positive Zahl, deren Quadrat '+str(sq)+' ist.','Teste Quadratzahlen.')
        for k in range(10):
            x=r.uniform(10,999); places=r.choice([0,1]); ans=round(x,places)
            label='ganze Zahl' if places==0 else 'eine Nachkommastelle'
            add('mittel',f"Runde {de(x,2)} auf {label}.",de(ans,places),f"Betrachte die nächste Stelle und runde: {de(ans,places)}.",'Die nächste Ziffer entscheidet.','0–4 abrunden, 5–9 aufrunden.')
        for k in range(10):
            price=r.randint(8,40)+r.choice([0.49,0.79,0.99]); count=r.randint(2,6); paid=math.ceil(price*count/10)*10; change=round(paid-price*count,2)
            add('anspruchsvoll',f"Im Kino kosten Snacks {de(price,2)} € pro Person. {count} Personen kaufen jeweils einen. Sie zahlen zusammen {paid} €. Wie viel Rückgeld erhalten sie?",de(change,2),f"Gesamtpreis: {count}·{de(price,2)} €={de(price*count,2)} €. Rückgeld: {paid}−{de(price*count,2)}={de(change,2)} €.",'Berechne zuerst den Gesamtpreis.','Ziehe den Gesamtpreis vom gezahlten Betrag ab.',unit='€',tolerance=.01)
    elif theme=='groessen':
        convs=[('m','cm',100),('km','m',1000),('kg','g',1000),('l','ml',1000),('h','min',60),('min','s',60),('dm','cm',10),('m²','dm²',100),('dm²','cm²',100),('dm³','cm³',1000)]
        for src,dst,f in convs:
            for k in range(5):
                a=r.choice([1.2,2.5,3.4,6.75,8.08,12.5])+k/10
                ans=a*f
                add('leicht',f"Rechne um: {de(a)} {src} = ? {dst}",de(ans),f"Von {src} zu {dst} wird mit {f} multipliziert: {de(a)}·{f}={de(ans)}.",'Überlege, ob die Ziel-Einheit kleiner ist.','Kleinere Einheit → Zahl wird größer.',unit=dst,tolerance=.001)
        # reverse conversions 20
        for k in range(20):
            src,dst,f=r.choice(convs)
            a=r.randint(2,25)*f
            ans=a/f
            add('mittel',f"Rechne um: {a} {dst} = ? {src}",de(ans),f"Von {dst} zu {src} wird durch {f} geteilt: {a}:{f}={de(ans)}.",'Die Ziel-Einheit ist größer.','Teile durch den Umrechnungsfaktor.',unit=src)
        for k in range(10):
            h=r.randint(0,3); m=r.choice([15,20,25,30,35,40,45,50]); total=h*60+m
            add('mittel',f"Eine Busfahrt dauert {h} h {m} min. Wie viele Minuten sind das?",str(total),f"{h} h = {h*60} min. Dazu {m} min: {total} min.",'Wandle Stunden in Minuten um.','1 h = 60 min.',unit='min')
        for k in range(10):
            scale=r.choice([50,100,200,500,1000]); cm=r.choice([2.4,3.5,4.2,5.6,7.5]); real_m=cm*scale/100
            add('anspruchsvoll',f"Auf einem Plan im Maßstab 1:{scale} ist eine Strecke {de(cm,1)} cm lang. Wie lang ist sie in Wirklichkeit in Metern?",de(real_m),f"{de(cm,1)}·{scale}={de(cm*scale)} cm = {de(real_m)} m.",'Multipliziere die Planlänge mit der Maßstabszahl.','Wandle danach Zentimeter in Meter um.',unit='m',tolerance=.01)
        for k in range(10):
            start_h=r.randint(7,18); start_m=r.choice([0,10,15,20,30,40,45,50]); duration=r.randint(35,180); end=start_h*60+start_m+duration; eh=(end//60)%24; em=end%60
            add('anspruchsvoll',f"Ein Training beginnt um {start_h:02d}:{start_m:02d} Uhr und dauert {duration} Minuten. Wann endet es?",f"{eh:02d}:{em:02d}",f"Startzeit in Minuten: {start_h*60+start_m}. +{duration}={end}. Das entspricht {eh:02d}:{em:02d} Uhr.",'Rechne die Dauer zur Startzeit hinzu.','Du kannst zunächst alles in Minuten umwandeln.')
    elif theme=='prozent':
        for k in range(20):
            G=r.choice([40,50,80,120,160,200,250,400,600,800]); p=r.choice([5,10,15,20,25,30,40,50]); W=G*p/100
            add('leicht',f"Berechne {p} % von {G}.",de(W),f"{p}% von {G} = {G}·{p}/100 = {de(W)}.",'Berechne zuerst 1 % oder nutze G·p/100.','Grundwert · Prozentsatz.',tolerance=.01)
        for k in range(15):
            G=r.choice([60,80,100,120,150,200,240,300]); p=r.choice([10,20,25,30,40,50]); W=G*p/100
            add('mittel',f"{de(W)} sind wie viel Prozent von {G}?",de(p),f"p = W/G·100 = {de(W)}/{G}·100 = {p}%.",'Teile den Anteil durch das Ganze.','Danach ·100.',unit='%',tolerance=.01)
        for k in range(15):
            p=r.choice([10,20,25,40,50]); W=r.choice([12,15,20,24,30,40,50]); G=W/(p/100)
            if abs(G-round(G))>.001: G=round(G,2)
            add('mittel',f"{W} entsprechen {p} %. Bestimme den Grundwert.",de(G),f"G = W : ({p}/100) = {de(G)}.",'100 % sind mehr als der gegebene Anteil.','Teile den Prozentwert durch den Dezimalwert des Prozentsatzes.',tolerance=.01)
        for k in range(20):
            price=r.choice([24,32,40,48,60,80,120,160,240]); p=r.choice([10,15,20,25,30]); new=price*(1-p/100)
            contexts=['Sneaker','Rucksack','Kopfhörer','Sportshirt','Ticket','Schulrucksack','Jacke','Fahrradhelm']
            item=contexts[k%len(contexts)]
            add('mittel',f"Ein {item} kostet {price} €. Im Angebot gibt es {p} % Rabatt. Wie hoch ist der neue Preis?",de(new,2),f"Rabatt: {price}·{p}/100={de(price*p/100,2)} €. Neuer Preis: {price}−{de(price*p/100,2)}={de(new,2)} €.",'Berechne den Rabattbetrag.','Ziehe den Rabatt vom ursprünglichen Preis ab.',unit='€',tolerance=.01)
        # real-world contexts with current price data
        for k in range(10):
            months=r.randint(2,12); total=63*months
            add('anspruchsvoll',f"Das Deutschland-Ticket kostet 2026 monatlich 63 €. Wie viel kosten {months} Monate insgesamt?",str(total),f"{months}·63 € = {total} €.",'Multipliziere Monatszahl und Monatspreis.','63 € pro Monat.',unit='€',source='Deutsche Bahn, Deutschland-Ticket 2026: 63 € pro Monat')
        for k in range(10):
            kwh=r.choice([80,120,150,180,200,250,300,350,400,450]); cost=kwh*.4055
            add('anspruchsvoll',f"Ein Haushalt verbraucht in einem Monat {kwh} kWh Strom. Rechne mit 40,55 ct pro kWh. Wie hoch sind die reinen Verbrauchskosten?",de(cost,2),f"40,55 ct = 0,4055 €. {kwh}·0,4055 €={de(cost,2)} €.",'Wandle Cent in Euro um.','40,55 ct = 0,4055 €.',unit='€',tolerance=.02,source='Destatis, durchschnittlicher Haushaltsstrompreis 2. Halbjahr 2025: 40,55 ct/kWh')
        for k in range(10):
            K=r.choice([200,500,800,1000,1500,2000]); p=r.choice([1,2,2.5,3,4]); Z=K*p/100
            add('anspruchsvoll',f"Ein Guthaben von {K} € wird ein Jahr lang mit {de(p)} % verzinst. Wie viele Euro Zinsen entstehen?",de(Z,2),f"Z = K·p/100 = {K}·{de(p)}/100 = {de(Z,2)} €.",'Nutze die Zinsformel wie bei Prozentrechnung.','Kapital · Zinssatz / 100.',unit='€',tolerance=.01)
    elif theme=='terme':
        for k in range(20):
            x=r.randint(-5,12); a=r.randint(2,8); b=r.randint(-10,12); ans=a*x+b
            add('leicht',f"Setze x = {x} in den Term {a}x {'+' if b>=0 else '−'} {abs(b)} ein.",str(ans),f"{a}·({x}) {'+' if b>=0 else '−'} {abs(b)} = {ans}.",'Ersetze x durch den gegebenen Wert.','Achte bei negativen Zahlen auf Klammern.')
        for k in range(20):
            a=r.randint(2,9); x=r.randint(-8,20); b=r.randint(-10,15); c=a*x+b
            add('mittel',f"Löse die Gleichung {a}x {'+' if b>=0 else '−'} {abs(b)} = {c}.",str(x),f"Zuerst {'−'+str(b) if b>=0 else '+'+str(abs(b))}: {a}x={a*x}. Dann durch {a}: x={x}.",'Bringe zuerst den konstanten Term auf die andere Seite.','Danach durch den Faktor vor x teilen.')
        for k in range(15):
            a=r.randint(2,6); x=r.randint(1,15); b=r.randint(1,8); c=a*(x+b)
            add('mittel',f"Löse {a}·(x + {b}) = {c}.",str(x),f"Durch {a}: x+{b}={c/a:g}. Dann −{b}: x={x}.",'Beseitige zuerst den Faktor vor der Klammer.','Teile beide Seiten durch '+str(a)+'.')
        for k in range(15):
            a=r.randint(2,8); b=r.randint(1,9); c=r.randint(1,9)
            ans=a*(b+c)
            add('leicht',f"Berechne den Wert des Terms {a}·({b}+{c}).",str(ans),f"Klammer zuerst: {b}+{c}={b+c}; dann {a}·{b+c}={ans}.",'Klammer zuerst.','Dann multiplizieren.')
        for k in range(10):
            a=r.randint(2,9); b=r.randint(2,9); c=r.randint(2,9); ans=a*b+a*c
            add('mittel',f"Multipliziere aus und berechne: {a}·({b}+{c}).",str(ans),f"{a}·{b}+{a}·{c}={a*b}+{a*c}={ans}.",'Distributivgesetz.','Multipliziere '+str(a)+' mit beiden Summanden.')
        for k in range(10):
            age=r.randint(10,16); older=r.randint(2,6); sumage=2*age+older
            add('anspruchsvoll',f"Mira ist x Jahre alt. Ihr Bruder ist {older} Jahre älter. Zusammen sind sie {sumage} Jahre alt. Wie alt ist Mira?",str(age),f"x+(x+{older})={sumage} → 2x+{older}={sumage} → 2x={2*age} → x={age}.",'Stelle eine Gleichung mit x auf.','Mira: x, Bruder: x+'+str(older)+'.')
        for k in range(10):
            x=r.randint(2,12); rate=r.randint(2,6); base=r.randint(1,5); total=base+rate*x
            add('anspruchsvoll',f"Ein Verleih verlangt {base} € Startgebühr und {rate} € pro Stunde. Die Rechnung beträgt {total} €. Wie viele Stunden wurde ausgeliehen?",str(x),f"{base}+{rate}x={total} → {rate}x={total-base} → x={x}.",'Stelle Startgebühr + Stundenpreis·x = Gesamtpreis auf.','Ziehe zuerst die Startgebühr ab.',unit='h')
    elif theme=='funktionen':
        for k in range(20):
            m=r.choice([0.5,1,1.5,2,2.5,3]); x=r.randint(1,12); y=m*x
            add('leicht',f"Bei der proportionalen Zuordnung y = {de(m)}·x: Bestimme y für x = {x}.",de(y),f"y={de(m)}·{x}={de(y)}.",'Setze x ein.','Multipliziere x mit dem Proportionalitätsfaktor.')
        for k in range(15):
            m=r.choice([-3,-2,-1,0.5,1,2,3]); n=r.randint(-5,8); x=r.randint(-4,8); y=m*x+n
            add('mittel',f"Gegeben ist y = {de(m)}x {'+' if n>=0 else '−'} {abs(n)}. Bestimme y für x={x}.",de(y),f"y={de(m)}·({x}) {'+' if n>=0 else '−'} {abs(n)}={de(y)}.",'Setze x in die Funktionsgleichung ein.','Zuerst multiplizieren, dann den y-Achsenabschnitt berücksichtigen.')
        for k in range(15):
            x1=r.randint(0,5); x2=x1+r.randint(1,5); m=r.choice([-2,-1,0.5,1,2,3]); n=r.randint(-3,6); y1=m*x1+n; y2=m*x2+n
            add('mittel',f"Eine Gerade geht durch A({x1}|{de(y1)}) und B({x2}|{de(y2)}). Bestimme die Steigung m.",de(m),f"m=(y₂−y₁)/(x₂−x₁)=({de(y2)}−{de(y1)})/({x2}−{x1})={de(m)}.",'Änderung in y durch Änderung in x.','m = Δy / Δx.',tolerance=.001)
        for k in range(15):
            m=r.choice([0.15,0.2,0.25,0.3,0.5]); base=r.choice([1,2,3,4]); mins=r.choice([10,15,20,25,30]); cost=base+m*mins
            add('mittel',f"Ein Leihdienst berechnet {de(base,2)} € Startgebühr und {de(m,2)} € pro Minute. Wie viel kosten {mins} Minuten?",de(cost,2),f"Kosten y={de(m,2)}·{mins}+{de(base,2)}={de(cost,2)} €.",'Lineares Modell: variable Kosten + Startgebühr.','Minutenpreis·Minuten + Startgebühr.',unit='€',tolerance=.01)
        for k in range(15):
            start=r.choice([100,200,400,500,800]); p=r.choice([5,10,20]); years=r.choice([2,3,4]); qf=1+p/100; val=start*(qf**years)
            add('anspruchsvoll',f"Eine Größe startet bei {start} und wächst jedes Jahr um {p} %. Wie groß ist sie nach {years} Jahren?",de(val,2),f"Wachstumsfaktor q=1+{p}/100={de(qf,2)}. Nach {years} Jahren: {start}·{de(qf,2)}^{years}={de(val,2)}.",'Bestimme zuerst den Wachstumsfaktor.','q = 1 + p/100.',tolerance=.02)
        for k in range(10):
            start=r.choice([500,800,1000,1500]); p=r.choice([5,10,20,25]); years=r.choice([2,3]); qf=1-p/100; val=start*(qf**years)
            add('anspruchsvoll',f"Der Wert eines Geräts beträgt anfangs {start} € und sinkt pro Jahr um {p} %. Wie hoch ist der Wert nach {years} Jahren?",de(val,2),f"Abnahmefaktor q=1−{p}/100={de(qf,2)}. Wert: {start}·{de(qf,2)}^{years}={de(val,2)} €.",'Bei Abnahme ist q kleiner als 1.','q=1−p/100.',unit='€',tolerance=.02)
        for k in range(10):
            m=r.choice([-2,-1,1,2,3]); n=r.randint(-5,5)
            add('anspruchsvoll',f"Welche Aussage passt zur Geraden y={m}x {'+' if n>=0 else '−'} {abs(n)}?",f"m={m};n={n}",f"Die Steigung ist m={m}; der y-Achsenabschnitt ist n={n}.",'Lies m und n direkt aus y=mx+n.','m steht vor x, n ist die Konstante.')
    elif theme=='geometrie':
        for k in range(15):
            a=r.randint(3,20); b=r.randint(2,15); A=a*b
            add('leicht',f"Ein Rechteck ist {a} cm lang und {b} cm breit. Berechne den Flächeninhalt.",str(A),f"A=a·b={a}·{b}={A} cm².",'Länge mal Breite.','A=a·b.',unit='cm²')
        for k in range(15):
            a=r.randint(3,20); b=r.randint(2,15); u=2*(a+b)
            add('leicht',f"Ein Rechteck ist {a} cm lang und {b} cm breit. Berechne den Umfang.",str(u),f"u=2a+2b=2·{a}+2·{b}={u} cm.",'Addiere alle vier Seiten.','u=2(a+b).',unit='cm')
        triples=[(3,4,5),(5,12,13),(6,8,10),(8,15,17),(7,24,25),(9,12,15),(12,16,20),(15,20,25),(9,40,41),(20,21,29)]
        for k in range(20):
            a,b,c=triples[k%len(triples)]
            scale=1 if k<10 else 2
            a*=scale;b*=scale;c*=scale
            add('mittel',f"Ein rechtwinkliges Dreieck hat Katheten {a} cm und {b} cm. Berechne die Hypotenuse.",str(c),f"c=√({a}²+{b}²)=√({a*a+b*b})={c} cm.",'Nutze a²+b²=c².','Quadriere die Katheten, addiere und ziehe die Wurzel.',unit='cm')
        for k in range(10):
            r0=r.randint(2,10); A=math.pi*r0*r0
            add('mittel',f"Ein Kreis hat Radius {r0} cm. Berechne seinen Flächeninhalt. Runde auf zwei Nachkommastellen.",de(A,2),f"A=π·r²=π·{r0}²≈{de(A,2)} cm².",'A=π·r².','Setze den Radius ein.',unit='cm²',tolerance=.03)
        for k in range(10):
            r0=r.randint(2,10); u=2*math.pi*r0
            add('mittel',f"Ein Kreis hat Radius {r0} cm. Berechne seinen Umfang. Runde auf zwei Nachkommastellen.",de(u,2),f"u=2·π·r=2·π·{r0}≈{de(u,2)} cm.",'u=2πr.','Setze den Radius ein.',unit='cm',tolerance=.03)
        for k in range(10):
            scale=r.choice([50,100,200]); plan=r.choice([3,4.5,6,7.5,8]); real=plan*scale/100
            add('anspruchsvoll',f"Auf einer Zeichnung im Maßstab 1:{scale} ist eine Strecke {de(plan)} cm lang. Berechne die reale Länge in Metern.",de(real),f"{de(plan)}·{scale}={de(plan*scale)} cm={de(real)} m.",'Maßstab bedeutet: Zeichnung·Maßstabszahl.','Danach cm in m umrechnen.',unit='m',tolerance=.01)
        for k in range(10):
            base=r.randint(4,16); h=r.randint(3,12); A=base*h/2
            add('mittel',f"Ein Dreieck hat Grundseite {base} cm und Höhe {h} cm. Berechne den Flächeninhalt.",de(A),f"A=g·h/2={base}·{h}/2={de(A)} cm².",'Dreiecksfläche ist die Hälfte von Grundseite mal Höhe.','A=g·h/2.',unit='cm²')
        for k in range(10):
            sym=r.choice([('Quadrat',4),('Rechteck (kein Quadrat)',2),('gleichseitiges Dreieck',3),('gleichschenkliges Dreieck',1),('allgemeines Dreieck',0)])
            add('leicht',f"Wie viele Symmetrieachsen hat ein {sym[0]}?",str(sym[1]),f"Ein {sym[0]} hat {sym[1]} Symmetrieachse(n).",'Stelle dir eine Spiegelung vor.','Zähle alle Geraden, an denen die Figur auf sich selbst abgebildet wird.')
    elif theme=='koerper':
        for k in range(20):
            a=r.randint(2,12); b=r.randint(2,10); c=r.randint(2,15); V=a*b*c
            add('leicht',f"Ein Quader ist {a} cm × {b} cm × {c} cm groß. Berechne das Volumen.",str(V),f"V=a·b·c={a}·{b}·{c}={V} cm³.",'Länge·Breite·Höhe.','V=a·b·c.',unit='cm³')
        for k in range(15):
            a=r.randint(2,10); O=6*a*a
            add('mittel',f"Ein Würfel hat Kantenlänge {a} cm. Berechne die Oberfläche.",str(O),f"O=6a²=6·{a}²={O} cm².",'Ein Würfel hat sechs quadratische Flächen.','6·a².',unit='cm²')
        for k in range(15):
            r0=r.randint(2,8); h=r.randint(3,15); V=math.pi*r0*r0*h
            add('mittel',f"Ein Zylinder hat Radius {r0} cm und Höhe {h} cm. Berechne das Volumen. Runde auf zwei Nachkommastellen.",de(V,2),f"V=π·r²·h=π·{r0}²·{h}≈{de(V,2)} cm³.",'Grundfläche Kreis mal Höhe.','V=πr²h.',unit='cm³',tolerance=.05)
        for k in range(10):
            r0=r.randint(2,8); h=r.randint(3,15); O=2*math.pi*r0*r0+2*math.pi*r0*h
            add('anspruchsvoll',f"Eine geschlossene zylinderförmige Dose hat Radius {r0} cm und Höhe {h} cm. Berechne die Oberfläche. Runde auf zwei Nachkommastellen.",de(O,2),f"O=2πr²+2πrh=2π·{r0}²+2π·{r0}·{h}≈{de(O,2)} cm².",'Zwei Kreisflächen plus Mantel.','O=2G+M.',unit='cm²',tolerance=.08)
        for k in range(10):
            a=r.randint(2,10); b=r.randint(2,10); h=r.randint(3,15); G=a*b; V=G*h
            add('mittel',f"Ein gerades Prisma hat eine rechteckige Grundfläche {a} cm × {b} cm und Höhe {h} cm. Berechne das Volumen.",str(V),f"G={a}·{b}={G} cm²; V=G·h={G}·{h}={V} cm³.",'Berechne zuerst die Grundfläche.','V=G·h.',unit='cm³')
        for k in range(10):
            a=r.randint(3,10); h=r.randint(4,15); V=a*a*h/3
            add('anspruchsvoll',f"Eine quadratische Pyramide hat Grundkante {a} cm und Höhe {h} cm. Berechne das Volumen.",de(V,2),f"G={a}²={a*a}; V=1/3·G·h=1/3·{a*a}·{h}={de(V,2)} cm³.",'Pyramidenvolumen: ein Drittel von Grundfläche mal Höhe.','V=1/3·G·h.',unit='cm³',tolerance=.02)
        for k in range(10):
            d=r.choice([4,6,8,10,12]); r0=d/2; V=4/3*math.pi*r0**3
            add('anspruchsvoll',f"Eine Kugel hat Durchmesser {d} cm. Berechne ihr Volumen. Runde auf zwei Nachkommastellen.",de(V,2),f"r={d}/2={de(r0)} cm; V=4/3·π·r³≈{de(V,2)} cm³.",'Bestimme zuerst den Radius.','V=4/3·π·r³.',unit='cm³',tolerance=.08)
        for k in range(10):
            side=r.randint(2,6); count=r.randint(8,40); total=count*side**3
            add('mittel',f"{count} kleine Würfel mit Kantenlänge {side} cm werden ohne Lücken zu einem Körper zusammengesetzt. Wie groß ist das Gesamtvolumen?",str(total),f"Ein Würfel: {side}³={side**3} cm³. {count} Würfel: {count}·{side**3}={total} cm³.",'Volumen eines kleinen Würfels mal Anzahl.','a³·Anzahl.',unit='cm³')
    else:
        for k in range(20):
            vals=[r.randint(5,20) for _ in range(5)]; mean=sum(vals)/5
            add('leicht',f"Bestimme den Mittelwert der Werte: {', '.join(map(str,vals))}.",de(mean,1),f"Summe={sum(vals)}; {sum(vals)}:5={de(mean,1)}.",'Addiere alle Werte.','Teile die Summe durch 5.',tolerance=.01)
        for k in range(15):
            vals=sorted([r.randint(1,30) for _ in range(5)]); med=vals[2]
            shuffled=vals[:]; r.shuffle(shuffled)
            add('leicht',f"Bestimme den Median: {', '.join(map(str,shuffled))}.",str(med),f"Geordnet: {', '.join(map(str,vals))}. Der mittlere Wert ist {med}.",'Sortiere zuerst die Werte.','Bei fünf Werten ist der dritte Wert der Median.')
        for k in range(15):
            vals=[r.randint(1,50) for _ in range(6)]; span=max(vals)-min(vals)
            add('leicht',f"Bestimme die Spannweite: {', '.join(map(str,vals))}.",str(span),f"Maximum {max(vals)} minus Minimum {min(vals)} = {span}.",'Suche größten und kleinsten Wert.','Spannweite = Maximum − Minimum.')
        for k in range(20):
            total=r.choice([20,30,40,50,100]); good=r.randint(1,total-1); p=good/total*100
            add('mittel',f"In einer Box liegen {total} Lose, davon {good} Gewinne. Wie groß ist die Gewinnwahrscheinlichkeit in Prozent?",de(p,1),f"P={good}/{total}={de(p/100,3)}={de(p,1)}%.",'Günstige Ergebnisse durch alle Ergebnisse.','Dann in Prozent umrechnen.',unit='%',tolerance=.11)
        for k in range(10):
            parts=[r.randint(10,40),r.randint(10,40),r.randint(10,40)]; s=sum(parts); vals=[round(100*x/s,1) for x in parts]
            add('mittel',f"Eine Umfrage ergibt {parts[0]}, {parts[1]} und {parts[2]} Stimmen für drei Optionen. Wie viel Prozent entfallen auf Option 1?",de(vals[0],1),f"Gesamt={s}. Anteil Option 1: {parts[0]}/{s}·100≈{de(vals[0],1)}%.",'Berechne zuerst die Gesamtzahl.','Stimmen Option 1 / alle Stimmen · 100.',unit='%',tolerance=.11)
        for k in range(10):
            grid=r.choice([8,10,12,16,20]); sample=r.randint(8,25); est=grid*sample
            add('anspruchsvoll',f"Ein Foto wird in {grid} gleich große Felder geteilt. In einem typischen Feld werden etwa {sample} Objekte gezählt. Schätze die Gesamtzahl.",str(est),f"Rastermethode: {grid} Felder · ca. {sample} Objekte/Feld = ca. {est} Objekte.",'Nutze die Rastermethode.','Typische Anzahl pro Feld mal Zahl der Felder.')
        for k in range(10):
            red=r.randint(2,8); blue=r.randint(2,8); green=r.randint(1,6); total=red+blue+green; p=(red+blue)/total*100
            add('anspruchsvoll',f"In einem Beutel sind {red} rote, {blue} blaue und {green} grüne Kugeln. Wie groß ist die Wahrscheinlichkeit, rot oder blau zu ziehen, in Prozent?",de(p,1),f"Günstig={red}+{blue}={red+blue}; Gesamt={total}. P={(red+blue)}/{total}≈{de(p,1)}%.",'Addiere zuerst alle günstigen Kugeln.','P=günstig/gesamt.',unit='%',tolerance=.11)
    assert len(arr)==100,(theme,len(arr))
    return arr

for t in THEMES:
    arr=make_theme(t['id'])
    json.dump(arr, open(DATA/f'tasks_{t["id"]}.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)

# Matching data from flashcards plus formula/application pairs
for t in THEMES:
    cards=json.load(open(DATA/f'flashcards_{t["id"]}.json',encoding='utf-8'))
    pairs=[{'left':c['term'],'right':c['definition']} for c in cards]
    json.dump(pairs, open(DATA/f'matching_{t["id"]}.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)

# Exam variants: 20 part 1 (6 short tasks each) and 20 part 2 (3 contextual blocks, 3-5 subitems each)
alltasks={t['id']:json.load(open(DATA/f'tasks_{t["id"]}.json',encoding='utf-8')) for t in THEMES}
part1=[]
for v in range(20):
    rr=random.Random(1000+v)
    selected=[]
    # typical short mix across content areas
    order=['zahlen','groessen','geometrie','daten','terme','prozent'] if v%2==0 else ['zahlen','groessen','koerper','daten','funktionen','geometrie']
    for th in order:
        pool=[x for x in alltasks[th] if x['difficulty'] in ('leicht','mittel')]
        item=rr.choice(pool).copy(); item['examId']=f'p1v{v+1}-{len(selected)+1}'; selected.append(item)
    part1.append({'id':f'P1-{v+1:02d}','title':f'Teil 1 – Variante {v+1}','tasks':selected})
json.dump(part1, open(DATA/'exam_part1.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)

contexts=[
('Schulcafé',['prozent','zahlen','daten']),('Sporttag',['daten','groessen','prozent']),('Fahrradtour',['groessen','funktionen','geometrie']),('Wohnung renovieren',['geometrie','prozent','groessen']),('Streaming & Datenvolumen',['funktionen','prozent','daten']),('Schulfest',['daten','prozent','geometrie']),('Fitnessuhr',['funktionen','daten','groessen']),('Bäckerei',['prozent','koerper','zahlen']),('Gartenprojekt',['geometrie','koerper','prozent']),('E-Scooter',['funktionen','groessen','prozent']),('Freizeitpark',['prozent','daten','groessen']),('Konzert',['prozent','zahlen','daten']),('Smartphone',['daten','funktionen','prozent']),('Wasserflasche',['koerper','groessen','prozent']),('Paketversand',['koerper','groessen','zahlen']),('Solarprojekt',['funktionen','prozent','geometrie']),('Klassenfahrt',['prozent','groessen','daten']),('Kiosk',['zahlen','prozent','terme']),('Trainingsplan',['daten','funktionen','terme']),('3D-Druck',['koerper','geometrie','prozent'])]
part2=[]
for v,(ctx,ths) in enumerate(contexts,1):
    rr=random.Random(2000+v)
    blocks=[]
    for bi,th in enumerate(ths,1):
        pool=[x for x in alltasks[th] if x['difficulty'] in ('mittel','anspruchsvoll')]
        subs=[]
        for si in range(3):
            item=rr.choice(pool).copy(); item['examId']=f'p2v{v}-{bi}-{si+1}'; subs.append(item)
        blocks.append({'title':f'Aufgabe {bi}: {ctx}' if bi==1 else f'Aufgabe {bi}','theme':th,'items':subs})
    part2.append({'id':f'P2-{v:02d}','title':f'Teil 2 – Variante {v}','context':ctx,'blocks':blocks})
json.dump(part2, open(DATA/'exam_part2.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)

# Metadata & source notes
meta={
 'generatedTasks':800,'tasksPerTheme':100,'examPart1Variants':20,'examPart2Variants':20,
 'sources':[
  {'label':'ZP10 NRW Vorgaben Mathematik EESA 2027','url':'https://www.standardsicherung.schulministerium.nrw.de/system/files/media/document/file/vorgaben_m27_eesa.pdf'},
  {'label':'ZP10 NRW Beispielaufgaben Teil 1 ab 2023','url':'https://www.standardsicherung.schulministerium.nrw.de/system/files/media/document/file/zp10_m_bsp_pt1_eesa.pdf'},
  {'label':'ZP10 NRW FAQ Bearbeitungszeiten','url':'https://www.standardsicherung.schulministerium.nrw.de/zp10/fragen-und-antworten/faq_0300.html'},
  {'label':'Deutsche Bahn – Deutschland-Ticket 2026','url':'https://www.bahn.de/faq/gk/angebot/zeitkarten/deutschland-ticket'},
  {'label':'Destatis – Strompreise Haushalte 2. Halbjahr 2025','url':'https://www.destatis.de/DE/Presse/Pressemitteilungen/2026/03/PD26_111_61243.html'}
 ]
}
json.dump(meta, open(DATA/'meta.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('Generated data files.')
