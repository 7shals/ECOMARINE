import numpy as np
import rasterio
from rasterio.transform import from_origin

# Create image
width, height = 300, 300
image = np.zeros((height, width), dtype=np.uint8)

# Simulated ship (bright rectangle)
image[140:155, 150:180] = 255

# Define geographic transform
# Top-left corner: lon=80°, lat=15°
# Pixel size: 0.001 degrees
transform = from_origin(80.0, 15.0, 0.001, 0.001)

with rasterio.open(
    "working_geotiff.tif",
    "w",
    driver="GTiff",
    height=height,
    width=width,
    count=1,
    dtype=image.dtype,
    crs="EPSG:4326",
    transform=transform,
) as dst:
    dst.write(image, 1)

print("GeoTIFF created successfully!")
