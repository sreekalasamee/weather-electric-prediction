# import pandas as pd
# import joblib

# # Load the trained model
# model = joblib.load('electricity_model1.pkl')

# # Accept user inputs for features
# fan = int(input("Enter number of fans: "))
# refrigerator = int(input("Enter number of refrigerators: "))
# air_conditioner = int(input("Enter number of air conditioners: "))
# television = int(input("Enter number of televisions: "))
# monitor = int(input("Enter number of monitors: "))
# motor_pump = int(input("Enter number of motor pumps: "))
# temperature = float(input("Enter temperature: "))
# humidity = float(input("Enter humidity: "))
# monthly_hours = int(input("Enter monthly hours: "))
# tariff_rate = float(input("Enter tariff rate: "))

# # Create a DataFrame with user inputs
# user_data = {
#     'Fan': [fan],
#     'Refrigerator': [refrigerator],
#     'AirConditioner': [air_conditioner],
#     'Television': [television],
#     'Monitor': [monitor],
#     'MotorPump': [motor_pump],
#     'Temperature': [temperature],
#     'Humidity': [humidity],
#     'MonthlyHours': [monthly_hours],
#     'TariffRate': [tariff_rate]
# }

# # Make prediction
# predicted_bill = model.predict(pd.DataFrame(user_data))

# # Print predicted bill
# print(f"Predicted electricity bill: ${predicted_bill[0]}")


import pandas as pd
import joblib

def predict_elec(values):
    print("values ",values)
    # Load the trained model
    model = joblib.load('electricity_model1.pkl')

    user_data = {
    'Fan': [values[0]],
    'Refrigerator': [values[1]],
    'AirConditioner': [values[2]],
    'Television': [values[3]],
    'Monitor': [values[4]],
    'MotorPump': [values[5]],
    'Temperature': [values[6]],
    'Humidity': [values[7]],
    'MonthlyHours': [values[8]],
    'TariffRate': [values[9]]
}
    print(user_data,"////////////////////////")

    # Make prediction
    predicted_bill = model.predict(pd.DataFrame(user_data))


    # Print predicted bill
    print(f"Predicted electricity bill: {predicted_bill[0]}")
    return predicted_bill[0]
