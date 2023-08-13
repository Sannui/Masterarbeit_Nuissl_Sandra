# Implementierung des Topic Modelling Modells: ZeroShotTM
Theoretischer Text

<Br>
<p align="center">
  <img width="850" height="400" src="img/ZeroSHotTM_Theorie.png">
</p>
<p align="center">Architektur des ZeroShotTM (Eigene Darstellung in Anlehnung an (Bianchi, Terragni, Hovy, Nozza, & Fersini, 2020))</p>

<Br>

## Besonderheiten der Implementierung
Im Rahmen dieser Masterarbeit wurde die Implementierung eines BERTopic Modelles mithilfe der [Library von BERTopic](https://maartengr.github.io/BERTopic/algorithm/algorithm.html#code-overview) selbst durchgeführt. Bevor die Implementierung von BERTopic beginnen kann, ist es hilfereich zur Beschleunigung der Prozesse des Embeddings und der Dimensionsreduktion PyTorch zu installieren. Auf diese Weise lässt sich mithilfe der NVIDIA-GPUs die Laufzeit um das bis zu 4,5 Fache beschleunigen (Grootendorst, Faster Topic Modeling with BERTopic and RAPIDS cuML, 2023).

Die Implementierung ist hierfür im Folgenden aufgeführt:

```
# Insatlationen
%pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
%pip install bertopic
```
```
# Imports
from bertopic import BERTopic
```

### __Intitialisierung__
Das Pre-Trained-Modell von BERtopic wird initialisiert, indem die Klasse „BERTopic“ aufgerufen und in einer Variable gespeichert wird. Hierbei sind die Stufen des Embeddings, der Dimensionsreduktion und des Clusterings zusammengefasst. 
```
bert_model = BERTopic(embedding_model          = SentenceTransformer("all-MiniLM-L6-v2")
                      umap_model               = UMAP(n_neighbors=15, n_components=3, min_dist=0.0, metric='cosine', verbose=True)
                      hdbscan_model            = HDBSCAN(min_cluster_size=15, metric='euclidean', cluster_selection_method='eom',
                                                         prediction_data=True, core_dist_n_jobs=-1)
                      vectorizer_model         = CountVectorizer(stop_words="english")
                      ctfidf_model             = ClassTfidfTransformer()
                      representation_model     = KeyBERTInspired()
                      calculate_probabilities  = True,
                      verbose                  = True)
```
<Br>

### __Anwendung des Modells__
Die Anwendung auf den Amazondatensatz erfolgt über ein "fit_transform()" Funktion, welche die Topics pro Review, sowie deren Wahrscheinlichkeiten ausgibt.
```
topics, probabilities = bert_model.fit_transform(cleaned_list)
```
<Br>

## Ergebnisse

BERTopic baut auf einem Clustering-Embeddings-Ansatz auf und erweitert diesen um eine klassenbasierte TF-IDF-Variante zur Darstellung der Themen (Grootendorst, 2022, S. 2). Die Dimensionsreduktion erfolgt mithilfe von UMAP und für das Clustering wurde HDBSCAN herangezogen, wodurch die semantische Komponente bei der Erstellung von Clustern berücksichtigt wird. Darüber hinaus sind alle Daten bei HDBSCAN normalisiert, um Größenunterschiede auszugleichen. Das Ergebnis ist eine Ansammlung von Clustern, welche in der Abbildung zu sehen sind. Der weiße "Nebel" stellt die Ausreißer da, welche keinem Cluster/ Topic zugeordnet werden konnten (Grootendorst, BERTopic, 2023).
<Br>

![BERTopic_Cluster](img/BERTopic_Cluster_Ausreißer.gif)
<p align="center">Darstellung der Dimensionsreduktion und des Clustering durch BERTopic (Eigene Darstellung)</p>
<Br>

### Repräsentative Wörter der Topics
Für die ermittelten Cluster werden Themen identifiziert. Das Topic Modelling Modell gibt für jedes Topic eine Reihe repräsentativer Wörter aus, welche zur Interpreation der Themen dienen. BERTopic verfügt hierfür über unterschiedlichste Visualisierungsmöglichkeiten:
<Br>
<p align="center">
  <img width="850" height="450" src="img/BERT_Topics.png">
</p>
<p align="center">Repräsentative Wörter je Topic (Eigene Darstellung)</p>
<Br>

Eine Weitere Möglichkeit von BERTopic ist die Visualisierung des Verhältnisses der Dokumente in Bezug auf die Topics. Hierbei werden die Dokumente in eine zweidimensionale Darstellung geplottet. Die Farbe Repräsentiert das Topic des Dokuments. Auf diese Weise lässt sich erkennen, ob die Dokumente den richtigen Themen zugeordnet wurden oder ob es überlappende Themen gibt.
<p align="center">
  <img width="850" height="450" src="img/BERT_Topic_Docs.png">
</p>
<p align="center">Verhältnis der Dokumente in Bezug auf die Topics (Eigene Darstellung)</p>
<Br>


## Literatur

