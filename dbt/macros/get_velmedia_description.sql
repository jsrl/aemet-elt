{#
    This macro returns the description of the air velmedia according to the Beaufort scale.
#}

{% macro categorize_velmedia(velmedia) %}
    case
        when {{ velmedia }} < 0.3 then 'Calm'
        when {{ velmedia }} between 0.3 and 1.5 then 'Light Air'
        when {{ velmedia }} between 1.6 and 3.3 then 'Light Breeze'
        when {{ velmedia }} between 3.4 and 5.4 then 'Gentle Breeze'
        when {{ velmedia }} between 5.5 and 7.9 then 'Moderate Breeze'
        when {{ velmedia }} between 8.0 and 10.7 then 'Fresh Breeze'
        when {{ velmedia }} between 10.8 and 13.8 then 'Strong Breeze'
        when {{ velmedia }} between 13.9 and 17.1 then 'Near Gale'
        when {{ velmedia }} between 17.2 and 20.7 then 'Gale'
        when {{ velmedia }} between 20.8 and 24.4 then 'Strong Gale'
        when {{ velmedia }} between 24.5 and 28.4 then 'Storm'
        when {{ velmedia }} between 28.5 and 32.6 then 'Violent Storm'
        else 'Hurricane-force'
    end
{% endmacro %}
