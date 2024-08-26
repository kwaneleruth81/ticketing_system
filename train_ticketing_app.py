import streamlit as st

# Define ticket prices
ticket_prices = {
    'Economy': 15.00,
    'First Class': 30.00,
    'Sleeper': 50.00
}

# App title
st.title("Train Smart Ticketing System")

# Select ticket class
st.header("Choose Your Ticket Class")
ticket_class = st.selectbox("Select Class", list(ticket_prices.keys()))

# Display selected ticket price
st.subheader(f"Ticket Price for {ticket_class}: ${ticket_prices[ticket_class]:.2f}")

# Number of tickets
st.header("Select Number of Tickets")
num_tickets = st.number_input("Enter number of tickets", min_value=1, value=1)

# Calculate total cost
total_cost = num_tickets * ticket_prices[ticket_class]
st.subheader(f"Total Cost: ${total_cost:.2f}")

# Checkout button
if st.button("Proceed to Checkout"):
    st.success(f"Thank you for purchasing {num_tickets} {ticket_class} ticket(s)!")
    st.info(f"Total Amount Charged: ${total_cost:.2f}")
    st.write("Your tickets will be emailed to you shortly.")
