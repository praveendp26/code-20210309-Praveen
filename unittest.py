import unittest 
from unittest.mock import patch, mock_open
import calculator  
import json
import os
class TestMyFunctions(unittest.TestCase):
	@patch("builtins.open", new_callable=mock_open,
       read_data=json.dumps([{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
							{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
							{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
							{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
							{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
							{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}])
	def test_loadData(self):
		expected_output = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
							{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
							{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
							{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
							{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
							{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
							
		filename = 'details.json'
		actual_output = test_loadData(filename, 'C:/Users/Praveen/Desktop/calculator')
		
		# Assert filename is file that is opened
        mock_file.assert_called_with(filename)	

		self.assertEqual(expected_output, actual_output)

if __name__ == '__main__': 
    unittest.main() 
