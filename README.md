postgisQueryBuilder
===================
User friendly postgis query compilation.
The plugin allows a semi-automatic compilation of common postgis sql queries by the assisted insertion/selection of the needed parameters (tables and fields names, operators and postgis functions)
Is also included postgres views support (with Materialize Directive, new from psql 9.3), aimed to allow dynamic manipulation of spatial data with chains of nested views.  Using views there is no need to write intermediate tables, as the typical workflow of gis software like Geomedia.