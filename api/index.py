from http.server import BaseHTTPRequestHandler
import importlib
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self._route()

    def do_POST(self):
        self._route()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.end_headers()

    def _route(self):
        clean_path = self.path.split('?')[0].rstrip('/')
        endpoint = clean_path.split('/')[-1] if clean_path else ''

        mapping = {
            'state': 'api.state',
            'approve': 'api.approve',
            'reject': 'api.reject',
            'killswitch': 'api.killswitch',
        }

        if endpoint in mapping:
            try:
                mod = importlib.import_module(mapping[endpoint])
                target = mod.handler
                if self.command == 'GET' and hasattr(target, 'do_GET'):
                    target.do_GET(self)
                elif self.command == 'POST' and hasattr(target, 'do_POST'):
                    target.do_POST(self)
                elif hasattr(target, 'do_GET'):
                    target.do_GET(self)
                else:
                    self.send_response(405)
                    self.end_headers()
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'error': str(e)}).encode())
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'Quant Swarm API Ready'}).encode())