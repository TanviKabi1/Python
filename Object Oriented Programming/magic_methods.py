class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __str__(self):
        return f"{self.name} ({self.rating}/10)"

    def __repr__(self):
        return f"Movie('{self.name}', {self.rating})"

    def __lt__(self, other):
        return self.rating < other.rating

movie1 = Movie("Inception", 9)
movie2 = Movie("Interstellar", 9.5)

print(movie1)
print(repr(movie2))
print("Is first movie rated lower?", movie1 < movie2)
