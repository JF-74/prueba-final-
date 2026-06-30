from dash import Dash, html, dash_table
import dash_bootstrap_components as dbc
import duckdb
import os

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

db_path = '/workspace/data/ecommerce_analytics.db'

try:
    con = duckdb.connect(db_path, read_only=True, config={'access_mode': 'read_only'})
    df = con.execute("SELECT * FROM main.fct_sales").df()
    con.close()

    tabla = dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i.replace("_", " ").title(), "id": i} for i in df.columns],
        page_size=15,
        style_table={'overflowX': 'auto', 'width': '100%'},
        style_cell={
            'textAlign': 'left', 
            'padding': '12px',
            'fontSize': '14px',
            'fontFamily': 'Arial, sans-serif'
        },
        style_header={
            'fontWeight': 'bold',
            'backgroundColor': '#e9ecef',
            'textAlign': 'center',
            'padding': '15px',
            'border': '1px solid #dee2e6'
        }
    )
except Exception as e:
    tabla = html.Div(f"Error cargando datos: {e}", className="text-danger")

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Dashboard de Ecommerce", className="text-center my-4"), width=12)
    ]),
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Detalle de Ventas"),
            dbc.CardBody(tabla)
        ], className="shadow-sm"), width=12)
    ])
], fluid=True, className="mb-5")

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050, debug=False)
