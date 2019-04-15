from app import app
from flask import Response 
import os, json

@app.route('/monitoring/adapters/zabbix/zones/indigo/types/infrastructure/groups/Cloud_Providers/hosts/<provider>')
def index(provider=None):
    print("provider: " + provider)
    with open('config/template-response.json') as stream:
        content=stream.read()
        payload = content.replace("__PROVIDER__", provider)
        return Response(payload, status=200, mimetype='application/json')
