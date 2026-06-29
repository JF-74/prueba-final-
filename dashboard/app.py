import dash
from dash import dcc, html
import plotly.express as px
import duckdb

def get_data():
    con = duckdb.connect('/workspace/data/ecommerce_analytics.dbdb', read_only=True)
    df = con.execute("SELECT * FROM fct_orders").df()
    con.close()
    return df

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard Ejecutivo: Ecomerce analytics"),
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': r, 'value': r} for r in sorted(get_data()['region'].unique())],
        placeholder="Seleccione una región..."
    ),
    dcc.Graph(id='ventas-graph')
])

@app.callback(
    Output('ventas-graph', 'figure'),
    [Input('region-dropdown', 'value')]
)
def update_graph(selected_region):
    if not selected_region:
        return px.bar(title="Seleccione una región para ver datos")
    df = get_data()
    filtered_df = df[df['region_clean'] == selected_region]
    fig = px.bar(filtered_df, x='product_category', y='sales',
                 title=f"Ventas en {selected_region}")
    return fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050)
