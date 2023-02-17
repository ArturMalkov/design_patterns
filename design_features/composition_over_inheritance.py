"""
Disadvantages of inheritance:
1. the relationship between a base class and a derived class is statically fixed
2. inheritance supports weak encapsulation and fragile structures
3. a derived class inherits everything, even things it doesn't need or want
4. changes in a base class interface impact all its derived classes

Advantages of composition:
1. implementations are configurable at runtime:
- since components are sent as parameters, we can change them dynamically at any moment
2. supports good encapsulation and adaptable structures:
- since we only use the interface of a component
3. interface changes have limited ripple effect
4. composition allows a composite class to have relationships with many component classes
"""