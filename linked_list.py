# adding to the head is O(1)
# removing from the head is also O(1)
# adding or removing anywhere else is O(N)
# searching is also O(N)

# best used for stacks and queues

# advantages, no need to resize, as arrays sometimes need,
# also can truly store different sized items, arrays assume
# all items have the same size so one large item in an array
# can result in a lot of wasted space in array if the rest
# of the items are small

# Disadvantages, requires more memory because of references.
# cannot go backwards because references only go one direction
# no random access, have to start from the head
