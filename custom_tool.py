# src/tools/custom_tool.py
"""
This simple tool provides calculator functionality.
"""

import ast

def calculate_expression(expr: str):
    """
    Safely evaluate a basic arithmetic expression.
    Supports: +, -, *, /, **, parentheses
    """
    node = ast.parse(expr, mode='eval')

    def eval_node(n):
        if isinstance(n, ast.Constant):     # Python 3.8+
            return n.value
        if isinstance(n, ast.BinOp):
            left = eval_node(n.left)
            right = eval_node(n.right)
            if isinstance(n.op, ast.Add): return left + right
            if isinstance(n.op, ast.Sub): return left - right
            if isinstance(n.op, ast.Mult): return left * right
            if isinstance(n.op, ast.Div): return left / right
            if isinstance(n.op, ast.Pow): return left ** right
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
            return -eval_node(n.operand)
        raise ValueError("Unsupported expression")

    return eval_node(node.body)

# Example usage:
if __name__ == "__main__":
    expr = input("Enter an arithmetic expression: ")
    try:
        result = calculate_expression(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
