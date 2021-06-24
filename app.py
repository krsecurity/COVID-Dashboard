import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("covid.csv")
data = data.query("areaCode == 'E92000001' and areaName == 'England'")
data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d")
data.sort_values("date", inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="COVID-19 in England",),
        html.P(
            children="An analysis of COVID-19"
            " throughout England"
            " from March 2020 to June 2021",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {"x": data["date"], "y": data["newCasesByPublishDate"], "type": "lines", "name": "Cases"},
                    {"x": data["date"], "y": data["newDeaths28DaysByPublishDate"], "type": "lines", "name": "Deaths"},
                    {"x": data["date"], "y": data["newAdmissions"], "type": "lines", "name": "Hospitalisations"},
                     ],
                "layout": {"title": "All Data"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["date"],
                        "y": data["newCasesByPublishDate"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Cases"},
                    },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["date"],
                        "y": data["newDeaths28DaysByPublishDate"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Deaths"},
                    },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["date"],
                        "y": data["newAdmissions"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Hospitalisations"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)