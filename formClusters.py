# import cv2
# import xml.etree.ElementTree as ETree
from bs4 import BeautifulSoup
from splitQuadrangles import quandrangleSplit
from PIL import Image
import pandas as pd
import numpy as np
import re, os, glob, pathlib
Image.MAX_IMAGE_PIXELS = None

# TMC2/ch2_tmc_ndn_20191224T0436128888_d_oth_d18/data/derived/20191224/ch2_tmc_ndn_20191224T0436128888_d_oth_d18.xml
input_path = "TMC2/**/data/**/**/"
output_path = "TMC2/"
pathLs = [xml for xml in sorted(glob.glob(os.path.join(input_path+"*.xml")))]
quadranglesLs = []
# print(pathLs)
 
def quadrangle(lat,lon):
	if (65<lat<=90):
		return 1
	elif (30<lat<=65 and -180<=lon<-120):
		return 2
	elif (30<lat<=65 and -120<=lon<-60):
		return 3
	elif (30<lat<=65 and -60<=lon<-0):
		return 4
	elif (30<lat<=65 and 0<=lon<60):
		return 5
	elif (30<lat<=65 and 60<=lon<120):
		return 6
	elif (30<lat<=65 and 120<=lon<180):
		return 7
	elif (0<lat<=30 and -180<=lon<-135):
		return 8
	elif (0<lat<=30 and -135<=lon<-90):
		return 9
	elif (0<lat<=30 and -90<=lon<-45):
		return 10
	elif (0<lat<=30 and -45<=lon<0):
		return 11
	elif (0<lat<=30 and 0<=lon<45):
		return 12
	elif (0<lat<=30 and 45<=lon<90):
		return 13
	elif (0<lat<=30 and 90<=lon<135):
		return 14
	elif (0<lat<=30 and 135<=lon<180):
		return 15
	elif (-30<lat<=0 and -180<=lon<-135):
		return 16
	elif (-30<lat<=0 and -135<=lon<-90):
		return 17
	elif (-30<lat<=0 and -90<=lon<-45):
		return 18
	elif (-30<lat<=0 and -45<=lon<0):
		return 19
	elif (-30<lat<=0 and 0<=lon<45):
		return 20
	elif (-30<lat<=0 and 45<=lon<90):
		return 21
	elif (-30<lat<=0 and 90<=lon<135):
		return 22
	elif (-30<lat<=0 and 135<=lon<180):
		return 23
	elif (-65<lat<=-30 and -180<=lon<-120):
		return 24
	elif (-65<lat<=-30 and -120<=lon<-60):
		return 25
	elif (-65<lat<=-30 and -60<=lon<-0):
		return 26
	elif (-65<lat<=-30 and 0<=lon<60):
		return 27
	elif (-65<lat<=-30 and 60<=lon<120):
		return 28
	elif (-65<lat<=-30 and 120<=lon<180):
		return 29
	elif (-90<=lat<-65):
		return 30
	

for path in pathLs:
    # Reading the data inside the xml
    # file to a variable under the name
    # data
    with open(path, 'r') as f:
        data = f.read()
    
    # Passing the stored data inside
    # # the beautifulsoup parser, storing
    # # the returned object
    Bs_data = BeautifulSoup(data, "xml")
    
    # # Finding all instances of tag
    # # `unique`
    b_unique = Bs_data.find_all('isda:Corrected_Corner_Coordinates')
    b_unique = ' '.join(map(str, b_unique))
    # print(b_unique)
    b_unique = b_unique.split(">")
    b_unique = ' '.join(map(str, b_unique))
    b_unique = b_unique.split("<")
    # print(b_unique)
    coordinates = []
    for i in range(len(b_unique)):
        coordinates.append(re.findall(r'[\d]*[.][\d]+', b_unique[i]))
    coordinates=[float(gps[0]) for gps in coordinates if gps!=[]]
    print(coordinates) 

    lat_mid = sum(coordinates[0::2])/4
    lon_mid = sum(coordinates[1::2])/4 - 180 # range changed from (0,360) to (-180,180)
    print(lat_mid, lon_mid)
    
    quad_split = quandrangleSplit(lat_mid,lon_mid)

    quad = quadrangle(lat_mid, lon_mid)
    print(quad)
    new_dir_name = str(quad)
    new_dir = pathlib.Path(output_path, new_dir_name)
    if(new_dir.exists()==False):
        new_dir.mkdir(parents=True, exist_ok=True)
    tif_path = path.split(".xml")[0]
    tif_name = tif_path.split("/")[-1]
    # im = Image.open(os.path.join(tif_path+".tif"))
    # imarray = np.array(im)
    # data = Image.fromarray(imarray)     
    # data.save(os.path.join(new_dir, tif_name+".tif"))

    ls = [quad, quad_split, tif_name, tif_path+".tif"]
    quadranglesLs.append(ls)

# To save all image names in a single csv file
df = pd.DataFrame(quadranglesLs, columns=["Quadrangle no.", "Quandrangle Split", "Image name", "Image path"]).sort_values(by=["Quadrangle no."], ascending=True)
df.to_csv("quadranglesLs.csv")

# # To save image names in 30 txt files
# quadranglesLs = np.array(quadranglesLs)
# quadranglesLs[quadranglesLs[:, 0].argsort()]
# for i in range(1,31):
#     q = quadranglesLs[quadranglesLs[:][0]==i]
#     print(q)
#     np.savetxt("quad_"+str(i)+".csv", q, delimiter=",")


# Passing the path of the
# xml document to enable the
# parsing process
# tree = ETree.parse(path)

# getting the parent tag of
# the xml document
# root = tree.getroot()
# print(root.tag)
# printing the root (parent) tag
# of the xml document, along with
# its memory location
# print(root)

# printing the attributes of the
# first tag from the parent
# print(root[1].attrib)
# parent_map = {c: p for p in tree.iter() for c in p}
# print(parent_map)
# for key,elem in parent_map.items:
#     print(key)
#<Element '{http://pds.nasa.gov/pds4/pds/v1}Observation_Area' at 0x12dcde4a0>
# print(parent_map['Observation_Area'])

# printing the text contained within
# first subtag of the 5th tag from
# the parent
# print(root[5][0].text)



# lines =[]
# with open(path, 'r') as f:
#     for line in f:
#         lines.append(line)
# # print((lines))
# counter = 0
# for line in lines:
#     counter += 1
#     if "Refined_Corner_Coordinates" in line:
#         print(counter)



 
# def latitude(lat):
#     if(30<=lat<65):
#         return 1
#     elif(0<=lat<30):
#         return 2

# def longitude(lon, lat_res):
#     if(-180<=lon<-120 and lat_res==1):
#         return 1
#     elif(-120<=lon<-60 and lat_res==1):
#         return 2
#     elif(-60<=lon<0 and lat_res==1):
#         return 3
#     elif(-180<=lon<-135 and lat_res==2):
#         return 7
#     elif(-135<=lon<-90 and lat_res==2):
#         return 8
#     elif(-90<=lon<-45 and lat_res==2):
#         return 9
#     elif(-45<=lon<0 and lat_res==2):
#         return 10

# lat=0
# lon=0
# temp_lat=0
# temp_lon=0
# if(lat<0):
#     temp_lat=8
#     lat=-lat
# if(lon>0):
#     temp_lon=4
#     lon=lon-180
# lat=latitude(lat)
# lon=longitude(lon, lat)
# quadrangle_num=lat+lon+temp_lat+temp_lon





# path = "TMC2/ch2_tmc_ndn_20191224T0436128888_d_oth_d18/browse/derived/20191224/*.xml"
# for xml_file in sorted(glob.glob(path)):
#     print("found")
#     f = pd.read_xml(xml_file)
#     print(f.head())
#     cols = f.columns
#     for col in cols:
#         print(col)
# #     # print(f['Geometry_Parameters'])

 
# # give the path where you saved the xml file
# # inside the quotes
# # xmldata = path
# # prstree = ETree.parse(xmldata)
# # root = prstree.getroot()
  
# # # print(root)
# # store_items = []
# # all_items = []
  
# # for storeno in root.iter('store'):
    
# #     store_Nr = storeno.attrib.get('slNo')
# #     itemsF = storeno.find('foodItem').text
# #     price = storeno.find('price').text
# #     quan = storeno.find('quantity').text
# #     dis = storeno.find('discount').text
  
# #     store_items = [store_Nr, itemsF, price, quan, dis]
# #     all_items.append(store_items)
  
# # xmlToDf = pd.DataFrame(all_items, columns=[
# #   'SL No', 'ITEM_NUMBER', 'PRICE', 'QUANTITY', 'DISCOUNT'])
  
# # print(xmlToDf.to_string(index=False))
