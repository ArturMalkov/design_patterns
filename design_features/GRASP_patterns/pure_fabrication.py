"""
Pure Fabrication Pattern.

Problem: which class must provide realization/implementation of low coupling and high cohesion patterns?
(according to OOP paradigm, code should reflect real-world system - where objects correspond to real-world objects).

Solution: when we need to adhere to low coupling and high cohesion patterns, we should create and use a class which
doesn't exist in real world (artificial entity is needed to ensure low coupling and high cohesion).

Pros:
- ensures low coupling and high cohesion;

Cons:
- do not abuse its usage - otherwise all functions within system will become classes.
"""