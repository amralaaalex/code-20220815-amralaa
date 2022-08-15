# This simple code solve "BMI Calculator Offline Coding Challenge V7".

## Description:-
it is a simple and direct class that takes a list of json objects with needed information which is a list of json objects. it calculates BMI for each json object, counting how many of these objects/people are classified as overwieht or higher.

## Configuration and tests:
import the class, call it with the list of json and that's it.

```
import bmiCalculator from bmiCalculator

rows = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
    { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
    {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
calculator = bmiCalculator(rows)
calculator.update_rows_with_bmi()
#prinitng updated rows and overwight counter
print(calculator.rows, calculator.overweight_counter)
```

also you can run it with simple data providied in the challenge description by just calling the file itself

`python3 bmiCalculator.py` 

you can run tests for this class as follow:

`python3 test_bmi_calculator.py`
