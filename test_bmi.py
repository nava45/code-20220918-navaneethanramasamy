import unittest
import bmi

class TestBmIApplication(unittest.TestCase):
    def setUp(self):
        self.json_data = [ {
                        "Gender": "Male",
                        "HeightCm": 180,
                        "WeightKg": 77
                    },
                    {
                        "Gender": "Female",
                        "HeightCm": 166,
                        "WeightKg": 62
                    }]
    
    def test_bmi_calculation(self):
        for data in self.json_data:
            result = bmi.bmi_calculation(data)
            self.assertIn('BmiRange', result)
            self.assertIn('BmiCategory', result)
            self.assertIn('HealthRisk', result)
            
    def test_bmi_logic(self):
        data = self.json_data[0]
        result = bmi.bmi_calculation(data)
        self.assertEquals(result['BmiRange'], '18.5 and 24.9')
        
    def test_observations(self):
        result = bmi.run_bmi_observations(self.json_data)
        expected = {'overweight_observations_count': 0,
                    'overweight_female_observations_count': 0,
                    'very_high_risk_count': 0
                    }
        self.assertEquals(result, expected)