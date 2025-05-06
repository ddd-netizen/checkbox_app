import streamlit as st

st.title("Choose Your Favorite Birds")

# List of birds
birds = ["Parrot", "Eagle", "Peacock", "Sparrow"]

# Show checkboxes
selected_birds = []
for bird in birds:
    if st.checkbox(bird):
        selected_birds.append(bird)

# Display selection
if selected_birds:
    st.write("You selected:")
    for bird in selected_birds:
        st.write(f"🐦 {bird}")
else:
    st.write("No birds selected.")