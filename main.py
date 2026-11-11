from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timezone
import yfinance as yf

app = FastAPI(
    title="TRINITY AI",
    description="Multi-Agent Trading Intelligence Platform",
    version="1.0.0"
)

# Frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalysisRequest(BaseModel):
    market: str
    symbol: str
    trading_style: str
    timeframe: str


@app.get("/")
def home():
    return {
        "project": "TRINITY AI",
        "status": "online",
        "version": "1.0.0",
        "message": "Three Minds. One Market. One Verdict."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.post("/api/analyze")
def analyze(request: AnalysisRequest):

    if not request.symbol.strip():
        raise HTTPException(
            status_code=400,
            detail="Symbol cannot be empty"
        )

    return {
        "project": "TRINITY AI",
        "symbol": request.symbol.upper(),
        "market": request.market,
        "trading_style": request.trading_style,
        "timeframe": request.timeframe,
        "status": "awaiting_market_data",
        "agents": {
            "bull": "WAITING",
            "bear": "WAITING",
            "god": "WAITING",
            "reality": "WAITING"
        },
        "verdict": "NO DATA",
        "message": (
            "Verified market data and AI providers "
            "must be connected before analysis."
        )
    }


@app.get("/api/agents")
def agents():
    return {
        "agents": [
            "BULL AI",
            "BEAR AI",
            "GOD AI",
            "REALITY AI",
            "RISK AI",
            "MEMORY AI",
            "PERFORMANCE AI"
        ],
        "status": "initialized"
  }
@app.get("/api/market-data/{symbol}")
def market_data(symbol: str):

    try:
        ticker_symbol = symbol.upper()

        if not ticker_symbol.endswith(".NS"):
            ticker_symbol += ".NS"

        stock = yf.Ticker(ticker_symbol)

        data = stock.history(
            period="5d",
            interval="5m"
        )

        if data.empty:
            raise HTTPException(
                status_code=404,
                detail="Market data unavailable"
            )

        candles = []

        for timestamp, row in data.tail(20).iterrows():
            candles.append({
                "time": timestamp.isoformat(),
                "open": float(row["Open"]),
"high": float(row["High"]),
"low": float(row["Low"]),
"close": float(row["Close"]),
"volume": int(row["Volume"])
            })

        return {
            "symbol": ticker_symbol,
            "status": "success",
            "source": "Yahoo Finance",
            "candles": candles
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
                )
