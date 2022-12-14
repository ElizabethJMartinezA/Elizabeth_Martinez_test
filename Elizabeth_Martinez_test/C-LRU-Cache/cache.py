
from threading import Timer

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int, ttl : int):
        self.cap = capacity
        self.cache = {}  # map key to node
        self.ttl = ttl
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right and show the relation between the previous and future data 
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    #Method get: In this function the code will get the data of the key desire and update the cache map o the leas recently used data
    def get(self, key: int) -> int:
        # When the key is contained in the cache. It will return the value, but also updating the cache
        if key in self.cache:
            #First remove the cache from the position where ever it is.
            self.remove(self.cache[key])
            #Second insert the cache in the most recent used
            self.insert(self.cache[key])
            return self.cache[key].val
        #If is not contained it will send a -1 as a response
        return -1

    #Method put: In this function the code will put the data of a value and key in the cache map. It will be added as the most recent data
    def put(self, key: int,value: int) -> None:
        #If the key already exist in the cache. The code will remove this key and old value from the cache
        if key in self.cache:
            self.remove(self.cache[key])
        #The key and value desire are inserted in the cache as the most recent value. The data is inserted as an key, value format for simplicity in other functions.
        self.cache[key] = Node(key, value)
        #The data inserted is place in the order of the conecction between previous and future values
        self.insert(self.cache[key])
        #Set an expiration time for the key
        self._expire_cache(key, self.ttl)
        
        #In case that the size of the cache surprase the fixed value. The data that is leas recently used is deleted from the cache.
        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


    def _expire_cache(self, key):
        if self.ttl > 0:
            # Add the expiration time for this cache record
            Timer(self.ttl, self.remove(self.cache[key])).start()
