import streamlit as st

# 1. Create a function called calculate_delivery()
def calculate_delivery():
    st.title("📦 Delivery Fee Calculator")
    st.write("Enter package details below to calculate the final bill.")
    
    # Session state to hold multiple packages history (simulating multiple iterations)
    if 'packages_list' not in st.session_state:
        st.session_state.packages_list = []

    # 2. Inputs captured with correct data types inside the structure
    name = st.text_input("Customer Name (string):", value="Ali")
    weight = st.number_input("Package Weight in kg (float):", min_value=0.1, value=2.5, format="%.2f")
    distance = st.number_input("Delivery Distance in km (int):", min_value=1, value=5, step=1)
    is_fragile = st.selectbox("Is the package fragile? (yes/no):", ["no", "yes"])
    
    base_cost = 10.0  # Default base cost in dollars ($)
    surcharge = 0.0
    
    # Button to process current package and check constraints
    if st.button("Calculate Bill", type="primary"):
        
        # 3. Correct if/elif/else logic: Over 10km OR package is fragile
        if distance > 10 or is_fragile == "yes":
            surcharge = 5.0  # Add a $5 surcharge to the base cost
            st.info("ℹ️ $5 Surcharge applied due to long distance or fragile item.")
        else:
            surcharge = 0.0
            
        total_bill = base_cost + surcharge
        
        # Storing data into history list (simulating the while loop behavior until stopped)
        current_bill = {
            "Customer": name,
            "Weight": f"{weight} kg",
            "Distance": f"{distance} km",
            "Fragile": is_fragile.capitalize(),
            "Total Fee": f"${total_bill:.2f}"
        }
        st.session_state.packages_list.append(current_bill)
        
        # 4. Clean, accurate final output for the customer
        st.write("---")
        st.subheader("📄 Final Bill Output")
        st.write(f"**Customer Name:** {name}")
        st.write(f"**Package Weight:** {weight} kg")
        st.write(f"**Delivery Distance:** {distance} km")
        st.success(f"💰 **Total Delivery Fee: ${total_bill:.2f}**")

    # Displaying loop history table
    if st.session_state.packages_list:
        st.write("---")
        st.subheader("📋 Calculated Packages History")
        st.table(st.session_state.packages_list)
        
        # Action button to clear the loop (Simulating type 'stop')
        if st.button("Stop & Clear All Packages"):
            st.session_state.packages_list = []
            st.rerun()

# Calling the function to execute the program
calculate_delivery()
