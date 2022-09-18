import json
import argparse
import os


def bmi_calculation(row_dict):
    '''
    row_dict: @type: dict
    @desc: contains WeightKg and HeightCm for bml calc
    @returns: adding 3 new fields bmi_cat, bmi_range, health_risk
    '''
    bmi_value = (row_dict['WeightKg'] / ((row_dict['HeightCm'] / 100.0) ** 2))
    if bmi_value <= 18.4:
        row_dict['BmiCategory'] = 'Underweight'
        row_dict['BmiRange'] = '18.4 and below'
        row_dict['HealthRisk'] = 'Malnutrition risk'
    elif bmi_value >= 18.5 and bmi_value <= 24.9:
        row_dict['BmiCategory'] = 'Normal weight'
        row_dict['BmiRange'] = '18.5 and 24.9'
        row_dict['HealthRisk'] = 'Low risk'
    elif bmi_value >= 25 and bmi_value <= 29.9:
        row_dict['BmiCategory'] = 'Overweight'
        row_dict['BmiRange'] = '25 and 29.9'
        row_dict['HealthRisk'] = 'Enhanced risk'
    elif bmi_value >= 30 and bmi_value <= 34.9:
        row_dict['BmiCategory'] = 'Moderately obese'
        row_dict['BmiRange'] = '30 and 34.9'
        row_dict['HealthRisk'] = 'Medium risk'
    elif bmi_value >= 35 and bmi_value <= 39.9:
        row_dict['BmiCategory'] = 'Severely obese'
        row_dict['BmiRange'] = '35 and 39.9'
        row_dict['HealthRisk'] = 'High risk'
    elif bmi_value >= 40:
        row_dict['BmiCategory'] = 'Very severely obese'
        row_dict['BmiRange'] = '40 and above'
        row_dict['HealthRisk'] = 'Very High risk'
        
    return row_dict
 
def run_bmi_observations(data):
    '''
    data @type: list of dict
    @return : dict with additional columns
    '''
    entries = []
    for row_dict in data:
        entries.append(bmi_calculation(row_dict))
        
    overweight_observations = filter(lambda row: row['BmiCategory'] == 'Overweight', entries)
    overweight_female_observations = filter(lambda row: row['BmiCategory'] == 'Overweight' and row['Gender'] == 'Female', entries)
    very_high_risk = filter(lambda row: row['HealthRisk'] == 'Very High risk', entries)
    
    print("Count of Overweight Observations: ", len(list(overweight_observations)))
    print("Count of Overweight Observations and Female Gender: ", len(list(overweight_female_observations)))
    print("Count of Very High Risk persons: ", len(list(very_high_risk)))
    
    return {'overweight_observations_count': len(list(overweight_observations)),
            'overweight_female_observations_count': len(list(overweight_female_observations)),
            'very_high_risk_count': len(list(very_high_risk))
            }
    

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--jsonFile', action='store', required=True)
    args = arg_parser.parse_args()
    json_file_path = args.jsonFile
    if os.path.exists(json_file_path):
        with open(json_file_path) as json_file:
            bmi_data = json.loads(json_file.read())
            run_bmi_observations(bmi_data)