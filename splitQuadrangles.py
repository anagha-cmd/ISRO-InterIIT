from formClusters import quadrangle
import numpy as np

lat, lon = -44.623022750000004, -60.522823750000015 #from xml file or metadata of tiff image like in formClusters
def quadrangleSplit(lat, lon):

    quad = quadrangle(lat, lon) 

    quad_split = 0

    quadranglesMidpt = []

    quadranglesMidpt.append(((65+90)/2, 0))

    quadranglesMidpt.append(((30+65)/2, (-180+-120)/2))
        
    quadranglesMidpt.append(((30+65)/2, (-120+-60)/2))
        
    quadranglesMidpt.append(((30+65)/2, (-60+-0)/2))
        
    quadranglesMidpt.append(((30+65)/2, (0+60)/2))
        
    quadranglesMidpt.append(((30+65)/2, (60+120)/2))
        
    quadranglesMidpt.append(((30+65)/2, (120+180)/2))
        
    quadranglesMidpt.append(((0+30)/2, (-180+-135)/2))
        
    quadranglesMidpt.append(((0+30)/2, (-135+-90)/2))
        
    quadranglesMidpt.append(((0+30)/2, (-90+-45)/2))
        
    quadranglesMidpt.append(((0+30)/2, (-45+0)/2))
        
    quadranglesMidpt.append(((0+30)/2, (0+45)/2))
        
    quadranglesMidpt.append(((0+30)/2, (45+90)/2))
        
    quadranglesMidpt.append(((0+30)/2, (90+135)/2))
        
    quadranglesMidpt.append(((0+30)/2, (135+180)/2))
        
    quadranglesMidpt.append(((-30+0)/2, (-180+-135)/2))
        
    quadranglesMidpt.append(((-30+0)/2, (-135+-90)/2))
        
    quadranglesMidpt.append(((-30+0)/2, (-90+-45)/2))
        
    quadranglesMidpt.append(((-30+0)/2, (-45+0)/2))
        
    quadranglesMidpt.append(((-30+0)/2, (0+45)/2))
        
    quadranglesMidpt.append(((-30+0)/2, (45+90)/2))
        
    quadranglesMidpt.append(((-30+0)/2, (90+135)/2))
        
    quadranglesMidpt.append(((-30+0)/2, (135+180)/2))
        
    quadranglesMidpt.append(((-65+-30)/2, (-180+-120)/2))
        
    quadranglesMidpt.append(((-65+-30)/2, (-120+-60)/2))
        
    quadranglesMidpt.append(((-65+-30)/2, (-60+-0)/2))
        
    quadranglesMidpt.append(((-65+-30)/2, (0+60)/2))
        
    quadranglesMidpt.append(((-65+-30)/2, (60+120)/2))
        
    quadranglesMidpt.append(((-65+-30)/2, (120+180)/2))
        
    quadranglesMidpt.append(((-90+65)/2, 0))

    # print(len(quadranglesMidpt), quadranglesMidpt)

    split = np.array([lat,lon]) - np.array(quadranglesMidpt[quad-1])
    if split[0]>0 and split[1]>0:
        quad_split = 1
    elif split[0]>0 and split[1]<=0:
        quad_split = 2
    elif split[0]<=0 and split[1]<=0:
        quad_split = 3
    elif split[0]<=0 and split[1]>0:
        quad_split = 4
    
    return quad_split
print(quadrangleSplit(lat,lon))