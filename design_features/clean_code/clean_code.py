"""
Clean Code - a code that is readable and easy to understand.

Clean Code should:
- be readable and meaningful;
- reduce cognitive load;
- be concise and "to the point";
- avoid unintuitive names, complex (deep) nesting and big code blocks;
- follow common best practices and patterns.


Clean Code rules:

Naming is the most important thing:
- names of variables must be meaningful and self-explanatory (descriptive);
- names must be concise and specific (avoid redundant information);
- names mustn't be confusing (should correspond to their roles/contents) (+ do not use slang and disinformation);
- names must be pronounceable (avoid abbreviations and deletion of vowels);
- do not use prefixes for names of objects within same module (it makes it more difficult to search by name);
- do not replace parts of a word with numbers (e.g. kubern8s);
- classes' and variables' names should be nouns (or short phrases with adjectives) (name is to be defined by contents - attributes,
not by behavior (task) like in methods), functions'/methods' names - verbs (or short phrases with adjectives);
- use same names for same things (one concept - one name - consistency) (+different names for different things - distinctive names);
- use terminology from subject area;
- include names in the context ('state' attribute within the class 'Address' vs 'state_address' as a standalone variable).

Methods'/functions' requirements:
- should be concise (up to 10 lines - one screen in practice);
- should be responsible for one thing only (no "and" in method's name);
- one level of abstraction for the method (analogy - Google Maps - country -> cities -> city -> street -> home - do not
mix these layers!) (e.g. do not mix low-level built-in operations with high-level developer-defined functions - functions
should only do work that's one level of abstraction below the level of abstraction implied by their names and their names
can add interpretation to this low-level code they contain (there should be no big gaps between function name and actual
code)) (high-level functions define steps to be executed to achieve a final result BUT the actual work that needs to be
done (lower-level operations) are outsourced to other (low-level) functions);
- do not use 'switch' operator in C-like languages;
- ideally 0 parameters in a method (up to 3 parameters - if more, group multiple parameters into one parameter - create
a parameter object which accepts those parameters as its attribute values (data container - e.g. a dict, an object))
(the number and order of arguments matters - calling the function should be readable as well);
- do not use flags (boolean value which defines method's behavior);
- try keeping functions pure: i) the same input should always yield the same output (same return value for the same arguments) (more predictability),
ii) they should have no side effects (i.e. operations which do not just act on function inputs and change its output but
which instead change the overall system/program state (incl changes in the outside code)) (especially when following functional programming approach) -
side effects are not automatically bad but unexpected side effects should be avoided - i.e. functions should do only
what's been explicitly specified and nothing else (whenever a function is impure, its name should signal or imply that
a side effect is likely to occur);
- shouldn't use passed argument as a result (shouldn't mutate passed in arguments and return changed arguments - you should
mutate and return a copied object instead);
- command-query separation (either do smth or return smth);
- put guard clause at the very beginning (not the end) of a method - if some condition is not met, return (or raise exception)
immediately - 'fail fast' (method's body (main code) should follow below - it won't be placed inside the 'if' statement
and, therefore, will be easier to read (minus one level of nesting)) (a good indicator for a guard is an 'if' statement
with a lot of code inside of it and 'else' statement with some error message).

Comments' requirements (most comments are bad - avoid them!):
Good comments:
- legal information (e.g.: copyright info, etc.);
- explain behavior of your code when necessary (especially if some business logic is counterintuitive);
- explain your intentions when necessary (especially if some business logic is counterintuitive);
- explain difficult parts of your code (e.g. complex business logic, regexes, etc.);
- notify of the consequences of certain further actions on your code/warnings;
- use a method or a variable instead of a comment;
- TODO (to indicate places needing improvements in future - checklist for the future of the technical debt).

Bad comments:
- comments for the sake of themselves;
- excessive (obvious) comments;
- misleading comments (changes in code must be accompanied by updates in comments);
- comments representing a journal of changes (e.g. last changes made by X at Y...);
- using dividers/block markers (e.g. '===* ... *===');
- commented out code - delete it!
- info about a system in a local comment;
- too much info;
- unclear comments.

Formatting (both vertical and horizontal) - very important!:
- use newspaper article metaphor - vertical order (header (variable name, docstring), content (most important ->
least important (e.g. constructor -> public methods -> private methods)));
- spaces between different concepts (one-two blank lines) (grouping of code) (+ consider splitting files with multiple
concepts (e.g. classes) into multiple files (e.g. one class per file)), similar concepts should not be separated by
spacing (blank lines) + related concepts should be kept close to each other (code should be readable like an essay
- top to bottom without too many "jumps") (i.e. keep related concepts together (vertical density) and separate concepts
which are not closely related (vertical distance));
- vertical distance (it's recommended to avoid it);
- line length - 80 - 100 - 120 (should be the same for one team - partly because of merge conflicts) - lines of code should
be readable without scrolling (break long statements into multiple shorter ones) - add line breaks to improve readability;
- alignment;
- avoid one-line if's and functions;
- use team-wide code styles.

Classes:
- should be short (up to 10 methods - each of which is up to 10 lines);
- SRP (Single Responsibility Principle) (not the same as "does one thing" principle for functions/methods);
- axis of change should be isolated (isolation of changes);
- OCP (Open-closed principle);
- Boy Scout rule - “Always leave the campground cleaner than you found it”;
- do not mix 'real' classes with 'data containers' (DTO - used only to store and transport data):
    - 'real' classes hide their internals (by making them private) and just expose public API (methods with high level of
     abstraction) (which allows you to do certain things with an object), abstractions over concretions are preferred
     (we want to expose methods which define a certain task that should be done and then we don't care how exactly an object
     executes that task - we just tell that object to do it);
    - 'data containers' internals are made available publicly (there's almost no public API besides that), concretions only
    (no high-level methods, only concrete data that can be utilized/accessed in all places where we have access to that 'data
    container' - so we don't tell the 'container' to do something, we directly use it however we need to use it).
- follow the 'Law of Demeter' when working with 'real' objects.

System:
- separate start of the system (initialization of objects, connections, assigning default values) from its usage -
start of the system can be even moved to a separate Python script;
- using factories;
- allow room for further scaling.


P.S.: Keep your control structures (if-else blocks, loops, etc.) clean:
- avoid deep nesting (e.g. by using guards or by extracting control structures into separate functions);
- use factory functions & polymorphism (to avoid duplicate 'if' checks);
- prefer positive checks (e.g. 'if is_empty' vs 'if is_not_empty');
- utilize errors (embrace errors & error handling - throwing and handling errors can replace 'if' statements and lead to
more focused functions (but keep in mind that error handling is a separate responsibility in itself (so comply with SRP))).


Simple Design Rules - Kent Beck:
- you can launch all tests;
- there are no repetitions in your code;
- your code expresses your intention;
- least possible number of classes and methods.
"""