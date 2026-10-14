import streamlit as st
import pandas as pd
from importlib import import_module

ProfitCalculator = import_module("class.classes").ProfitCalculator

st.set_page_config(
    page_title="Uganda Agricultural Market System",
    layout="wide"
)

# LOAD DATA
farmers_df = pd.read_csv("farmers.csv")
prices_df = pd.read_csv("prices.csv")

# SIDEBAR
st.sidebar.title(" Uganda Market System")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Market Prices",
        "Farmer Records",
        "Profit Calculator"
    ]
)

# DASHBOARD
if menu == "Dashboard":
    st.title("Uganda Agricultural Market System")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Farmers",
            len(farmers_df)
        )
    with col2:
        st.metric(
            "Products",
            prices_df["Produce"].nunique()
        )
    with col3:
        st.metric(
            "Districts",
            farmers_df["District"].nunique()
        )
    st.subheader("Registered Farmers")
    st.dataframe(
        farmers_df,
        width='stretch'
    )

# MARKET PRICES
elif menu == "Market Prices":

    st.title("Current Market Prices")

    search = st.text_input(
        "Search Produce"
    )

    filtered = prices_df[
        prices_df["Produce"]
        .str.contains(search, case=False, na=False)
    ]
    st.dataframe(
        filtered,
        width='stretch'
    )

# FARMER RECORDS
elif menu == "Farmer Records":
    st.title("Farmer Records")
    with st.form("farmer_form"):
        name = st.text_input("Farmer Name")
        district = st.text_input("District")
        produce = st.text_input("Produce")
        quantity = st.number_input(
            "Quantity",
            min_value=1,
        )
        submit = st.form_submit_button(
            "Add Farmer"
        )
        if submit:
            new_row = pd.DataFrame({
                "Name": [name],
                "District": [district],
                "Produce": [produce],
                "Quantity": [quantity]
            })
            farmers_df = pd.concat(
                [farmers_df, new_row],
                ignore_index=True
            )
            farmers_df.to_csv(
                "farmers.csv",
                index=False
            )
            st.success(
                "Farmer Added Successfully"
            )
    st.subheader("All Farmers")
    st.dataframe(
        farmers_df,
        width='stretch'
    )

# PROFIT CALCULATOR
elif menu == "Profit Calculator":
    st.title("Profit Calculator")
    quantity = st.number_input(
        "Quantity (Kg)",
        min_value=0.0
    )
    price = st.number_input(
        "Price Per Kg",
        min_value=0.0
    )

    transport = st.number_input(
        "Transport Cost",
        min_value=0.0
    )
    if st.button("Calculate"):
        profit = ProfitCalculator.calculate(
            quantity,
            price,
            transport
        )
        st.success(
            f"Expected Profit: UGX {profit:,.0f}"
        )