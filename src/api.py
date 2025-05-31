import os
import ee
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client
from utils.environmental_fetch import fetch_all_environmental_data, fetch_night_lights_and_daylight
import psycopg2
from datetime import datetime
from utils.functions import calculate_aqi_ispu
import pickle
import json
import numpy as np
from data.coordinates import province_coords
import csv
from src.routes import router 

load_dotenv()
print("start")

try:
    with open("./models/poverty_model.pkl", "rb") as f:
        poverty_model = pickle.load(f)
except Exception as e:
    print("Error loading poverty model:", str(e))
    poverty_model = None

def get_db_connection():
    load_dotenv()
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_ANON_KEY: str = os.getenv("SUPABASE_ANON_KEY")

if not SUPABASE_URL or not SUPABASE_ANON_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_ANON_KEY must be set in the .env file")

def get_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

app = FastAPI()

headers = {'User-Agent': 'Mozilla/5.0'}

def initialize_ee():
    try:    
        ee.Initialize(project='ee-kurniakharisma17')
    except Exception as e:
        print("Error initializing Earth Engine:", str(e))

# initialize_ee()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
print("hai")

class Test(BaseModel):
    id: str | None = None 
    text: str | None = None
    created_at: str | None = None

app.include_router(
    router
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI with Supabase!"}

@app.get("/test", response_model=list[Test])
def read_test_data(supabase: Client = Depends(get_supabase_client)):
    try:
        data, count = supabase.table("test").select("*").execute()
        print(f"Retrieved {count} records from 'test' table")
        if not data or not data[1]:
            return []
        return [Test(**item) for item in data[1]]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Supabase error: {e}")

@app.post("/add-test/", response_model=Test)
def create_item(item: Test, supabase: Client = Depends(get_supabase_client)):
    try:
        data, count = supabase.table("test").insert(item.model_dump(exclude_unset=True)).execute()
        if not data:
            raise HTTPException(status_code=500, detail="Failed to create item in Supabase")
        return Test(**data[1][0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Supabase error: {e}")


@app.get("/get-night-lights-and-daylight")
def get_night_lights_and_daylight():
    geospatial_dict = fetch_night_lights_and_daylight()
    # write it into csv
    with open('geospatial_dict.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['province', 'night_lights', 'daylight'])
        for province, data in geospatial_dict.items():
            writer.writerow([province, data['night_lights'], data['daylight']])
    
    return geospatial_dict


def predict_poverty_index(province, geospatial_data):
    if poverty_model is None:
        return "Model not available"

    if province not in geospatial_data:
        return "Province data not available"

    try:
        data = geospatial_data[province]
        night_lights = data.get("night_lights", 0.0)
        daylight_duration = data.get("daylight", 0.0)

        features = np.array([[night_lights, daylight_duration]])
        predicted_poverty = poverty_model.predict(features)[0]

        return round(predicted_poverty, 2)

    except Exception as e:
        print(f"Error predicting poverty index for {province}: {str(e)}")
        return 0.0
    
@app.get("/populate-environmental-data")
def populate_environmental_data():
    try:
        data_coords = {}
        period = datetime.now().strftime("%Y-%m-%d")
        
        with open('geospatial_dict.json', 'r') as f:
            geospatial_dict = json.load(f)
        
        environmental_data = fetch_all_environmental_data()
        
        for province, datas in environmental_data.items():
            poverty_index = predict_poverty_index(province, geospatial_dict)

            try:
                ndvi = float(datas.get("ndvi", 0))
            except (ValueError, TypeError):
                ndvi = 0.0
                
            try:
                co = float(datas.get("co", 0))
            except (ValueError, TypeError):
                co = 0.0
                
            try:
                so2 = float(datas.get("so2", 0))
            except (ValueError, TypeError):
                so2 = 0.0
                
            try:
                no2 = float(datas.get("no2", 0))
            except (ValueError, TypeError):
                no2 = 0.0
                
            try:
                precipitation = float(datas.get("precipitation", 0))
            except (ValueError, TypeError):
                precipitation = 0.0
                
            try:
                sentinel = float(datas.get("sentinel", 0))
            except (ValueError, TypeError):
                sentinel = 0.0
                
            try:
                o3 = float(datas.get("o3", 0))
            except (ValueError, TypeError):
                o3 = 0.0
                
            try:
                pm25 = float(datas.get("pm25", 0))
            except (ValueError, TypeError):
                pm25 = 0.0
            
            safe_poverty_index = 9.0
            if poverty_index is not None and not isinstance(poverty_index, str):
                try:
                    safe_poverty_index = float(poverty_index)
                except (ValueError, TypeError):
                    pass  
        
            try:
                aqi_values = calculate_aqi_ispu(pm25)
            except Exception:
                aqi_values = 0 
 
 
            isProvince = province.lower() in province_coords
            
            data_coords[province] = {
                "province": province,
                "infrastructure": "Placeholder",
                "renewable_energy": "Placeholder",
                "poverty_index": safe_poverty_index,
                "ndvi": ndvi,
                "precipitation": precipitation,
                "sentinel": sentinel,
                "no2": no2,
                "co": co,
                "so2": so2,
                "o3": o3,
                "pm25": pm25,
                "ai_investment_score": float(0),
                "period": period,
                "level": 'province' if isProvince else 'city',
                "aqi": aqi_values
            }

        conn = get_db_connection()
        cur = conn.cursor()

        data_list = []
        for province, data in data_coords.items():
            data_list.append((
                data["province"],
                data["infrastructure"],
                data["renewable_energy"],
                data["poverty_index"],
                data["ndvi"],
                data["precipitation"],
                data["sentinel"],
                data["no2"],
                data["co"],
                data["so2"],
                data["o3"],
                data["pm25"],
                data["ai_investment_score"],
                data["period"],
                data["level"],
                data["aqi"]
            ))

        # Execute the batch insert function with the list of composite values
        cur.execute("SELECT insert_infrastructure_data_batch(%s::infrastructure_input[])", (data_list,))
        conn.commit()
        
        return {"status": "Success", "data_count": len(data_list)}
        
    except Exception as ex:
        print("Error inserting data into Database:", ex)
        return {"error": "An error occurred while processing the request: " + str(ex)}
    
@app.get("/get-infrastructure/all-province")
def get_all_province_environmental_data(province: str = None):
    query = "SELECT * FROM infrastructure WHERE level = 'province'"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, (province,))    
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()

    result = []
    for row in rows:
        row_dict = {}
        for key, value in zip(columns, row):
            if key != 'period':
                row_dict[key] = value
        result.append(row_dict)

    return result
        
@app.get("/get-infrastructure/provinceCity")
def get_province_environmental_data(provinceName : str = None):
    with open('citiesList.json', 'r') as json_file:
        cityprovince_dict = json.load(json_file)
    if provinceName is None:
        return {"error": "Province name is required"}
    provinceName = provinceName.lower()
    list_cities = set()

    for entry in cityprovince_dict:
        if provinceName in entry:
            list_cities = set(entry[provinceName])
            break

    if not list_cities:
        return {"error": f"No cities found for province: {provinceName}"}

    # Create a list of parameters for the query
    params = list(list_cities)
    placeholders = ','.join(['%s'] * len(params))
    
    query = f"SELECT * FROM infrastructure WHERE province IN ({placeholders})"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()    
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    
    result = []
    for row in rows:
        row_dict = {}
        for key, value in zip(columns, row):
            row_dict[key] = value
        result.append(row_dict)

    return result

@app.get("/get-infrastructure/province")
def get_province_environmental_data(provinceName: str = None):
    query = f"SELECT * FROM infrastructure WHERE province = '{provinceName}'"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    
    result = []
    for row in rows:
        row_dict = {}
        for key, value in zip(columns, row):
            row_dict[key] = value
        result.append(row_dict)

    return result

@app.get("/get-infrastructure/city")
def get_city_environmental_data(provinceName: str = None):
    query = f"SELECT * FROM infrastructure WHERE level = 'city' AND province = '{provinceName}'"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    
    result = []
    for row in rows:
        row_dict = {}
        for key, value in zip(columns, row):
            row_dict[key] = value
        result.append(row_dict)

    return result


@app.get("/get-infrastructure/allKelurahan")
def get_all_kelurahan_environmental_data(kecamatanName: str = None):
    query = f"SELECT * FROM infrastructure WHERE level = 'kelurahan' AND kecamatan = '{kecamatanName}'"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    
    result = []
    for row in rows:
        row_dict = {}
        for key, value in zip(columns, row):
            row_dict[key] = value
        result.append(row_dict)

    return result

@app.get("/get-infrastructure/kecamatan")
def get_kecamatan_kelurahan_data(kecamatanName: str = None):
    with open('kecamatanList.json', 'r') as json_file:
        kecamatan_dict = json.load(json_file)
    
    if kecamatanName is None:
        return {"error": "Kecamatan name is required"}
    
    kecamatanName = kecamatanName.lower()
    list_kelurahan = set()

    for entry in kecamatan_dict:
        if kecamatanName in entry:
            list_kelurahan = set(entry[kecamatanName])
            break

    if not list_kelurahan:
        return {"error": f"No kelurahan found for kecamatan: {kecamatanName}"}

    # Create a list of parameters for the query
    params = list(list_kelurahan)
    placeholders = ','.join(['%s'] * len(params))
    
    query = f"SELECT * FROM infrastructure WHERE province IN ({placeholders}) AND level = 'kelurahan'"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()    
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    
    result = []
    for row in rows:
        row_dict = {}
        for key, value in zip(columns, row):
            row_dict[key] = value
        result.append(row_dict)

    return result


# Need to change this into kelurahan fetch all desa
@app.get("/get-infrastructure/kelurahan")
def get_kelurahan_environmental_data(provinceName: str = None):
    query = f"SELECT * FROM infrastructure WHERE level = 'kelurahan' AND province = '{provinceName}'"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()

    result = []
    for row in rows:
        row_dict = {}
        for key, value in zip(columns, row):
            row_dict[key] = value
        result.append(row_dict)

    return result

@app.delete("/delete-all-infrastructure")
def delete_all_infrastructure():
    query = "DELETE FROM infrastructure"
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        conn.commit()
        deleted_rows = cursor.rowcount
        return {"message": f"Successfully deleted {deleted_rows} rows from infrastructure table"}
    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        conn.close()

@app.post("/save-risk-assessment")
def save_risk_assessment(location: str, diseaseData: dict):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Convert diseaseData to JSON string
        disease_json = json.dumps(diseaseData)
        
        # Update query to set diseases column
        query = """
            UPDATE infrastructure 
            SET diseases = %s::jsonb 
            WHERE province = %s
        """
        
        cur.execute(query, (disease_json, location))
        conn.commit()
        
        if cur.rowcount == 0:
            return {"status": "Warning", "message": f"No record found for location: {location}"}
            
        return {
            "status": "Success", 
            "message": f"Successfully updated risk assessment data for {location}",
            "affected_rows": cur.rowcount
        }
        
    except Exception as ex:
        print("Error saving risk assessment data:", ex)
        return {"error": "An error occurred while saving the data: " + str(ex)}
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()


