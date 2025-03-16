from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import pandas as pd
from io import StringIO
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enabling CORS for frontend requests, directly using in frontend code
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def home():
    return {"message":"welcome to trading strategy backtest api"}

@app.post('/upload-csv/')
async def upload_csv(file: UploadFile):
    content = await file.read()
    df = pd.read_csv(StringIO(content.decode()))
    return {"message": "File uploaded successfully", "columns": list(df.columns)}

@app.post('/backtest/')
async def backt_strat(file: UploadFile = File(...)):
    try:
        content = await file.read()
        df = pd.read_csv(StringIO(content.decode()))
        if "Close" not in df.columns:
            return {"error": "CSV file must have a 'Close' column"}
        df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
        df.dropna(subset=["Close"], inplace=True)
        df["SMA_5"] = df["Close"].rolling(window=5, min_periods=1).mean()
        df["Signal"] = (df["Close"] > df["SMA_5"]).astype(int)
        df["Daily Return"] = df["Close"].pct_change() * df["Signal"].shift(1)
        df.fillna(0, inplace=True)
        df.replace([float("inf"), float("-inf")], 0, inplace=True)
        total_return = df["Daily Return"].sum()

        return {"total_return": total_return, "data": df.to_dict(orient="records")}

    except Exception as e:
        return {"error": str(e)}