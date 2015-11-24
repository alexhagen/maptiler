# first, lets write a shapefile with our trip plans
from shapely.geometry import Polygon,LineString,mapping
from fiona import collection
import math
import shapefile
shpf = shapefile.Reader("/home/ahagen/mapdata/" + 'death_valley_topo' +
						"/Shape/Elev_Contour.shp");
elev = shapefile.Writer(shapefile.POLYLINE)
elev.fields = list(shpf.fields)
['death_valley_topo', 'fresno_e_topo', 'fresno_w_topo',
				 'goldfield_w_topo', 'mariposa_e_topo', 'mariposa_w_topo',
				 'tonopah_w_topo', 'walker_lake_e_topo', 'walker_lake_w_topo']
for filename in ['death_valley_topo', 'mariposa_e_topo', 'walker_lake_w_topo']:
	print filename
	shpf = shapefile.Reader("/home/ahagen/mapdata/" + filename +
							"/Shape/Elev_Contour.shp");
	i = 0
	for shaperec in shpf.shapeRecords():
		if shaperec.record[5] == 500.0 * math.floor(shaperec.record[5]/500.) \
			and len(shaperec.shape.points) >= 3:
			i = i + 1
			if shaperec.record in elev.records:
				elev._shapes.extend(shaperec.shape)
			else:
				elev.records.append(shaperec.record)
				elev._shapes.append(shaperec.shape)
	print i
elev.save("elev.shp")