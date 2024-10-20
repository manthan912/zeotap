# rule_engine.py

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # 'operator' or 'operand'
        self.left = left       # Left child (Node)
        self.right = right     # Right child (Node)
        self.value = value     # Operand value or operator ('AND', 'OR')

    def __str__(self):
        if self.type == 'operator':
            return f"({str(self.left)} {self.value} {str(self.right)})"
        else:
            return self.value

# Function to create a rule and return an AST
def create_rule(rule_string):
    try:
        # Simplified parsing logic (you can expand this)
        # In practice, use Python's ast module or regex parsing
        condition = rule_string.strip()
        if 'AND' in condition:
            left, right = condition.split('AND')
            return Node('operator', Node('operand', value=left.strip()), Node('operand', value=right.strip()), 'AND')
        elif 'OR' in condition:
            left, right = condition.split('OR')
            return Node('operator', Node('operand', value=left.strip()), Node('operand', value=right.strip()), 'OR')
        else:
            return Node('operand', value=condition)
    except Exception as e:
        raise ValueError(f"Invalid rule string: {str(e)}")

# Function to combine rules
def combine_rules(rule_list, operator='OR'):
    combined_rule = create_rule(rule_list[0])
    for rule in rule_list[1:]:
        combined_rule = Node('operator', combined_rule, create_rule(rule), operator)
    return combined_rule

# Function to evaluate a rule AST
def evaluate_rule(ast_node, data):
    if ast_node.type == 'operator':
        left_eval = evaluate_rule(ast_node.left, data)
        right_eval = evaluate_rule(ast_node.right, data)
        if ast_node.value == 'AND':
            return left_eval and right_eval
        elif ast_node.value == 'OR':
            return left_eval or right_eval
    elif ast_node.type == 'operand':
        return evaluate_operand(ast_node.value, data)

def evaluate_operand(condition, data):
    # Convert condition string to Python expression using eval
    try:
        return eval(condition, {}, data)
    except Exception as e:
        raise ValueError(f"Error evaluating condition: {condition}, Error: {str(e)}")
