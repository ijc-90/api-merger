from unittest import TestCase
from src import json_merger


class JsonMergerTest(TestCase):

    def test_merge(self):
        merger = json_merger.JsonMerger()
        merger.add_element({'deductible': 1000, 'stop_loss': 14000, 'oop_max': 5000})
        merger.add_element({'deductible': 1300, 'stop_loss': 0, 'oop_max': 5000})
        merger.add_element({'deductible': 1000, 'stop_loss': 13000, 'oop_max': 5000})
        result = merger.get_result()
        self.assertTrue(result.get('deductible') == 1100)
        self.assertTrue(result.get('stop_loss') == 9000)
        self.assertTrue(result.get('oop_max') == 5000)


