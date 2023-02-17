"""
Command-Query Separation (CQS) - initially formulated by Bertrand Meyer.
You should separate your queries from your commands - methods shouldn't mix query operations with command operations.

Query - a method that asks for some info.
Command - a method that performs some action.

Queries do not cause mutation of the state of your application whereas commands do.
Separate methods that mutate the state of your application from methods that don't.

"Asking a question should not change the answer".

Popping from a stack is an edge case - it both removes and returns uppermost element in the stack.
"""