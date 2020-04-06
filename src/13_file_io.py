
"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
foo = open("./foo.txt")
print(foo.read())
foo.close()
# Close the file?

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain.

# YOUR CODE HERE
bar = open("./bar.txt", mode="w+")
bar.write('John\'s feet creaked up the steps to the house. The address matched the one Stacy gave him, but he felt uncomfortable walking inside.')
bar.write('\nHe knocked on the door first. "I-Is... anyone there?"')
bar.write('\n\nSilence.')
