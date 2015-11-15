import shapefile
import numpy as np

jmt = shapefile.Reader("jmt.shp");

print jmt.shapeRecord(1).shape.points # this is a list of lists of the coordinates
points = []
for record in jmt.shapeRecords():
    points.extend(record.shape.points)
print points
print len(points)
