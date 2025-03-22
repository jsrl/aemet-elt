{{ config(materialized="table") }}

with fact_weather as (select * from {{ ref("fact_weather") }})

select
    provincia as province,
    autonomous_community as region,

    -- Temporal grouping: Grouping data by first month day
    {{ dbt.date_trunc("month", "fecha") }} as weather_month,

    -- Climatic values summary: Aggregating minimum, maximum and average temperatures
    round(avg(tmin), 2) as avg_monthly_tmin,  -- Average of the minimum daily temperature rounded to 2 decimals
    round(avg(tmax), 2) as avg_monthly_tmax,  -- Average of the maximum daily temperature rounded to 2 decimals
    round(avg((tmin + tmax) / 2), 2) as avg_monthly_tmed,  -- Calculating the average daily temperature from tmin and tmax rounded to 2 decimals
    round(avg(velmedia), 2) as avg_monthly_wind_speed,  -- Average monthly wind speed rounded to 2 decimals

    -- Additional calculation: Total number of climate records for the month
    count(record_id) as total_monthly_records

from fact_weather
group by 1, 2, 3
