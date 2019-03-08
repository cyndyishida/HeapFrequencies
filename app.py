import Project6.Heap as Heap
from string import ascii_lowercase

heap = Heap.Heap(26)
for i,ch in enumerate(ascii_lowercase):
    heap.push(key=i, val=ch)
    heap.push(key=1, val=ch)

result = heap.levels
print("\n".join(str(lvl) for lvl in result))

#print(",\n".join('['+ ", ".join(f"Node({i._key}, '{i._val}')" for i in lvl) +']' for lvl in result))


