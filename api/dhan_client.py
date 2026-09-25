import os
import time
import json
import base64
import hmac
import hashlib
import struct
import urllib.request
import urllib.error
from datetime import datetime, timedelta

DHAN_CLIENT_ID = os.environ.get('DHAN_CLIENT_ID') or os.environ.get('DHAN CLIENT ID') or ''
DHAN_PIN = os.environ.get('DHAN_PIN') or os.environ.get('DHAN PIN') or ''
DHAN_TOTP_SECRET = os.environ.get('DHAN_TOTP_SECRET') or os.environ.get('DHAN TOTP SECRET') or ''

_cached_token = None
_token_expiry = 0

def get_totp(secret):
    clean_secret = secret.strip().replace(' ', '').upper()
    key = base64.b32decode(clean_secret, True)
    counter = int(time.time() // 30)
    msg = struct.pack('>Q', counter)
    digest = hmac.new(key, msg, hashlib.sha1).digest()
    offset = digest[-1] & 0xF
    code = struct.unpack('>I', digest[offset:offset + 4])[0] & 0x7FFFFFFF
    return str(code % 1000000).zfill(6)

def get_access_token():
    global _cached_token, _token_expiry
    if _cached_token and time.time() < _token_expiry:
        return _cached_token

    if not DHAN_CLIENT_ID or not DHAN_PIN or not DHAN_TOTP_SECRET:
        return None

    totp_code = get_totp(DHAN_TOTP_SECRET)
    url = f'https://auth.dhan.co/app/generateAccessToken?dhanClientId={DHAN_CLIENT_ID}&pin={DHAN_PIN}&totp={totp_code}'
    req = urllib.request.Request(url, method='POST')

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            _cached_token = data.get('accessToken')
            _token_expiry = time.time() + (23 * 3600)
            return _cached_token
    except Exception as e:
        print(f'Dhan auto-login error: {e}')
        return None

def dhan_api_request(endpoint, method='GET', body=None):
    token = get_access_token()
    if not token:
        return {'error': 'Missing credentials or auth failed'}

    clean_ep = endpoint.lstrip('/')
    url = f'https://api.dhan.co/v2/{clean_ep}'
    headers = {
        'access-token': token,
        'dhanClientId': DHAN_CLIENT_ID,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    data_bytes = json.dumps(body).encode('utf-8') if body else None
    req = urllib.request.Request(url, data=data_bytes, headers=headers, method=method)

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        return {'error': f'HTTP {e.code}: {e.read().decode("utf-8")}'}
    except Exception as e:
        return {'error': str(e)}

def get_historical_trades(days=30):
    to_date = datetime.now().strftime('%Y-%m-%d')
    from_date = (datetime.now() - timedelta(days=days)).strftime('%Y-%m-%d')
    res = dhan_api_request(f'trades/{from_date}/{to_date}/0')
    return res if isinstance(res, list) else []