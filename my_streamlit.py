import pandas as pd
import numpy as np
import streamlit as st

st.title("Welcome to my streamlit application.")
st.write("This is the simple text.")

# Create a DataFrame
df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
})

st.write("Here is the dataframe.")
st.write(df)  # This should display the DataFrame

# Create random data for the line chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])


# Call the line_chart function correctly
st.line_chart(chart_data)  # This should display the line chart
