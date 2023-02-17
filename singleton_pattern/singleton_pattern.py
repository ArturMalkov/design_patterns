"""
Singleton - a component which is instantiated only once (meaning everyone works with the same instance in different parts
of the program).

Considered a code smell by many - thus, it is to be avoided:
- avoid globals (i.e. leaking to the global namespace) (difficult to control changes);
- you can't be sure you won't need more instances of a particular class;

Ensures a class has only one instance and provides global point of access to it (you always get the same instance).

Motivation:
- for some components it only makes sense to have one in the system (database repository, object factory, cache,
connection pool, logging system, authentication system, config object, etc.)
- the initializer call is expensive
- need to prevent anyone from creating additional copies
- need to take care of lazy instantiation
"""


class Database:
    _instance = None  # points to singleton pattern (by convention)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


database_1 = Database()
database_2 = Database()
print(database_1 is database_2)
