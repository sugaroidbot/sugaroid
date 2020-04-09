# Sugaroid Core

This is the directory of modules that sugaroid scans. All modules are called `Adapters`. 
Sugaroid scans each adapter by a set of operations, namely `can_process` and `process`.

## `Adapter.can_process`
The `can_process` is an object method, that helps to identify the `SugaroidStatement` or simply 
the input statement can be processed in the first place. It uses **brute force** to filter out
the unwanted statements by returning a Boolean Value `False` if it cannot be processed else
`True`. These algorithms are tried to kept as simple as possible to reduce execution time.
If `can_process` returns a positive boolean integer, the `process` block is executed

## `Adapter.process`
The `process` is a complex set of algorithms that can help to assign a valid confidence number 
to the `SugaroidStatement` that is returned. The chatbot instance scans through all of the classes
and then selects the `SugaroidStatement` with the highest confidence as the best or most closest 
answer. The `process` returns a `SugaroidStatement`. The text of the object is returned to the CLI
/ GUI / WEB wrappers respectively.

## `sugaroid.brain.neuron`
Neuron is the Arithmetic Logic Unit of Sugaroid. It tells which adapters are to be targeted, or gives
quick responses to some predefined adapters like `time`. The Neuron preprocesses the input statement
and removes all types of slang, jargon, as well ICP accepted Internet shorthands. As `Sugaroid` bot 
processes all statements with proper grammar only, the bot cleans the statement an replaces the 
compact words with the full forms appropriately. 


