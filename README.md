# DynamoDB Local Operations
Automation of DynamoDB Local operations using Python and boto3

## Overview 🌐
DynamoDB Local Operations is a Python script designed to automate various operations on DynamoDB Local. This script utilizes the boto3 library to perform tasks such as creating tables, adding items, listing tables, and deleting tables. It provides a straightforward way to interact with a local instance of DynamoDB for testing and development purposes.

## Requirements 🛠️
- Python 3.12 or higher
- boto3

## Getting Started 🚀

Run Docker Compose to start DynamoDB Local:

bash

docker-compose -f docker-compose.dynamo.yml up
Clone the DynamoDB Local Operations repository to your local machine.

Install the necessary dependencies:


With poetry
Clone the DynamoDB Local Operations repository to your local machine.

bash

git clone https://github.com/yourusername/dynamodb-local-operations.git
cd dynamodb-local-operations
Install poetry if you haven't already. Follow the installation instructions from the Poetry website.

Install the project dependencies using poetry:

bash

poetry install
Run the script within the Poetry environment:

bash

poetry run python dynamodb_operations.py


## Usage 💡
The script provides several functions to interact with DynamoDB Local:

- create_table(): Creates a table in DynamoDB Local with a simple schema.
- list_tables(): Lists all tables in DynamoDB Local.
- add_item(): Adds an item to the specified table.
- delete_table(table_name: str): Deletes the specified table from DynamoDB Local.

## Features 🌟
- Create Table: Initializes a new table with a specified schema.
- List Tables: Displays all existing tables in the local DynamoDB instance.
- Add Item: Inserts an item into a specific table.
- Delete Table: Removes a table from the local DynamoDB instance.

## Screenshots 📸


## Contributing 🤝
Contributions are welcome. Please follow the contribution guidelines.

## License 📄
DynamoDB Local Operations is licensed under the MIT License. See the LICENSE file for more details.

