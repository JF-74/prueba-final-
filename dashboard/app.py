from dash import Dash, html, dash_table
import duckdb
import os

app = Dash(__name__)

db_path = ('/workspace/data/ecommerce_analytics.db')

try:
    con = duckdb.connect(db_path, read_only=True, config={'access_mode': 'read_only'})
    df = con.execute("SELECT * FROM main.fct_sales").df()
    con.close()

    table = dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{"name": i, "id": i} for i in df.columns]
    )
except Exception as e:
    table = html.Div(f"Error cargando datos: {e}")

app.layout = html.Div([
    html.H1("Dashboard de Ecommerce"),
    table
])

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8050, debug=False)
