# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 07:50:59 2022

@author: abstractengineer2000
"""
import utilitiesfuncs as uf

sp = uf.spaceenginefuncs('myfunc')
outfilepath = 'Z://SteamLibrary//steamapps//common//SpaceEngine//addons//catalogs//galaxies//galacticdeepfield.sc'

sp.GalaticDeepField('ABC',300,outfilepath,15,15.05,7,7.45,1e8,2e8,20000,30000,-25,-22)

sp.GalaticDeepField('PQR',100,outfilepath,25,25.025,10,10.226,1e8,2e8,20000,30000,-25,-22)

sp.GalaticDeepField('XYZ',50,outfilepath,30,30.025,20,20.185,1e8,2e8,20000,30000,-25,-22)


