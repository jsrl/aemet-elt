{{
    config(
        materialized='table'
    )
}}

with climatic_values as (
    select *
    from {{ ref('stg_climatic_values') }}
),

stations as (
    select *
    from {{ ref('stg_weather_stations') }}
)

select
    c.record_id,
    c.fecha,
    c.indicativo,
    c.tmin,
    c.tmax,
    c.tmed,
    c.velmedia,
    c.velmedia_description,    
    c.prec,
    c.ano,
    s.nombre,
    s.provincia,
    s.autonomous_community
from climatic_values c
left join stations s
    on c.indicativo = s.indicativo