import cv2
import rasterio
from datetime import datetime

# ---------------------------------
# OPEN THE GEOTIFF FILE
# ---------------------------------

dataset = rasterio.open("chennai.tif")

print("Number of bands:", dataset.count)
print("CRS:", dataset.crs)
print("Image size:", dataset.width, "x", dataset.height)

# ---------------------------------
# READ SAR IMAGE (Band 1)
# ---------------------------------

sar_band = dataset.read(1)

# Normalize for visualization
sar_vis = cv2.normalize(sar_band, None, 0, 255, cv2.NORM_MINMAX)
sar_vis = sar_vis.astype('uint8')

# ---------------------------------
# READ TIMESTAMP BAND (Band 2)
# ---------------------------------

timestamp_band = dataset.read(2)

# Since timestamp is constant across image,
# we can read any pixel (top-left pixel)
timestamp_value = timestamp_band[0, 0]

print("\nRaw Timestamp (milliseconds):", timestamp_value)

# Convert to human-readable datetime
timestamp_seconds = timestamp_value / 1000
human_time = datetime.utcfromtimestamp(timestamp_seconds)

print("Human Readable Time (UTC):", human_time)

# ---------------------------------
# EXAMPLE: Get Latitude & Longitude of Pixel
# ---------------------------------

x_pixel = 200
y_pixel = 150

lon, lat = dataset.xy(y_pixel, x_pixel)

print("\nPixel location:")
print("Latitude:", lat)
print("Longitude:", lon)

# ---------------------------------
# OPTIONAL: Display image (if needed)
# ---------------------------------

cv2.imshow("SAR Image", sar_vis)
cv2.waitKey(0)
cv2.destroyAllWindows()
