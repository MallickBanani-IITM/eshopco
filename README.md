# Virtual TA - eShopCo

This is a FastAPI-based app for answering questions related to the course content scraped from Moodle/Discourse.

## Endpoint

**POST** `/api/`  
Request:
```json
{ "query": "Your question here" }
