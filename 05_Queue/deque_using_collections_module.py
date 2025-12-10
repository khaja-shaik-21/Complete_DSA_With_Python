"""
Python implementation of deque using the collections module with all common queue operations:
"""

from collections import deque

# Create a deque
dq = deque()

# -------------------------
# 1. Enqueue / Insert
# -------------------------

# Add to the right (rear)
dq.append(10)
dq.append(20)

# Add to the left (front)
dq.appendleft(5)

print("Deque after insertions:", dq)

# -------------------------
# 2. Dequeue / Delete
# -------------------------

# Remove from right
right_item = dq.pop()
print("Removed from right:", right_item)

# Remove from left
left_item = dq.popleft()
print("Removed from left:", left_item)

print("Deque after deletions:", dq)

# -------------------------
# 3. Peek Operations
# -------------------------

if dq:
    print("Front element:", dq[0])
    print("Rear element:", dq[-1])

# -------------------------
# 4. Check if Empty
# -------------------------

if not dq:
    print("Deque is empty")
else:
    print("Deque is not empty")

# -------------------------
# 5. Size of Deque
# -------------------------

print("Size of deque:", len(dq))

# -------------------------
# 6. Clear Deque
# -------------------------

dq.clear()
print("Deque after clearing:", dq)

# -------------------------
# 7. Extend Operations
# -------------------------

dq.extend([1, 2, 3])           # Add multiple items at right
dq.extendleft([0, -1, -2])    # Add multiple items at left (reverse order)

print("Deque after extending:", dq)

# -------------------------
# 8. Rotate Deque
# -------------------------

dq.rotate(1)   # Rotate right by 1
print("After rotating right:", dq)

dq.rotate(-1)  # Rotate left by 1
print("After rotating left:", dq)


#############   Time & Space Complexity Table: Queue Using collections.deque   ############

# | Method         | Time Complexity | Space Complexity | Notes                                       |
# | -------------- | --------------- | ---------------- | --------------------------------------------|
# |  enqueue()     | O(1)            | O(1)             | Insert at rear using append()               |
# |  enqueueLeft() | O(1)            | O(1)             | Insert at front using appendleft()          |
# |  dequeue()     | O(1)            | O(1)             | Remove from front using popleft()           |
# |  dequeueRear() | O(1)            | O(1)             | Remove from rear using pop()                |
# |  peekFront()   | O(1)            | O(1)             | Access first element using dq[0]            |
# |  peekRear()    | O(1)            | O(1)             | Access last element using dq[-1]            |
# |  isEmpty()     | O(1)            | O(1)             | Length check (len(dq) == 0)                 |
# |  size()        | O(1)            | O(1)             | Returns number of elements                  |
# |  clear()       | O(n)            | O(1)             | Removes all elements                        |
# |  rotate(k)     | O(k)            | O(1)             | Rotates deque left/right by k positions     |
# |  __str__()     | O(n)            | O(n)             | Builds string from all elements             |
