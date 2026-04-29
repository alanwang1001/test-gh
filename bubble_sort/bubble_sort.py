"""
冒泡排序 (Bubble Sort) 實作
這是一個簡單的排序演算法，通過重複交換相鄰的逆序元素來排序
時間複雜度: O(n²)
空間複雜度: O(1)
"""

def bubble_sort(arr):
    """
    使用冒泡排序法對陣列進行排序
    
    參數:
        arr: 要排序的數字陣列
        
    返回:
        排序後的陣列
    """
    n = len(arr)
    # 外層迴圈：控制排序輪數
    for i in range(n):
        # 內層迴圈：比較相鄰元素並交換
        for j in range(0, n - i - 1):
            # 如果前一個元素大於後一個元素，則交換
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("原始陣列:", numbers)
    sorted_numbers = bubble_sort(numbers.copy())
    print("排序後:", sorted_numbers)
