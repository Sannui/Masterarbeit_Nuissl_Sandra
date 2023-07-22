# Datenalalyse der Amazon Datensätze "Sport and Outdoors"

Im Rahmen dieses Notebooks wurde eine Analyse der aufbereiteten [Review und Meta Daten der Amazon Datensätze](https://nijianmo.github.io/amazon/index.html) von Jianmo Ni durchgeführt. Im Rahmen der Masterarbeit wurden die Datensätze zu "Sport and Outdoors" untersucht. Aus Kapazitätsgründen wurde für die Analyse der Review Daten der verkleinerte Datensatz mit 2.839.940 reviews herangezogen, da ohne Beschleunigung die Verarbeitung von mehr als 12 Mio. Zeilen zu lange Laufzeiten aufweist.


<p align="center">
  <img width="800" height="400" src="wordcloud.png">
</p>


## Aufbau der Analyse

Neben dem ersten strukturellen und inhaltlichen Analyse der beiden Datensätze werden bewusst Spalten selektiert, welche evtl. für die verwendung der Topic Modelling Modelle von Bedeutung sind und eingehender untersucht.

<ul>1. Analyse der Review Daten</ul>
    <ul>
     <ul>1.1. Allgemeiner Überblick</ul>
     <ul>1.2. Analyse einzelner Spalten</ul>
        <ul>
         <ul>1.2.1. reviewText</ul>
         <ul>1.2.2. unixReviewTime</ul>
         <ul>1.2.3. overall</ul>
         <ul>1.2.4. asin</ul>
        </ul>
    </ul>
<ul>2. Analyse der Meta Daten</ul>
    <ul>
     <ul>2.1. Allgemeiner Überblick</ul>
     <ul>2.2. Analyse einzelner Spalten</ul>
        <ul>
         <ul>2.2.1. title</ul>
         <ul>2.2.2. brand</ul>
        </ul>
     </ul>
</ul>
