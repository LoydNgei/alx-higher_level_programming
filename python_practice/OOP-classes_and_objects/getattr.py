"""The working of a getattr function"""

class GO:
"""Declaring class GO"""
   name = "Bigi"
   age = 24

obj = GO()

print("The name is " + getattr(obj, 'name'))

print("Description is " + getattr(obj, 'description', 'CS portal'))
