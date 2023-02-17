"""
Information Expert Pattern:

Problem: each system must accumulate, handle, etc. some information - which part of the system must do this?;

Solution: Assign the responsibility to accumulate, handle, calculate etc. information to a particular class
- Information Expert - which holds/owns/stores that information (i.e. information necessary to fulfill that responsibility)
- implementation of the encapsulation principle.
In other words, the design of your software should follow the structure of the way the data flows. Think about where you
are storing what data and which part of your program needs what data.

As a result, we divide responsibilities among relevant classes so that each of classes performs its own work - making code
maintainable and reusable.

Recommendations: several classes can be information experts.
Closely related to Creator pattern.
"""