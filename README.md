# Test GH

這是一個用於測試 GitHub 功能的 Python 專案。

## 專案結構

```
test-gh/
├── bubble_sort/
│   └── bubble_sort.py
└── README.md
```

## 功能

### 冒泡排序 (Bubble Sort)

位置: `bubble_sort/bubble_sort.py`

實作了一個經典的冒泡排序演算法，包含詳細的中文註釋說明。

**特性:**
- 時間複雜度: O(n²)
- 空間複雜度: O(1)
- 原地排序 (in-place sorting)

**使用方法:**

```python
from bubble_sort.bubble_sort import bubble_sort

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers.copy())
print(sorted_numbers)  # [11, 12, 22, 25, 34, 64, 90]
```

## 如何執行

```bash
python bubble_sort/bubble_sort.py
```

## 授權

MIT License
