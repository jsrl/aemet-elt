{{ config(materialized="view") }}

with weather_stations as (select * from {{ source("staging", "weather_stations") }})

select
    {{ dbt_utils.generate_surrogate_key(["indicativo", "nombre"]) }} as record_id,
    nombre,
    indicativo,
    provincia,
    {{ categorize_provincia("provincia") }} as autonomous_community    
from weather_stations
