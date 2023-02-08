
def search(arr, target):
    return binary(arr, target, 0, len(arr) - 1)
    
def binary(arr, target, left, right):
    mid = (right + left) // 2
    if arr[mid] == target: return mid

    if target < arr[mid]: return binary(arr, target, left, mid - 1)
    else: return binary(arr, target, mid + 1, right)

if __name__ == "__main__":
    x = search([ 2, 3, 4, 5, 8, 9, 10, 12, 18, 24, 40 ], 10)
    print(x)