#!/home/ahagen/envs/kartograph/bin/python2.7
from kartograph import Kartograph

class mapconfig(object):
	def __init__(self):
		# initialize the configuration string
		self.config = ''
	def add_projection(id='satellite',lon=8.9328,lat=44.41111,dist=1.08,up=-20.0,tilt=-2.0):
		self.config = self.config

K = Kartograph();
css = open('styles.css').read()

# first, lets write a shapefile with our trip plans
from shapely.geometry import Polygon,LineString,mapping
from fiona import collection
schema = { 'geometry': 'LineString', 'properties': { 'id': 'int' } }
with collection(
	'trip.shp','w','ESRI Shapefile', schema) as output:
	import shapefile
	jmt = shapefile.Reader("jmt.shp");
	points = []
	for record in jmt.shapeRecords():
	    points.extend(record.shape.points)
	geo = LineString(points)
	m = mapping(geo)
	print m['type']
	output.write({
		'properties': {
			'id': 123
		},
		'geometry': m
		})

#def cityfilter(record):
#	return record['NAME'] == 'Geneva' or record['NAME'] == 'Rome'

config = {
	"proj": {
		"id": "satellite",
	    "lon0": -119.5587,
	    "lat0": 37.7317,
	    "dist": 1.08,
	    "up": -40.0,
	    "tilt": -4.0
	},
	"layers": {
		"mygraticule": { "special": "graticule", "latitudes": 12, "longitudes": 12, },
		"countries": {
			"src": "/home/ahagen/mapdata/10m_cultural/ne_10m_admin_0_countries.shp",
			"simplify": 0,
		},
		"lakes": {
			"src": "/home/ahagen/mapdata/california_natural.shp",
			"simplify": 1,
		},
		"rivers": {
			"src": "/home/ahagen/mapdata/ne_10m_rivers_north_america.shp",
			"simplify": 0,
		},
		"parks": {
			"src": "/home/ahagen/mapdata/ne_10m_parks_and_protected_lands_area.shp",
			"simplify": 0,
			"labeling": {
				"key": "NAME_1",
			},
		},
		"forests": {
			"src": "/home/ahagen/mapdata/VegetationNorthAmericaPolygons.shp",
			"simplify": 0,
		},
		"state-parks": {
			"src": "/home/ahagen/mapdata/caStateParkBdys2014a.shp",
			"simplify": 0,
		},
		"elevation": {
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_geography_regions_elevation_points.shp",
		},
		"roads": {
			"src": "/home/ahagen/mapdata/10m_cultural/ne_10m_roads_north_america.shp",
		},
		"city": {
			"src": "/home/ahagen/mapdata/10m_cultural/ne_10m_urban_areas.shp",
			"simplify": 0,
		},
		"city2": {
			"src": "/home/ahagen/mapdata/10m_cultural/ne_10m_populated_places.shp",
			"labeling": {
		        "key": "NAME"
		    }
		},
		"trip": {
			"src": "trip.shp",
			"simplify": 0,
		},
	},
	"export": {
		"width": 1200,
	},
	"bounds": {
		"mode": "bbox",
		"data": [-120, 37.5, -117, 37.85],
	}
}

K.generate(config,outfile='/home/ahagen/code/maps/mymap.svg', stylesheet=css);

'''
		"geneva": {
			"src": "/home/ahagen/mapdata/10m_cultural",
			"simplify": 0
		},
		"cinque-terra": {
			"src": "/home/ahagen/mapdata/10m_cultural",
			"simplify": 0
		},
		"gran-paradiso": {
			"src": "/home/ahagen/mapdata/10m_cultural",
			"simplify": 0
		}
				"countries": {
					"src": "/home/ahagen/mapdata/10m_cultural/ne_10m_admin_0_countries.shp",
					"simplify": 0,
				},

'''
