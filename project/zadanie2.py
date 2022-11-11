#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    nums = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    print(nums)

    # инвертирование словаря
    new_nums = {n: d for d, n in nums.items()}
    print(new_nums)