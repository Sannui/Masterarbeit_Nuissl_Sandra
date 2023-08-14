# Instalationen
#!pip install dash
#!pip install jupyter_dash
#!pip install bertopic


# Imports
import pandas as pd

# Visualisierung
import dash
from dash import Dash, callback, dash_table, html
from jupyter_dash import JupyterDash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc

# Modell
from bertopic import BERTopic

# Verwendete Marken
brand_list = ["adidas", "Columbia", "Speedo"]

# Laden der Datensäzte
# Datensätze
adidas_df = pd.read_hdf('adidas_df.h5')
columbia_df = pd.read_hdf('columbia_df.h5')
speedo_df = pd.read_hdf('speedo_df.h5')

# Umwandeln in Listen
adidas_list = adidas_df["cleanedText"].to_list()
columbia_list = columbia_df["cleanedText"].to_list()
speedo_list = speedo_df["cleanedText"].to_list() 

# Modelling
# Initialisierung (mehr ist nicht nötig => zeigt dann an, wie lange es noch zum laden braucht)
adidas_bert_model = BERTopic(verbose=True)
columbia_bert_model = BERTopic(verbose=True)
speedo_bert_model = BERTopic(verbose=True)

# Training der Modelle
adiadas_topics = adidas_bert_model.fit_transform(adidas_list)
columbia_topics = columbia_bert_model.fit_transform(columbia_list)
speedo_topics = speedo_bert_model.fit_transform(speedo_list)

# Ergänzung der DataFrames um die Topics und Probabilities
# Hinzufügen der Topics
adidas_df["Topics"] = adiadas_topics[0]
columbia_df["Topics"] = columbia_topics[0]
speedo_df["Topics"] = speedo_topics[0]

# Hinzufügen der Wahrscheinlichkeiten
adidas_df["Probabilities"] = adiadas_topics[1]
columbia_df["Probabilities"] = columbia_topics[1]
speedo_df["Probabilities"] = speedo_topics[1]


# Dashboard
# Initialisierung der App
app = dash.Dash(suppress_callback_exceptions=True, title= "Konzept zur Analyse der Produktreviews",
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

# Layout
app.layout = html.Div([
    # Container Head
    html.Div([
        # Überschrift
        html.H1("Topic Modelling Analyse der Amazon Daten", style={'textAlign': 'center', 'marginTop': '50px', 'font-size': '30px'}),
        # Unterüberschrift
        html.H2("- Sport and Outdoors -", style={'textAlign': 'center'}),
        # Trennlinie
        html.Hr(),
        # Fließtext
        html.Div([
            html.P("Dieses Dashboard ist Teil der Masterarbeit ", style={'display': 'inline'}),
            html.A("„Empirische Evaluation von 'State Of The Art Topic Modeling' Ansätze am Beispiel von Produktreviews für die Entscheidungsunterstützung in Unternehmen“", href='https://github.com/Sannui/Masterarbeit_Nuissl_Sandra/tree/main', target='_blank', style={'display': 'inline'}),
            html.P(" . Es stellt ein Konzept zur möglichen Optimierung von der Analyse von Prouktreviews unter der Anwendung von ", style={'display': 'inline'}),
            html.A("BERTopic", href='https://arxiv.org/abs/2203.05794', target='_blank', style={'display': 'inline'}),
            html.P(" dar. Das Topic Modelling wurde anhand eines Ausschnitts der ", style={'display': 'inline'}),
            html.A("Amanzon Datensat von Jianmo Ni", href='https://cseweb.ucsd.edu/~jmcauley/datasets/amazon_v2/', target='_blank', style={'display': 'inline'}),
            html.P(" erstellt. Da die Ladedauer bei großen Datenmengen stark ansteigt, enthält der hier verwendete Datensatz lediglich die Daten von „adidas“ „Columbia“ und „Speedo“. Des Weitern wird zur Selektion lediglich der Filter „Marke“ verwendet. Für zukünftige Arbeiten könnte dies um den Filter „Produkt“ und „Overall“ erweitert werden. Auf diese Weise wäre eine noch detailierte Analyse von Unternehmensdaten möglich und es könnte über die selektion der Sternebewertung auch ein Stimmungsbild eingefangen werden.", style={'display': 'inline'}),
        ], style={'font-size': '20px', "marginTop": "50px", 'text-align': 'justify', 'line-height': '2.0'}),
]),

    # Container Verfasser und Datum
    html.Div([
        # Verfasser
        html.Div([
            html.P("von Sandra Nuißl"),
        ], style={'width': '15%', 'display': 'inline-block', 'font-size': '18px'}),
        # Datum
        html.Div([
            html.P("14.08.2023"),
        ], style={'width': '30%', 'display': 'inline-block', 'font-size': '18px'}),
    
    ], style={'marginTop': '20px', 'color': 'darkgray'}),

    
    # Container Filter
    html.Div([ 
        # Überschrift
        html.H2("Filteroptionen", style={'marginTop': '50px'}),
        # Filter
        html.Div([
            # Überschrift
            html.Div([
                html.P("Marken:"),
            ], style={'width': '10%', 'display': 'inline-block', 'font-size': '18px'}),
            # Dropdown
            html.Div([
                dcc.Dropdown(
                  options=[{'label': brand, 'value': brand} for brand in brand_list],
                  value="adidas",
                  id='input_brand',
                  clearable=False),
            ], style={'width': '15%', 'display': 'inline-block'}),
        ]),
    ]),


    # Auswertungen: Allgemeines zu den Topics
    html.Div([
        # Überschrift
        html.Div([
            html.H2("Die Topics des Datensatzes"),
            html.Hr(),
        ], style={'marginTop': '80px'}),
        # Grafik: Balkendiagramm Topics + Text
        html.Div([
            html.Div([
              dcc.Graph(id='topics_fig'),
            ], style={'display': 'inline-block', 'marginTop': '25px'}),
            html.Div([
                html.H4("Repräsentative Wörter"),
                html.P(id ='output-text'),
                html.P("Die Balkendiagramme repräsentieren die Häufigkeit, mit welcher das Wort in dem Topic vorkommt. Je häufiger es Auftritt, desto länger ist der Balken. Auf diese Weise lassen sich die Topics durch eine Ansammlung von Wörtern interpretieren. Jedoch ist zu beachten, dass die Interpretaion rein subjektiv ist, da jeder Mensch die Wörter mit unterschiedlichen Themen assoziieren kann."),
            ], style={'width': '40%', 'display': 'inline-block', 'vertical-align': 'top', 'marginTop': '25px', 'font-size': '18px', 'line-height': '2.0'}),
        ]),
    ]),

    # Auswertungen: Timeline
    html.Div([
        # Überschrift
        html.Div([
            html.H2("Topics im zeitlichen Verlauf"),
            html.Hr(),
        ], style={'marginTop': '80px'}),
        html.Div([
            html.P("Mithilfe von BERTopic lassen sich die Topics auch in einem Zeitlichen Verlauf darstellen. Jede Linie repräsentiert hierbei ein Topic, die y-Achse gibt die Menge der Reviews an und die x-Achse ist eine Zeitachse von 2011 bis 2018. Für eine bessere Analyse lassen sich mithilfe der Legende einzelne Topics selektieren. Hierfür zuerst einen Doppelklick auf die weiße Fläche der Legende und dann das gewünschte Topic auswählen. Es können natürlich auch mehrere Topics selektiert werden, um diese miteinander zu vergleichen."),
        ], style={'marginTop': '10px', 'font-size': '18px', 'line-height': '2.0'}),
        # Grafik: Balkendiagramm Topics + Text
        html.Div([
          dcc.Graph(id='time_fig'),
        ], style={'marginTop': '35px', 'display': 'flex', 'justify-content': 'center'}),
    ]),


    # Intertopic Distanz und Doc-Topic
    html.Div([
        # Überschrift
        html.Div([
            html.H2("Cluster der Topics"),
            html.Hr(),
        ], style={'marginTop': '80px'}),
        # Unterüberschriften
        html.Div([
            html.Div([
                html.H3("Cluster der Reviews pro Topic"),
            ], style={'width': '50%', 'display': 'inline-block', 'textAlign': 'center', 'marginTop': '25px'}),
            html.Div([
                html.H3("Intertopic Distance Map"),
            ], style={'width': '50%', 'display': 'inline-block', 'textAlign': 'center', 'marginTop': '25px'}),
        ]),
      
        # Grafiken
        html.Div([
            html.Div([
              dcc.Graph(id='topic_docs_fig'),
            ], style={'width': '50%', 'justify-content': 'center', 'display': 'inline-block', 'marginTop': '25px'}),
            html.Div([
                dcc.Graph(id='intertopic_distanz_fig'),
            ], style={'width': '50%', 'justify-content': 'center', 'display': 'inline-block', 'marginTop': '25px'}),
        ]),

        # Texte
        html.Div([
            html.Div([
                html.P("Die Grafik zeigt die Reviews in eine zweidimensionale Matrix geplottet. Die Farben stellen die verschiedenen Topics dar und die einzelnen Punkte stehen für die Reviews. Je näher diese zusammen liegen, desto dichter ist das gebildete Cluster und desto ähnlicher sind sich die Inhalte der Reviews. Die Grauen bereiche bilden die Ausreißer, welche zu keinem Topic zugeordnert werden können."),
            ], style={'width': '40%', 'display': 'inline-block', 'marginTop': '25px',  'font-size': '18px', 'line-height': '2.0', 'paddingLeft': '70px', 'paddingRight': '50px', 'text-align': 'justify'}),
            html.Div([
                html.P("Die Intertopic Distance Map visualisiert den Umfang der Topics im Verhältnis zu ihrer semantischen Bedeutung. Die Größe der Bubbels repräsentiert die Anzahl der Reviews welche in dieses Thema fallen. Die Lage im Raum steht für den Inhalt eines Topics. Je ähnlicher sich die Inhalte verschiedener Topics sind, desto näher liegen diese beieinander. Auf diese Weise lassen sich Themengruppen und überlappende Themen identifizieren."),
            ], style={'width': '40%', 'display': 'inline-block', 'marginTop': '25px',  'font-size': '18px', 'line-height': '2.0', 'paddingLeft': '80px', 'paddingRight': '40px', 'text-align': 'justify'}),
        ]),
    ]),
        
    # Auswertungen: Hierarchisches Clustering
    html.Div([
        # Überschrift
        html.Div([
            html.H2("Hierarchisches Clustering der Topics"),
            html.Hr(),
        ], style={'marginTop': '80px'}),
        html.Div([
            html.P("Das Dendrogram zeigt die hierarchischen Verknüpfungen zwischen den einzelnen Topics. Dies ist eine weitere Form die semantischen Beziehungen zwischen den Topics zu visualisieren. Je ähnlicher sich die Themen sind, desto eher werden diese im Baum verknüpft. Die Abbildung zeigt die ersten 30 Topics, für eine ausfürlichere Analyse könnte dies jedoch ebenfalls programmatisch mit einem DropDown Menu versehen werden, über welches die gewünschte Anzahl der Topics eingegeben wird, die der Anwender auslesen möchte."),
        ], style={'marginTop': '10px', 'font-size': '18px', 'line-height': '2.0'}),
        # Grafik: Balkendiagramm Topics + Text
        html.Div([
          dcc.Graph(id='hierarchical_topics_fig'),
        ], style={'marginTop': '35px', 'display': 'flex', 'justify-content': 'center'}),
    ]),

    
    # Auswertung: Klassen der Topics
    html.Div([
        # Überschrift
        html.Div([
            html.H2("Topics in Bezug auf die Sternebewertung der Reviews"),
            html.Hr(),
        ], style={'marginTop': '80px'}),
        # Grafik: Balkendiagramm Topics + Text
        html.Div([
            html.Div([
              dcc.Graph(id='class_fig'),
            ], style={'display': 'inline-block', 'marginTop': '25px'}),
            html.Div([
                html.H4("Sternebewertungen als Klassen"),
                html.P("BERTopic bietet die Möglichkeit die Analyse auf das Gruppieren in Klassen auszuweiten. Was als Klasse definiert werden soll, kann durch die Informationen des Datensatzes festgelegt werden. Man könnte beispielsweise auch die Produkte einer Firma als Klassen definieren. Im Rahmen dieser Masterarbeit wurden die Sternebewertungen als Klassen festgelegt. Auf diese Weise lässt sich identifizieren, zu welcher Sternebewertung es die meisten Reviews gibt. Dadurch lassen sich ebenfalls Rückschlüsse auf die allgemeine Zufriedenheit der Kunden ziehen."),
            ], style={'width': '40%', 'display': 'inline-block', 'vertical-align': 'top', 'marginTop': '25px', 'font-size': '18px', 'line-height': '2.0', 'marginLeft': '50px'}),
        ]),
    ]),



html.Br(),
    
], style={"font-family": "Corbel", "background-color": "#FFFFFF", 'marginLeft': '40px', 'marginRight': '40px'})




# Initialisierung des Callbacks
@app.callback(Output(component_id='output-text',component_property='children'),
              Output(component_id='topics_fig',component_property='figure'),
              Output(component_id='time_fig',component_property='figure'),
              Output(component_id='topic_docs_fig',component_property='figure'),
              Output(component_id='intertopic_distanz_fig',component_property='figure'),
              Output(component_id='hierarchical_topics_fig',component_property='figure'),
              Output(component_id='class_fig',component_property='figure'),
              [Input(component_id='input_brand',component_property='value')])

# Definition der Funktion zur Errechnung der Anzahl von Produkte und Reviews

# Definition der Funktion zur Auswahl der Marke

def update_figures(brand):
    # Auswahl der richtigen Parameter über die Marke
    if brand == "adidas":
        bert_model = adidas_bert_model
        docs_list = adidas_list
        timestamps = adidas_df["year"].to_list()
        classes = adidas_df["overall"].to_list()
    elif brand == "Columbia":
        bert_model = columbia_bert_model
        docs_list = columbia_list
        timestamps = columbia_df["year"].to_list()
        classes = columbia_df["overall"].to_list()
    elif brand == "Speedo":
        bert_model = speedo_bert_model
        docs_list = speedo_list
        timestamps = speedo_df["year"].to_list()
        classes = speedo_df["overall"].to_list()
    
    # Anzahl der Topics ermitteln
    number_of_topics = len(bert_model.get_topic_info())
    text = (f"Es wurden für die Marke {brand} mithilfe des Modells BERTopic {number_of_topics} Topics identifiziert.")

    # Erstellen der Graphiken
    topics_fig = bert_model.visualize_barchart(top_n_topics=8)                                                   # Barchart

    topics_over_time            = bert_model.topics_over_time(docs_list, timestamps)                             # Zeitlicher Verlauf
    time_fig                    = bert_model.visualize_topics_over_time(topics_over_time, top_n_topics= 15)

    topic_docs_fig              = bert_model.visualize_documents(docs_list, topics=[0,1,2,3,4,5,6,7,8,9,10])     # Scatter Docs zu Topics
    intertopic_distanz_fig      = bert_model.visualize_topics(top_n_topics=100)                                  # Intertopic Distance map
    hierarchical_topics_fig     = bert_model.visualize_hierarchy(top_n_topics=30)                                # Hierarchie  

    topics_per_class            = bert_model.topics_per_class(docs_list, classes)                                # Topics in Klassen
    class_fig                   = bert_model.visualize_topics_per_class(topics_per_class)

    # Update der Layouts
    topics_fig.update_layout(width= 800, title="", margin=dict(t=30, b=20))
    time_fig.update_layout(height= 300, title="", margin=dict(t=30, b=20))
    topic_docs_fig.update_layout(width= 650, height= 550, title="", margin=dict(t=30, b=20), showlegend= False)
    intertopic_distanz_fig.update_layout(width= 650, height= 550, title="", margin=dict(t=30, b=20))
    hierarchical_topics_fig.update_layout(width= 1200, height= 550, title="", margin=dict(t=30, b=20))
    class_fig.update_layout(width= 800, height= 550, title="", margin=dict(t=30, b=20))

    return text, topics_fig, time_fig, topic_docs_fig, intertopic_distanz_fig, hierarchical_topics_fig, class_fig


if __name__ == '__main__':
    app.run_server()
