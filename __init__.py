# -*- coding: utf-8 -*-
"""
/***************************************************************************
 postgisQueryBuilder
                                 A QGIS plugin
 helps to build views in postgis
                             -------------------
        begin                : 2014-04-24
        copyright            : (C) 2014 by Enrico Ferreguti
        email                : enricofer@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
from __future__ import absolute_import
import site
import os

site.addsitedir(os.path.dirname(__file__))
site.addsitedir(os.path.join(os.path.dirname(__file__),'extlibs'))

def classFactory(iface):
    # load postgisQueryBuilder class from file postgisQueryBuilder
    from .postgisquerybuilder import postgisQueryBuilder
    return postgisQueryBuilder(iface)
