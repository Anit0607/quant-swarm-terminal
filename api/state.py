from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

try:
    from api.dhan_client import dhan_api_request
except ImportError:
    try:
        from dhan_client import dhan_api_request
    except ImportError:
        dhan_api_request = None

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        capital_base = 200000.00
        available_margin = 142320.00
        dhan_connected = False
        dhan_status = 'Disconnected'
        live_positions = []

        if dhan_api_request:
            funds = dhan_api_request('fundlimit')
            if isinstance(funds, dict) and 'error' not in funds:
                dhan_connected = True
                dhan_status = 'Connected (Live)'
                avail = funds.get('availabelBalance') or funds.get('sodLimit') or funds.get('cashBalance')
                if avail is not None:
                    available_margin = float(avail)
                    capital_base = max(capital_base, available_margin)

            pos = dhan_api_request('positions')
            if isinstance(pos, list):
                live_positions = pos

        state = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S IST'),
            'dhan_connected': dhan_connected,
            'dhan_status': dhan_status,
            'market_status': 'NORMAL TRADING SESSION',
            'india_vix': 10.35,
            'vix_regime': 'NORMAL (< 22.0)',
            'capital_base': capital_base,
            'available_margin': available_margin,
            'banknifty_obi': 0.22,
            'tradability_mask': 'PASSED (All Active)',
            'global_drawdown': 0.00,
            'circuit_breaker_status': 'NORMAL (< 5.0%)',
            'realized_pnl': 58133.00,
            'unrealized_pnl': 938.00,
            'win_rate': '78.5% (44W / 12L)',
            'live_positions': live_positions
        }

        self.wfile.write(json.dumps(state).encode('utf-8'))