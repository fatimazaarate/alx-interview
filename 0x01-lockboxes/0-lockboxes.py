#!/usr/bin/python3
def canUnlockAll(boxes):
  index_unlocked = [0]
  keys = set(boxes[0])
  while True:
        new_keys = False
        for i in range(len(boxes)):
            print(i)
            if i not in index_unlocked and i in keys:
                index_unlocked.append(i)
                print(index_unlocked)
                keys.update(boxes[i])
                print(keys)
                new_keys = True
        if not new_keys:
            break
  return len(index_unlocked) == len(boxes)
