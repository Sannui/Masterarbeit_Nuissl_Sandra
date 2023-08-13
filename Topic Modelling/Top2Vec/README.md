# Implementierung des Topic Modelling Modells: Top2Vec
Top2Vec ist ein modernerer Ansatz des Topic Modelling und gehört ebenfalls in den Bereich des unsupervised learning (Lande, 2022). Das Modell wurde 2020 von Dimo Angelov veröffentlicht und es ermöglicht, dem Anwender die komplexen Topic Modelling Algorithmen in lediglich einer Codezeile zu trainieren und auszuführen (Weng, 2020). Der Algorithmus erstellt Themenvektoren durch eine semitische Einbettung der Dokumente. Hierfür wird das "Doc2Vec" Verfahren herangezogen, welches eine Weiterentwicklung des „Word2Vec“ – Algorithmus darstellt. Dieser verwendet das Bag-of-Words-Modell “CBOW”, welches ein sogenanntes Schiebefenster um das zu betrachtende Wort zieht, um den Kontext des Wortes zu betrachten. Nach dem Training des Algorithmus wird das Wort dann von einem Merkmalsvektor zu einem Wordvektor. „Doc2Vec“ erweitert dieses Modell um einen zusätzlichen dokumentenspezifischen Merkmalsvektor, welcher auch unter dem Namen „Distributed Memory-Version of Paragraph Vector“ bekannt ist. Dieser Vektor ist sozusagen das Gedächtnis des Algorithmus, welches sich an den Kontext bzw. das Thema des Absatzes erinnert. Zusammenfassend lässt sich sagen, dass „Doc2Vec“ das Konzept der Wörter über den Wortvektor mit dem Kontext eines Dokuments über den Dokumentenvektor miteinander kombiniert und auf diese Weise die Semantik und Reihenfolge eines Textes berücksichtigt (Le & Mikolov, 2014, S. 3 f.)

<Br>
<p align="center">
  <img width="850" height="250" src="img/Top2Vec_Theorie.png">
</p>
<p align="center">Continuos Bag-of-Words-Modell erweitert um den Distributed Memory-Version of Paragraph Vector (Eigene Abbildung in Anlehnung an (Le & Mikolov, 2014, S. 3))</p>

<Br>

## Besonderheiten der Implementierung
Im Rahmen dieser Masterarbeit wurde die Implementierung eines Top2Vec Modelles mithilfe der [Library von Top2Vec](https://top2vec.readthedocs.io/en/stable/) selbstdurchgeführt. Die Implementierung ist hierfür im Folgenden aufgeführt:

```
# Insatlationen
%pip install top2vec
```
```
# Imports
from top2vec import Top2Vec
```

### __Intitialisierung und Training__
   


```
model_top2vec = Top2Vec(sentence_list,                        # Liste der zu untersuchenden Texte
                        embedding_model = 'doc2vec',          # Verwendetes Embedding Model
                        min_count = 50,                       # Excludieren der Wörter, welche eine geringere Frequenz haben
                        umap_args=None,                       # Verwendung der Default Werte von UMAP
                        hdbscan_args=None,                    # Verwendung der Default Werte von HDBSCAN
                        verbose=True)
```
<Br>

## Ergebnisse
Gensim beitet ein interaktives Visualisierungstool, welches die Ergebnisse der Topic Modelling Abalyse von LDA optisch darstellt. Auf der linken Seite sind die Abstände zwischen den einzelnen Topics zu erkennen. Wird ein Thema ausgewählt gibt das Balkendiagramm auf der rechten Seite Aufschluss über die Häufigkeitsverteilung der Wörter in dem entsprechenden Topic (Mageshwaran, 2019).
<Br>
```
visualization_lda = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
```

![Property_per_Topic](img/LDA_visualization.gif)
<p align="center">Wahrscheinlichkeitsverteilung der Topics pro Review (Eigene Darstellung)</p>
<Br>

### Repräsentative Wörter der Topics
Durch dieser Wahrscheinlichkeiten lassen sich Dominate Reviews eines Topics identivizieren, welche zur Interpreation der Themen dienen.

-	Topic 0: lasagna deliciozs tasty bland flavour
-	Topic 1: recommend price good quality overall
-	Topic 2: lansky stone sharpening stone strop
-	Topic 3: hatchet fiskars hatchets logs chopping
-	Topic 4: mirrors mirror mirrycle view traffic
-	Topic 5: mat xoga manduka mats jade poses studio
-	Topic 6: helmet helmets giro visor crash ventilator
-	Topic 7: elbow flexbar tennis tendonitis thera
-	Topic 8: coolers cooler igloo ice drinks yeti
-	Topic 9: frisbee frisbees disc aerobie discs

<Br>

Top2Vec bietet zur Visualisierung die Implementierung einer Wordcloud mithilfe einer Funktion an.
<p align="center">
  <img width="850" height="400" src="img/To2Vec_Wordcloud.PNG">
</p>
<p align="center">Wahl der optimalen Anzahl von Topics für eine optimierte Kohärenz (Eigene Darstellung)</p>
<Br>

## Literatur


