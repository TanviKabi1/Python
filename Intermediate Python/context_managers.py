from contextlib import contextmanager

@contextmanager
def manage_resource():
    print("Resource acquired")
    try:
        yield "Database Connection"
    finally:
        print("Resource released")

with manage_resource() as resource:
    print("Using:", resource)

print("Program completed")
