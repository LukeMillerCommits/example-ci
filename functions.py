def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  # <--- fix this in step 7

def multiply(a, b):
    return a * b

def convert_fahrenheit_to_celsius(fahrenheit):
    if (fahrenheit < -459.67):
        raise AssertionError("Tempurature cannot be lower than -459.67 fahrenheit")
    
    return multiply(subtract(fahrenheit, 32), 5 / 9) # <-- Fix this in step 7