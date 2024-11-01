#!/usr/bin/env python3
'''A module for implementing a simple pagination logic'''
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Returns the range of values of a list for a pagination'''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Returns a paginated list of items'''
        assert(type(page) == int and type(page_size) == int)
        assert(page > 0 and page_size > 0)
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if end_index < len(data):
            return self.dataset()[start_index:end_index]
        else:
            return []
