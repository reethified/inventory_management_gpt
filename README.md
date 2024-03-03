# Inventory Management System
## Lean Code development Approach

This repository contains a inventory management system designed for efficient inventory organization and sales tracking. Showcasing the possbility of can a end to end applications be developed without the having expertise of full stack developer. It was generated using a series of GPT prompts

## Project Structure

The project is structured into the following modules:

- `models`: Contains Python model classes for managing inventory items, stocks, admins, and transactions.
- `frontend`: This directory will host the Streamlit web application for interacting with the inventory management system.
- `tests`: Holds the unit test cases for testing the functionality of the inventory management system.
- `config.toml`: Configuration file for the Streamlit app and logging settings.
- `logging.yaml`: YAML configuration file for logging setup.

## Model Classes

- **Stock**: Manages multiple items in the inventory.
- **Item**: Represents individual inventory items.
- **Admin**: Handles admin authentication and management.
- **Transaction**: Records sales transactions and updates the inventory accordingly.

## Streamlit App

The Streamlit app provides a user friendly interface for managing inventory items, adding/removing/updating stocks, recording transactions, and viewing available stocks.

### Features

- Add, remove, update items and stocks.
- View all available stocks.
- Record transactions for items and update stock quantities accordingly.
- Logging of each request with proper DEBUG, INFO, ERROR, WARN levels.
- Separate configuration files for logging and Streamlit settings.

## Docker Compose

The Docker Compose file sets up the Python Streamlit app and PostgreSQL database:

- Launches Streamlit with specified configurations.
- Mounts volumes for logging and database data storage.

## Manually Execute

    pip install -r requirements.txt
    stmrealit run app.py

## Usage

To run the application locally, follow these steps:

1. Clone the repository to your local machine.
2. Set up Python environment with necessary dependencies.
3. Modify configurations in `config.toml` and `logging.yaml` if needed.
4. Execute the Docker Compose command to launch the application.