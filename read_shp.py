# first, lets write a shapefile with our trip plans
from shapely.geometry import Polygon,LineString,mapping
from fiona import collection
import math
import shapefile
#shpf = shapefile.Reader("/home/ahagen/mapdata/nps_boundary.shp")
shpf = shapefile.Reader("/home/ahagen/mapdata/50m_cultural/ne_50m_admin_1_states_provinces_shp.shp")
print list(shpf.fields)
#for record in shpf.shapeRecords():
#    print record.record
