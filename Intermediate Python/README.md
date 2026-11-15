# Intermediate Python

This folder contains practical examples of Python features that become important once you move beyond basic variables, conditions, loops, and simple functions. The programs cover collections, flexible function arguments, functional programming tools, generators, file and JSON handling, exception handling, decorators, context managers, threads, and processes.

The examples are small and independent. Run one file at a time so that its output and behaviour are easy to understand.

## Learning map

| Area | Files | What you learn |
|---|---|---|
| Collections | `Lists.py`, `Tuple.py`, `Dictionary.py`, `Sets.py` | Choosing and manipulating Python data structures |
| Function flexibility | `Asterisk.py`, `Function Arguments.py` | Unpacking, default values, `*args`, `**kwargs`, scope, mutation |
| Functional tools | `lambda_map_filter.py` | Small anonymous functions and transforming/filtering data |
| Iteration | `iterators_generators.py` | Lazy values, `yield`, `next()`, memory-aware iteration |
| Resource and data handling | `file_handling.py`, `example.py`, `json.py`, `exception_handling.py` | Files, JSON, errors, cleanup |
| Reusable behaviour | `decorators.py`, `context_managers.py` | Wrapping functions and managing resources |
| Concurrency | `Threading.py`, `multithreading.py`, `Multiprocessing.py` | Threads, processes, locks, queues, process pools |
| Randomness | `Random_example.py` | Pseudorandom values, shuffling, reproducibility, secure randomness |

---

## 1. `Asterisk.py` | Repetition, argument unpacking, and extended unpacking

### Concept
The asterisk (`*`) has several related uses in Python. It can repeat sequences, collect extra positional arguments, unpack an iterable into positional arguments, and collect part of an iterable during assignment. Double asterisk (`**`) unpacks or collects keyword arguments.

### How this file works
- `[0] * 10` creates a list containing ten zeroes. `(1, 2) * 5` repeats a tuple pattern five times. The same repetition works with strings such as `"A" * 10`.
- `my_function(*args, **kwargs)` accepts any number of positional and named arguments. The first loop prints values collected in the tuple `args`; the second prints key-value pairs collected in the dictionary `kwargs`.
- `foo(*my_list)` expands the list into three positional arguments. A string can also be unpacked character by character. `foo(**my_dict)` passes dictionary values as named arguments, so its keys must match the function parameter names.
- `*beginning, last = numbers` stores all values except the final one in `beginning`, and the final value in `last`.
- `[*my_tuple, *my_set]` combines values from two iterables into a new list. A set has no guaranteed display order.

### Where it is used
Argument unpacking is common when forwarding arguments to another function, combining configuration values, passing data to APIs, and building flexible utility functions. Extended unpacking is useful when separating a header or final item from a sequence.

### Benefits
It reduces repetitive code, makes functions reusable with different inputs, and makes sequence transformations concise.

### Important points
- `*args` is a tuple; `**kwargs` is a dictionary.
- Keyword names supplied through `**kwargs` must match accepted parameter names unless the called function accepts arbitrary keyword arguments.
- The starred target in an assignment receives a list.

---

## 2. `Dictionary.py` | Key-value data storage

### Concept
A dictionary stores information as key-value pairs. Keys are unique and are used to retrieve their associated values.

### How this file works
- It creates dictionaries using both literal syntax (`{...}`) and the `dict()` constructor.
- `"name" in my_dict` checks whether a key exists before accessing it.
- Accessing a missing key with square brackets raises `KeyError`. The `try/except` block catches that error and prints a friendly message.
- The loops demonstrate iteration over the dictionary itself, `.keys()`, `.values()`, and `.items()`. The last form provides each key and value together.
- `dict_copy = dict_org` does not create a second dictionary. Both names refer to the same object, so changing one changes what is seen through the other.
- `dict_org.copy()` creates a shallow copy. Replacing a top-level value in the copy does not change the original dictionary.

### Where it is used
Dictionaries are used for user profiles, product details, configuration settings, API responses, JSON data, lookup tables, and counting or grouping records.

### Benefits
They provide readable access by meaningful keys and generally offer efficient average-case lookup, insertion, and deletion.

### Important points
- Keys must be hashable.
- `in` checks keys by default, not values.
- `.copy()` is shallow. Nested mutable objects are still shared between the original and the copy.

---

## 3. `Function Arguments.py` | Parameters, scope, and mutable arguments

### Concept
Functions receive information through parameters. Python supports required parameters, default values, extra positional arguments, and extra keyword arguments. This file also demonstrates variable scope and how mutable objects behave when passed to functions.

### How this file works
- `foo(a, b, c, d=4)` gives `d` a default value, so the function can be called with only three arguments.
- `foo1(a, b, *args, **kwargs)` accepts additional positional and keyword arguments and prints each group.
- `foo2()` reads the global variable `number`. Reading a global name does not require the `global` keyword.
- `foo3()` declares `global number` because it assigns a new value to the module-level variable.
- `foo4(a_list)` changes elements of the same list object. The caller sees those changes.
- `foo5()` uses in-place list extension with `+=`, which mutates the list. `bar()` creates a new list with `a_list + [4, 5]` and assigns it only to the local parameter, leaving the caller's list unchanged.

### Where it is used
Flexible parameters are useful in libraries, reusable utilities, wrappers, and functions that accept optional settings. Understanding scope and mutation is essential when writing functions that work with shared data.

### Benefits
Default arguments make calls shorter, `*args/**kwargs` make interfaces flexible, and a clear understanding of mutation prevents surprising side effects.

### Important points
- Avoid using mutable objects as default parameter values unless shared state is intentional.
- Use `global` sparingly; passing values and returning results is often easier to test.
- Assignment to a parameter does not normally rebind the caller's variable, but mutating the referenced object can be visible to the caller.

---

## 4. `Lists.py` | Mutable ordered collections

### Concept
A list is an ordered, mutable collection. It can store duplicate values and values of different types.

### How this file works
- `len()` returns the number of elements.
- `.append()` adds an element to the end; `.insert(index, value)` adds it at a chosen position.
- `.pop()` removes and returns an item (the last item when no index is supplied). `.remove(value)` removes the first matching value. `.clear()` removes all elements.
- `.reverse()` reverses the existing list in place.
- `.sort()` sorts the existing list in place. `sorted(my_list)` instead returns a new sorted list.
- Multiplication repeats a list, addition concatenates lists, and `list("Hello")` converts a string into a list of characters.

### Where it is used
Lists are useful for shopping carts, task queues, collections of records, search results, sensor readings, and data that changes while a program runs.

### Benefits
They are flexible, easy to iterate over, and support indexing, slicing, and many built-in operations.

### Important points
- In-place methods such as `.sort()`, `.reverse()`, and `.append()` modify the original list.
- `sorted()` returns a new list.
- `.remove()` raises `ValueError` if the value is absent; `.pop()` raises `IndexError` if the list is empty.

---

## 5. `Multiprocessing.py` | Parallel work with a process pool

### Concept
Multiprocessing runs work in separate operating-system processes. Each process has its own Python interpreter and memory space. A process pool manages a group of worker processes.

### How this file works
- It imports `Pool` from `multiprocessing`.
- `cube(number)` returns the cube of its input.
- Inside the `if __name__ == "__main__":` guard, the program creates a range of numbers and a pool.
- `pool.map(cube, numbers)` distributes the inputs across workers and collects results in input order.
- `close()` prevents new tasks from being submitted, and `join()` waits for workers to finish.
- The final list contains the cube of each number from 0 through 9.

### Where it is used
Multiprocessing is useful for CPU-heavy tasks such as image processing, scientific calculations, simulations, data transformation, and independent batch jobs.

### Benefits
It can use multiple CPU cores for CPU-bound work and can bypass the usual limitation of Python threads for executing Python bytecode in parallel in standard CPython builds.

### Important points
- Keep process creation under the main guard, especially on Windows and platforms that use spawn.
- Starting processes has overhead, so multiprocessing is not automatically faster for tiny tasks.
- The file imports several names that are not used in the current example; they can be removed without changing its demonstrated pool behaviour.

---

## 6. `Random_example.py` | Random values and secure randomness

### Concept
Python offers pseudorandom generation for simulations and ordinary program behaviour, plus a separate `secrets` module for security-sensitive random values.

### How this file works
- `random.shuffle(mylist)` shuffles the list in place. Its return value is `None`, so the list itself is printed.
- `random.seed(1)` sets a repeatable starting state. The following `random.random()` call produces a reproducible pseudorandom float for that seed and Python implementation.
- `secrets.randbits(4)` generates a security-oriented random integer using four bits.
- NumPy is imported as `np`, but the final line `a.np.random.rand(3)` is incorrect: `a` is an integer, and NumPy should be accessed through `np.random.rand(3)`. The result should be assigned to a separate variable if it needs to be printed.

### Where it is used
The `random` module is useful for games, simulations, sampling, and randomized testing. `secrets` is appropriate for password-reset tokens, authentication tokens, and other security-sensitive values. NumPy random functions are useful for numerical arrays and machine-learning experiments.

### Benefits
The modules provide different tools for reproducible experiments, randomized behaviour, and cryptographically stronger randomness.

### Important points
- Do not use `random` to generate passwords, API keys, or security tokens; use `secrets`.
- `shuffle()` changes the original list.
- Correct NumPy call: `np.random.rand(3)`.

---

## 7. `Sets.py` | Unique elements and set operations

### Concept
A set is an unordered collection of unique, hashable elements. Duplicate values are automatically removed.

### How this file works
- Sets are created with braces or the `set()` constructor. Passing a string to `set()` produces its distinct characters.
- `{}` creates an empty dictionary, not a set; `set()` creates an empty set.
- `.add()` inserts an element and `.remove()` deletes one. `.remove()` raises `KeyError` if the item is missing.
- `.union()` combines unique values. `.intersection()` finds common values.
- `.update()`, `.intersection_update()`, `.difference_update()`, and `.symmetric_difference_update()` modify the set in place.
- The final assignments demonstrate reference assignment and copying. `SetA = setB.copy()` creates a shallow copy, whereas `setA = setB` makes both names refer to the same set.

### Where it is used
Sets are useful for removing duplicate records, checking membership, comparing permissions, finding common interests, and comparing tags or categories.

### Benefits
They enforce uniqueness and provide efficient average-case membership checks and mathematical set operations.

### Important points
- Sets do not support indexing.
- Elements must be hashable.
- Use `.discard()` if you want to remove an element without an error when it is absent.

---

## 8. `Threading.py` | Threads, locks, and queues

### Concept
A thread is a path of execution inside a process. Threads share process memory, which makes communication convenient but can create race conditions when multiple threads update shared data.

### How this file is intended to work
- `square_numbers()` performs a simple loop. The main block creates ten `Thread` objects, starts each one, and calls `join()` to wait for completion.
- The shared `database_value` example starts two threads that both increment a shared variable. A lock is intended to protect the read-modify-write operation.
- The `Queue` example inserts three values with `put()`, retrieves one with `get()`, and uses `task_done()` and `join()` to track task completion.

### Important correction in the current code
The lock section contains two problems: `with lock:` already acquires the lock, so calling `lock.aquire()` inside it is unnecessary and the method is misspelled (`acquire`, not `aquire`). With a normal non-reentrant `Lock`, acquiring it again from the same thread can block forever. Use either `with lock:` alone or explicit `lock.acquire()` with a matching `lock.release()` in a `finally` block. Also, the queue example calls `q.join()` after retrieving only one of three queued items; the remaining tasks are never marked complete, so the program can wait indefinitely. Consume and acknowledge every item, or use a queue example with only one item.

### Where it is used
Threads are useful for I/O-bound work such as network requests, file operations, background tasks, and keeping user interfaces responsive.

### Benefits
Threads share memory easily and can overlap waiting time, improving responsiveness for I/O-heavy applications.

### Important points
- Protect shared mutable state with a lock.
- Always balance every successful queue `get()` with `task_done()` when using `join()`.
- Threads are not generally the best way to speed up CPU-bound Python code in standard CPython.

---

## 9. `Tuple.py` | Immutable ordered collections

### Concept
A tuple is an ordered collection that cannot be structurally changed after it is created. It can contain duplicate values and different data types.

### How this file works
- It creates tuples with parentheses and also demonstrates that parentheses can be omitted in tuple packing.
- `(25,)` shows the comma required to create a one-element tuple.
- `tuple([...])` converts an iterable into a tuple.
- `len()`, `.count()`, and `.index()` inspect tuple contents.
- Multiplication repeats a tuple, addition concatenates tuples, and the final examples convert between lists, tuples, and strings.

### Where it is used
Tuples are useful for fixed records, coordinates, RGB colours, database rows, and returning multiple values from functions.

### Benefits
Their immutability communicates that a collection should not be structurally modified and allows tuples containing hashable values to be used as dictionary keys or set elements.

### Important points
- A tuple is immutable, but it can contain a mutable object whose contents can still change.
- A one-element tuple requires a trailing comma.
- Use a list when the collection needs frequent modification.

---

## 10. `context_managers.py` | Reliable resource management

### Concept
A context manager controls setup and cleanup around a block of code. The `with` statement ensures cleanup runs when the block exits, including when an exception occurs.

### How this file works
- `@contextmanager` from `contextlib` turns a generator function into a context manager.
- The code before `yield` represents setup and prints that the resource is acquired.
- The yielded string is made available through the `resource` variable in the `with` block.
- The `finally` section runs when the block exits and prints that the resource is released.
- The final message runs after the context has closed.

### Where it is used
Context managers are used for files, database connections, locks, temporary resources, transactions, and temporary changes to program state.

### Benefits
They make cleanup predictable, reduce resource leaks, and keep setup and teardown logic together.

### Important points
- Code before `yield` is setup; code in `finally` is cleanup.
- A context manager should release resources even when the managed block raises an exception.
- Python file objects already support `with open(...)`.

---

## 11. `decorators.py` | Extending a function without rewriting it

### Concept
A decorator is a callable that takes a function and returns a replacement or wrapped function. It adds behaviour around an existing function.

### How this file works
- `execution_timer(function)` receives the original function.
- Its inner `wrapper(*args, **kwargs)` accepts the same kinds of arguments and prints a message before and after calling the original function.
- The wrapper stores the original return value and returns it to the caller.
- `@execution_timer` is shorthand for replacing `calculate_total` with `execution_timer(calculate_total)`.
- `functools.wraps` preserves useful metadata such as the original function's name and docstring. The calls to `help()` and `__name__` demonstrate this.

### Where it is used
Decorators are common in web frameworks for routes and authentication, logging, caching, timing, validation, retries, and access control.

### Benefits
They separate cross-cutting behaviour from the core function logic and allow the same behaviour to be reused.

### Important points
- The wrapper should return the original function's result when that result matters.
- `functools.wraps` helps preserve metadata.
- This example prints start and completion messages; despite its name, it does not actually measure elapsed time.

---

## 12. `example.py` | JSON serialization and deserialization

### Concept
JSON (JavaScript Object Notation) is a text format for exchanging structured data. Python's `json` module converts between Python objects and JSON text or files.

### What the file demonstrates
- The `person` dictionary contains strings, an integer, a Boolean, and a list.
- `json.dumps(person, indent=4)` serializes the dictionary into a formatted JSON string.
- The file then opens `person.json` and attempts to read JSON data.

### Important correction in the current code
The current call `json.load(personJSON)` is incorrect because `json.load()` expects a file-like object, not the JSON string created by `dumps()`. Also, the file is opened in read mode, so it must already exist and contain valid JSON. To read the string, use `json.loads(personJSON)`. To write and then read the file, use `json.dump(person, file, indent=4)` with a file opened in write mode, followed by `json.load(file)` in a separate read block.

### Where it is used
JSON is widely used in REST APIs, configuration files, browser-server communication, application settings, and data exchange between different programming languages.

### Benefits
It is human-readable, language-independent, and maps naturally to common data structures.

### Important points
- `dumps()` converts a Python object to a JSON string; `loads()` parses a JSON string.
- `dump()` writes JSON to a file; `load()` reads JSON from a file.
- JSON has a limited set of data types; custom Python objects need explicit conversion.

---

## 13. `exception_handling.py` | Handling invalid input safely

### Concept
Exceptions are runtime errors or unusual conditions that interrupt normal program flow. Python uses `try`, `except`, `else`, and `finally` to handle them.

### How this file works
- The program asks the user for an age and converts the input to an integer.
- If conversion fails, Python raises `ValueError`.
- The program also explicitly raises `ValueError` when the age is negative.
- Ages below 18 receive an eligibility message; other valid ages receive a successful registration message.
- The `except` block catches the invalid-value error and displays its message.
- The `finally` block runs whether the input is valid or invalid.

### Where it is used
Exception handling is important in form validation, file operations, network requests, database access, payment workflows, and any application that receives unpredictable input.

### Benefits
It prevents expected errors from abruptly terminating the application and allows meaningful feedback or recovery.

### Important points
- Catch specific exceptions where possible.
- Do not silently ignore errors that need attention.
- `finally` is appropriate for cleanup or actions that must always happen.

---

## 14. `file_handling.py` | Reading and writing text files

### Concept
File handling allows a program to store information beyond the lifetime of a running process. Python's `open()` function provides access to files.

### How this file works
- The program defines a filename and a list of shopping items.
- Opening with mode `"w"` creates or overwrites the file. Each item is written on a separate line.
- The file is reopened in mode `"r"` and each line is read and displayed. `.strip()` removes the trailing newline and surrounding whitespace.
- Mode `"a"` appends a new item without replacing existing contents.

### Where it is used
Text files are used for logs, simple records, exports, reports, configuration, and data exchange.

### Benefits
Files provide persistent storage and allow programs to process data incrementally.

### Important points
- `"r"`: read, `"w"`: write/overwrite, `"a"`: append.
- The `with` statement closes the file automatically.
- For larger or structured datasets, consider CSV, JSON, or a database.

---

## 15. `iterators_generators.py` | Lazy iteration with yield

### Concept
An iterator produces values one at a time. A generator is a convenient way to create an iterator using a function containing `yield`. It pauses at each yield and resumes when the next value is requested.

### How this file works
- `countdown(start)` yields the current number and decreases it until it reaches zero.
- `square_generator(values)` yields the square of each input value.
- `mygen()` shows a generator with three explicit yield statements.
- `next(cd)` requests one value at a time from a countdown generator. Each call resumes execution from the previous yield.
- `fibonacci(n)` yields Fibonacci numbers while the current value is below the limit.
- A generator expression and a list comprehension both select even numbers, but the generator expression produces values lazily while the list stores all selected values immediately.
- `sys.getsizeof()` reports the shallow size of the generator object or list object, not the complete memory footprint of all referenced data.

### Where it is used
Generators are useful for reading large files, processing data streams, pagination, pipelines, and producing values that do not need to exist in memory all at once.

### Benefits
They can reduce memory usage, support streaming, and make data-processing pipelines easier to compose.

### Important points
- A generator is usually exhausted after iteration.
- Calling `next()` after exhaustion raises `StopIteration`.
- `yield` pauses a function; `return` ends it.
- The memory-size comparison in this file is illustrative, not a complete measurement of total memory consumption.

---

## 16. `json.py` | Reserved practice file

This file is currently empty. It is a natural place to add focused examples of the `json` module, such as encoding dictionaries with `json.dumps()`, writing with `json.dump()`, parsing strings with `json.loads()`, and reading files with `json.load()`.

No executable behaviour is present in the current file, so there is no output to describe yet.

---

## 17. `lambda_map_filter.py` | Functional transformations

### Concept
A lambda is a small anonymous function. `map()` applies a function to every element of an iterable, while `filter()` keeps only elements for which a condition is true.

### How this file works
- `employees` stores employee names and monthly salaries as tuples.
- `map(lambda emp: (emp[0], emp[1] * 12), employees)` creates name and annual-salary pairs.
- `filter(lambda emp: emp[1] >= 35000, employees)` keeps employees whose monthly salary meets the threshold.
- A second `map()` calculates a 10% bonus for each employee.
- `list()` materializes the results so they can be printed and reused.

### Where it is used
These tools are useful for transforming records, filtering datasets, preparing reports, and writing concise data pipelines.

### Benefits
They express common transformations compactly and work with many iterable types.

### Important points
- A lambda contains one expression, not a block of statements.
- In Python 3, `map()` and `filter()` return iterators; converting to `list` consumes them.
- For complex logic, a named function or list comprehension may be easier to read.

---

## 18. `multithreading.py` | Multiple processes and a comparison with threads

### Concept
The active code demonstrates multiprocessing, while a triple-quoted section contains an example of threading. Processes have separate memory spaces; threads share memory within one process.

### How this file works
- The commented-as-a-string example imports `threading`, defines number and letter printing functions, starts two threads, and waits for both with `join()`. Because it is inside a triple-quoted string, it is not executed.
- The active `square_numbers()` function performs a simple calculation loop.
- The main guard creates a list of `Process` objects based on `os.cpu_count()`.
- Each process is started, then the main program waits for all processes to finish.
- The final message is printed after all child processes have joined.

### Where it is used
Multiprocessing is useful for CPU-intensive independent work. Threading is useful for I/O-bound tasks where work often waits for files, networks, or other resources.

### Benefits
Processes can run Python CPU work across multiple cores. Threads can overlap waiting operations with lower startup and communication overhead.

### Important points
- The active example creates processes, not threads, despite the filename.
- The calculation result is not stored or displayed, so this is mainly a process-creation and synchronization demonstration.
- Creating as many processes as CPU cores is not always optimal; the right number depends on task size and system resources.

---

## 19. `Threading.py` vs `multithreading.py` vs `Multiprocessing.py`

These files cover related but distinct approaches:

| Approach | Memory model | Best suited for | Example in this folder |
|---|---|---|---|
| Threading | Threads share process memory | I/O-bound concurrent tasks | `Threading.py` |
| Multiprocessing | Processes have separate memory | CPU-bound parallel tasks | `Multiprocessing.py`, active part of `multithreading.py` |
| Process pool | Managed worker processes | Applying one function to many inputs | `Multiprocessing.py` |

## Running the examples

From the repository root, quote folder and file names that contain spaces:

```bash
python "Intermediate Python/Lists.py"
python "Intermediate Python/Function Arguments.py"
python "Intermediate Python/exception_handling.py"
```

For the age-validation example, enter an integer when prompted. The multiprocessing examples should be run as standalone scripts.

## Overall learning outcomes

After working through this folder, you should be able to:
- Select an appropriate Python collection for a task.
- Write flexible functions and understand argument passing, scope, and mutation.
- Transform and filter data with functional tools.
- Build iterators and generators for lazy processing.
- Read and write files and exchange structured JSON data.
- Handle runtime errors and manage resources safely.
- Use decorators to add reusable behaviour to functions.
- Understand when to use threads, processes, locks, queues, and process pools.

## Notes on the current examples

A few files are practice snippets and contain issues worth understanding rather than copying blindly:
- `Random_example.py`: the NumPy expression should use `np.random.rand(3)`, not `a.np.random.rand(3)`.
- `Threading.py`: the lock is acquired twice and the queue is not fully acknowledged, which can cause the program to hang.
- `example.py`: `json.load()` is given a string instead of a file object, and the file is opened for reading without first being created by this program.
- `decorators.py`: the decorator demonstrates before/after messages, not elapsed-time measurement.
- `json.py`: currently empty.

These notes describe the code as it exists and identify the behaviour that should be corrected when you revisit the examples.
