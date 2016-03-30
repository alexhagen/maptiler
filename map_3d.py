#import matplotlib
#matplotlib.use('svg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PolyCollection
from mpl_toolkits.basemap import Basemap, shiftgrid, cm
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib import cm

# read in etopo5 topography/bathymetry.
url = 'http://ferret.pmel.noaa.gov/thredds/dodsC/data/PMEL/etopo5.nc'
etopodata = Dataset(url)

topoin = etopodata.variables['ROSE'][:]
lons = etopodata.variables['ETOPO05_X'][:]
lats = etopodata.variables['ETOPO05_Y'][:]
# shift data so lons go from -180 to 180 instead of 20 to 380.
topoin,lons = shiftgrid(180.,topoin,lons,start=False)

# plot topography/bathymetry as an image.

# create the figure and axes instances.
# setup of basemap ('lcc' = lambert conformal conic).
# use major and minor sphere radii from WGS84 ellipsoid.
m = Basemap(llcrnrlon=-122,llcrnrlat=34.0,urcrnrlon=-116,urcrnrlat=40.0,\
            resolution='h',projection='lcc',\
            lat_0=38.,lon_0=-100.)
# transform to nx x ny regularly spaced 5km native projection grid
nx = int((m.xmax-m.xmin)/5000.)+1; ny = int((m.ymax-m.ymin)/5000.)+1
topodat,x,y = m.transform_scalar(topoin,lons,lats,nx,ny,returnxy=True)


fig2 = plt.figure(2)
ax2 = Axes3D(fig2)

from scipy.interpolate import *

#interp = interp2d(x,y,topodat)
print len(np.unique(x))
print len(np.unique(y))
print np.array(topodat).shape
interp = RectBivariateSpline(np.unique(x), np.unique(y), topodat.T)
ax2.plot_surface(x, y, topodat, rstride=1, cstride=1,
				 cmap=cm.terrain,linewidth=0, antialiased=True,
				 shade=True, vmin=-1000., vmax=3700.)
ax2.contour(x, y, topodat, 15, extend3d=False, cmap=cm.terrain,  vmin=-1000., vmax=3700.)

import shapefile
jmt = shapefile.Reader("jmt.shp");
points = []
for record in jmt.shapeRecords():
    points.extend(record.shape.points)
x3 = []
y3 = []
z3 = []
for point in points:
	x1, y1 = m(point[0],point[1])
	z1 = interp(x1, y1)
	x3.extend([x1])
	y3.extend([y1])
	z3.extend([z1])
ax2.plot(x3[::5], y3[::5], zs=z3[::5], zdir='z', linewidth=3.0, color='#FC8D82')


ax2.azim=-105
ax2.elev=75
ax2.dist=8

ax2.axis("off")

#plt.show()
plt.savefig('john_muir_trail_3d_map.svg')
