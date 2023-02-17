"""
When you're about to instantiate a class, let's encapsulate that instantiation so that we can make it uniform in all
the places.  You call the factory whenever you want to instantiate objects.  The factory is responsible for
instantiating objects properly.
'Wrapper' around instantiation.
E.g. - needed when instantiation itself is a complex process - we need to calculate arguments passed to the object,
encapsulate business logic of creation objects, etc.
E.g. - when random creation is required.
etc.
Factory defines an interface for creating objects but lets its subclasses decide which classes to instantiate (and what
to pass to a class which it instantiates).

Based on parameters passed to it, factory makes decisions.

Creator -> ConcreteCreator(Creator)
Product -> ConcreteProduct(Product)
"""
