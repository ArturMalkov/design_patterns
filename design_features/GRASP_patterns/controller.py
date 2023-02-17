"""
Controller Pattern.

Problem: "who" should be responsible for handling incoming system events (logging, authentication, authorization, caching)?
(incoming system events shouldn't be mixed with business logic - they must be isolated)

Solution: All incoming system messages must be localized (as opposed to mixing it with business logic) - handled by a
special class - Controller - which is responsible for handling system events and doesn't belong to the user interface. Controller defines methods for
performing system operations.

Recommendations: for different situations it's logical to use different controllers - they don't have to be overloaded

Pros:
- suitable for accumulating information on system events;
- makes components more reusable (system events are handled by a Controller - not by elements of user interface).

Cons:
- controller can be overloaded
"""