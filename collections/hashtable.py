"""
Provides an implementation of a hash table based on an
array of linked lists.

@author Alejandro Baldominos <me@bal.do>
"""

from typing import Any, Hashable

class HashTable:

    def __init__ (self, num_buckets : int = 512):
        """
        Creates a new hash table with the specified number of buckets.

        Parameters:
           bucket_space (int): The size of the buckets array. 
        """
        self.num_buckets = num_buckets
        self.buckets = [None] * num_buckets


    def add (self, key : Hashable, value : Any):
        """
        Stores a new key-value pair in the hash table.

        Parameters:
            key (Hashable): The key of the new object, must be hashable.
            value (Any): The value of the new object, can be of any type.
        """
        bucket_ix = hash(key) % self.num_buckets
        if self.buckets[bucket_ix] is None:
            self.buckets[bucket_ix] = []
        for i, (k, _) in enumerate(self.buckets[bucket_ix]):
            if k == key:
                self.buckets[bucket_ix][i] = (key, value)
                return
        self.buckets[bucket_ix].append((key, value))

    
    def get (self, key : Hashable) -> Any:
        """
        Retrieves a value from the hash table given its key.

        Parameters:
            key (Hashable): The key of the object being searched.

        Returns:
            value (Any): The value associated with the string, or None if
                         the key does not exist in the hash table.
        """
        bucket_ix = hash(key) % self.num_buckets
        if self.buckets[bucket_ix] is None:
           return None
        for k, v in self.buckets[bucket_ix]:
            if k == key:
                return v
        return None