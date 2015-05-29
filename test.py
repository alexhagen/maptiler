#!/home/ahagen/envs/kartograph/bin/python2.7
from kartograph import Kartograph

K = Kartograph();
css = open('styles.css').read()

config = {
	"proj": {
		"id": "satellite",
	    "lon0": 8.9328,
	    "lat0": 44.4111,
	    "dist": 1.08,
	    "up": -20.0,
	    "tilt": -2.0
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
		"bath5": { 
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_bathymetry_all/ne_10m_bathymetry_H_3000.shp",
			"simplify": 0,
		},
		"bath4": { 
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_bathymetry_all/ne_10m_bathymetry_I_2000.shp",
			"simplify": 0,
		},
		"bath3": { 
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_bathymetry_all/ne_10m_bathymetry_J_1000.shp",
			"simplify": 0,
		},
		"bath2": { 
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_bathymetry_all/ne_10m_bathymetry_K_200.shp",
			"simplify": 0,
		},
		"bath1": { 
			"src": "/home/ahagen/mapdata/10m_physical/ne_10m_bathymetry_all/ne_10m_bathymetry_L_0.shp",
			"simplify": 0,
		},
	},
	
	"export": {
		"width": 800,
		"round": 2
	},
		"bounds": {
		"mode": "bbox",
		"data": [5.15, 39.35, 16.1667, 46.2],
		"crop": [2.15, 37.35, 20.1667, 52.2],
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
'''