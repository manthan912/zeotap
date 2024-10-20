# zeotap
Weather Forecast & Rule Engine with AST
Overview
This repository contains two main applications:

Weather Forecast API: A simple weather forecasting API that retrieves real-time weather data using the OpenWeather API.
3-Tier Rule Engine with AST: A rule engine that determines user eligibility based on attributes like age, department, income, etc. It uses an Abstract Syntax Tree (AST) to dynamically create, combine, and evaluate conditional rules.
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
License
Weather Forecast API
Setup
Clone the repository:

bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
Install dependencies: The weather API uses Flask and requests. Install them using:

bash

pip install flask requests
Configure API Key: You'll need an API key from OpenWeather. After signing up and generating an API key, create a .env file in the project root and add your key:

bash
 
OPENWEATHER_API_KEY=your_api_key_here
Run the application:

bash
python weather_app.py
Usage
Get Weather Data: You can retrieve the weather forecast for a specific city by making a GET request to the /weather endpoint. Example:

bash
curl "http://127.0.0.1:5000/weather?city=London"
The response will provide real-time weather data for the requested city.

3-Tier Rule Engine with AST
This part of the project determines user eligibility based on attributes such as age, department, income, etc., using dynamically created rules. The system represents these rules using an Abstract Syntax Tree (AST).

Project Structure
bash
rule-engine/
├── app.py                # Flask app to expose API endpoints
├── rule_engine.py        # Core logic for AST, rule creation, combination, and evaluation
├── db_setup.py           # Script for setting up the SQLite database
├── requirements.txt      # Dependencies for the project
└── database.db           # SQLite database (generated after running db_setup.py)
Database Setup
The project uses SQLite to store the rule metadata. You can set up the database by running:

bash
python db_setup.py
This will create a rules table in the database.db file with the following schema:

sql
CREATE TABLE IF NOT EXISTS rules (
    rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_string TEXT NOT NULL
);
API Endpoints
Create Rule

URL: /create_rule
Method: POST
Payload:
json
 
{
  "rule_string": "age > 30 AND department = 'Sales'"
}
Response: The created rule's AST.
Evaluate Rule

URL: /evaluate_rule
Method: POST
Payload:
json
 
{
  "rule_ast": { "type": "operator", "left": ..., "right": ..., "value": "AND" },
  "data": { "age": 35, "department": "Sales", "salary": 60000, "experience": 3 }
}
Response: Returns True or False based on the rule evaluation.
Combine Rules

URL: /combine_rules
Method: POST
Payload:
json
{
  "rules": [
    "age > 30 AND department = 'Sales'",
    "age < 25 AND department = 'Marketing'"
  ],
  "operator": "AND"
}
Response: The combined rule AST.
Usage
Install dependencies: Install the necessary dependencies using:

bash
pip install -r requirements.txt
Run the application: To start the Flask API, run:

bash
python app.py
Testing the Endpoints: Use tools like Postman or curl to test the API. Below are a few sample commands:

Create Rule:

bash
curl -X POST http://127.0.0.1:5000/create_rule \
     -H "Content-Type: application/json" \
     -d '{"rule_string": "age > 30 AND department = '\''Sales'\''"}'
Evaluate Rule: Once a rule has been created, evaluate it using:

bash
 
curl -X POST http://127.0.0.1:5000/evaluate_rule \
     -H "Content-Type: application/json" \
     -d '{
           "rule_ast": { "type": "operator", "left": ..., "right": ..., "value": "AND" },
           "data": { "age": 35, "department": "Sales", "salary": 60000, "experience": 3 }
         }'
