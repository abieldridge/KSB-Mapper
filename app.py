import streamlit as st

# Sample KSBs for demonstration (replace with full data for each apprenticeship)
ksb_data = {
    "L2 Horticulture or Landscape Operative": [
        "K1: Principles of plant growth and development",
        "S1: Maintain plants and sites",
        "B1: Work safely and responsibly"
    ],
    "L3 Content Creator": [
        "K1: Principles of storytelling and audience engagement",
        "S1: Create and edit digital content",
        "B1: Take initiative and adapt to feedback"
    ]
}

# Streamlit UI
st.title("Apprenticeship KSB Mapper")

# Dropdown for apprenticeship selection
selected_standard = st.selectbox("Select your apprenticeship standard", list(ksb_data.keys()))

# Text area for learning reflection
entry = st.text_area("Describe what you learned or did:")

# Submit button
if st.button("Find Relevant KSBs"):
    if entry.strip() == "":
        st.warning("Please enter a reflection to analyze.")
    else:
        # Simple keyword-based matching (replace with AI logic for production)
        matched_ksbs = []
        for ksb in ksb_data[selected_standard]:
            if any(word.lower() in ksb.lower() for word in entry.split()):
                matched_ksbs.append(ksb)

        # Display results
        if matched_ksbs:
            st.subheader("Matched KSBs:")
            for ksb in matched_ksbs:
                st.write(f"- {ksb}")
        else:
            st.info("No direct matches found. Try expanding your reflection.")
