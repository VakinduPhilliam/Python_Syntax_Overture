# Python List Mutation
# Unlike strings, which are immutable, lists are a mutable type, 
# i.e. it is possible to change their content: 

cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!

cubes[3] = 64  # replace the wrong value
cubes
