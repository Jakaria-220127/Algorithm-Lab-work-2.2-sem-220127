def binary_search_dac(arr, low, high, target):
    if low > high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_dac(arr, low, mid - 1, target)
    else:
        return binary_search_dac(arr, mid + 1, high, target)

def main():
    arr = [2, 4, 6, 8, 10, 12, 14]
    target = 10
    n = len(arr)
    result = binary_search_dac(arr, 0, n - 1, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found")

if __name__ == "__main__":
    main()