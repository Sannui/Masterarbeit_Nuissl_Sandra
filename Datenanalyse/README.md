# Datenalalyse der Amazon Datensätze "Sport and Outdoors"

Im Rahmen dieses Notebooks wurde eine Analyse der aufbereiteten [Review und Meta Daten der Amazon Datensätze](https://nijianmo.github.io/amazon/index.html) von Jianmo Ni durchgeführt. Im Rahmen der Masterarbeit wurden die Datensätze zu "Sport and Outdoors" untersucht. Aus Kapazitätsgründen wurde für die Analyse der Review Daten der verkleinerte Datensatz mit 2.839.940 reviews herangezogen, da ohne Beschleunigung die Verarbeitung von mehr als 12 Mio. Zeilen zu lange Laufzeiten aufweist.


<p align="center">
  <img width="800" height="400" src="wordcloud.png">
</p>


## Aufbau der Analyse

Die Analyse der Daten Gliedert sich in in drei Kategorien:
<ul>4. Analyse der Review Daten</ul>
    <ul>
     <ul>4.1. Allgemeiner Überblick</ul>
     <ul>4.2. Analyse einzelner Spalten</ul>
        <ul>
         <ul>4.2.1. reviewText</ul>
         <ul>4.2.2. unixReviewTime</ul>
         <ul>4.2.3. overall</ul>
         <ul>4.2.4. asin</ul>
        </ul>
    </ul>
<ul>5. Analyse der Meta Daten</ul>
    <ul>
     <ul>5.1. Allgemeiner Überblick</ul>
     <ul>5.2. Analyse einzelner Spalten</ul>
        <ul>
         <ul>5.2.1. title</ul>
         <ul>5.2.2. brand</ul>
        </ul>
