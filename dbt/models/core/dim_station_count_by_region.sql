{{ config(materialized="table") }}

with stations as (select * from {{ ref("stg_weather_stations") }})

select autonomous_community as region, count(distinct indicativo) as total_stations
from stations
group by 1
order by total_stations desc
