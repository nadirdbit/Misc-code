import streamlit as st

# Add your own conditions if you like
conditions = {
    'Minimum 26 characters': lambda pw: len(pw) >= 26,
    'Maximum 52 characters': lambda pw: len(pw) <= 52,
    'At least one uppercase letter':
        lambda pw: any(char.isupper() for char in pw),
    'At least one lowercase letter':
        lambda pw: any(char.islower() for char in pw),
    'At least one number':
        lambda pw: any(char.isnumeric() for char in pw),
    'At least one special character':
        # Removed $ and & characters from the list of special characters
        lambda pw: any(char in ",.!?@#%^*()-_+=|\/:;<>~" for char in pw),
}


def get_password_properties(password):
    return {cond: check(password) for cond, check in conditions.items()}


st.title("Password Checker")
password_input = st.text_input("Enter your password", type="password")

if st.button("Check password!"):
    if password_input:
        properties = get_password_properties(password_input)

        # Loop through password conditions and show the status for each
        for condition, passes in properties.items():
            if passes:
                st.success(f'✔ Pass: {condition}')
            else:
                st.error(f'✖ Fail: {condition}')
    else:
        st.write("Please enter a password.")
