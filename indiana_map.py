import matplotlib
matplotlib.use('svg')
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
fig = plt.figure()
ax = plt.gca()
# create the figure and axes instances.
# setup of basemap ('lcc' = lambert conformal conic).
# use major and minor sphere radii from WGS84 ellipsoid.
m = Basemap(llcrnrlon=-88.1,llcrnrlat=37.8,urcrnrlon=-84,urcrnrlat=42.0,\
            resolution='h',projection='lcc',\
            lat_0=39.7910,lon_0=-86.1480)
# transform to nx x ny regularly spaced 5km native projection grid
nx = int((m.xmax-m.xmin)/5000.)+1; ny = int((m.ymax-m.ymin)/5000.)+1
topodat,x,y = m.transform_scalar(topoin,lons,lats,nx,ny,returnxy=True)
# lafayette
plt.plot(*m(-86.8786,40.4172), marker='d')
# prophetstown
plt.plot(*m(-86.83,40.5),marker='o')
# turkey run
plt.plot(*m(-87.2033, 39.8850), marker='>')
# dunes
plt.plot(*m(-87.0400, 41.6600), marker='^')
# radius circles
ts = np.linspace(0, 2. * np.pi, 1000.)
little_circle_x = []
little_circle_y = []
big_circle_x = []
big_circle_y = []
x1,y1 = m(-86.8786,40.4172)
for t in ts:
    little_circle_x.append(x1 + 80000.*np.cos(t))
    little_circle_y.append(y1 + 80000.*np.sin(t))
    big_circle_x.append(x1 + 160000.*np.cos(t))
    big_circle_y.append(y1 + 160000.*np.sin(t))
plt.plot(little_circle_x, little_circle_y, 'k-')
plt.plot(big_circle_x, big_circle_y, 'k-')

m.ax = ax
m.drawstates(linewidth=0.1)
m.fillcontinents(color='white', lake_color='#bbbbff')
m.drawcoastlines(linewidth=0.1)
#m.drawcounties(linewidth=0.1)


ax.contour(x, y, topodat, 15, cmap=cm.terrain,  vmin=-800.0, vmax=2000.,
           linewidth=0.3)


ax.axis("off")

#plt.show()
plt.savefig('indiana_map.png')
