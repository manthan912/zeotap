# zeotap
Weather Forecast & Rule Engine with Abstract Syntax Tree (AST)
Overview
This repository encompasses two distinct applications:

Weather Forecast API: A service that fetches real-time weather data utilizing the OpenWeather API.
3-Tier Rule Engine with AST: A dynamic rule engine that evaluates user eligibility based on specific attributes, such as age, department, income, and more. This system employs an Abstract Syntax Tree (AST) to construct, combine, and evaluate rules.
Table of Contents
Weather Forecast API
Setup
Usage
3-Tier Rule Engine with AST
Project Structure
Database Setup
API Endpoints
Usage
Testing
Weather Forecast API
Setup
Repository Clone: Clone the repository and navigate into the project directory.

Dependencies Installation: Install the necessary dependencies, ensuring you have the correct versions of Flask and any other required packages.

API Key Configuration: Obtain an API key from OpenWeather and store it securely in the project environment to ensure secure access to the weather API.

Application Execution: Execute the application locally to initiate the weather forecasting service.

Usage
To retrieve weather data for a specific location, users can make a GET request to the designated endpoint. The weather data returned will reflect real-time conditions for the queried city.

3-Tier Rule Engine with AST
This component evaluates user eligibility by processing dynamic conditional rules. The rules, represented using an Abstract Syntax Tree (AST), can be created, combined, and evaluated in real-time.

Project Structure
The rule engine component comprises several key files, including the core logic for rule creation and evaluation, the database setup script, and the Flask application exposing API endpoints. These components work together to provide a flexible and scalable rule-based system.

Database Setup
The system leverages SQLite for storing rule metadata. Users can initialize the database using a provided script, which creates a table to store the rule definitions.

API Endpoints
The application provides several key endpoints:

Create Rule: This endpoint allows users to define new rules, which are represented and stored as ASTs.

Evaluate Rule: This endpoint evaluates a rule against user data to determine if the conditions are met.

Combine Rules: This functionality enables the combination of multiple rules using logical operators, such as AND or OR, to create more complex rule structures.

Usage
To use the rule engine, users can submit rule definitions and evaluate them against provided user data. The system dynamically constructs and processes AST representations of these rules, ensuring flexibility and precision in rule evaluation.

Testing
Users can interact with the API via tools such as Postman or curl, allowing them to define rules, evaluate conditions, and test the system's response to various datasets.

