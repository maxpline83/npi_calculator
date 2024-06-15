
# NPI Calculator

## Overview
The NPI Calculator is a tool designed to perform specific calculations related to National Provider Identifier (NPI) data. This project includes API handling, database interactions, and computation logic to process and manage NPI-related data efficiently.

## Table of Contents
- [Project Overview](#overview)
- [Directory Structure](#directory-structure)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
    - [Compute NPI Expression](#compute-npi-expression)
    - [Insert Example Data](#insert-example-data)
    - [Get Calculation History](#get-calculation-history)
    - [Clear Calculation History](#clear-calculation-history)
    - [Export Data to CSV](#export-data-to-csv)
- [Testing](#testing)
- [CI/CD](#cicd)

## Directory Structure
The project directory is organized as follows:


```
npi_calculator/
├── .github/
│   └── workflows/
│       └── ci_cd.yaml
├── .venv/
├── data/
│   ├── api_requests.db
│   └── test_api_requests.db
├── output_files/
│   └── test.csv
├── src/
│   ├── api/
│   │   ├── routers/
│   │   │   └── init.py
│   │   └── app.py
│   ├── calculator/
│   │   ├── init.py
│   │   └── npi_calculator.py
│   └── database/
│       ├── init.py
│       └── database.py
├── tests/
│   ├── api/
│   │   └── test.py
│   ├── calculator/
│   │   └── test.py
│   └── database/
│       └── test.py
├── .flake8
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
├── requirements.txt
```

## Setup Instructions

To set up the NPI Calculator project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/your-username/npi_calculator.git
```

2. Navigate to the project directory:

```bash
cd npi_calculator
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment:

```bash
source .venv/bin/activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Run the application using Docker Compose:

```bash
docker-compose up
```

7. Access the NPI Calculator API at `http://localhost:8000` and start performing NPI calculations.




## API Endpoints

### Overview

The NPI Calculator API provides several endpoints to interact with the calculator and database functionalities. Below are the endpoints available:

### Endpoint Details

#### Compute NPI Expression
- **Endpoint:** `/npi_calculator/{expression}`
- **Method:** `GET`
- **Description:** Computes an NPI-related expression and stores the result in the database.
- **Parameters:**
  - `expression` (string): The NPI expression to evaluate.
- **Usage Example:**
```http
GET /npi_calculator/1 3 +
```
Response Example (Success):
```json
{
    "expression": "1 3 +",
    "result": "4"
}
```
Response Example (Error):
```json
{
    "expression": "1 0 /",
    "error": "Division by zero is not allowed"
}
```

#### Insert Example Data
- **Endpoint:** `database/insert_example_data`
- **Method:** `GET`
- **Description:** Inserts example data into the database for testing purposes.
- **Usage Example:**
```http
GET database/insert_example_data
```
Response Example:
```json
{
    "message": "Example data inserted!"
}
```


#### Get Calculation History

- **Endpoint:** `database/history`
- **Method:** `GET`
- **Description:** Retrieves the history of calculations stored in the database.
- **Usage Example:**
```http
GET database/history
```
Response Example:
```json
[
  {
    "query": "5 3 +",
    "result": 8
  },
  {
    "query": "4 2 * 3 +",
    "result": 11
  },
  {
    "query": "10 2 ÷",
    "result": 5
  }
]
```

#### Clear Calculation History
- **Endpoint:** `database/clear`
- **Method:** `GET`
- **Description:** Clears all calculation history from the database.
- **Usage Example:**
```http
GET database/clear
```
Response Example:
```json
{
    "message": "DB Reset!"
}
```



#### Export Data to CSV
- **Endpoint:** `database/export_to_csv/{filename}`
- **Method:** `GET`
- **Description:** Exports the calculation history to a CSV file with the specified filename.
- **Parameters:**
  - `filename` (string): The name of the CSV file to export.
- **Usage Example:**
```http
GET database/export_to_csv/test.csv
```
Response Example:
```json
{
    "message": "Data exported to test.csv"
}
```

#### Using `curl`:

```bash
# Compute NPI Expression
curl -X GET http://localhost:8000/npi_calculator/1%203%20%2B

# Insert Example Data
curl -X GET http://localhost:8000/database/insert_example_data

# Get Calculation History
curl -X GET http://localhost:8000/database/history

# Clear Calculation History
curl -X GET http://localhost:8000/database/clear

# Export Data to CSV
curl -X GET http://localhost:8000/database/export_to_csv/test.csv
```

## Testing

### Running Tests Locally

The project uses `unittest` for testing. You can run the tests locally using the following commands:

#### Calculator Module Tests

To run the tests for the calculator module:

```bash
python -m unittest tests.calculator.test
```

#### Basic API Tests
To run the basic API tests:

```bash
python -m unittest tests.api.test
```
#### Calculator API Tests
To run the calculator API tests:

```bash
python -m unittest tests.api.test_calculator
```
#### API Integration Tests
To run the API integration tests:

```bash
python -m unittest tests.api.test_database
```

#### Database Tests  
To run the database tests:

```bash
python -m unittest tests.database.test
```

## CI/CD
The project uses GitHub Actions for continuous integration and deployment. The CI/CD pipeline is defined in `.github/workflows/ci_cd.yaml`.