{{
  config({    
    "materialized": "ephemeral",
    "database": "ayush_demos",
    "schema": "demos"
  })
}}

WITH customer_events_tracking AS (

  {#Loads data from the ayush_demos_demos table for further processing in the pipeline.#}
  SELECT * 
  
  FROM {{ source('ayush_demos_demos', 'a1') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM customer_events_tracking AS in0

)

SELECT *

FROM Reformat_1
