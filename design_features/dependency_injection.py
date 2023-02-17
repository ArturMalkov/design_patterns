"""
Dependency injection (DI) - a variable is passed into a class instead of being created inside a class.
(or instead of instantiating a class inside a regular function, we pass an object as an argument to that function).
It's a technique in which an object receives other objects that it depends on, called dependencies.
Typically, the receiving object is called a client and the passed-in ('injected') object is called a service.

The code that passes the service to the client is called the injector (or DI container). Instead of the client specifying which service
it will use, the injector tells the client what service to use. The 'injection' refers to the passing of a dependency
(a service) into the client that uses it.

Dependency injection is one form of the broader technique of inversion of control (IoC) - a client who wants to call some services
should not have to know how to construct those services. Instead, the client delegates to external code (the injector).
The client is not aware of the injector.
The injector passes the services, which might exist or be constructed by the injector itself, to the client.
The client then uses the services.
This means the client does not need to know about the injector, how to construct the services, or even which services it
is actually using. The client only needs to know the interfaces of the services, because these define how the client may
use the services. This separates the responsibility of 'use' from the responsibility of 'construction'.

It's a very useful technique for testing, since it allows dependencies to be mocked or stubbed out.

Dependency injection implements inversion of control through composition.

Dependency injection involves four roles:
- the service objects, which contain useful functionality;
- the interfaces by which those services are known to other parts of the code;
- the client object, whose behavior depends on the services it uses;
- the injector, which constructs the services and injects them into the client.

Types of DI:
- Constructor injection: The dependencies are provided through a client's class constructor.
- Setter injection: The client exposes a setter method that the injector uses to inject the dependency.
- Interface injection: The dependency's interface provides an injector method that will inject the dependency into any client passed to it.

Advantages:
- decoupling the creation of object (in other word, separate usage from the creation of object);
- ability to replace dependencies (eg: Wheel, Battery) without changing the class that uses it (Car) at runtime;
- promotes "Code to interface not to implementation" principle;
- ability to create and use mock dependency during test (if we want to use a Mock of Wheel during test instead of a real
 instance, we can create Mock Wheel object and let DI framework inject to Car);
- lower coupling and the possibility to reuse code;
- placing all patches to a method/function in a single place in our code (method/function signature).
"""
