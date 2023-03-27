import graph

# Matrix transformations: Version 1.0
# Calculations and graph generation is contained within the graph class

print("/* Clarity, MarkerRange and DarkMode can be altered at the start of the source code */"
      + "\nInput a matrix in the form [a b c d] and see the resulting transformation!")
transformation = input()
transformation = transformation[1:len(transformation) - 1]
transformation = transformation.split(" ")

# Choose your preferred parameters here
graph.create_plot(transformation, 300, 10, True, "blue")