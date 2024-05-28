from typing import List


def heap_sort(arr):
    n = len(arr)
    # 确认最深最后的那个根节点的位置
    first_root = n // 2 - 1
    # 由后向前遍历所有的根节点，建堆并进行调整
    for root in range(first_root, -1, -1):
        build(arr, root, n - 1)

    # # 调整完成后，将堆顶的根节点与堆内最后一个元素调换位置，此时为数组中最大的元素，然后重新调整堆，将最大的元素冒到堆顶。依次重复上述操作
    # for end in range(n - 1, 0, -1):
    #     arr[0], arr[end] = arr[end], arr[0]
    #     build(arr, 0, end - 1)


def build(arr, root, end):
    while True:
        # 左子节点的位置
        child = 2 * root + 1
        # 若左子节点超过了最后一个节点，则终止循环
        if child > end:
            break
        # 若右子节点在最后一个节点之前，并且右子节点比左子节点大，则我们的孩子指针移到右子节点上
        if (child + 1 <= end) and (arr[child + 1] > arr[child]):
            child += 1
        # 若最大的孩子节点大于根节点，则交换两者顺序，并且将根节点指针，移到这个孩子节点上
        if arr[child] > arr[root]:
            arr[child], arr[root] = arr[root], arr[child]
            root = child
        else:
            break


def build_heap(number_list):
    n = len(number_list)
    first_root = n // 2 - 1
    for tmp_root in range(first_root, -1, -1):
        # 建堆
        while True:
            child = 2 * tmp_root + 1
            if child >= n:
                break
            if (child + 1 < n) and (number_list[child+1] > number_list[child]):
                child += 1
            if number_list[child] > number_list[tmp_root]:
                number_list[tmp_root], number_list[child] = number_list[child], number_list[tmp_root]
                tmp_root = child
            else:
                break


if __name__ == '__main__':
    # number_list = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    # build_heap(number_list)
    # print(number_list)
    """
    原始数据： [17, 56, 71, 38, 61, 62, 48, 28, 57, 42]
    堆排序结果： [17, 28, 38, 42, 48, 56, 57, 61, 62, 71]
    """