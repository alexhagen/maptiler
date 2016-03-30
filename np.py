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

def toprivers(record):
	return record['scalerank'] < 50.

config = {
	"proj": {
		"id": "satellite",
	    "lon0": -100.0,
	    "lat0": 35.0,
	    "dist": 4.0,
	    "up": 0.0,
	    "tilt": -25.0
	},
	"layers": {
		"mygraticule": { "special": "graticule", "latitudes": 12, "longitudes": 12, },
		"oceans": {
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_bathymetry_all/ne_10m_bathymetry_L_0.shp",
			"simplify": 1,
		},
		"countries": {
			"src": "/home/ahagen/mapdata/10m_cultural/ne_10m_admin_0_countries.shp",
			"simplify": 1,
		},
		"states": {
			"src": "/home/ahagen/mapdata/50m_cultural/ne_50m_admin_1_states_provinces_shp.shp",
			"simplify": 1,
			"filter": {
				"admin": "United States of America",
			},
		},
		"city": {
			"src": "/home/ahagen/mapdata/50m_cultural/ne_50m_urban_areas.shp",
			"simplify": 1,
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
			"src": "/home/ahagen/mapdata/nps_boundary.shp",
			"simplify": 1,
			"filter": {
				"UNIT_TYPE": "National Park",
			},
			"labeling": {
				"key": "UNIT_NAME",
			},
		},


	},
	"export": {
		"width": 1920,
	},
	"bounds": {
		"mode": "bbox",
		"data": [-175, 20, -40, 115],
	}
}

K.generate(config,outfile='/home/ahagen/code/maps/np.svg', stylesheet=css)
for key, layer in K.layerCache.iteritems():
	print key
	print layer.id
