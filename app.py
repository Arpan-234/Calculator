import streamlit as st
import math
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Advanced Calculator",
    page_icon="🔢",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize session state variables
def initialize_session_state():
    """Initialize all session state variables"""
    if 'current_number' not in st.session_state:
        st.session_state.current_number = "0"
    if 'previous_number' not in st.session_state:
        st.session_state.previous_number = None
    if 'operation' not in st.session_state:
        st.session_state.operation = None
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'new_number' not in st.session_state:
        st.session_state.new_number = True
    if 'dark_theme' not in st.session_state:
        st.session_state.dark_theme = True

initialize_session_state()

# Apply custom CSS styling
def apply_custom_css():
    """Apply custom CSS for calculator styling"""
    theme_bg = "#1E1E1E" if st.session_state.dark_theme else "#FFFFFF"
    theme_text = "#FFFFFF" if st.session_state.dark_theme else "#000000"
    display_bg = "#2D2D2D" if st.session_state.dark_theme else "#F0F0F0"
    button_bg = "#3D3D3D" if st.session_state.dark_theme else "#E0E0E0"
    button_hover = "#4D4D4D" if st.session_state.dark_theme else "#D0D0D0"
    operator_bg = "#FF9500"
    
    st.markdown(f"""
    <style>
    .stApp {{
        background-color: {theme_bg};
    }}
    .calculator-display {{
        background-color: {display_bg};
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: right;
        font-size: 48px;
        font-weight: bold;
        color: {theme_text};
        min-height: 80px;
        word-wrap: break-word;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.2);
    }}
    .stButton > button {{
        width: 100%;
        height: 70px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        border: none;
        background-color: {button_bg};
        color: {theme_text};
        transition: all 0.3s;
    }}
    .stButton > button:hover {{
        background-color: {button_hover};
        transform: scale(1.05);
    }}
    .history-section {{
        background-color: {display_bg};
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        max-height: 300px;
        overflow-y: auto;
    }}
    h1, h2, h3 {{
        color: {theme_text} !important;
    }}
    </style>
    """, unsafe_allow_html=True)

apply_custom_css()

# Mathematical operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def percentage(a):
    return a / 100

def factorial(a):
    if a < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if not a.is_integer():
        raise ValueError("Factorial only works with integers")
    return math.factorial(int(a))

# Calculator functions
def append_number(number):
    """Append a number to the current display"""
    if st.session_state.new_number:
        st.session_state.current_number = str(number)
        st.session_state.new_number = False
    else:
        if st.session_state.current_number == "0" and number != ".":
            st.session_state.current_number = str(number)
        else:
            st.session_state.current_number += str(number)

def set_operation(op):
    """Set the operation and store the previous number"""
    try:
        st.session_state.previous_number = float(st.session_state.current_number)
        st.session_state.operation = op
        st.session_state.new_number = True
    except ValueError:
        st.error("Invalid number format")

def calculate_result():
    """Calculate the final result based on operation"""
    if st.session_state.previous_number is None or st.session_state.operation is None:
        return
    
    try:
        current = float(st.session_state.current_number)
        previous = st.session_state.previous_number
        operation = st.session_state.operation
        
        operations = {
            '+': add,
            '-': subtract,
            '×': multiply,
            '÷': divide,
            '^': power
        }
        
        if operation in operations:
            result = operations[operation](previous, current)
        else:
            return
        
        # Add to history
        history_entry = f"{previous} {operation} {current} = {result}"
        st.session_state.history.insert(0, {
            'calculation': history_entry,
            'timestamp': datetime.now().strftime("%H:%M:%S")
        })
        
        # Update display
        st.session_state.current_number = str(result)
        st.session_state.previous_number = None
        st.session_state.operation = None
        st.session_state.new_number = True
    except ValueError as e:
        st.error(f"Error: {str(e)}")
        clear_calculator()
    except Exception as e:
        st.error(f"Calculation error: {str(e)}")
        clear_calculator()

def calculate_unary_operation(operation):
    """Calculate operations that work on a single number"""
    try:
        current = float(st.session_state.current_number)
        
        if operation == '√':
            result = square_root(current)
            history_entry = f"√{current} = {result}"
        elif operation == '%':
            result = percentage(current)
            history_entry = f"{current}% = {result}"
        elif operation == '!':
            result = factorial(current)
            history_entry = f"{current}! = {result}"
        else:
            return
        
        st.session_state.history.insert(0, {
            'calculation': history_entry,
            'timestamp': datetime.now().strftime("%H:%M:%S")
        })
        
        st.session_state.current_number = str(result)
        st.session_state.new_number = True
    except ValueError as e:
        st.error(f"Error: {str(e)}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

def clear_calculator():
    """Clear the calculator"""
    st.session_state.current_number = "0"
    st.session_state.previous_number = None
    st.session_state.operation = None
    st.session_state.new_number = True

def clear_history():
    """Clear the history"""
    st.session_state.history = []

# Main UI
st.title("🔢 Advanced Calculator")

# Display and controls
col1, col2 = st.columns([4, 1])
with col1:
    st.markdown(f'<div class="calculator-display">{st.session_state.current_number}</div>', unsafe_allow_html=True)
with col2:
    st.session_state.dark_theme = st.checkbox("Dark", value=st.session_state.dark_theme)

# Number buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("7", use_container_width=True, key="7"):
        append_number(7)
    if st.button("4", use_container_width=True, key="4"):
        append_number(4)
    if st.button("1", use_container_width=True, key="1"):
        append_number(1)
    if st.button("0", use_container_width=True, key="0"):
        append_number(0)

with col2:
    if st.button("8", use_container_width=True, key="8"):
        append_number(8)
    if st.button("5", use_container_width=True, key="5"):
        append_number(5)
    if st.button("2", use_container_width=True, key="2"):
        append_number(2)
    if st.button(".", use_container_width=True, key="."):
        append_number(".")

with col3:
    if st.button("9", use_container_width=True, key="9"):
        append_number(9)
    if st.button("6", use_container_width=True, key="6"):
        append_number(6)
    if st.button("3", use_container_width=True, key="3"):
        append_number(3)
    if st.button("=", use_container_width=True, key="="):
        calculate_result()

with col4:
    if st.button("+", use_container_width=True, key="+"):
        set_operation("+")
    if st.button("-", use_container_width=True, key="-"):
        set_operation("-")
    if st.button("×", use_container_width=True, key="×"):
        set_operation("×")
    if st.button("÷", use_container_width=True, key="÷"):
        set_operation("÷")

# Advanced operations
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("√", use_container_width=True, key="sqrt"):
        calculate_unary_operation("√")
with col2:
    if st.button("^", use_container_width=True, key="power"):
        set_operation("^")
with col3:
    if st.button("%", use_container_width=True, key="percent"):
        calculate_unary_operation("%")
with col4:
    if st.button("!", use_container_width=True, key="factorial"):
        calculate_unary_operation("!")

# Clear buttons
col1, col2 = st.columns(2)
with col1:
    if st.button("Clear", use_container_width=True, key="clear"):
        clear_calculator()
with col2:
    if st.button("Clear History", use_container_width=True, key="clear_history"):
        clear_history()

# History section
if st.session_state.history:
    st.markdown("### 📊 Calculation History")
    for i, item in enumerate(st.session_state.history[:10]):
        st.text(f"{item['timestamp']} - {item['calculation']}")
