

# WARNING the code doesn't work, because there few files needed to complete the task. 
# case only to show how C is faster than Python.

words = set()

# def keyword for defining a func.

def check(word):
  if word.lower() in words:
    return True
  else:
    return False

#to load the file into memory. It takes a string, name of the file to load
def load(dictionary):
  #open the file by read mode('r')
  file = open(dictionary, "r")
  for line in file:
    word = line.rstrip()
    words.add(word)
    file.close()
    return True


#size() returns a size of the dictionary
def size():
  return len(words)

#malloc an free
def unload():
  return True
