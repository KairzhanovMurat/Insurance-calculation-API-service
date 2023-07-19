# Insurance-calculation-API-service
This project is a REST API service that calculates insurance costs based on the type of cargo and declared value. It retrieves the tariff rates from an external source via an API and uses the latest applicable rate for the calculation.

## Features

- Calculates insurance cost based on cargo type and declared value using the latest applicable tariff rate.
- Supports retrieval of tariff rates from an external API source.
- Stores tariff rates in a database for easy retrieval and management.
- Dockerized application for easy deployment and portability.
- Developed using FastAPI framework, Tortoise ORM, and PostgreSQL database.
- Utilizes Docker and Docker Compose for containerization and database setup.

## Getting Started

### Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

### Installation and Setup

1. Clone the repository:
git clone https://github.com/KairzhanovMurat/Insurance-calculation-API-service.git

2. Navigate to the project directory:
cd Insurance-calculation-API-service

3.Build and run the Docker containers:
docker-compose up --build

### Usage

- To calculate insurance cost, make a GET request to `/calculate-insurance` endpoint with the following query parameters:
- `cargo_type`: Type of cargo (e.g., Glass, Other)
- `declared_value`: Declared value of the cargo
- `tariff_date` (optional): Date of the tariff (default: current date)

- To upload tariff rates, make a POST request to `/tariffs/upload` endpoint with a JSON payload containing the tariff rates in the specified format.

Refer to the API documentation and examples for detailed usage instructions.


## Note
create your own .env file with database credentials like in .env.example

