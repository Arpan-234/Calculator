# 🔢 Advanced Calculator

A production-ready calculator application built with Python and Streamlit. Features basic and advanced mathematical operations with a clean, user-friendly interface.

## Features

✨ **Basic Operations**
- Addition (+)
- Subtraction (-)
- Multiplication (×)
- Division (÷)

🔬 **Advanced Operations**
- Square Root (√)
- Power (^)
- Percentage (%)
- Factorial (!)

📊 **Additional Features**
- Real-time calculation results
- Comprehensive calculation history with timestamps
- Dark/Light theme toggle
- Error handling for invalid inputs
- Support for decimal numbers
- Clean, intuitive user interface

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Local Setup

1. Clone the repository:
```bash
git clone https://github.com/Arpan-234/Calculator.git
cd Calculator
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

The calculator will open in your default browser at `http://localhost:8501`

## Deployment on Streamlit Cloud

### Steps:

1. **Fork the Repository** (optional) or ensure you have access to your own GitHub repository

2. **Go to Streamlit Cloud**:
   - Visit https://streamlit.io/cloud
   - Click "Create app"

3. **Connect GitHub**:
   - Select your GitHub repository (Calculator)
   - Select the branch (main)
   - Set the main file path to `app.py`

4. **Deploy**:
   - Click "Deploy"
   - Streamlit will automatically install dependencies from `requirements.txt` and run the app

## Live Demo

Once deployed, your calculator will be accessible at a URL like:
`https://[your-username]-calculator.streamlit.app`

## Usage

1. **Number Input**: Click number buttons (0-9) or use decimal point
2. **Operations**: Click operation buttons (+, -, ×, ÷, ^)
3. **Calculate**: Click = to see the result
4. **Advanced Operations**: Use √, %, or ! for advanced calculations
5. **Clear**: Click "Clear" to reset the calculator
6. **History**: View all your previous calculations with timestamps
7. **Theme**: Toggle dark/light mode with the checkbox

## Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Language**: Python 3
- **Math**: Python's built-in `math` module
- **Styling**: Custom CSS

## Project Structure

```
Calculator/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── .gitignore         # Git ignore file
```

## Error Handling

The calculator includes robust error handling for:
- Division by zero
- Square root of negative numbers
- Factorial of non-integers
- Invalid number formats
- Mathematical overflow

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have suggestions, please create an issue on the GitHub repository.

---

**Created with ❤️ using Streamlit**
