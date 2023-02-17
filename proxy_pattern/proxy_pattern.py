"""
Proxy pattern is a class that functions as an interface for accessing a particular resource.
That resource may be remote, expensive to construct, or may require logging or some other added functionality.
Proxy pattern provides a surrogate/placeholder for another object to control access to it.
I.e. you interact with some object indirectly, i.e. through a proxy (which forwards call to the real object).
Introducing a level of indirection - you call a thing that calls a thing you want.

Adds additional behavior with the intent of controlling access to the underlying object.

3 versions:
- remote proxy (responsible for interacting with a remote resource - on a server, a different module, etc.);
- virtual proxy (controls access to a resource that is expensive to create/instantiate - you interact with a proxy instead - and
if gives you the access to the object when you really need it - to defer the expensive operation, make it lazy by
sticking proxy in between (controls access to the instantiation of an expensive object));
- protection proxy (access management based on access rights - makes sure only authorized users get access to a resource).

It doesn't change the interface. You simply intersect the accessing of a particular object for some reason -
security, caching, etc. It delays the instantiation of the resource until it knows that you actually do need the resource.

Client -> Proxy -> Resource

The proxy asks the resource for the value the first time, but then assumes that the value will stay the same in the
future (i.e. caches it).
Proxy is interchangeable with the thing it is proxying:
- A proxy has the same interface as its underlying object.
- To create a proxy, simply replicate the existing interface of an object.
- Add relevant functionality to the redefined member functions.
"""
