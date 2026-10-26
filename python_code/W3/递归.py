def jiecheng(n):
    #基线条件
    if n == 1:
        return 1
    #递归条件
    return n*jiecheng(n-1)
print(jiecheng(5))

cache = {}
def feibonaqie(n):
    if n in cache:
        return cache[n]
    if n == 1 or n == 2:
        return 1
    res = feibonaqie(n-1) + feibonaqie(n-2)
    cache[n] = res
    return res
print(feibonaqie(50))

def split_grid(grid_id,n):
    if n == 0:
        return [grid_id]
    all_children = []
    for i in range(4):
        child_id = f"{grid_id}_{i}"
        child_result = split_grid(child_id,n-1)
        all_children.extend(child_result)
    return all_children
print(split_grid("ROOT",2))