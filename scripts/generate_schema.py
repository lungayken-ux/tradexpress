# scripts/generate_schema.py
import sys

def generate_markdown():
    # In a real scenario, you would import your DB models here
    # Example: from my_app.models import User, Product
    
    markdown_content = """# Database Schema
This document is automatically generated from the source code.

| Table Name | Description | Key Columns |
| :--- | :--- | :--- |
| Users | User profile data | id, email, password |
| Products | Catalog information | id, sku, price |
"""
    print(markdown_content)

if __name__ == "__main__":
    generate_markdown()
