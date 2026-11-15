# Object Oriented Programming (OOP)

This folder contains small Python programs that introduce Object-Oriented Programming. OOP organises a program around objects that combine data (attributes) and behaviour (methods). The examples use familiar entities such as products, employees, hospitals, vehicles, and animals to demonstrate how classes model real-world concepts.

Run each file independently. Most examples define their own classes and create a few objects to demonstrate one concept.

## Learning map

| Concept | File |
|---|---|
| Classes, objects, and methods | `classes_and_objects.py` |
| Constructors and validation | `constructors_and_methods.py` |
| Class and instance variables | `class_and_instance_variables.py`, `Class Attributes.py` |
| Encapsulation | `encapsulation.py` |
| Inheritance and reuse | `inheritance.py`, `multiple_inheritance.py` |
| Abstraction | `abstraction.py` |
| Polymorphism | `polymorphism.py` |
| Composition | `composition.py` |
| Method overloading pattern | `method_overloading.py` |
| Operator overloading | `operator_overloading.py` |
| Static and class methods | `static_and_class_methods.py` |
| Empty practice file | `rough.py` |

---

## 1. `classes_and_objects.py` | Creating classes and objects

### Concept
A class is a blueprint that defines the attributes and methods its objects can use. An object is an instance created from that class. Methods describe behaviour associated with an object.

### How this file works
- `class Item` defines an `Item` class.
- `calculate_total_price(self, x, y)` is an instance method. Python supplies the object as `self` when the method is called through an instance.
- `item1 = Item()` and `item2 = Item()` create two separate objects.
- The program assigns each object's `name`, `price`, and `quantity` attributes.
- It calls the method with each object's price and quantity, returning the product of those values.

### Where it is used
Classes and objects are used to represent customers, orders, products, accounts, vehicles, users, and components in larger applications.

### Benefits
They group related data and behaviour, make programs easier to organise, and allow multiple independent instances to follow the same structure.

### Important points
- `self` refers to the current object.
- In this example, the method receives price and quantity as explicit arguments. A later example stores them in the object and calculates using `self.price` and `self.quantity`.
- Python allows attributes to be added dynamically, but defining expected attributes in `__init__` generally makes a class easier to understand.

---

## 2. `constructors_and_methods.py` | Initialising objects with __init__

### Concept
A constructor-style initialisation method sets up an object's starting state. In Python, `__init__` is called automatically after a new instance is created.

### How this file works
- `Item.__init__(self, name, price, quantity=0)` receives the values needed to initialise an item. Quantity defaults to zero.
- Two `assert` statements check that price and quantity are not negative.
- The values are stored in instance attributes: `self.name`, `self.price`, and `self.quantity`.
- `calculate_total_price()` uses the object's own attributes and returns price multiplied by quantity.
- Two Item objects are created and their totals are printed.

### Where it is used
Initialisation is used whenever objects need valid starting data, such as creating a bank account, shopping-cart item, student record, or booking.

### Benefits
It ensures objects are ready to use immediately after creation and keeps setup logic in one place.

### Important points
- `__init__` is an initialiser, not technically the method that creates the object; `__new__` handles object creation.
- `assert` is useful for learning and internal assumptions, but it can be disabled with Python optimisation. Production validation should generally use explicit checks and raise an appropriate exception such as `ValueError`.
- Type hints such as `name: str` document expected types but do not enforce them at runtime.

---

## 3. `class_and_instance_variables.py` | Shared data vs object-specific data

### Concept
An instance variable belongs to an individual object. A class variable is stored on the class and is shared by its instances unless an instance shadows it with its own attribute.

### How this file works
- `hospital_name` and `patient_count` are class attributes defined directly inside `Hospital`.
- `name` and `room` are instance attributes created through `self` inside `__init__`.
- Every time a patient object is created, `Hospital.patient_count += 1` updates the shared count.
- `show_patient()` prints the shared hospital name along with that particular patient's details.
- Two patient objects are created, displayed, and the shared count is printed.

### Where it is used
Class attributes are useful for shared configuration, constants, default settings, and tracking a count of instances. Instance attributes store each record's individual details.

### Benefits
The distinction avoids duplicating shared values and makes object-specific information independent.

### Important points
- Updating a mutable class attribute can affect every instance that uses it.
- Use `self.attribute` for per-object state and `ClassName.attribute` for explicitly shared state.
- A class-level counter can be useful, but in a multi-threaded application it may need synchronisation.

---

## 4. `Class Attributes.py` | Class-level state, validation, and object representation

### Concept
This example builds on class attributes and instance attributes. It also demonstrates validation with assertions, a class-level collection of created objects, a discount rate, and a custom representation method.

### How this file works
- `pay_rate = 0.8` is a class attribute representing an 80% price multiplier.
- `all = []` is a class-level list intended to collect every created `Item`.
- `__init__` checks that price and quantity are non-negative, then stores the object's name, price, and quantity.
- `Item.all.append(self)` adds the newly created object to the shared list.
- `calculate_total_price()` returns price multiplied by quantity.
- `apply_discount()` multiplies the instance's price by `self.pay_rate`. Since the instance does not define its own `pay_rate`, it reads the class attribute.
- `__repr__()` returns a developer-friendly string representation.
- Five objects are created and the shared list is printed. Python uses `__repr__` for each object in that list.

### Where it is used
This pattern is useful in inventory systems, product catalogues, order management, and small object registries.

### Benefits
A shared class-level list provides a simple way to inspect created instances, while a class-level rate provides a common default.

### Important points
- `all` is shared by all instances. It should not be confused with a per-object list.
- A discount method changes the object's stored price. Calling it more than once applies the discount repeatedly.
- Consider naming the list `all_items` to avoid shadowing Python's built-in `all()` function.
- Assertions are useful for demonstrations; explicit exceptions are more reliable for production validation.

---

## 5. `encapsulation.py` | Protecting internal object state

### Concept
Encapsulation groups data and methods together and controls how an object's internal state is accessed or modified. Python uses naming conventions rather than strict private access modifiers.

### How this file works
- The `Product` class stores a public `product_id` and a name-mangled attribute named `__price`.
- `update_price()` is the controlled update method. It changes the price only when the new value is positive.
- `get_price()` provides a way to read the current price.
- `show_product()` displays the product ID and internal price.
- The program creates a product, displays it, updates its price, and retrieves the updated value through the getter.

### Where it is used
Encapsulation is useful for bank balances, account permissions, product prices, user settings, and any state that should only change through validation rules.

### Benefits
It reduces accidental changes, keeps validation close to the data, and gives a class control over how its state changes.

### Important points
- A double underscore triggers name mangling, not absolute privacy. It mainly helps avoid accidental name clashes.
- A single leading underscore is the conventional signal that an attribute is intended for internal use.
- Properties (`@property`) are another Pythonic way to provide controlled attribute access.

---

## 6. `inheritance.py` | Reusing and extending a parent class

### Concept
Inheritance allows a child class to reuse attributes and methods from a parent class and add specialised behaviour. The child class in this example is `Phone`, and the parent class is `Item`.

### How this file works
- The parent `Item` class defines shared data such as name, price, quantity, and a class-level discount rate.
- Its constructor validates price and quantity and appends each created item to `Item.all`.
- `calculate_total_price()` and `apply_discount()` provide common item behaviour.
- `instantiate_from_csv()` is a class method that reads rows from `items.csv` using `csv.DictReader`, converts price and quantity to numeric types, and creates Item objects.
- `is_integer()` is a static method that checks whether a value is an integer or a float with no fractional part.
- `__repr__()` formats an object using its actual class name.
- `Phone(Item)` declares Phone as a subclass of Item.
- `super().__init__(name, price, quantity)` calls the parent initialiser so the Phone receives the common Item attributes and is added to the shared list.
- Phone then validates and stores its additional `broken_phones` attribute.
- The final statement creates one Phone and prints the shared Item registry.

### Where it is used
Inheritance is useful when several types share common data and behaviour, such as different products, employee roles, payment methods, or vehicle types.

### Benefits
It reduces duplicated code, provides a natural parent-child structure, and allows specialised classes to extend a common interface.

### Important points
- `super()` calls the next implementation in Python's method resolution order.
- The CSV method expects an `items.csv` file in the program's current working directory with columns named `name`, `price`, and `quantity`.
- The current example defines `instantiate_from_csv()` but does not call it.
- The child class inherits methods such as `calculate_total_price()` and `apply_discount()`.

---

## 7. `abstraction.py` | Defining required behaviour

### Concept
Abstraction exposes what an object should do while hiding the details of how it does it. Python's `abc` module supports abstract base classes and abstract methods.

### How this file works
- `Vehicle(ABC)` defines an abstract base class.
- The `@abstractmethod` decorator marks `start()` as a method that concrete subclasses must implement.
- `Bike` implements the method with a key-start message.
- `ElectricCar` implements it with a button-start message.
- A list stores one object of each concrete class, and a loop calls the common `start()` interface.

### Where it is used
Abstraction is useful for payment gateways, storage providers, notification systems, database adapters, and other systems where different implementations should follow the same contract.

### Benefits
It encourages consistent interfaces, makes implementations interchangeable, and separates high-level usage from implementation details.

### Important points
- You cannot normally instantiate a class while it still has unimplemented abstract methods.
- Each concrete subclass provides its own implementation.
- The caller can use the shared method without needing to know the internal starting mechanism.

---

## 8. `composition.py` | Building objects from other objects

### Concept
Composition models a has-a relationship. One object contains and uses another object as one of its components.

### How this file works
- `Battery` defines a `charge()` method.
- `Smartphone.__init__()` stores the model and creates a Battery object as `self.battery`.
- `use_phone()` displays the model, calls the battery's `charge()` method, and prints a final status.
- A Smartphone object is created and its method is called.

### Where it is used
Composition is common in software systems such as a car containing an engine, a computer containing a processor, an order containing line items, or a page containing UI components.

### Benefits
It builds complex behaviour from smaller reusable components and often creates more flexible designs than deep inheritance hierarchies.

### Important points
- In this example, the Smartphone creates and owns its Battery object.
- Composition is a has-a relationship; inheritance is an is-a relationship.
- A component can be replaced or expanded without making it a parent class.

---

## 9. `constructors_and_methods.py` and `classes_and_objects.py` | How the examples build on each other

The first class example creates objects and assigns attributes after construction. The constructor example moves that setup into `__init__`, so every Item is initialised consistently. It also changes the calculation method to use the object's own attributes. This progression illustrates why constructors make classes safer and easier to reuse.

---

## 10. `method_overloading.py` | One method name with different argument patterns

### Concept
In some languages, method overloading means defining several methods with the same name but different parameter signatures. Python does not support traditional signature-based method overloading directly. A common Python approach is to use default parameters or flexible arguments.

### How this file works
- `calculate_area(self, length, width=None)` always receives a length.
- If width is omitted, the method treats the shape as a circle and calculates `3.14 * length * length`.
- If width is provided, it calculates the area of a rectangle using `length * width`.
- The two calls demonstrate the two supported input patterns.

### Where it is used
This approach is useful when one operation can reasonably accept different forms of input, such as formatting, geometry calculations, optional configuration, or flexible utility functions.

### Benefits
It keeps related operations under one method name and avoids duplicating similar logic.

### Important points
- This is conditional behaviour based on an optional parameter, not traditional compile-time method overloading.
- For more complex cases, consider explicit separate methods, keyword-only arguments, or type-based dispatch with `functools.singledispatch`.

---

## 11. `multiple_inheritance.py` | Inheriting from more than one parent

### Concept
Multiple inheritance allows a class to inherit behaviour from multiple parent classes. It is useful when a class combines independent capabilities.

### How this file works
- `Camera` provides `take_photo()`.
- `MusicPlayer` provides `play_music()`.
- `SmartPhone(Camera, MusicPlayer)` inherits from both classes.
- Its `show_features()` method calls both inherited methods.
- A SmartPhone instance is created and asked to display its features.

### Where it is used
Multiple inheritance can represent mixin-based capabilities, such as logging, serialization, permissions, or independent interface behaviours.

### Benefits
It allows a class to combine reusable behaviours without copying their implementations.

### Important points
- Parent order matters because Python uses the method resolution order (MRO) to decide which method is selected when names conflict.
- Keep multiple-inheritance hierarchies simple and cooperative.
- Mixins are often a clearer use case than inheriting from several large stateful classes.

---

## 12. `operator_overloading.py` | Customising built-in operators

### Concept
Operator overloading lets user-defined objects respond to operators such as `+` and `>` through special methods, also called dunder methods.

### How this file works
- `Product.__init__()` stores a product name and price.
- `__add__(self, other)` defines what happens when two Product objects are added. Here, it returns the sum of their prices.
- `__gt__(self, other)` defines the greater-than comparison using prices.
- `__str__()` defines the readable text shown by `print()`.
- Two products are created, printed, added, and compared.

### Where it is used
Operator overloading is useful in mathematical libraries, vector and matrix types, money classes, date/time types, and domain-specific objects where operators have intuitive meanings.

### Benefits
It makes custom objects easier to use with familiar Python syntax.

### Important points
- The meaning of an overloaded operator should be intuitive and consistent.
- This `__add__` returns a number, not a new Product object.
- `__str__` is intended for readable output; `__repr__` is generally used for a developer-oriented representation.

---

## 13. `polymorphism.py` | Same interface, different behaviour

### Concept
Polymorphism means that different object types can be used through a common interface while each type provides its own behaviour.

### How this file works
- `Animal` defines a general `sound()` method.
- `Dog`, `Cat`, and `Cow` inherit from Animal and override `sound()` with their own implementations.
- The list contains instances of all three subclasses.
- The loop calls `animal.sound()` without checking the object's exact class. Python selects the correct overridden method for each object.

### Where it is used
Polymorphism is useful in notification systems, payment processing, graphics, game characters, and any application where different classes respond to the same operation in their own way.

### Benefits
It reduces conditional code, makes new implementations easier to add, and lets calling code depend on a common interface.

### Important points
- Method overriding occurs when a subclass provides its own implementation of an inherited method.
- The caller only needs to know that each object supports the expected method.
- This example demonstrates runtime polymorphism through method overriding.

---

## 14. `static_and_class_methods.py` | Methods tied to the class rather than one instance

### Concept
Instance methods receive the current object as `self`. Static methods receive no automatic first argument. Class methods receive the class itself as `cls`.

### How this file works
- `company` is a class attribute shared by Employee instances.
- `__init__()` creates instance-specific `name` and `salary` values.
- `@staticmethod calculate_bonus(salary)` calculates a 10% bonus using the supplied salary. It does not need to read or change instance or class state.
- `@classmethod change_company(cls, name)` updates the class attribute through `cls`.
- `display()` is an instance method and prints the current employee's details and the company.
- The program creates one employee, displays the details, calculates a bonus, changes the company name, and displays the employee again.

### Where it is used
Static methods are useful for helper operations logically related to a class. Class methods are useful for alternative constructors, class-level configuration, and operations that update shared class state.

### Benefits
The decorators make the intended relationship of a method clear and avoid passing the class or object manually.

### Important points
- Use `self` when the method needs one object's data.
- Use `cls` when the method needs the class or class-level state.
- Use a static method when the operation belongs conceptually to the class but needs neither the object nor the class as an implicit argument.

---

## 15. `rough.py` | Reserved practice file

This file is currently empty. It contains no class definitions or executable statements, so there is no behaviour to explain yet. It can be used for temporary experiments while learning OOP.

---

## Running the examples

From the repository root, run a file by passing its path to Python. Quote paths that contain spaces:

```bash
python "Object Oriented Programming/classes_and_objects.py"
python "Object Oriented Programming/constructors_and_methods.py"
python "Object Oriented Programming/Class Attributes.py"
python "Object Oriented Programming/inheritance.py"
```

The inheritance example includes a CSV-reading class method. To use that method, create an `items.csv` file in the current working directory with `name`, `price`, and `quantity` columns, then call `Item.instantiate_from_csv()`.

## The four pillars of OOP

| Pillar | Meaning | Example in this folder |
|---|---|---|
| Encapsulation | Keep data and the operations that manage it together | `encapsulation.py` |
| Abstraction | Expose essential behaviour and hide implementation detail | `abstraction.py` |
| Inheritance | Reuse and extend a parent class | `inheritance.py`, `multiple_inheritance.py` |
| Polymorphism | Use a shared interface with type-specific behaviour | `polymorphism.py` |

Composition is another important design technique demonstrated in `composition.py`. It is often used alongside the four pillars to build larger systems from smaller components.

## Overall learning outcomes

After completing these examples, you should be able to:
- Explain the difference between a class and an object.
- Initialise objects with constructors and define instance methods.
- Distinguish class attributes from instance attributes.
- Control access to internal state through encapsulation.
- Reuse behaviour through inheritance and combine capabilities through composition.
- Apply abstraction and polymorphism to create consistent interfaces.
- Understand Python's approach to method overloading and operator overloading.
- Choose between instance, class, and static methods.

## Notes on the current examples

- `classes_and_objects.py` assigns attributes after object creation; `constructors_and_methods.py` demonstrates the more structured initialisation pattern.
- `Class Attributes.py` stores all instances in a shared class list. The list is shared, not copied for each object.
- `inheritance.py` defines a CSV-loading class method but does not invoke it automatically.
- `method_overloading.py` uses an optional parameter to provide two behaviours; Python does not perform traditional signature-based overloading.
- `rough.py` is empty at present.

The explanations above follow the actual examples in this folder and distinguish demonstrated behaviour from broader real-world applications.
