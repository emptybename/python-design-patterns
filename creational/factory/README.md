# Factory Patterns:
1. Factories are used to encapsulate the information about classes we are using, while instantiating them based on certain parameters we are providing with them.
2. By using factory we can switch out an implementation by another by simply changing the parameter.

# Factory Methods:
1. These are responsible for creation of object
2. Since Initializer is not descriptive enough
    e.g  __init__ this does not tell much
    So from factory method we can return objects as discussed above through factory patterns

Factory is responsible for wholesale creation of an object(non piecewise unlike builder) It can be using - 
* Separate method i.e Factory Method
* Separate class i.e Factory class
* Hierarchy of factories i.e Abstract Factory
    
   
 