#Proyecto final: Pipeline de Datos - Ecommerce Analytics

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

#flujos de datos
Python Ingest -> DuckDB (raw) -> dbt(tranforma -> DuckDB(marts) -> Dash (UI)

## ejecucion 
`docker-compose up -d`
para permitir que el pipeline se ejecute de manera completa con los servicios

##Ingesta de datos
`docker-compose run --rm pipeline python src/ingest.py` 
esto permite que al ocupar el src/ingest.py descargue la base de datos 

##Transformación
`docker-compose run --rm pipeline sh -c "cd dbt && dbt run` 
esto permite cargar el dbt y hacer un dbt run para este pipeline


##Dashboard
`docker-compose up -d dashboard` 
esta parte permite que levante el dashboard 

para acceder al dashboard en `http://localhost:8050`
