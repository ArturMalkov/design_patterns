"""
Law of Demeter (LoD) or Principle of Least Knowledge - 'don't talk to strangers' (don't depend on the internals of strangers -
other objects which you don't directly know):
- Each unit should have only limited knowledge about other units: only units "closely" related to the current unit.
- Each unit should only talk to its friends; don't talk to strangers - via accessing their attributes/methods
(one dot vs two dots).
- Only talk to your immediate friends:
    method of an object may only access direct internals (properties and methods) of:
    1) the same object;
    2) objects on which current object directly depends (e.g. inheritance, dependency injection (e.g. objects stored in properties of that object));
    3) objects created in the current method;
    4) objects passed as arguments to the current method.

(Exception from the Law of Demeter: if we're dealing with 'data containers', not 'real' classes).

The fundamental notion is that a given object should assume as little as possible about the structure or properties of
anything else (including its subcomponents), in accordance with the principle of "information hiding".

An object a can request a service (call a method) of an object instance b, but object a should not "reach through" (drill
deeply) object b to access yet another object, c, to request its services. Doing so would mean that object a implicitly
requires greater knowledge of object b's internal structure.
(+ simple changes in the internal structure of that 'stranger' object can result in a lot of changes in a lot of places
in our application)

Instead, b's interface should be modified if necessary so it can directly serve object a's request, propagating it to any
relevant subcomponents. Alternatively, a might have a direct reference to object c and make the request directly to that.
If the law is followed, only object b knows its own internal structure.

Aimed at reducing coupling.

One of the solutions to this problem - Tell, Don't Ask!
"""
