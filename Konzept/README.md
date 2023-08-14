# Konzept zur optimierten Analyse von Produktreviews


Resultierend aus den Ausführungen im Rahmen dieser Masterarbeit bietet sich für eine Konzepterstellung zur Implementierung einer optimierten Analyse von Produktreviews zur Unterstützung von Entscheidungsträgern das Topic Modelling Modell BERTopic an. Es besitzt bereits eine umfangreiche Pipeline zur Bildung von Clustern und der Identifikation von Topics. Darüber hinaus lassen sich schnell diverse Visualisierungen implementieren. Für eine erhöhte Variabilität können Filteroptionen mitaufgenommen werden, welche eine Selektion einer Marke oder darüber hinaus ein bestimmtes Produkt dieser Marke.


![Konzept](img/Konzept_Webanwendung.gif)
<p align="center">Webapp, welche das Konzept einer optimierten Analyse von Reviewdaten enthält</p>
<Br>



## Zukünftige Schritte und Möglichkeiten

Um das Konzept ganzheitlich zu gestalten, ist es wichtig die Punkte des Preprocessing und der Laufzeit des Modells selbst mit einzubeziehen. Beide haben sich im Rahmen dieser Masterarbeit als laufzeitkritisch erweisen, wodurch für eine effiziente Nutzung des Analysetools dringend eine Form von Beschleunigung mit zu berücksichtigen ist. Wie bereits in Kapitel vier kurz erläutert ist die Verwendung von PySpark eine valide Lösung. Um die im Rahmen diese Masterarbeit aufgetretenen Probleme mit der lokalen Nutzung von PySpark zu vermeiden, kann die entwickelte Preprocessing Pipeline in Databricks implementiert werden. Bevor die modernen Topic Modelling Modelle in Databricks implementiert werden können, müssen nach dem Preprocessing mit PySpark die Inputwerte in Python-Variablen überführt werden, da es hierfür noch keine Implementierungen in Scala gibt.


