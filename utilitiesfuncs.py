# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 21:23:50 2022

@author: abstractengineer2000
"""        
import numpy as np    

class spaceenginefuncs(object):
    def __init__(self,name):
        self.name = name           

    def GalaticDeepField(self,name,numgalaxies,outfilepath,RAmin,RAmax,Decmin,Decmax,Distmin,Distmax,radiusmin,radiusmax,absmin,absmax):
                
        with open(outfilepath, 'w') as f:
            np.random.seed(1)
            RAvalue = np.random.uniform(RAmin,RAmax,size=(numgalaxies))            
            Decvalue = np.random.uniform(Decmin,Decmax,size=numgalaxies)
            Dist = np.random.uniform(Distmin,Distmax,size=numgalaxies)
            radius = np.random.uniform(radiusmin,radiusmax,size=numgalaxies)
            absmag = np.random.uniform(absmin,absmax,size=numgalaxies)
            galaxytype = ["E0", "E1", "E2", "E3", "E4", "E5", "E6", "E7","S0","Sa", "Sb", "Sc", "Sd","Irr"]
            vals = np.arange(0,14)
            probs =[0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.025,0.15,0.15,0.15,0.15,0.15,0.05]
            galaxytypeint=np.random.choice(vals, size=numgalaxies, p=probs)            
            for i in range(numgalaxies):                                 
                f.write('Galaxy "'+name +'-G-'+ str(i)+'"\n')   
                f.write('{\n')
                f.write('	Type    "' + galaxytype[galaxytypeint[i]] + '"\n')
                f.write('	RA  '+str(RAvalue[i])+'\n')
                f.write('	Dec ' + str(Decvalue[i]) +'\n')
                f.write('	Dist ' + str(Dist[i]) +'\n')
                f.write('	Radius ' + str(radius[i]) +'\n')
                f.write('	AbsMagn ' + str(absmag[i]) +'\n')               
                f.write('}\n')
                f.write('\n')
                        