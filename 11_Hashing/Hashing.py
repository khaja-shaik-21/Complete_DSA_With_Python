###### Integer Hashing
def mod(num, cellnumber):
	return num % cellnumber

mod(400, 24)# --> 16 Hash value
	
mod(700, 24)# --> 4 Hash value


###### String Hashing By using ASCII Function
def modASCII(word, cellnumber):
		total = 0
		for i in word:
				total += ord(i)
		return total % cellnumber

modASCII("ABC", 24)# ---> 6 Hash value



def simple_hash(key):
    return len(key) % 5 

keys = ["apple", "grape", "banana"]

for k in keys:
    print(f"{k} -> {simple_hash(k)}")


####Output:

# apple  -> 0   (length 5 % 5 = 0)
# grape  -> 0   (length 5 % 5 = 0)
# banana -> 1   (length 6 % 5 = 1)


######## Handle Collisions ##########


# 1.Direct Chaining Method
hash_table = {
    0: [("apple", 1), ("grape", 2)],
    1: [("banana", 3)]
}


# 2. Open Addressing

# If a collision occurs, find another empty slot using a probing technique.
	# Linear Probing: Try next slot → index + 1
	# Quadratic Probing: Try index + 1², 2², 3²...
	# Double Hashing: Use a second hash function to jump slots