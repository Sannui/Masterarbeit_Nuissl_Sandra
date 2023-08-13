# Implementierung des Topic Modelling Modells: ZeroShotTM
Theoretischer Text...

<Br>
<p align="center">
  <img width="850" height="400" src="img/ZeroSHotTM_Theorie.png">
</p>
<p align="center">Architektur des ZeroShotTM (Eigene Darstellung in Anlehnung an (Bianchi, Terragni, Hovy, Nozza, & Fersini, 2020))</p>

<Br>

## Besonderheiten der Implementierung
Im Rahmen dieser Masterarbeit wurde die Implementierung eines ZeroShotTM Modelles mithilfe der [Library von ZeroSHotTM](https://github.com/MilaNLProc/contextualized-topic-models) selbst durchgeführt. Bevor die Implementierung von BERTopic beginnen kann, ist es hilfereich zur Beschleunigung der Prozesse des Embeddings und der Dimensionsreduktion PyTorch zu installieren. Auf diese Weise lässt sich mithilfe der NVIDIA-GPUs die Laufzeit um das bis zu 4,5 Fache beschleunigen (Grootendorst, Faster Topic Modeling with BERTopic and RAPIDS cuML, 2023).

Die Implementierung ist hierfür im Folgenden aufgeführt:

```
# Insatlationen
%pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116
%pip install -U contextualized_topic_models
```
```
# Imports
import contextualized_topic_models
from contextualized_topic_models.utils.preprocessing import WhiteSpacePreprocessing
from contextualized_topic_models.models.ctm import ZeroShotTM
from contextualized_topic_models.utils.data_preparation import TopicModelDataPreparation
from contextualized_topic_models.utils.data_preparation import bert_embeddings_from_file
```

### __Intitialisierung__
Das Pre-Trained-Modell von BERtopic wird initialisiert, indem die Klasse „BERTopic“ aufgerufen und in einer Variable gespeichert wird. Hierbei sind die Stufen des Embeddings, der Dimensionsreduktion und des Clusterings zusammengefasst. 
```
zeroshot_model = ZeroShotTM(bow_size=len(embedding_model.vocab),
                            contextual_size=embeddings[1]["X_contextual"].shape[0])
```
<Br>

### __Anwendung des Modells__
Die Anwendung auf den Amazondatensatz erfolgt über ein "fit_transform()" Funktion, welche die Topics pro Review, sowie deren Wahrscheinlichkeiten ausgibt.
```
zeroshot_model.fit(embeddings)
```
<Br>

## Ergebnisse

-	Topic 0: camp cooler backpacking food trip pack ice emergency camping oven
-	Topic 1: considered coat meaning micro drawback anyways factor http suspect afford
-	Topic 2: socks pants gloves pair her she balls wear shorts sock
-	Topic 3: was up so on to have in water it that
-	Topic 4: targets tings rifle sights 22 tires installed install bikes gun
-	Topic 5: delivery delivered thank shipped described expectations sign seller thanks
-	Topic 6: extreme scale internal admit entirely grade ensure lowest bending exception
-	Topic 7: is the this with it knife for be but as
-	Topic 8: whistle disc bass chalk trout flies lure stopwatch therapy frisbee
-	Topic 9: considered complained meaning drawback sat admit factor search suspect

<p align="center">
  <img width="850" height="450" src="img/BERT_Topics.png">
</p>
<p align="center">Repräsentative Wörter je Topic (Eigene Darstellung)</p>
<Br>



## Literatur

