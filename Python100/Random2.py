'''list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].'''

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
                     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee",
                     "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                     "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada",
                     "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",
                     "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska"]    ##this is a "list"
print(states_of_america)   
states_of_america.append("Hawaii") #in the list "state of america" add hawaii
print(states_of_america) #print the new list with Haeaii
print("The number 10 of the list is = " + states_of_america[9]) #print item number 10 of the list
b = len(states_of_america)
print(f"The number of states of america is '{b}'")
