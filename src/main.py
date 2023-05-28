import gc
import RBT
import Hash_Table
import time
import random
import sys
from Graphic import create_graphic


def randomizer(res, size):
    for _ in range(size):
        res.append(random.randint(1, 100))
    return res


def get_size(obj, seen=None):
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()

    obj_id = id(obj)
    if obj_id in seen:
        return 0

    seen.add(obj_id)

    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])

    return size


def HT_insertion(filling):
    insertion_res_time = []
    table = Hash_Table.HashTable()
    sizes = [i*10 for i in range(1, 1000)]
    for size in sizes:
        res = []
        if filling == "randomly":
            randomizer(res, size)
        else:
            res = [i for i in range(size)]
        gc.disable()
        start_insert_time = time.time()
        for x in range(size):
            table.put(res[x], 10)
        end_insert_time = time.time()
        gc.enable()
        insertion_res_time.append(end_insert_time - start_insert_time)
    create_graphic(sizes, insertion_res_time, "HT", "Insertion")


def RBT_insertion(filling):
    insertion_res_time = []
    tree = RBT.Tree()
    sizes = [i*10 for i in range(1, 1000)]
    for size in sizes:
        res = []
        if filling == "randomly":
            randomizer(res, size)
        else:
            res = [i for i in range(size)]
        gc.disable()
        start_insert_time = time.time()
        for x in range(size):
            tree.insert(res[x])
        end_insert_time = time.time()
        gc.enable()
        insertion_res_time.append(end_insert_time - start_insert_time)
    create_graphic(sizes, insertion_res_time, "RBT", "Insertion")


def RBT_deletion(filling):
    deletion_res_time = []
    tree = RBT.Tree()
    sizes = [i*10 for i in range(1, 1000)]
    for size in sizes:
        res = []
        if filling == "randomly":
            randomizer(res, size)
        else:
            res = [i for i in range(size)]
        for x in range(size):
            tree.insert(res[x])
        gc.disable()
        start_insert_time = time.time()
        for x in res:
            tree.delete(x)
        end_insert_time = time.time()
        gc.enable()
        deletion_res_time.append(end_insert_time - start_insert_time)
    create_graphic(sizes, deletion_res_time, "RBT", "Deletion")


def HT_deletion(filling):
    deletion_res_time = []
    table = Hash_Table.HashTable()
    sizes = [i*10 for i in range(1, 1000)]
    for size in sizes:
        res = []
        if filling == "randomly":
            randomizer(res, size)
        else:
            res = [i for i in range(size)]
        for x in range(size):
            table.put(res[x], 10)
        gc.disable()
        start_insert_time = time.time()
        for x in res:
            table.delete(x)
        end_insert_time = time.time()
        gc.enable()
        deletion_res_time.append(end_insert_time - start_insert_time)
    create_graphic(sizes, deletion_res_time, "HT", "Deletion")


def HT_searching(filling):
    deletion_res_time = []
    table = Hash_Table.HashTable()
    sizes = [i*10 for i in range(1, 1000)]
    for size in sizes:
        res = []
        if filling == "randomly":
            randomizer(res, size)
        else:
            res = [i for i in range(size)]
        for x in range(size):
            table.put(res[x], 10)
        gc.disable()
        start_insert_time = time.time()
        for x in res:
            table.find(x)
        end_insert_time = time.time()
        gc.enable()
        deletion_res_time.append(end_insert_time - start_insert_time)
    create_graphic(sizes, deletion_res_time, "HT", "Searching")


def RBT_searching(filling):
    deletion_res_time = []
    tree = RBT.Tree()
    sizes = [i*10 for i in range(1, 1000)]
    for size in sizes:
        res = []
        if filling == "randomly":
            randomizer(res, size)
        else:
            res = [i for i in range(size)]
        for x in range(size):
            tree.insert(res[x])
        gc.disable()
        start_insert_time = time.time()
        for x in res:
            tree.find(x)
        end_insert_time = time.time()
        gc.enable()
        deletion_res_time.append(end_insert_time - start_insert_time)
    create_graphic(sizes, deletion_res_time, "RBT", "Searching")


def RBT_memory_usage(filling):
    memory_usage = []
    tree = RBT.Tree()
    sizes = [i*2 for i in range(1, 200)]
    for size in sizes:
        res = []
        if filling == "randomly":
            randomizer(res, size)
        else:
            res = [i for i in range(size)]
        for x in range(size):
            tree.insert(res[x])
        memory_usage.append(get_size(tree))
    create_graphic(sizes, memory_usage, "RBT-", "Memory_Usage", "Size in bytes")


def HT_memory_usage(filling):
    memory_usage = []
    table = Hash_Table.HashTable()
    sizes = [i*5 for i in range(1, 200)]
    for size in sizes:
        res = []
        if filling == "randomly":
            randomizer(res, size)
        else:
            res = [i for i in range(size)]
        for x in range(size):
            table.put(res[x], 10)
        memory_usage.append(get_size(table))
    create_graphic(sizes, memory_usage, "HT", "Memory_Usage", "Size in bytes")


if __name__ == "__main__":
    HT_memory_usage("randomly")
    RBT_memory_usage("randomly")
    HT_insertion("Hi")
    RBT_insertion("randomly")
    RBT_deletion("hi")
    HT_deletion("randomly")
    HT_searching("randomly")
    RBT_searching("hi")
