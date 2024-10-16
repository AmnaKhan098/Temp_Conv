import streamlit as st

# Set a custom background color
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f5f9;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title and description
st.title("🌡️ Interactive Temperature Converter")
st.write("Convert temperatures easily between Celsius, Fahrenheit, and Kelvin.")

# Divider
st.markdown("---")

# User input for the temperature value
temperature = st.number_input(
    "Enter the temperature value you want to convert:",
    min_value=-273.15,
    max_value=10000.0,
    value=0.0,
    step=0.1,
    format="%.2f",
    help="You can enter a value between -273.15 and 10,000."
)

# Dropdowns for current and target units
st.subheader("Select Temperature Units")
col1, col2 = st.columns(2)

with col1:
    current_unit = st.selectbox(
        "Current Temperature Unit",
        ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"],
        help="Choose the unit of the temperature you are converting from."
    )

with col2:
    target_unit = st.selectbox(
        "Target Temperature Unit",
        ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"],
        help="Choose the unit you want to convert the temperature to."
    )

# Button for conversion and result output
st.markdown("---")
if st.button("🔄 Convert Temperature"):
    unit_mapping = {"Celsius (°C)": "C", "Fahrenheit (°F)": "F", "Kelvin (K)": "K"}

    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15

    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32

    def convert_temperature(temp, current, target):
        if current == target:
            return temp
        if current == 'C':
            if target == 'F':
                return celsius_to_fahrenheit(temp)
            elif target == 'K':
                return celsius_to_kelvin(temp)
        elif current == 'F':
            if target == 'C':
                return fahrenheit_to_celsius(temp)
            elif target == 'K':
                return fahrenheit_to_kelvin(temp)
        elif current == 'K':
            if target == 'C':
                return kelvin_to_celsius(temp)
            elif target == 'F':
                return kelvin_to_fahrenheit(temp)
        return None

    # Perform conversion
    result = convert_temperature(temperature, unit_mapping[current_unit], unit_mapping[target_unit])

    # Display result with color coding and formatting
    if result is not None:
        st.success(f"**{temperature}°{unit_mapping[current_unit]}** is equal to **{result:.2f}°{unit_mapping[target_unit]}**")
    else:
        st.error("Error: Invalid conversion units.")
