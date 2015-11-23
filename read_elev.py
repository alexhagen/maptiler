# first, lets write a shapefile with our trip plans
from shapely.geometry import Polygon,LineString,mapping
from fiona import collection
import math
import shapefile
mariposa = shapefile.Reader("/home/ahagen/mapdata/Elev_Contour.shp");
elev = shapefile.Writer(shapefile.POLYLINE)
elev.fields = list(mariposa.fields)
for shaperec in mariposa.shapeRecords():
	if shaperec.record[5] == 500.0 * math.floor(shaperec.record[5]/500.) \
		and len(shaperec.shape.points) >= 3:
		print shaperec.record
		geo = Polygon(shaperec.shape.points)
		m = mapping(geo)
		elev.records.append(shaperec.record)
		elev._shapes.append(shaperec.shape)
elev.save("elev.shp")
		