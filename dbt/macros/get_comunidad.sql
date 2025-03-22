{#
    This macro returns the comunidad from a province given
#}

{% macro categorize_provincia(province) %}
    case
        when {{ province }} in ('ARABA/ALAVA', 'GIPUZKOA', 'BIZKAIA') then 'BASQUE COUNTRY'
        when {{ province }} in ('BARCELONA', 'GIRONA', 'TARRAGONA','LLEIDA') then 'CATALONIA'
        when {{ province }} in ('CASTELLON','ALICANTE','VALENCIA') then 'VALENCIAN COMMUNITY'
        when {{ province }} in ('SEVILLA', 'CADIZ', 'MALAGA', 'CORDOBA', 'HUELVA', 'GRANADA', 'JAEN','ALMERIA') then 'ANDALUSIA'
        when {{ province }} in ('CEUTA') then 'CEUTA'
        when {{ province }} in ('ZARAGOZA', 'HUESCA','TERUEL') then 'ARAGON'
        when {{ province }} in ('CASTILLA Y LEON', 'ZAMORA','LEON','SORIA','SEGOVIA','PALENCIA','VALLADOLID','SALAMANCA') then 'CASTILE AND LEON'
        when {{ province }} in ('BURGOS', 'AVILA', 'CÁCERES', 'BADAJOZ') then 'CASTILE AND LEON'
        when {{ province }} in ('ALBACETE', 'CIUDAD REAL', 'CORDOBA', 'TOLEDO', 'GUADALAJARA', 'CUENCA') then 'CASTILLA-LA MANCHA'
        when {{ province }} in ('LUGO', 'OURENSE', 'PONTEVEDRA', 'A CORUÑA') then 'GALICIA'
        when {{ province }} in ('CANTABRIA') then 'CANTABRIA'
        when {{ province }} in ('MURCIA') then 'MURCIA'
        when {{ province }} in ('MADRID') then 'MADRID'
        when {{ province }} in ('LA RIOJA') then 'LA RIOJA'
        when {{ province }} in ('CACERES') then 'EXTREMADURA'
        when {{ province }} in ('BALEARES','ILLES BALEARS') then 'BALEARIC ISLANDS'
        when {{ province }} in ('ASTURIAS') then 'ASTURIAS'
        when {{ province }} in ('STA. CRUZ DE TENERIFE', 'LAS PALMAS','SANTA CRUZ DE TENERIFE') then 'CANARY ISLANDS'
        when {{ province }} in ('NAVARRA') then 'NAVARRE'
        when {{ province }} in ('CEUTA') then 'CEUTA'
        when {{ province }} in ('MELILLA') then 'MELILLA'
        else 'Unknown'
    end
{% endmacro %}
