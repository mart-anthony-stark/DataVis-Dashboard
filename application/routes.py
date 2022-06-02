from application import app
from flask import render_template, url_for
import pandas as pd
import json
import plotly
import plotly.express as px
@app.route('/')

def index() :
    # Graph one
    df = px.data.medals_wide()
    # df = pd.DataFrame(dict(nation=["Philippines","China","USA"]), dict(gold=[dict(Philippines=3, China=2, USA=12)], silver=[5,4,3], bronze=[10,5,3]))
    print(df)
    d = {"nation":["Philippines","China","USA"], "gold":[4,5,6], "silver":[6,5,4], "bronze":[10,8,4]}
    df = pd.DataFrame(data=d)
    fig1 = px.bar(df, x="nation", y=["gold", "silver", "bronze"], title="Wide=Form Input")


    # Graph 2
    df = px.data.iris()
    # print(df)
    fig2 = px.scatter_3d(df, x = "sepal_length", y = "sepal_width", z = "petal_width", color='species', title="Iris Dataset")

    graph1JSON = json.dumps(fig1,cls=plotly.utils.PlotlyJSONEncoder)
    graph2JSON = json.dumps(fig2,cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", title="Home", graph1JSON = graph1JSON, graph2JSON=graph2JSON)