# Apprenticeship KSB Mapper

This is a Streamlit app that allows apprentices to select their apprenticeship standard, enter a learning reflection, and receive matched Knowledge, Skills, and Behaviours (KSBs).

## How to Deploy on Streamlit Cloud

1. Create a GitHub account (if you don't have one).
2. Create a new repository and upload the following files:
   - `app.py`
   - `requirements.txt`
   - `README.md`
3. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in with GitHub.
4. Click "New App" and select your repository.
5. Click "Deploy" — your app will be live in seconds!

## How to Use

1. Select your apprenticeship standard from the dropdown.
2. Enter a reflection about what you learned or did.
3. Click "Find Relevant KSBs" to see matched KSBs.

## Notes

- This prototype uses simple keyword matching. For production, you can integrate AI-based semantic matching.
- You can expand the `ksb_data` dictionary in `app.py` with full KSBs for each apprenticeship.
