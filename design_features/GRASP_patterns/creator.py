"""
Creator Pattern.

Problem: "Who" should be responsible for creating instances of a class?

Solution: Assign the responsibility to create instances of class A to another class - B - which contains, aggregates,
actively uses, etc. instances of class A (another side of Information Expert Pattern).

Pros:
- Creator pattern doesn't affect coupling negatively since the created class is seen (as a rule) only to its creator class
Cons:
- in case the instantiation of a class is difficult/expensive, etc., it's more appropriate to use Abstract Factory pattern.
"""