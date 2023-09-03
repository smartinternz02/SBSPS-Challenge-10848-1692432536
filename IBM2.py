import math

def calculate_gas_concentration(Q, u, H, x, y):
    """
    Q: Emission rate of the gas (kg/s)
    u: Wind speed (m/s)
    H: Mixing height (m)
    x: Downwind distance (m)
    y: Crosswind distance (m)
    """
    sigma_y = 0.3 * x ** 0.5 #
    sigma_z = 0.3 * H #
    t1 = (Q / (2 * math.pi * u * sigma_y * sigma_z))
    t2 = math.exp(-(y ** 2) / (2 * sigma_y ** 2))
    t3 = (1 - math.exp(-H / (2 * sigma_z ** 2)))
    C = (t1) * (t2) * (t3)
    return C

emission_rate = float(input("enter the rate of emission in kg/s:"))
wind_speed = float(input("enter the wind speed in m/s:"))
chimney_height = float(input("enter the height of the chimney in m:"))
downwind_distance = float(input("enter the downward distance in m:")) 
crosswind_distance = float(input("enter the crosswind distance in m:"))


concentration = calculate_gas_concentration(emission_rate, wind_speed, chimney_height, downwind_distance, crosswind_distance)
print(f"Gas concentration: {concentration} kg/m³")

