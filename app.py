import streamlit as st

# Title of the application
st.title('Simple Calculator')

# Get user input for two numbers
num1 = st.number_input('Enter the first number:')
num2 = st.number_input('Enter the second number:')

# Dropdown menu for selecting operation
operation = st.selectbox('Select operation:', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

# Perform calculation based on selected operation
if operation == 'Addition':
    result = num1 + num2
    st.write('Result:', result)
elif operation == 'Subtraction':
    result = num1 - num2
    st.write('Result:', result)
elif operation == 'Multiplication':
    result = num1 * num2
    st.write('Result:', result)
elif operation == 'Division':
    if num2 == 0:
        st.write('Error: Cannot divide by zero!')
    else:
        result = num1 / num2
        st.write('Result:', result)
