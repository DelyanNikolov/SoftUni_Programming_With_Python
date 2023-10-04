def transform_grade(data):
    if 2.00 <= data <= 2.99:
        return "Fail"
    elif 3.00 <= data <= 3.49:
        return "Poor"
    elif 3.50 <= data <= 4.49:
        return "Good"
    elif 4.50 <= data <= 5.49:
        return "Very Good"
    elif 5.50 <= data <= 6.00:
        return "Excellent"


data = float(input())
print(transform_grade(data))
