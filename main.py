from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timezone

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
