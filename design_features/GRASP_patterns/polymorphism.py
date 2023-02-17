"""
Polymorphism Pattern ('polymorphism' - the ability of an object to take on many forms)

Problem: how to handle alternative behavior options based on types? How to replace plug-in system elements?

Solution: Responsibilities for different behavior options are distributed using polymorphic operations for this class -
i.e. interaction with different (alternative) external (plugin) systems must be delegated to a separate (abstract/interface)
class (outside the business logic) whose implementations - concrete classes - each must handle relevant external system -
instead of mixing it with our business logic and adding multiple 'if' checks, etc. to it.
It's all about using polymorphism principle in real code - address the external system only through its interface.

Pros:
- easy to support, maintain, extend, modify code, helps to avoid code duplication.
"""