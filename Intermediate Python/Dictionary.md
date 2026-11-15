# Dictionary

Documentation for `Dictionary.py`.

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

## Source code

See [`Dictionary.py`](./Dictionary.py) in this folder.
