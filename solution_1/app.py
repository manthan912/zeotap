# app.py

from flask import Flask, request, jsonify
from rule_engine import create_rule, evaluate_rule, combine_rules

app = Flask(__name__)

# Endpoint for creating a rule
@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json.get('rule_string')
    try:
        rule_ast = create_rule(rule_string)
        return jsonify({"message": "Rule created successfully", "rule_ast": str(rule_ast)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Endpoint for evaluating a rule
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    rule_ast = request.json.get('rule_ast')
    data = request.json.get('data')
    try:
        result = evaluate_rule(rule_ast, data)
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to combine multiple rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = request.json.get('rules')
    operator = request.json.get('operator', 'OR')
    try:
        combined_rule = combine_rules(rules, operator)
        return jsonify({"message": "Rules combined successfully", "combined_rule": str(combined_rule)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
