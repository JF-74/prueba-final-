# prueba-final-

## Integrantes
- Jose Aravena
- Daniel Pellegrini
- Vicente Heredia
- Matias Cisternas

## Descripción del Proyecto
este proyecto cuanta con la implememtacion de Data Lakehouse
- *orquestacion* prefec.
- *ingesta* polars.
- *almacenamiento* DuckDB.
- *tranformacion* dbt Core.
- *visualizacion* plotly/Dash.

## Modelo Multidimensional

- *dimenciones* `dim_date`,`dim_customer`,`dim_producto`,`dim_geography`. esta dimenciones nos permiten agrupar y filtrar los datos de este negocio
- *medidas* `sales`,`delivery_days_diff`,`orden_count`. estos son las valores del rendimiento de los numeros cuantificados
- *tabla de hechos*`fct_ordens`. como esta es la tabla que vincula las dimenciones y almacenar las medidas, lo que permite el rendimiento del analisis de logistica

## ejecucion 
para permitir que el pipeline se ejecute de manera completa
`docker compose up`
