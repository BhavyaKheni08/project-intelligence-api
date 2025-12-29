import httpx
import asyncio
import json

BASE_URL = "http://54.87.212.225:3001/api/v1/real_time/dashboard/close_loop_analytics"


def fetch_dashboard_context():
    # MOCK DATA MODE
    return {
        # --- POSITIVE DATA (Provided by User) ---
        "Analytics (Positive)": {
            "total_responses": 85,
            "acted_on": 5,
            "resolved_positively": 4,
            "not_resolved_positively": 1,
            "too_late_to_act": 0
        },
        "Top Action Takers (Positive)": [
            {
                "id": "2",
                "imgUrl": "/rails/active_storage/...",
                "name": "Guest User",
                "email": "guest@test.org",
                "acted_on": 5
            }
        ],
        "Top Reasons (Positive)": [
            {"reason": "Other", "acted_on": 5, "id": "1"}
        ],

        # --- NEGATIVE (Empty Placeholders) ---
        "Analytics (Negative)": {"total_responses": 0, "acted_on": 0},
        "Top Action Takers (Negative)": [],
        "Top Reasons (Negative)": [],

        # --- NEUTRAL (Empty Placeholders) ---
        "Analytics (Neutral)": {"total_responses": 0, "acted_on": 0},
        "Top Action Takers (Neutral)": [],
        "Top Reasons (Neutral)": []
    }

# async def fetch_dashboard_context() -> str:
#     """
#     Fetches Close Loop Analytics dashboard data from external API.
#     Aggregates data across 'positive', 'negative', 'neutral' sentiments for:
#     - /analytics
#     - /top_reasons
#     - /top_action_taker
#     """
#     
#     sentiments = ["positive", "negative", "neutral"]
#     endpoints = {
#         "Analytics": "analytics",
#         "Top Reasons": "top_reasons",
#         "Top Action Takers": "top_action_taker"
#     }
#     
#     dashboard_data = {}
# 
#     async with httpx.AsyncClient(timeout=10.0) as client:
#         tasks = []
#         labels = []
#         
#         for sentiment in sentiments:
#             for category, endpoint in endpoints.items():
#                 url = f"{BASE_URL}/{endpoint}"
#                 params = {"response_type": sentiment}
#                 
#                 # We save label to map result back later
#                 label = f"{category} ({sentiment.capitalize()})"
#                 labels.append(label)
#                 
#                 tasks.append(client.get(url, params=params))
#         
#         # Run all requests in parallel
#         responses = await asyncio.gather(*tasks, return_exceptions=True)
#         
#         for i, response in enumerate(responses):
#             label = labels[i]
#             if isinstance(response, Exception):
#                 dashboard_data[label] = {"error": str(response)}
#             elif response.status_code == 200:
#                 try:
#                     dashboard_data[label] = response.json()
#                 except json.JSONDecodeError:
#                     dashboard_data[label] = {"error": "Invalid JSON response"}
#             else:
#                 dashboard_data[label] = {"error": f"API Error: {response.status_code}"}


#     return json.dumps(dashboard_data, indent=2)
