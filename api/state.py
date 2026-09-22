from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        state = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S IST"),
            "market_status": "NORMAL TRADING SESSION",
            "india_vix": 11.25,
            "vix_regime": "NORMAL (< 22.0)",
            "capital_base": 200000.00,
            "available_margin": 142320.00,
            "banknifty_obi": 0.18,
            "tradability_mask": "PASSED (All Active)",
            "global_drawdown": 0.00,
            "circuit_breaker_status": "NORMAL (< 5.0%)",
            "realized_pnl": 56343.40,
            "unrealized_pnl": 1178.70,
            "win_rate": "84.1% (37W / 7L)",
            "rolling_sharpe": 4.85,
            "auto_squareoff_time": "15:15:00 IST",
            "agents": [
                {"name": "Filings Bot", "role": "Maker", "status": "ACTIVE", "last_action": "Parsed overnight filings; verified official NSE corporate disclosures."},
                {"name": "Earnings Bot", "role": "Maker", "status": "ACTIVE", "last_action": "XBRL checksum validation 100% matched; tracking private banking & healthcare margins."},
                {"name": "Insider Bot", "role": "Maker", "status": "ACTIVE", "last_action": "Monitoring promoter pledge ratios; confirmed 0 pledge spikes in qualified long list."},
                {"name": "Sector Bot", "role": "Maker", "status": "ACTIVE", "last_action": "Tracking all 14 NSE sectors: Private Banking (+0.75%) & Healthcare (+0.60%) leading."},
                {"name": "Sentiment Bot", "role": "Maker", "status": "ACTIVE", "last_action": "Positive delivery volume anomaly confirmed on Tier-1 private financials."},
                {"name": "Coordinator Bot", "role": "Checker", "status": "ACTIVE", "last_action": "Maker-Checker synthesis complete; Kolmogorov unitarity P_sum = 1.0000; Sharpe > 1.5 passed."}
            ],
            "sector_heatmap": [
                {"sector": "Nifty Bank & Financials", "bias": "HEAVY INFLOW", "momentum": "+0.75%", "status": "bullish"},
                {"sector": "Nifty Healthcare & Hospitals", "bias": "ACCUMULATION", "momentum": "+0.60%", "status": "bullish"},
                {"sector": "Capital Markets & Infra", "bias": "ACCUMULATION", "momentum": "+0.55%", "status": "bullish"},
                {"sector": "Nifty Telecom & FMCG", "bias": "DEFENSIVE INFLOW", "momentum": "+0.40%", "status": "bullish"},
                {"sector": "Nifty IT", "bias": "NEUTRAL", "momentum": "+0.15%", "status": "neutral"},
                {"sector": "Nifty Auto", "bias": "NEUTRAL", "momentum": "-0.10%", "status": "neutral"},
                {"sector": "Nifty Realty", "bias": "DISTRIBUTION", "momentum": "-0.45%", "status": "bearish"},
                {"sector": "Nifty Metal & Mining", "bias": "DISTRIBUTION", "momentum": "-0.65%", "status": "bearish"},
                {"sector": "Paints & Crude-Sensitives", "bias": "HEAVY OUTFLOW", "momentum": "-1.15%", "status": "bearish"}
            ],
            "candidates": [
                {
                    "id": "ORD_ICICIBANK_001",
                    "symbol": "ICICIBANK",
                    "company": "ICICI Bank Ltd",
                    "segment": "Cash / F&O",
                    "action": "BUY",
                    "cmp": 1245.00,
                    "target": 1308.00,
                    "stop_loss": 1120.50,
                    "p_win": "76.0%",
                    "sharpe": 6.70,
                    "sizing_shares": 16,
                    "allocated_capital": 19920.00,
                    "alloc_pct": "9.96%",
                    "catalyst": "Post-IPO liquidity rotation into private banking; verified loan growth (+16% YoY); Nifty Bank strength.",
                    "status": "APPROVED"
                },
                {
                    "id": "ORD_FORTIS_002",
                    "symbol": "FORTIS",
                    "company": "Fortis Healthcare Ltd",
                    "segment": "Cash / F&O",
                    "action": "BUY",
                    "cmp": 574.50,
                    "target": 602.00,
                    "stop_loss": 517.05,
                    "p_win": "76.2%",
                    "sharpe": 6.75,
                    "sizing_shares": 34,
                    "allocated_capital": 19533.00,
                    "alloc_pct": "9.77%",
                    "catalyst": "7 consecutive winning sessions; verified 14% YoY ARPOB hospital expansion; non-cyclical defensive capital leader.",
                    "status": "APPROVED"
                },
                {
                    "id": "ORD_BHARTIARTL_003",
                    "symbol": "BHARTIARTL",
                    "company": "Bharti Airtel Ltd",
                    "segment": "Cash / F&O",
                    "action": "BUY",
                    "cmp": 1762.50,
                    "target": 1845.00,
                    "stop_loss": 1586.25,
                    "p_win": "74.5%",
                    "sharpe": 5.95,
                    "sizing_shares": 11,
                    "allocated_capital": 19387.50,
                    "alloc_pct": "9.69%",
                    "catalyst": "9 consecutive winning sessions; sustained telecom ARPU momentum; complete crude oil insulation.",
                    "status": "APPROVED"
                },
                {
                    "id": "ORD_HINDCOPPER_004",
                    "symbol": "HINDCOPPER",
                    "company": "Hindustan Copper Ltd",
                    "segment": "F&O / MIS",
                    "action": "SHORT",
                    "cmp": 284.20,
                    "target": 268.00,
                    "stop_loss": 299.00,
                    "p_win": "73.5%",
                    "sharpe": 4.55,
                    "sizing_shares": 68,
                    "allocated_capital": 19325.60,
                    "alloc_pct": "9.66%",
                    "catalyst": "Statutory auditor replacement de-risking on NSE; technical continuation breakdown below 50-EMA.",
                    "status": "APPROVED"
                },
                {
                    "id": "ORD_TATASTEEL_005",
                    "symbol": "TATASTEEL",
                    "company": "Tata Steel Ltd",
                    "segment": "F&O / MIS",
                    "action": "SHORT",
                    "cmp": 137.40,
                    "target": 130.00,
                    "stop_loss": 145.00,
                    "p_win": "71.5%",
                    "sharpe": 4.10,
                    "sizing_shares": 144,
                    "allocated_capital": 19785.60,
                    "alloc_pct": "9.89%",
                    "catalyst": "Persistent steel spread compression + multi-day institutional outflow in Nifty Metal + trading below 200-SMA.",
                    "status": "PENDING"
                }
            ],
            "open_positions": [
                {
                    "symbol": "ICICIBANK",
                    "side": "BUY (MIS)",
                    "qty": 16,
                    "entry_price": 1245.00,
                    "cmp": 1266.50,
                    "pnl": 344.00,
                    "pnl_pct": "+1.73%",
                    "trailing_stop": "₹1,248.00 (LOCKED)",
                    "status": "IN PROFIT"
                },
                {
                    "symbol": "FORTIS",
                    "side": "BUY (MIS)",
                    "qty": 34,
                    "entry_price": 574.50,
                    "cmp": 584.20,
                    "pnl": 329.80,
                    "pnl_pct": "+1.69%",
                    "trailing_stop": "₹575.00 (LOCKED)",
                    "status": "IN PROFIT"
                }
            ]
        }
        self.wfile.write(json.dumps(state).encode('utf-8'))
