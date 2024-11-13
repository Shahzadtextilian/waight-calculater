import streamlit as st

# Function to convert weight to different units
def convert_weight(weight, unit_from, unit_to):
    if unit_from == 'Kilograms':
        weight_in_kg = weight
    elif unit_from == 'Grams':
        weight_in_kg = weight / 1000
    elif unit_from == 'Pounds':
        weight_in_kg = weight / 2.205
    elif unit_from == 'Ounces':
        weight_in_kg = weight / 35.274
    
    # Convert the weight in kilograms to the target unit
    if unit_to == 'Kilograms':
        return weight_in_kg
    elif unit_to == 'Grams':
        return weight_in_kg * 1000
    elif unit_to == 'Pounds':
        return weight_in_kg * 2.205
    elif unit_to == 'Ounces':
        return weight_in_kg * 35.274

# Title of the app
st.title("Weight Converter and Calculator")

# Sidebar for options
st.sidebar.header("Choose Your Units")

# Input fields
weight = st.number_input("Enter your weight", min_value=0.0, value=70.0, step=0.1)
unit_from = st.selectbox("Select the unit of your weight", ["Kilograms", "Grams", "Pounds", "Ounces"])
unit_to = st.selectbox("Select the unit to convert to", ["Kilograms", "Grams", "Pounds", "Ounces"])

# Calculate and display the converted weight
if st.button("Convert"):
    converted_weight = convert_weight(weight, unit_from, unit_to)
    st.write(f"{weight} {unit_from} is equal to {converted_weight:.2f} {unit_to}")
