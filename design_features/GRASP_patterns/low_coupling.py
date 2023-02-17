"""
Low Coupling Pattern

Coupling is the degree of interdependence between software modules; a measure of how closely connected two modules are;
the strength of relationships between modules.

Problem: ensure low coupling when creating an instance of a class and linking it with another class -
i.e. ensure the lowest possible number of links/connections between different objects of the system (minimum arrows on
UML diagram) -> minimize connections between classes.

Solution: delegate responsibilities among objects in a way that ensures low degree of connection between objects.
"""

# how to achieve low coupling?
# 1. avoid deep inheritance relationships
# 2. separate creating resources from using them
# 3. introduce abstractions
# 4. avoid inappropriate intimacy (e.g. only pass what's necessary to a function)
