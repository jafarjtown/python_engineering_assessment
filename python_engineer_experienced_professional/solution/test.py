import unittest
import os
from json_schema import JsonScema


class TestSchema(unittest.TestCase):
    
    def test_with_look_up(self):
        self.assertEqual(JsonScema('../data/data_1.json', '../schema/schema_with_look_up_1.json', 'message').generate_schema(), True)
        os.remove('../schema/schema_with_look_up_1.json')
        
    def test_with_no_look_up(self):
        self.assertEqual(JsonScema('../data/data_1.json', '../schema/schema_with_look_up_1.json').generate_schema(), True)
        os.remove('../schema/schema_with_look_up_1.json')
        
    
    def test_with_schema_file_does_not_exist(self):
        self.assertEqual(JsonScema('../data/data_1.json', '../schema/not_exist_file.json').generate_schema(), True)
        os.remove('../schema/not_exist_file.json')
        
        

if __name__ == '__main__':
    unittest.main()