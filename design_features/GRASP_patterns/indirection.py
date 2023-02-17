"""
Indirection Pattern (IoC - inversion of control).

Problem: how to distribute responsibilities among classes to ensure there's no direct coupling?

Solution: assign the responsibility to provide connection among services or components to some intermediate object -
interface/abstract class.

(Client (business logic) -> interface) -> server
instead of client (business logic) -> (interface -> server), thus, allowing us to invert the control (server depends on
its interface rather than client (business logic) depends on the server).

Pros:
- makes code reusable
"""