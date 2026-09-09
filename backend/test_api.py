import sys
import traceback
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
print('Testing /api/v1/auth/register...')
try:
    response = client.post('/api/v1/auth/register', json={
        'email': 'direct_test@example.com',
        'password': 'Test@1234',
        'full_name': 'Direct Test'
    })
    print(f'Status Code: {response.status_code}')
    print(f'Response: {response.text}')
except Exception as e:
    print('Exception occurred:')
    traceback.print_exc()
