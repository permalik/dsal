"""
=====================================================
UNIVERSAL TEST DATASET + EXHAUSTIVE ALGORITHM PROMPTS
(PYTHON LANGUAGE FOCUS WITH LINE NUMBERS)
=====================================================
"""

# Dataset

integers = [3, 1, 4, 1, 5, 9, -2, 6, 5, 3, 5]
strings = ["apple", "banana", "apple", "cherry", "date", "fig", "grape"]

key_value_pairs = {
    "apple": 3,
    "banana": 5,
    "cherry": 2,
    "date": 1,
    "fig": 6,
    "grape": 4,
}

graph_edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
graph_nodes = [1, 2, 3, 4, 5]

# For trees, use nested dict or class TreeNode in Python (can build dynamically)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

text = "madam racecar level deed civic noon rotor stats"

coordinates = [(1, 2), (3, 4), (-1, -2), (0, 0)]

# =====================================================
# USAGE PROMPTS (NUMBERED)
# =====================================================

usage_prompts = [
    # === BASIC ARRAY OPERATIONS ===
    "1. Array Traversal: Iterate over 'integers' list and print each element.",
    "2. Linear Search: Search for number 5 in 'integers' using simple linear search.",
    "3. Binary Search: Sort 'integers' then implement binary search function.",
    "4. Remove Duplicates: Remove duplicates from 'integers' creating a new list or in-place.",
    # === SORTING ALGORITHMS ===
    "5. Bubble Sort: Implement bubble sort on 'integers'.",
    "6. Selection Sort: Implement selection sort on 'integers'.",
    "7. Insertion Sort: Implement insertion sort on 'integers'.",
    "8. Merge Sort: Implement recursive merge sort on 'integers'.",
    "9. Quick Sort: Implement quick sort on 'integers'.",
    "10. Heap Sort: Implement heap sort using heapq or manual heapify.",
    "11. Counting Sort: Implement counting sort for non-negative 'integers'.",
    "12. Radix Sort: Implement radix sort using counting sort as subroutine.",
    "13. Bucket Sort: Implement bucket sort on 'integers'.",
    # === STRINGS ===
    "14. Palindrome Check: Write function to check if a string is palindrome.",
    "15. Frequency Count: Count word frequency in 'strings' using dictionary.",
    "16. Substring Search (Naive): Implement naive substring search of 'civic' in 'text'.",
    "17. KMP Algorithm: Implement Knuth-Morris-Pratt substring search.",
    "18. Rabin-Karp: Implement Rabin-Karp substring search.",
    "19. Z-Algorithm: Implement Z-algorithm for pattern occurrences.",
    "20. Manacher's Algorithm: Find longest palindromic substring using Manacher’s algorithm.",
    "21. Aho-Corasick: Build Aho-Corasick automaton to find multiple patterns.",
    "22. Longest Common Subsequence (LCS): Implement LCS between 'apple' and 'grape'.",
    "23. Longest Common Substring: Implement longest common substring between 'banana' and 'bandana'.",
    # === HASHING ===
    "24. Hash Map Lookup: Lookup 'fig' in key_value_pairs dictionary.",
    "25. Detect Duplicates Using Set: Detect duplicates in 'strings' using set.",
    "26. Group Anagrams: Group 'strings' that are anagrams using dictionary.",
    "27. Word Frequency: Count frequencies of words in 'text' using dictionary.",
    # === TREES ===
    "28. Inorder Traversal: Implement recursive inorder traversal on binary tree.",
    "29. Preorder Traversal: Implement recursive preorder traversal.",
    "30. Postorder Traversal: Implement recursive postorder traversal.",
    "31. Level Order Traversal: Implement BFS level order traversal using queue.",
    "32. Search in BST: Search for a value in binary search tree.",
    "33. Tree Height: Compute tree height recursively.",
    "34. Validate BST: Check if tree satisfies BST properties.",
    "35. Lowest Common Ancestor (LCA): Find LCA of two nodes in binary tree.",
    # === ADVANCED TREES ===
    "36. AVL Tree: Implement AVL tree insertion and rotations.",
    "37. Red-Black Tree: Implement Red-Black tree insertions.",
    "38. Segment Tree: Build segment tree for range sum queries on 'integers'.",
    "39. Fenwick Tree (BIT): Build Fenwick tree and query prefix sums.",
    "40. Suffix Tree: Build suffix tree from 'text' (Ukkonen’s algorithm).",
    "41. Trie: Build Trie from 'strings' and implement prefix search.",
    "42. Radix Tree: Implement compressed trie (Radix tree).",
    "43. Treap: Implement randomized BST (Treap) insertion.",
    "44. Cartesian Tree: Build Cartesian tree from 'integers'.",
    "45. Interval Tree: Implement interval tree for interval overlaps.",
    "46. Rope: Implement Rope data structure for efficient string concatenation.",
    # === HEAPS & PRIORITY QUEUES ===
    "47. Min-Heap: Implement min-heap insert and extract-min.",
    "48. Max-Heap: Implement max-heap.",
    "49. Median Heap: Implement two heaps to track median dynamically.",
    "50. Fibonacci Heap: Implement Fibonacci heap operations.",
    "51. Pairing Heap: Implement pairing heap insert and delete operations.",
    # === GRAPH ALGORITHMS ===
    "52. BFS: Implement BFS on adjacency list starting from node 1.",
    "53. DFS: Implement DFS recursively or iteratively.",
    "54. Topological Sort: Implement topological sort using DFS or Kahn’s algorithm.",
    "55. Dijkstra’s Algorithm: Implement Dijkstra's shortest path with priority queue.",
    "56. Bellman-Ford: Implement Bellman-Ford to detect negative cycles.",
    "57. Floyd-Warshall: Implement all-pairs shortest path.",
    "58. Kruskal’s MST: Implement MST using Union-Find and sorting edges.",
    "59. Prim’s MST: Implement Prim’s algorithm.",
    "60. Tarjan’s SCC: Implement Tarjan’s strongly connected components.",
    "61. Kosaraju’s SCC: Implement Kosaraju’s algorithm.",
    "62. Union-Find (Disjoint Set): Implement Union-Find and use to detect cycles.",
    "63. Edmonds-Karp: Implement max flow using Edmonds-Karp.",
    # === DYNAMIC PROGRAMMING ===
    "64. Fibonacci (Memoization): Implement recursive memoized Fibonacci.",
    "65. 0/1 Knapsack: Solve knapsack problem using DP.",
    "66. Subset Sum: Check subset sums to 10 with DP.",
    "67. Longest Increasing Subsequence: Implement LIS using DP or binary search.",
    "68. Matrix Chain Multiplication: Minimize multiplication cost DP.",
    "69. Edit Distance: Compute edit distance between strings using DP.",
    "70. Bitmask DP: Solve simplified TSP on 4 nodes using bitmask DP.",
    "71. Digit DP: Count numbers without repeated digits using digit DP.",
    "72. DP with Monotonic Queue: Sliding window optimization.",
    "73. Convex Hull Trick: Optimize DP using convex hull trick.",
    # === MATH & NUMBER THEORY ===
    "74. GCD (Euclidean): Compute GCD of numbers in 'integers'.",
    "75. LCM: Compute LCM of numbers in 'integers'.",
    "76. Sieve of Eratosthenes: Generate primes less than 100.",
    "77. Modular Exponentiation: Implement fast modular exponentiation.",
    "78. Chinese Remainder Theorem: Solve modular linear equations.",
    "79. Fast Fourier Transform: Implement FFT for polynomial multiplication.",
    "80. Modular Inverse: Compute modular inverse using Extended Euclidean.",
    "81. Combinatorics (nCr): Compute combinations with modular arithmetic.",
    # === GEOMETRY ===
    "82. Convex Hull (Graham Scan): Compute convex hull of 'coordinates'.",
    "83. Point in Polygon: Use ray casting to check if point is inside polygon.",
    "84. Closest Pair of Points: Use divide & conquer on 'coordinates'.",
    "85. Line Sweep: Detect line segment intersections.",
    "86. Rotating Calipers: Compute polygon diameter.",
    # === SLIDING WINDOW / TWO POINTERS ===
    "87. Max Sum Subarray (Fixed size): Sliding window max sum of size 3.",
    "88. Longest Unique Substring: Sliding window for longest substring without repeats.",
    "89. Two Sum: Use hash map or two pointers to find pairs summing to 7.",
    "90. Three Sum: Find triplets summing to zero.",
    "91. Minimum Window Substring: Find smallest substring containing 'civic'.",
    # === CACHING & STORAGE STRUCTURES ===
    "92. LRU Cache: Implement LRU cache with OrderedDict or linked list + dict.",
    "93. Bloom Filter: Implement Bloom filter with multiple hash functions.",
    "94. Skip List: Implement skip list insert and search.",
    "95. Discretization: Coordinate compress 'integers'.",
    "96. Circular Buffer: Implement circular queue with fixed size.",
]

# ===========================
# Example: print prompts
# ===========================

if __name__ == "__main__":
    print("🧠 Python Data Structures & Algorithms Usage Prompts:\n")
    for prompt in usage_prompts:
        print(prompt)
