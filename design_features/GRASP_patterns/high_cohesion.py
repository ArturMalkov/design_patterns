"""
High Cohesion Pattern

Cohesion - how much certain pieces belong together and how much sense they make.

Problem: it's needed to ensure that objects perform various functions - how do we distribute all such functions?

Solution: provide distribution of responsibilities with high cohesion - i.e. each class must be responsible for one
function only (or closely related functions) - implementation of single responsibility principle.
Each class must be internally coherent (logical and consistent).

Cohesion may be measured by the extent to which methods of a class use its properties:
- Maximum cohesion: all methods of a class each use all properties of a class (can hardly be achieved in practice);
- Minimum cohesion: of all methods of a class, no method uses any property of a class - i.e. properties of a class are not
managed by its methods, instead they probably are public and can be used from outside that class - avoid classes with no
cohesion unless you want to have a 'data container' with utility methods.

The goal is to have highly cohesive classes where all their methods use many of their properties (you should have a good
usage of properties in your methods).

Pros:
- classes with high cohesion are maintainable and reusable.

Cons:
- sometimes it's more appropriate to avoid high cohesion - especially when it comes to distributed server objects.
In such case, for performance purposes it's recommended to create several large server objects with low cohesion.
"""