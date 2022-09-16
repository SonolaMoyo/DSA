"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [[None]]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash_value = self.calculate_hash_value(string)
        hash = hash_value % 10000
        try:
            self.table[hash].append(string)
            return
        except:
            print("something went wrong while storing")
            return

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        available = False
        hash_value = self.calculate_hash_value(string)
        hash = hash_value % 10000
        for values in self.table[hash]:
            if values == string:
                available = True
                break
        
        if available == True:
            return hash
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        if not (len(string) > 2):
            print("string length not sufficent")
            return -1
        hash_value = (ord(string[0])*100) + (ord(string[1]))
        return hash_value
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print (hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print (hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print (hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print (hash_table.lookup('UDACIOUS'))
