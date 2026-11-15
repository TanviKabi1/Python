# Asterisk

Documentation for `Asterisk.py`.

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

## Source code

See [`Asterisk.py`](./Asterisk.py) in this folder.
