
# API Reference
This document provides details of the available API endpoints.

## `/predict` [POST]
- **Description**: Predicts the emotion from input data.
- **Request Body**:
```json
{
  "data": [0.5, 0.2, 0.1]
}
```
- **Response**:
```json
{
  "prediction": ["happy"]
}
```

## `/status` [GET]
- **Description**: Returns the status of the API.
