# 🚗 Odd-Even Vehicle Rule Checker

Welcome to the Odd-Even Vehicle Rule Checker! This project is inspired by real-world traffic control policies that aim to reduce congestion and pollution. With a simple and intuitive interface, you can easily verify whether your vehicle is allowed to drive on a specific day based on the vehicle number's parity and today's date.

## ✨ Features
- **Odd-Even Rule Checking**: Determine whether your vehicle is allowed to drive today based on the odd or even status of the last digit of its number in comparison to today’s date.
- **User-Friendly Interface**: A simple, clean UI powered by Streamlit makes checking your vehicle status a breeze.
- **Interactive Progress Bar**: Get real-time visual feedback while checking your vehicle number.
- **Helpful Messages**: Users receive clear success, warning, or error messages based on input validation and rule checking.

## 🛠 Installation

To run this application locally, you need to have Python installed on your machine. Follow these steps to get started:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/odd-even-vehicle-checker.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd odd-even-vehicle-checker
   ```

3. **Install dependencies**:
   It's recommended to use a uv to manage dependencies.
   ```bash
   pip install uv
   uv sync
   ```
3. **Virtual Enviroment Activate**:
   It's recommended to use a virtual environment to run project.
   1.  **Mac OS**:
   ```bash
   source .venv/bin/activate 
   ```
   2.  **Window OS**:
   ```bash
   .venv/Scripts/activate 
   ```
## 🚀 Usage

Once you have installed the dependencies, you can run the app using:
```bash
streamlit run app.py
```
Visit the URL provided in the terminal (typically `http://localhost:8501`) to use the application.

## 📖 Example

1. **Open the app**:
   Use the provided Streamlit command to launch the app.

2. **Enter your vehicle number**:
   Type your complete vehicle number (e.g., DL3CAF1234) in the input field.

3. **Check your result**:
   Click the "Check Parking 🅿️" button. The app will process your input and inform you if you are allowed to drive based on the odd-even rule.

## 📜 License

This project does not specify a license, but contributions and usage should follow best open-source practices.

---

Made with ❤️ by [Krishi Devani](https://github.com/KrishiDevani15)  
If you find this app helpful, consider making a contribution or buying me a virtual coffee! ☕
