# dictionary =  a collection of
#               {key:value} pairs
#               ordered and changeable.
#               No duplicates

capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("USA"))
# prints the value associated with the key
# (If we type out the key that does not
# exist, it will print "None"

#if capitals.get("(key)"):
#    print("That capital exists")
#else:
#    print("That capital doesn't exist")

#capitals.update({"Germany": "Berlin"})
# (Appends at the end of dictionary)

#capitals.update({"USA": "Detroit"})
# (Changes the value associated with the key)

#capitals.pop("China")
# (Removes the key along with its value)

#capitals.popitem()
# (Removes the latest key:value)

# capitals.clear()

#keys = capitals.keys()
#for key in capitals.keys():
#   print(key)
# (Prints ONLY the keys (not the values)
# in the dictionary)

#values = capitals.values()
#for value in capitals.values():
#   print(value)
# (Prints ONLY the values (not the keys)
# in the dictionary)

#items = capitals.items()
#for key, value in capitals.items():
#    print(f"{key}: {value}")

