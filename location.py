import cv2
import rasterio
from rasterio.transform import xy

# Open GeoTIFF with rasterio
dataset = rasterio.open("chennai.tif")

# Read image for OpenCV
image = dataset.read(1)  # first band
image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
image = image.astype('uint8')

# Example detected bounding box center
x_pixel = 200
y_pixel = 150

# Convert pixel to geographic coordinates
lon, lat = dataset.xy(y_pixel, x_pixel)

print("Latitude:", lat)
print("Longitude:", lon)

# Get timestamp
print("Timestamp:", dataset.tags().get("TIFFTAG_DATETIME"))
