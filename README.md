# Empirische Evaluation von "State Of The Art" Topic Modeling Ansätze am Beispiel von Produktreviews für die Entscheidungsunterstützung in Unternehmen

<center><img src="https://www.cloudways.com/blog/wp-content/uploads/Product-Review-1024x576.jpg" height="300px" width="1100px"/></center>
Masterarbeit von Sandra Nuißl - 14.08.2023



## Hinweis zu den Notebooks
### Glitly

Dieses Jupyter Notebook enthält Plotly Graphiken. Da diese in Github normalerweise aufgrund der statistischen Viewer nicht angezeigt werden können, wurde der Code mithilfe der Library [Gitly](https://github.com/Tiagoeem/gitly) in einem statistischen Format gerendert. Hierfür muss eine bestimmte Version von Plotly sowie glitly installiert werden:

```
%pip install gitly==1.0.1
%pip install plotly>4.0.0
```
Für eine statistische Darstellung muss nach dem Import der Library das Objekt für GitHub instanziiert werden. Dies erfolgt durch die eingabe von "github" als Parameter.

```
# Import des Glitly Plotters
from gitly.colab.plot import GitlyPlotter

# Instanziierung des Objekts
gitly = GitlyPlotter('github')
```

Nun können alle Plotlygraphiken auch in GitHub angezeigt werden, indem die Ausgabe der Diagramme angepasst wird:

```
fig = px.bar(df, x="column_1", y="column_2")
gitly.show(fig)
```

Um wieder auf eine dynamische Darstellung zu wechseln, muss das Objekt mithilfe des Parameters "colab" neu instanziiert werden. Wichtig hierbei zu beachten ist, dass diese Library speziell für Colab entwickelt wurde und auch nur in diesem Framework verwendet werden kann. Wird das Notebook in einem anderen Editor ausgeführt, kann glitly gelöscht werden und die Ausgabe der Graphiken erfolgt wie gewohnt über die übelichen Befehle von Plotly.

```
# Instanziierung des Objekts
gitly = GitlyPlotter('colab')
```
