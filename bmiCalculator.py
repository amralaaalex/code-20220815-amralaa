import pprint


class bmiCalculator:

    def __init__(self, rows):
        ''' init function for calculator class
        args:
        rows: list of json objects, here's an example:
        [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
        { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }]
        '''
        self.rows = rows
        self.bmi_cat_health_risk_dict = {
            'Underweight': 'Malnutrition risk',
            'Normal weight': 'Low risk',
            'Overweight': 'Enhanced risk',
            'Moderately obese': 'Medium risk',
            'Severely obese': 'High risk',
            'Very severely obese': 'Very high risk',
            }
        self.overweight_counter = 0

    def calculate_bmi(self, mass, height):
        return round(mass/((height/100)**2),2)
    
    def catgeorize_bmi(self, bmi):
        if bmi <= 18.4:
            bmi_catgeory = 'Underweight'
            return bmi_catgeory
        elif bmi <= 24.9:
            bmi_catgeory = 'Normal weight'
            return bmi_catgeory
        #breaking elif block to update overweight counter and avoid repeating the same line in all coming cases
        self.overweight_counter += 1
        if bmi <= 29.9:
            bmi_catgeory = 'Overweight'
            return bmi_catgeory
        elif bmi <= 34.9:
            bmi_catgeory = 'Moderately obese'
            return bmi_catgeory
        elif bmi <= 39.9:
            bmi_catgeory = 'Severely obese'
            return bmi_catgeory
        else:
            bmi_catgeory = 'Very severely obese'
            return bmi_catgeory
    
    def update_rows_with_bmi(self):
        for row in self.rows:
            row['bmi'] = self.calculate_bmi(row.get('WeightKg'), row.get('HeightCm'))
            row['bmi_catgeory'] = self.catgeorize_bmi(row['bmi'])
            row['health_risk'] = self.bmi_cat_health_risk_dict.get(row['bmi_catgeory'])

def main():
    rows = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
            { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
            { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
            { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
    calculator = bmiCalculator(rows)
    calculator.update_rows_with_bmi()
    #returning updated rows and overwight counter
    return calculator.rows, calculator.overweight_counter

if __name__ == '__main__':
    updated_rows, counter = main()
    print ('updated json data:')
    pprint.pprint (updated_rows)
    print ('total number of overweight people:', counter)
