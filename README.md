postgisQueryBuilder
===================
Automated/assisted postgis query compilation.
The plugin allows a semi-automatic compilation of common postgis sql queries by the assisted insertion/selection of the needed parameters (tables and fields names, operators and postgis functions) It's included postgres views and materialized views (new from psql 9.3) support.
The plugin is aimed to allow the creation of a framework of common spatial queries (selection, join, intersection, difference, union) that, nested and chain each other from source tables bring to complex and dynamic spatial analysis.