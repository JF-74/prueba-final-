
  
    
    

    create  table
      "ecommerce_analytics"."main"."ventas_resumen__dbt_tmp"
  
    as (
      

SELECT
    id,
    valor
FROM ventas
    );
  
  