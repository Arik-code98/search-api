# FastAPI Items API

## Overview

This project is a simple **REST API built with FastAPI** that allows users to create and retrieve items.
Each item has a **name, price, and stock availability**. The API also supports **filtering items using query parameters**.

This project demonstrates:

* Building REST APIs with **FastAPI**
* Using **Pydantic models** for request validation
* Implementing **CRUD-style endpoints**
* Using **query parameters for filtering**
* Handling errors with **HTTPException**

---

# Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **Uvicorn** (for running the server)

---

# Installation

### 1. Clone the repository

```bash
git clone https://github.com/Arik-code98/search-api
cd search-api
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn
```

### 3. Run the server

```bash
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

# API Endpoints

## 1. Root Endpoint

### GET /

Checks if the API is running.

**Response**

```json
{
  "Message": "api is running"
}
```

---

# Create an Item

### POST /items

Creates a new item and stores it in memory.

### Request Body

```json
{
  "name": "Laptop",
  "price": 45000,
  "in_stock": true
}
```

### Response

```json
{
  "ID": 1,
  "Name": "Laptop",
  "Price": 45000,
  "In Stock": true
}
```

---

# Get All Items

### GET /items

Returns all stored items.

### Example Response

```json
{
  "1": {
    "ID": 1,
    "Name": "Laptop",
    "Price": 45000,
    "In Stock": true
  }
}
```

---

# Filter Items

The endpoint supports **optional query parameters**.

### 1. Filter by Stock

```
GET /items?in_stock=true
```

Returns only items that are currently in stock.

---

### 2. Filter by Maximum Price

```
GET /items?max_price=500
```

Returns items priced below the specified value.

---

### 3. Combine Filters

```
GET /items?in_stock=true&max_price=500
```

Returns items that satisfy **both conditions**.

---

# Get Item by ID

### GET /items/{item_id}

Fetches a specific item using its ID.

Example:

```
GET /items/1
```

### Response

```json
{
  "Item": {
    "ID": 1,
    "Name": "Laptop",
    "Price": 45000,
    "In Stock": true
  }
}
```

### Error Response

If the item does not exist:

```json
{
  "detail": "Item not found"
}
```

Status Code: **404**

---

# Data Model

The API uses a **Pydantic model** for validating item input.

```python
class Items(BaseModel):
    name: str
    price: float
    in_stock: bool
```

---

# Automatic API Documentation

FastAPI automatically provides interactive documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```
---

# Author

Developed as a **practice project to learn FastAPI and backend development with Python.**
