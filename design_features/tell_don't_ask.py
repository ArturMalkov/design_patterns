"""
Tell, Don't Ask!

Asking the object about its state (i.e. checking its attributes), and then calling methods on that object based on decisions
made outside of the object, means that the object is now a leaky abstraction; some of its behavior is located outside
of the object, and internal state is exposed (perhaps unnecessarily) to the outside world.

You should endeavor to tell objects what you want them to do; do not ask them questions about their state, make a decision on their behalf,
and then tell them what to do. Let the object itself figure out how to do it (based on its internal state - it will do
check on its internal state itself).

As the caller, you should not be making decisions based on the state of the called object that result in you then changing
the state of the object. The logic you are implementing is probably the called object’s responsibility, not yours.
For you to make decisions outside the object violates its encapsulation.

In other words: don't ask for information to then use it - instead, simply tell other classes what to do (if that is possible)
"""