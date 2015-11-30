#!/home/ahagen/envs/kartograph/bin/python2.7
from kartograph import Kartograph
import os
import numpy as np
from shapely.geometry import Polygon,LineString,mapping
from fiona import collection
import fiona

class mapconfig(object):
	def __init__(self):
		# initialize the configuration string
		self.config = ''
	def add_projection(id='satellite',lon=8.9328,lat=44.41111,dist=1.08,up=-20.0,tilt=-2.0):
		self.config = self.config

K = Kartograph();
css = open('styles.css').read()

schema = { 'geometry': 'LineString', 'properties': { 'name': 'str' } }
'''
# first, lets write a shapefile with the john muir trail
with collection(
	'jmt_trip.shp','w','ESRI Shapefile', schema) as output:
	import shapefile
	jmt = shapefile.Reader("jmt.shp");
	points = []
	for record in jmt.shapeRecords():
	    points.extend(record.shape.points)
	geo = LineString(points)
	m = mapping(geo)
	output.write({
		'properties': {
			'name': 'john_muir_trail'
		},
		'geometry': m
		})

# then, lets write a shapefile with the bruce trail

points = []
nums = os.listdir('/home/ahagen/mapdata/bruce_trail_number')
nums = sorted(nums)
for num in nums:
	btfname = '/home/ahagen/mapdata/bruce_trail_number/' + num + '/BTmap' + num + '.gpx'
	bt = fiona.open(btfname, layer='tracks')
	geom = bt[0]
	for pts in geom['geometry']['coordinates']:
		points.extend(pts)
with collection(
	'bt_trip.shp','w','ESRI Shapefile', schema) as output:
	geo = LineString(points)
	m = mapping(geo)
	output.write({
		'properties': {
			'name': 'bruce_trail'
		},
		'geometry': m
		})

points = []
ltfname = '/home/ahagen/mapdata/long_trail.gpx'
lt = fiona.open(ltfname, layer='tracks')
geom = lt[0]
for pts in geom['geometry']['coordinates']:
	points.extend(pts)
with collection(
	'lt_trip.shp','w','ESRI Shapefile', schema) as output:
	geo = LineString(points)
	m = mapping(geo)
	output.write({
		'properties': {
			'name': 'long_trail'
		},
		'geometry': m
		})

points = []
ctfname = '/home/ahagen/mapdata/CTR2014b_1x9K.gpx'
ct = fiona.open(ctfname, layer='tracks')
geom = ct[0]
for pts in geom['geometry']['coordinates']:
	points.extend(pts)
with collection(
	'ct_trip.shp','w','ESRI Shapefile', schema) as output:
	geo = LineString(points)
	m = mapping(geo)
	output.write({
		'properties': {
			'name': 'colorado_trail'
		},
		'geometry': m
		})

points = []
iatfname = '/home/ahagen/mapdata/ice_age_trail.gpx'
iat = fiona.open(iatfname, layer='tracks')
geom = iat[0]
for pts in geom['geometry']['coordinates']:
	points.extend(pts)
with collection(
	'iat_trip.shp','w','ESRI Shapefile', schema) as output:
	geo = LineString(points)
	m = mapping(geo)
	output.write({
		'properties': {
			'name': 'ice_age_trail'
		},
		'geometry': m
		})

points = []
ntfname = '/home/ahagen/mapdata/natchez_trace.gpx'
nt = fiona.open(ntfname, layer='routes')
for geom in nt:
	for pts in geom['geometry']['coordinates']:
		points.append(pts)
with collection(
	'nt_trip.shp','w','ESRI Shapefile', schema) as output:
	geo = LineString(points)
	m = mapping(geo)
	output.write({
		'properties': {
			'name': 'natchez_trace'
		},
		'geometry': m
		})

points = []
stfname = '/home/ahagen/mapdata/sheltowee_trace.gpx'
st = fiona.open(stfname, layer='tracks')
geom = st[0]
for pts in geom['geometry']['coordinates']:
	points.extend(pts)
with collection(
	'st_trip.shp','w','ESRI Shapefile', schema) as output:
	geo = LineString(points)
	m = mapping(geo)
	output.write({
		'properties': {
			'name': 'sheltowee_trace'
		},
		'geometry': m
		})
'''

def toprivers(record):
	return record['scalerank'] < 50.

config = {
	"proj": {
		"id": "satellite",
	    "lon0": -97.0,
	    "lat0": 25.0,
	    "dist": 1.5,
	    "up": 0.0,
	    "tilt": -25.0
	},
	"layers": {
		"mygraticule": { "special": "graticule", "latitudes": 12, "longitudes": 12, },
		"background": {
			"special": "sea",
		},
		"trip": {
			"src": "jmt_trip.shp",
			"simplify": 0,
		},
		"trip2": {
			"src": "bt_trip.shp",
			"simplify": 0,
		},
		"trip3": {
			"src": "lt_trip.shp",
			"simplify": 0,
		},
		"trip4": {
			"src": "ct_trip.shp",
			"simplify": 0,
		},
		"trip5": {
			"src": "iat_trip.shp",
			"simplify": 0,
		},
		"trip7": {
			"src": "st_trip.shp",
			"simplify": 0,
		},
		"lakes": {
			"src": "/home/ahagen/mapdata/50m_physical/ne_50m_lakes.shp",
			"simplify": 1,
		},
		"rivers": {
			"src": "/home/ahagen/mapdata/ne_10m_rivers_lake_centerlines_scale_rank.shp",
			"simplify": 1,
			"filter": toprivers,
		},
		"parks": {
			"src": "/home/ahagen/mapdata/ne_10m_parks_and_protected_lands_area.shp",
			"simplify": 1,
		},
		"city": {
			"src": "/home/ahagen/mapdata/50m_cultural/ne_50m_urban_areas.shp",
			"simplify": 1,
		},
		"states": {
			"src": "/home/ahagen/mapdata/50m_cultural/ne_50m_admin_1_states_provinces_shp.shp",
			"simplify": 1,
		},
		"oceans": {
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_ocean.shp",
			"simplify": 0,
		},
		"countries": {
			"src": "/home/ahagen/mapdata/10m_cultural/ne_10m_admin_0_countries.shp",
			"simplify": 1,
		},
		
	},
	"export": {
		"width": 1920,
	},
	"bounds": {
		"mode": "bbox",
		"data": [-170, 25, -40, 90],
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
		"elevation": {
			"src": "elev.shp",
			"simplify": 0,
		},

'''
