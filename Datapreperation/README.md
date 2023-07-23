# Datapreperation
Dieses Notebook umfasst die Datenvorverarbeitung der Textdaten, da die Topic Modelling Modelle des Machine und Deep Learning ausschließlich numerische Daten verarbeiten können. Es werden alle nicht relevanten Informationen vereinheitlicht oder aus dem Datensatz entgernt, damit diese später in ein berechenbares Format konvertiert werden können und untenstehender Datensatz erzeugt wird. Im Rahmen dieser Masterarbeit wurde die Datapreparation anhand des kleinen Datensatz der Kategorie ["Sports and Outdoors" der Amazon Daten](https://nijianmo.github.io/amazon/index.html) durchgeführt.

<Br>

### Bild

<Br>



Die Preparation gliedert sich in zwei Kathegorien, die allgemeinen Bereinigungsschritte und die Bereinigung der Textdaten:

<ul>1. Allgemeine Datenbereinigung</ul>
    <ul>
     <ul>1.1. Selectieren und Zusammenführen der Spalten</ul>
     <ul>1.2. Nan-Values und doppelte Werte</ul>
     <ul>1.3. Löschen zu kurzer Reviews</ul>
     <ul>1.4. Selectieren der Jahre 2011 bis 2018</ul>
    </ul>
<ul>2. Bereinigung der Textdaten</ul>
    <ul>
     <ul>2.1. Lowercasing</ul>
     <ul>2.2. Lemmatisierung</ul>
     <ul>2.3. Stemming</ul>
     <ul>2.4. Entfernung von Satzzeichen</ul>
     <ul>2.5. Entfernung von Stopwords</ul>
     <ul>2.6. Entfernung von Zahlen</ul>
     <ul>2.7. Entfernung von nicht ASCII konformen Wörtern</ul>
    </ul>

<Br>

## Wichtigste Schritte der Datapreparation
Die Implementierung der Bereinigungsschritte sind dem Jupyter Notebook zu entnehmen. Im folgenden sind die wichtigsten Funktionen zusammengefasst. Diese lassen sich auf unterschiedliche weiße in eine Pipeline integrieren. Im Rahmen dieser Masterarbeit wurden sie mithilfe einer For-Schleife und der Beschleunigung durch Joblib durchgeführt. Die Beschleunigung zeigte bei dem verkleinerten Datensatz zu ["Sports and Outdoors"](https://nijianmo.github.io/amazon/index.html) mit über 2 Mio. Zeilen gute Ergebnisse. Bei der Verarbeitung größerer Textmengen erhöhen sich Laufzeit rapiede. Aus diesem Grund lohnt sich die Implementierung mit PySpark, welche [hier](https://github.com/Sannui/Masterarbeit_Nuissl_Sandra/tree/main/Beschleunigung%20mit%20PySpark) beschrieben wurde.


<Br>

### Lowercasing

Das Lowercasing beschäftigt sich mit der Groß- und Kleinschreibung in TExten. Da es für das Verständnis eines Textes bzw. der Wörter keiner Groß- und Kleinschreibung bedarf, kann der Datensatz in diesem Punkt vereinheitlicht werden(Pomer, 2022). 

```
# Konvertierung der Groß- und Kleinschreibung
def to_lower(in_string):
    out_string = in_string.lower()
    return out_string
```

<center><img src="Lowercasing_time.PNG" height="100px" width="1000px"/></center>
<p align="center">Parralelisierung des Lowercasing mithilfe von Joblib</p>

<Br>

### Lemmatisierung

```
# Überführen der Wörter in ihre Grundform
def lemmatize(in_string):
    # Definition der notwendigen Parameter
    list_pos = 0                                  # Zuordnung einer Positionsnummer
    cleaned_str = ''                              # Leerer String für bereinigte Wörter
    text_token = nltk.word_tokenize(in_string)    # Tokenisieren der Sätze in einzelne Strings
    tagged_words = pos_tag(text_token)            # Grammatikalisches Tagging
    wnl = WordNetLemmatizer()                     # Klasse von NLTK für Lemmatisierung

    # Durchfürhung der Lemmatisation und Zusammenführung der Ergebnisse in einen String
    for word in tagged_words:
        if 'v' in word[1].lower():
            lemma = wnl.lemmatize(word[0], pos='v')
        else:
            lemma = wnl.lemmatize(word[0], pos='n')
        if list_pos == 0:
            cleaned_str = lemma
        else:
            cleaned_str = cleaned_str + ' ' + lemma
        list_pos += 1
    return cleaned_str
```



<Br>

### Stemming

```

```

<Br>

### Entfernung von Satzzeichen

```

```

<Br>

### Entfernung von Stopwords

```

```


<Br>

### Entfernung von Zahlen

```

```


<Br>

### Entfernung von nicht ASCII konformen Wörtern

```

```

