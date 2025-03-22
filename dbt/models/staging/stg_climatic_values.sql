{{ config(materialized="view") }}

with climatic_values as (select * from {{ source("staging", "climatic_values") }})

select
    {{ dbt_utils.generate_surrogate_key(["indicativo", "fecha"]) }} as record_id,
    --hora_pres_min,
    --hora_pres_max,
    ano,
    --racha,
    --pres_max,
    --hr_media,
    --_dlt_load_id,
    --hora_hr_min,
    --horaracha,
    --_dlt_id,
    --hr_min,
    --sol,
    tmin,
    --hora_hr_max,
    --dir,
    --pres_min,
    --hr_max,
    --horatmax,
    tmax,
    indicativo,
    tmed,
    --horatmin,
    velmedia,
    {{ categorize_velmedia("velmedia") }} as velmedia_description,
    fecha,
    prec,
    --provincia,
    --nombre,
    --altitud
from climatic_values
