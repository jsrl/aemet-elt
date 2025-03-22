{{ config(materialized="view") }}

with weather_stations as (select * from {{ source("staging", "weather_stations") }})

select
    {{ dbt_utils.generate_surrogate_key(["indicativo", "nombre"]) }} as record_id,
    --_dlt_id,
    --longitud,
    --indsinop,
    --_dlt_load_id,
    nombre,
    indicativo,
    --latitud,
    --altitud,
    provincia,
    {{ categorize_provincia("provincia") }} as autonomous_community,

from weather_stations
