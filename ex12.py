#!/usr/bin/env python

class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tokenize(string):
    return string.replace("(", " ( ").replace(")", " ) ").split()

def consume(token_list):
    return token_list.pop(0)

def build_parse_tree(token_list):
    """Takes in a token list and produces a parse 
    tree according to the rules in the README"""
    node = BinaryTreeNode(None)
    while token_list: 
        current_token = consume(token_list)
        if current_token == "(": 
            node.left = build_parse_tree(token_list)
        elif current_token in "+-/*": 
            node.value = current_token
            node.right = build_parse_tree(token_list)
        elif current_token == ")": 
            return node
        else: 
            node.value = int(current_token)
            return node 

def is_num(string):
    try:
        int(string)
        return True
    except:
        return False

def evaluate_tree(node):
    if node is None:
        return
    if type(node.value) == int:
        return node.value
    elif node.value == "+":
        return evaluate_tree(node.left) + evaluate_tree(node.right)
    elif node.value == "*":
        return evaluate_tree(node.left) * evaluate_tree(node.right)
    elif node.value == "/":
        return evaluate_tree(node.left) / evaluate_tree(node.right)
    elif node.value == "-":
        return evaluate_tree(node.left) - evaluate_tree(node.right)

def main():
    sample_string = "(((3 + 2) * (4 - 1) / 3 + 7) * (1 + (-5 + 6)))"
    tokens = tokenize(sample_string)
    tree = build_parse_tree(tokens)
    print evaluate_tree(tree)

if __name__ == "__main__":
    main()