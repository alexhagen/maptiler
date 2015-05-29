#!/home/ahagen/envs/kartograph/bin/python2.7
from kartograph import Kartograph

K = Kartograph();
css = open('styles.css').read()

config = {
	"proj": {
		"id": "satellite",
	    "lon0": -76,
	    "lat0": 34.50435523955831,
	    "dist": 1.1,
	    "up": -32.122944029340516,
	    "tilt": -3.002581776358639
	},
	"layers": {	
		"mygraticule": { "special": "graticule", "latitudes": 3, "longitudes": 3, },	
		"lakes": { 
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_lakes.shp",
			"simplify": 0,
		},
		"rivers": { 
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_rivers_lake_centerlines_scale_rank.shp",
			"simplify": 0,
		},
		"cities": {
			"src": "/home/ahagen/mapdata/10m_cultural/ne_10m_urban_areas.shp",
			"simplify":0,
		},
		"countries": { 
			"src": "/home/ahagen/mapdata/10m_cultural/ne_10m_admin_0_countries.shp",
			"simplify": 0,
		},
		"bath2": { 
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_bathymetry_all/ne_10m_bathymetry_L_0.shp",
			"simplify": 0,
		},
		"bath1": { 
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_bathymetry_all/ne_10m_bathymetry_K_200.shp",
			"simplify": 0,
		},
	},
	
	"export": {
		"width": 800,
		"round": 2
	},
	"bounds": {
		"mode": "bbox",
		"data": [-180., -90., -51.0, 41.9]
	}
}

K.generate(config,outfile='/home/ahagen/code/maps/mymap.svg', stylesheet=css);