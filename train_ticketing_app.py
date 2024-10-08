import streamlit as st

# Set a background image
st.markdown(
    """
    <style>
    .main {
        background-image: url("https://media.istockphoto.com/id/1211274325/photo/train-wagons-carrying-cargo-containers-for-shipping-companies.webp?b=1&s=612x612&w=0&k=20&c=PQNSFEL-xDNe1LhrOr3cPk313ApYuKYYdSPtBAgXnJE=");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #333333;
    }
    h1, h2, h3 {
        color: #ffffff;
        font-family: 'Arial';
    }
    .stButton>button {
        background-color: #4CAF50;
        color: black;
        font-size: 16px;
    }
    .stSelectbox>div>div>div>div>div>div {
        color: #2c3e50;
        font-size: 18px;
    }
    .stNumberInput>div>div>div>input {
        color: #2c3e50;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Conversion rates
conversion_rates = {
    'USD ($)': 1,
    'Zig (ZWG)': 15,
    'Rand (ZAR)': 18.5
}

# Define ticket prices in USD
ticket_prices_usd = {
    'Economy': 15.00,
    'First Class': 30.00,
    'Sleeper': 50.00
}

# App title
st.title("Smart Train Ticketing System")

# Currency selection
st.sidebar.header("Currency")
currency = st.sidebar.selectbox("Select Currency", list(conversion_rates.keys()))

# Convert prices to the selected currency
ticket_prices = {k: v * conversion_rates[currency] for k, v in ticket_prices_usd.items()}

# Origin and Destination
st.sidebar.header("Journey Details")
origin = "Bulawayo"
destination = st.sidebar.selectbox("Select Destination", ['Harare', 'Masvingo', 'Mutare', 'Hwange', 'Victoria Falls'])

# Select ticket class
st.header("Choose Your Ticket Class")
ticket_class = st.selectbox("Select Class", list(ticket_prices.keys()))

# Display selected ticket price
st.subheader(f"Ticket Price for {ticket_class} in {currency}: {ticket_prices[ticket_class]:.2f}")

# Number of tickets
st.header("Select Number of Tickets")
num_tickets = st.number_input("Enter number of tickets", min_value=1, value=1)

# Calculate total cost
total_cost = num_tickets * ticket_prices[ticket_class]
st.subheader(f"Total Cost: {total_cost:.2f} {currency}")

# Checkout button
if st.button("Proceed to Checkout"):
    st.success(f"Thank you for purchasing {num_tickets} {ticket_class} ticket(s) from {origin} to {destination}!")
    st.info(f"Total Amount Charged: {total_cost:.2f} {currency}")
    st.write("Your tickets will be emailed to you shortly.")
