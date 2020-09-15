# Proxy Design Pattern

- Interface for accessing a particular resource

``
A class that functions as an interface to a particular resource. That resource may be remote, expensive to construct or may require logging or some other added functionality. 
``

# Proxy Vs Decorator (Looks same but not)

- Proxy provides an identical interface but Decorator provides and enhanced interface.
- The decorator typically aggregates(or has a reference to) what is decorating but Proxy doesn't have to.
- Proxy might not even be working with a materialized object(e.g virtual proxy).