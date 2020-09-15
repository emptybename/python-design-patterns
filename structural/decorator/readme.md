# Decorator Design Pattern
- Adding behaviour without altering the class itself
- Want to augment an object with additional functionality
- Do not want to rewrite or alter existing code(Open-close-principle)
- Need to be able to interact with existing structure. 
- Two options -
    1. Inherit from required object(if possible)
    2. Build a Decorator which simply references the decorated object(s)
