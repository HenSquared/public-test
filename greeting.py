#!/usr/bin/env python3
"""
A simple greeting utility module.
This demonstrates basic Python functionality for the agent task.
"""


def greet(name):
    """
    Generate a personalized greeting.
    
    Args:
        name (str): The name to greet
        
    Returns:
        str: A greeting message
        
    Raises:
        ValueError: If name is not a non-empty string
    """
    if not name or not isinstance(name, str):
        raise ValueError("Name must be a non-empty string")
    
    return f"Hello, {name}! Welcome to the agent task implementation."


def greet_multiple(names):
    """
    Generate greetings for multiple people.
    
    Args:
        names (list): A list of names to greet
        
    Returns:
        list: A list of greeting messages
        
    Raises:
        TypeError: If names is not a list
        ValueError: If any name in the list is not a non-empty string
    """
    if not isinstance(names, list):
        raise TypeError("Names must be provided as a list")
    
    # Validate all names before processing
    for name in names:
        if not name or not isinstance(name, str):
            raise ValueError("All names must be non-empty strings")
    
    return [greet(name) for name in names]


def main():
    """Main function to demonstrate the greeting utility."""
    print(greet("Agent"))
    print("\nGreeting multiple people:")
    for greeting in greet_multiple(["Alice", "Bob", "Charlie"]):
        print(f"  - {greeting}")


if __name__ == "__main__":
    main()
