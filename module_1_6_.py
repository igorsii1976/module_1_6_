print()
my_dict = {"Igor":1976, "Tanya":1969, "Larisa":1967}
print("Dict:",my_dict)
print("Existing value:",my_dict.get('Larisa'))
print("Not existing value:",my_dict.get('Ivan'))
my_dict.update({"Katya":1980,
                "Anna":2007})
a = my_dict.pop("Tanya")
print("Deleted value:",a)
print("Modified dictionary:",my_dict)
print()
my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко', 42.314}
print("Set:", my_set)
my_set.update({13, (5, 6, 1.6)})
b = my_set.discard(1)
print("Modified set:", my_set)