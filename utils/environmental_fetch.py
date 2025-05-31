import ee
from datetime import datetime, timedelta
import json
from data.coordinates import province_coords
from data.AllCoordinates import allCoordinates
from data.kota_coords import district_coords, duri_kepa_coords

def fetch_province_environmental_data():
    features = []

    for province, (lat, lon) in province_coords.items():
        point = ee.Geometry.Point(lon, lat)
        feature = ee.Feature(point, {"province": province})
        features.append(feature)

    feature_collection = ee.FeatureCollection(features)

    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=150)).strftime('%Y-%m-%d')

    # Preload all necessary image collections
    ndvi = ee.ImageCollection("MODIS/061/MOD13Q1") \
        .filterDate(start_date, end_date).select("NDVI").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    precipitation = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY") \
        .filterDate(start_date, end_date).mean()
    
    soil_moisture = ee.ImageCollection("COPERNICUS/S1_GRD") \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')) \
        .select("VV") \
        .mean()

    no2 = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_NO2") \
        .filterDate(start_date, end_date).select("NO2_column_number_density").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    co = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_CO") \
        .filterDate(start_date, end_date).select("CO_column_number_density").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    so2 = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_SO2") \
        .filterDate(start_date, end_date).select("SO2_column_number_density").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    pm25 = ee.ImageCollection("NASA/GEOS-CF/v1/rpl/htf") \
        .filterDate(start_date, end_date) \
        .select("PM25_RH35_GCC") \
        .map(lambda img: img.updateMask(img.gt(0))) \
        .mean()
    
    # O3 Collection from Sentinel-5P
    o3 = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_O3") \
        .filterDate(start_date, end_date) \
        .select("O3_column_number_density") \
        .map(lambda img: img.updateMask(img.gt(0))) \
        .mean()

    def compute_stats(feature):
        geom = feature.geometry()
        buffer_radius = 10000  # 10km buffer for province level
        
        return feature.set({
            "ndvi": ndvi.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 250).get("NDVI"),
            "precipitation": precipitation.reduceRegion(ee.Reducer.mean(), geom, 500).get("precipitation"),
            "sentinel": soil_moisture.reduceRegion(ee.Reducer.mean(), geom, 500).get("VV"),
            "no2": no2.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("NO2_column_number_density"),
            "co": co.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("CO_column_number_density"),
            "so2": so2.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("SO2_column_number_density"),
            "pm25": pm25.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("PM25_RH35_GCC"),
            "o3": o3.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("O3_column_number_density"),
        })

    enriched = feature_collection.map(compute_stats)
    enriched_data = enriched.getInfo()

    result = {}
    for feature in enriched_data['features']:
        props = feature['properties']
        result[props['province']] = {
            "ndvi": round((props.get("ndvi", 0) or 0) * 0.0001, 2),
            "precipitation": round(props.get("precipitation", 0) or 0, 1),
            "sentinel": round(props.get("sentinel", 0) or 0, 3),
            "no2": round((props.get("no2", 0) or 0) * 1000000, 3),
            "co": round((props.get("co", 0) or 0) * 1000, 3),
            "so2": round((props.get("so2", 0) or 0) * 1000000, 3),
            "o3": round((props.get("o3", 0) or 0), 3),
            "aod": 0,
            "pm25": round(props.get("pm25", 0), 1)
        }

    return result

def fetch_district_environmental_data():
    
    features = []

    for district, (lat, lon) in district_coords.items():
        point = ee.Geometry.Point(lon, lat)
        feature = ee.Feature(point, {"province": district})
        features.append(feature)

    feature_collection = ee.FeatureCollection(features)

    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=150)).strftime('%Y-%m-%d')

    # Preload all necessary image collections
    ndvi = ee.ImageCollection("MODIS/061/MOD13Q1") \
        .filterDate(start_date, end_date).select("NDVI").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    precipitation = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY") \
        .filterDate(start_date, end_date).mean()
    
    soil_moisture = ee.ImageCollection("COPERNICUS/S1_GRD") \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')) \
        .select("VV") \
        .mean()

    no2 = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_NO2") \
        .filterDate(start_date, end_date).select("NO2_column_number_density").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    co = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_CO") \
        .filterDate(start_date, end_date).select("CO_column_number_density").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    so2 = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_SO2") \
        .filterDate(start_date, end_date).select("SO2_column_number_density").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    pm25 = ee.ImageCollection("NASA/GEOS-CF/v1/rpl/htf") \
        .filterDate(start_date, end_date) \
        .select("PM25_RH35_GCC") \
        .map(lambda img: img.updateMask(img.gt(0))) \
        .mean()
    
    # O3 Collection from Sentinel-5P
    o3 = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_O3") \
        .filterDate(start_date, end_date) \
        .select("O3_column_number_density") \
        .map(lambda img: img.updateMask(img.gt(0))) \
        .mean()

    def compute_stats(feature):
        geom = feature.geometry()
        buffer_radius = 5000  # 5km buffer for district level (smaller than province)
        
        return feature.set({
            "ndvi": ndvi.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 250).get("NDVI"),
            "precipitation": precipitation.reduceRegion(ee.Reducer.mean(), geom, 500).get("precipitation"),
            "sentinel": soil_moisture.reduceRegion(ee.Reducer.mean(), geom, 500).get("VV"),
            "no2": no2.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("NO2_column_number_density"),
            "co": co.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("CO_column_number_density"),
            "so2": so2.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("SO2_column_number_density"),
            "pm25": pm25.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("PM25_RH35_GCC"),
            "o3": o3.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("O3_column_number_density"),
        })

    enriched = feature_collection.map(compute_stats)
    enriched_data = enriched.getInfo()

    result = {}
    for feature in enriched_data['features']:
        props = feature['properties']
        result[props['province']] = {
            "ndvi": round((props.get("ndvi", 0) or 0) * 0.0001, 2),
            "precipitation": round(props.get("precipitation", 0) or 0, 1),
            "sentinel": round(props.get("sentinel", 0) or 0, 3),
            "no2": round((props.get("no2", 0) or 0) * 1000000, 3),
            "co": round((props.get("co", 0) or 0) * 1000, 3),
            "so2": round((props.get("so2", 0) or 0) * 1000000, 3),
            "o3": round((props.get("o3", 0) or 0), 3),
            "aod": 0,
            "pm25": round(props.get("pm25", 0), 1)
        }

    return result

def fetch_kelurahan_environmental_data():
    
    features = []

    for district, (lon, lat) in duri_kepa_coords.items():  # Note: coordinates are in (lon, lat) format
        point = ee.Geometry.Point(lon, lat)
        feature = ee.Feature(point, {"province": district})
        features.append(feature)

    feature_collection = ee.FeatureCollection(features)

    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=150)).strftime('%Y-%m-%d')

    # Preload all necessary image collections
    ndvi = ee.ImageCollection("MODIS/061/MOD13Q1") \
        .filterDate(start_date, end_date).select("NDVI").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    precipitation = ee.ImageCollection("UCSB-CHG/CHIRPS/DAILY") \
        .filterDate(start_date, end_date).mean()
    
    soil_moisture = ee.ImageCollection("COPERNICUS/S1_GRD") \
        .filterDate(start_date, end_date) \
        .filter(ee.Filter.listContains('transmitterReceiverPolarisation', 'VV')) \
        .select("VV") \
        .mean()

    no2 = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_NO2") \
        .filterDate(start_date, end_date).select("NO2_column_number_density").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    co = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_CO") \
        .filterDate(start_date, end_date).select("CO_column_number_density").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    so2 = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_SO2") \
        .filterDate(start_date, end_date).select("SO2_column_number_density").map(lambda img: img.updateMask(img.gt(0))).mean()
    
    pm25 = ee.ImageCollection("NASA/GEOS-CF/v1/rpl/htf") \
        .filterDate(start_date, end_date) \
        .select("PM25_RH35_GCC") \
        .map(lambda img: img.updateMask(img.gt(0))) \
        .mean()
    
    # O3 Collection from Sentinel-5P
    o3 = ee.ImageCollection("COPERNICUS/S5P/NRTI/L3_O3") \
        .filterDate(start_date, end_date) \
        .select("O3_column_number_density") \
        .map(lambda img: img.updateMask(img.gt(0))) \
        .mean()

    def compute_stats(feature):
        geom = feature.geometry()
        buffer_radius = 1000  # 1km buffer for kelurahan level
        
        return feature.set({
            "ndvi": ndvi.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 250).get("NDVI"),
            "precipitation": precipitation.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 500).get("precipitation"),
            "sentinel": soil_moisture.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 500).get("VV"),
            "no2": no2.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("NO2_column_number_density"),
            "co": co.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("CO_column_number_density"),
            "so2": so2.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("SO2_column_number_density"),
            "pm25": pm25.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("PM25_RH35_GCC"),
            "o3": o3.reduceRegion(ee.Reducer.mean(), geom.buffer(buffer_radius), 1000).get("O3_column_number_density"),
        })
    
    enriched = feature_collection.map(compute_stats)
    enriched_data = enriched.getInfo()

    result = {}
    for feature in enriched_data['features']:
        props = feature['properties']
        result[props['province']] = {
            "ndvi": round((props.get("ndvi", 0) or 0) * 0.0001, 2),
            "precipitation": round(props.get("precipitation", 0) or 0, 1),
            "sentinel": round(props.get("sentinel", 0) or 0, 3),
            "no2": round((props.get("no2", 0) or 0) * 1000000, 3),
            "co": round((props.get("co", 0) or 0) * 1000, 3),
            "so2": round((props.get("so2", 0) or 0) * 1000000, 3),
            "o3": round((props.get("o3", 0) or 0), 3),
            "aod": 0,
            "pm25": round(props.get("pm25", 0), 1)
        }

    return result


def fetch_night_lights_and_daylight():
    end_date = ee.Date("2024-01-01")
    start_date = end_date.advance(-60, "day")

    # Fetch and cache the averaged images
    viirs_image = ee.ImageCollection("NOAA/VIIRS/DNB/MONTHLY_V1/VCMSLCFG")\
        .filterDate(start_date, end_date)\
        .select("avg_rad")\
        .mean()

    solar_image = ee.ImageCollection("ECMWF/ERA5_LAND/HOURLY")\
        .filterDate(start_date, end_date)\
        .select("surface_solar_radiation_downwards")\
        .filter(ee.Filter.calendarRange(6, 18, 'hour'))\
        .sum()

    results = {}

    for province, (lat, lon) in allCoordinates.items():
        try:
            point = ee.Geometry.Point(lon, lat).buffer(5000)
            buffered_point = point.buffer(1000)

            night_lights_result = viirs_image.reduceRegion(
                reducer=ee.Reducer.mean(),
                geometry=buffered_point,
                scale=500,
                bestEffort=True
            ).getInfo()

            solar_result = solar_image.reduceRegion(
                reducer=ee.Reducer.mean(),
                geometry=buffered_point,
                scale=1000,
                bestEffort=True
            ).getInfo()

            night_lights = night_lights_result.get("avg_rad", 0.0) or 0.0
            daylight = solar_result.get("surface_solar_radiation_downwards", 0.0) or 0.0

            results[province] = {
                "night_lights": float(night_lights),
                "daylight": float(daylight)
            }

        except Exception as e:
            print(f"Error fetching data for {province}: {str(e)}")
            results[province] = {
                "night_lights": 0.0,
                "daylight": 0.0
            }

    return results

def fetch_all_environmental_data():
    # province_data = fetch_province_environmental_data()
    # district_data = fetch_district_environmental_data()
    kelurahan_data = fetch_kelurahan_environmental_data()

    # combined_data = {**province_data, **district_data}
    
    
    # unique_data = {k: combined_data[k] for k in set(combined_data.keys())}

    return kelurahan_data
    # return unique_data
