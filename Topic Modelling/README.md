# Implementierung der Topic Modelling Modelle und deren empirische Evaluierung






## Kohärenz

Die Kohärenz bezieht sich auf die semitische Verbundenheit von Wörtern, welche im Rahmen des Topic Modelling in Wortlisten gespeichert sind. Durch Sinnbeziehungen der Einheiten des Textes wirkt dieser auf den Leser semantisch konsistent und logisch (Rüdiger, Antons, Joshi, & Salge, 2022). Verallgemeinert gesagt ist eine Aussage kohärent, wenn sich die Inhalte gegenseitig stützen. Mithilfe von Themenkohärenzmaße lässt sich die Ähnlichkeit der Wörter in Bezug auf ein bestimmtes Thema messen (Kapadia, 2019). 

```
coherence_model = CoherenceModel(topics     = topic_list, 
                                 texts      = token_list, 
                                 corpus     = corpus,
                                 dictionary = dictionary, 
                                 coherence  = 'c_v')

```




## Perplexity



```
log_perplexity = -1 * np.mean(np.log(np.sum(probabilities, axis=1)))
perplexity = np.exp(log_perplexity)

```


## Similarity



```
similarity = cosine_similarity(doc_1, doc_2)
```



## Literatur

