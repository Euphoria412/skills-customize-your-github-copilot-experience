# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build REST APIs using the FastAPI framework by creating endpoints, handling requests, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create API Endpoints

#### Description
Build a FastAPI application with multiple REST endpoints for CRUD-style operations.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define at least three endpoints using `@app.get`, `@app.post`, or other HTTP methods
- Return JSON responses from each endpoint
- Use path or query parameters in at least one endpoint

### 🛠️ Request Handling and Data Models

#### Description
Use Pydantic models to validate incoming request data and return structured responses.

#### Requirements
Completed program should:

- Define one or more Pydantic models for request or response data
- Validate data sent to a POST or PUT endpoint
- Return the validated data in the API response
- Handle invalid input with meaningful error messages

### 🛠️ Run and Test the API

#### Description
Run the FastAPI app, test the endpoints, and document how to use the API.

#### Requirements
Completed program should:

- Include instructions for starting the app with `uvicorn`
- List the available endpoints and how to call them
- Confirm that endpoints return the expected JSON output
- Optionally use the interactive Swagger UI at `/docs`
