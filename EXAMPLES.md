# API Usage Examples

This document provides practical examples of using the Project Intelligence API.

## Basic Usage

### Python

```python
import requests
import json

# Base URL
BASE_URL = "http://localhost:8000"

# Generate summary
response = requests.post(
    f"{BASE_URL}/summarize",
    json={"project_id": 123}
)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

### JavaScript/Node.js

```javascript
const axios = require('axios');

const BASE_URL = 'http://localhost:8000';

async function generateSummary(projectId) {
  try {
    const response = await axios.post(`${BASE_URL}/summarize`, {
      project_id: projectId
    });
    
    console.log(JSON.stringify(response.data, null, 2));
    return response.data;
  } catch (error) {
    console.error('Error:', error.response?.data || error.message);
  }
}

// Usage
generateSummary(123);
```

### cURL

```bash
# Generate summary
curl -X POST "http://localhost:8000/summarize" \
  -H "Content-Type: application/json" \
  -d '{"project_id": 123}'

# Get API info
curl http://localhost:8000/
```

## Advanced Examples

### Using with Async/Await (Python)

```python
import asyncio
import httpx

async def get_summary(project_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:8000/summarize",
            json={"project_id": project_id},
            timeout=30.0
        )
        return response.json()

# Usage
summary = asyncio.run(get_summary(123))
print(summary)
```

### Error Handling

```python
import requests

def safe_summarize(project_id):
    try:
        response = requests.post(
            "http://localhost:8000/summarize",
            json={"project_id": project_id},
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.ConnectionError:
        return {"error": "Could not connect to API"}
    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTP error: {e.response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

result = safe_summarize(123)
```

### Batch Processing

```python
import asyncio
import httpx

async def batch_summarize(project_ids: list[int]):
    async with httpx.AsyncClient() as client:
        tasks = [
            client.post(
                "http://localhost:8000/summarize",
                json={"project_id": pid}
            )
            for pid in project_ids
        ]
        responses = await asyncio.gather(*tasks)
        return [r.json() for r in responses]

# Usage
project_ids = [123, 456, 789]
summaries = asyncio.run(batch_summarize(project_ids))
```

## Expected Response Format

```json
{
  "project_id": 123,
  "summary": {
    "project_name": "Project Alpha",
    "executive_summary": "The project is progressing well with key milestones achieved...",
    "activity_log": [
      {
        "date": "2023-10-01",
        "description": "Initial project setup completed",
        "category": "Planning"
      },
      {
        "date": "2023-10-02",
        "description": "Database schema implemented",
        "category": "Development"
      }
    ],
    "pending_action_items": [
      "Complete API documentation",
      "Set up CI/CD pipeline",
      "Conduct code review"
    ]
  }
}
```

## Integration Examples

### Flask Integration

```python
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
INTELLIGENCE_API = "http://localhost:8000"

@app.route('/project/<int:project_id>/summary', methods=['GET'])
def get_project_summary(project_id):
    response = requests.post(
        f"{INTELLIGENCE_API}/summarize",
        json={"project_id": project_id}
    )
    return jsonify(response.json())
```

### Django Integration

```python
# views.py
import requests
from django.http import JsonResponse

def project_summary(request, project_id):
    response = requests.post(
        "http://localhost:8000/summarize",
        json={"project_id": project_id}
    )
    return JsonResponse(response.json())
```

