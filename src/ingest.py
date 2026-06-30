import pandas as pd
import os
import duckdb

RAW_DATA_PATH = "data/raw"
DB_PATH = "data/ecommerce_analytics.db"
CSV_PATH = os.path.join(RAW_DATA_PATH,"olist_orders_dataset.csv")

def descargar_y_cargar():
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    url = "https://raw.githubusercontent.com/olist/olist-dataset/master/dataset/olist_orders_dataset.csv"

    if not os.path.exists(CSV_PATH):
        print(f"Descargando...")
        try:
            df = pd.read_csv(url)
            df.to_csv(CSV_PATH, index=False)
            print("Descarga exitosa.")
        except Exception as e:
            print(f"Error en la descarga: {e}")
            return

    con = duckdb.connect(DB_PATH)
    con.execute(f"CREATE OR REPLACE TABLE orders AS SELECT * FROM read_csv_auto('{CSV_PATH}')")
    con.close()
    print("Datos cargados en DuckDB correctamente.")

if __name__ == "__main__":
    descargar_y_cargar()
