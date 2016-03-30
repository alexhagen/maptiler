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
from shapely.geometry import Polygon,LineString,mapping
from fiona import collection
import fiona


# read in etopo5 topography/bathymetry.
url = 'http://ferret.pmel.noaa.gov/thredds/dodsC/data/PMEL/etopo5.nc'
url = '/home/ahagen/mapdata/etopo1.nc'
# url = '/home/ahagen/mapdata/srtm_ne_250m.asc'
etopodata = Dataset(url)


print etopodata.variables
# topoin = etopodata.variables['ROSE'][:]
#lons = etopodata.variables['ETOPO05_X'][:]
#lats = etopodata.variables['ETOPO05_Y'][:]
topoin = etopodata.variables['Band1'][:]
lons = etopodata.variables['lon'][:]
lats = etopodata.variables['lat'][:]

print topoin

# shift data so lons go from -180 to 180 instead of 20 to 380.
#topoin,lons = shiftgrid(-87.27541666666674,topoin,lons,start=False)
#topoin,lats = shiftgrid(39.6654166666667,topoin,lats,start=False)

ttfname = '/home/ahagen/mapdata/TecumsehTrailTrack1.gpx'
tt = fiona.open(ttfname, layer='tracks')
geom = tt[0]
ttx = []
tty = []
for pts in geom['geometry']['coordinates']:
    for arr in pts:
        ttx.append(arr[0])
        tty.append(arr[1])


# plot topography/bathymetry as an image.
fig = plt.figure()
ax = plt.gca()
# create the figure and axes instances.
# setup of basemap ('lcc' = lambert conformal conic).
# use major and minor sphere radii from WGS84 ellipsoid.
dx = max(ttx) - min(ttx)
dy = max(tty) - min(tty)
m = Basemap(llcrnrlon=min(ttx) - 0.25 * dx, llcrnrlat=min(tty) - 0.1 * dy,
            urcrnrlon=max(ttx) + 0.25 * dx, urcrnrlat=max(tty) + 0.1 * dy,
            resolution='i', projection='lcc',
            lat_0=(max(tty) + min(tty))/2.,
            lon_0=(max(ttx)+min(ttx))/2.)
# transform to nx x ny regularly spaced 10 m native projection grid
nx = int((m.xmax-m.xmin)/10.)+1; ny = int((m.ymax-m.ymin)/10.)+1
# topodat,x,y = m.transform_scalar(topoin,lons,lats,nx,ny,returnxy=True)
m.ax = ax
m.drawstates(linewidth=0.1)
m.fillcontinents(color='white', lake_color='#bbbbff')
m.drawcoastlines(linewidth=0.1)
m.drawcounties(linewidth=0.1)
m.drawrivers(linewidth=0.1)
m.bluemarble()
# m.plot(ttx, tty, latlon=True)
# m.readshapefile('/home/ahagen/mapdata/Vegetation', 'vegetation')

# topodat = topodat * 3.28084

# cs = ax.contour(x, y, topodat, np.arange(0,1000,25), cmap=cm.terrain,
#                 vmin=0.0, vmax=3000., linewidth=0.5)
# plt.clabel(cs, fmt='%d')


ax.axis("off")

plt.show()
#plt.savefig('tecumseh_trail_day_1.png')
