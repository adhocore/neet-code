"""Top K frequent items in a list
"""


def top_k_frequent(nums, k):
    cts = {}
    for num in nums:
        cts[num] = cts.get(num, 0) + 1
    cts = sorted(cts, reverse=True)
    return cts[0:k]


if __name__ == "__main__":
    print(top_k_frequent([1, 2, 1, 3, 4, 2, 1, 5, 7, 7, 7, 7, 7, 7, 7, 7], 2))
    # => [7, 5]
