import pyproj

def hk80toWGS(x_in, y_in):
    inProj = pyproj.Proj("ESRI:102140")  # This is the HK1980 Grid
    outProj = pyproj.Proj("epsg:4326")  # This is WGS 84
    latitude, longitude = pyproj.transform(inProj, outProj, x_in, y_in)
    return f"{latitude}.{longitude}"

# x_in, y_in = 840734, 844917.6
# print(hk80toWGS(x_in, y_in))