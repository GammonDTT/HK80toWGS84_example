import pyproj

inProj = pyproj.Proj("ESRI:102140")  # This is the HK1980 Grid
outProj = pyproj.Proj("epsg:4326")

x_in, y_in = 840734, 844917.6
latitude, longitude = pyproj.transform(inProj, outProj, x_in, y_in)

print(latitude, longitude)