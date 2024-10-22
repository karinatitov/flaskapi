# Flask-Postgres API

This is a simple Flask API that interacts with a Postgres database. The project is containerized using Docker and uses Docker Compose to run both the Flask app and the Postgres database.

## Features

- Create, read, and filter customer records.
- Query customers by city using the /customers endpoint.
- Containerized with Docker for easy deployment.
- PostgreSQL for persistent data storage.
- Auto-seeding of the database using seed.sql.

## Prerequisites

- **[Docker](https://www.docker.com/products/docker-desktop)** (v19.03+ recommended)
- **[Docker Compose](https://docs.docker.com/compose/install/)** (v1.27+ recommended)
- **Git** (to clone the repository)

## 📂 Project Structure

```
flask-postgres-app/
├── app.py                  # Flask application (API logic)
├── models.py               # SQLAlchemy models (Customer schema)
├── client.py               # Example client script using `requests` to interact with the API
├── requirements.txt        # Python dependencies
├── Dockerfile              # Dockerfile for the Flask app
├── seed.sql                # SQL file to seed the database
└── docker-compose.yml      # Docker Compose configuration file
```

# 🚀 Getting Started

### 1. Clone the repository:

    ```
    git clone https://github.com/your-username/flask-postgres-app.git
    cd flask-postgres-app
    ```

### 2. Create a `.env` File (Optional, for development)

    Create a `.env` file in the project root to define environment variables for the Postgres database.

    Example `.env` file: (This is the default configuration for the Postgres database.)

    ```
    POSTGRES_USER=flaskuser
    POSTGRES_PASSWORD=flaskpassword
    POSTGRES_DB=customerdb
    ```

### 3. Build and Run the Containers

    Use Docker Compose to build and run the Flask and Postgres containers.

    ```
    docker-compose up --build
    ```

    This will:

    - Build the Flask app.
    - Pull the Postgres image and start the database.
    - Seed the database with initial customer data from seed.sql.

### 4. Verify the Setup

    Once the containers are running, you can test the API by making a GET request to fetch all customers.

    ```
    curl http://localhost:5001/customers
    ```

# 📖 API Documentation

### 1. GET `/customers`
Retrieve all customers or filter by city using a query parameter.

- URL: `/customers?city=<city_name>`
- Method: GET
- Query Parameters: city (optional)

### Example Request:

To get all customers in "San Antonio":

```bash
curl "http://localhost:5001/customers?city=San%20Antonio"
```
Example Response:
```json

[
  {
    "id": 1,
    "first_name": "Jane",
    "last_name": "Doe",
    "email": "jane.doe@example.com",
    "address": "456 Oak St",
    "city": "San Antonio",
    "state": "TX",
    "zip": "78205"
  }
]
```

### 3. GET `/customers/<int:customer_id>`

Retrieve a customer by their unique ID.

- URL: `/customers/<int:customer_id>`
- Method: GET

Example Request:
```
curl http://localhost:5001/customers/1
```

Example Response:

```json
{
  "id": 1,
  "first_name": "Jane",
  "last_name": "Doe",
  "email": "jane.doe@example.com",
  "address": "456 Oak St",
  "city": "San Antonio",
  "state": "TX",
  "zip": "78205"
}
```

### 3. POST `/customers`

Create a new customer.

- URL: /customers
- Method: POST
- *Request Body*: JSON containing customer data (`first_name`, `last_name`, `email`, `address`, `city`, `state`, `zip`)

Example Request:

```
curl -X POST http://localhost:5001/customers \
-H "Content-Type: application/json" \
-d '{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "address": "789 Maple St",
  "city": "Austin",
  "state": "TX",
  "zip": "73301"
}'
```

Example Response:

```
{
  "id": 2,
  "first_name": "John",
  "last_name": "Doe",
  "email": "john.doe@example.com",
  "address": "789 Maple St",
  "city": "Austin",
  "state": "TX",
  "zip": "73301"
}
```

## 🛑 Stopping the Containers

To stop the running containers, use:

```
docker-compose down -v
```
This will stop both the Flask app and Postgres containers and remove the associated volumes.

## 🔄 Rebuilding the Containers

If you make changes to the code or any dependencies, rebuild the containers by running:

```
docker-compose up --build
```

## 🔐 Handling Secrets

- For development, use a `.env` file to manage sensitive information like database credentials. Ensure the `.env` file is excluded from version control (i.e., add it to `.gitignore`).

- For production, consider using Docker/Kubernetes Secrets, Vault, Sops or environment variables passed securely to the container. Never hardcode credentials or secrets in your source code.

## 🧪 Running Tests

You can write unit tests for your API using Python’s `unittest` or `pytest` libraries. Here’s an example of how you might test retrieving customers:

```
import requests
import unittest

class TestFlaskAPI(unittest.TestCase):
    BASE_URL = "http://localhost:5001"

    def test_get_customers(self):
        response = requests.get(f"{self.BASE_URL}/customers")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```

To run the tests:

```
python -m unittest tests/tests.py
```

## 🏗 Built With
- [Flask](https://flask.palletsprojects.com/en/2.3.x/) - The web framework used
- [SQLAlchemy](https://www.sqlalchemy.org/) - The SQL toolkit and Object Relational Mapper
- [Docker](https://www.docker.com/) - Containerization platform
- [Docker Compose](https://docs.docker.com/compose/) - Tool for defining and running multi-container Docker applications
- [Postgres](https://www.postgresql.org/) - The relational database management system

## 🧑‍💻 Author

- Karina Titov