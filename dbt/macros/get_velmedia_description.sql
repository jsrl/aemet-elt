{#
    This macro returns the description of the air velmedia
#}

{% macro categorize_velmedia(velmedia) %}
    case
        when {{ velmedia }} between 0 and 5.4 then 'Calm'
        when {{ velmedia }} between 5.5 and 11.9 then 'Light Breeze'
        when {{ velmedia }} between 12.0 and 19.4 then 'Gentle Breeze'
        when {{ velmedia }} between 19.5 and 28.4 then 'Moderate Breeze'
        when {{ velmedia }} between 28.5 and 38.5 then 'Fresh Breeze'
        when {{ velmedia }} between 38.6 and 49.7 then 'Strong Breeze'
        when {{ velmedia }} between 49.8 and 61.6 then 'Near Gale'
        when {{ velmedia }} between 61.7 and 74.5 then 'Gale'
        when {{ velmedia }} between 74.6 and 87.9 then 'Strong Gale'
        when {{ velmedia }} between 88.0 and 102.2 then 'Storm'
        when {{ velmedia }} between 102.3 and 117.4 then 'Violent Storm'
        else 'Hurricane-force'
    end
{% endmacro %}
