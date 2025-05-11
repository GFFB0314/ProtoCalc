# Project Title: **ProtoCalc** 🧮

Welcome to **ProtoCalc** – a sleek, touch-friendly calculator app built with [Kivy](https://kivy.org/) that brings powerful math and trigonometry functions right to your desktop or mobile device! Whether you need quick arithmetic, percentages, or advanced trig operations, ProtoCalc delivers a smooth, intuitive experience across platforms.

---

## Table of Contents
- [Project Title: **ProtoCalc** 🧮](#project-title-protocalc-)
  - [Table of Contents](#table-of-contents)
  - [About the Project 📖](#about-the-project-)
  - [Technologies \& Libraries Used 🛠️](#technologies--libraries-used-️)
  - [Getting Started 🚀](#getting-started-)
  - [Usage Guide 📝](#usage-guide-)
  - [Building an Executable 🔧](#building-an-executable-)
  - [Contributing 🤝](#contributing-)
  - [Contact 📬](#contact-)

---

## About the Project 📖

**ProtoCalc** is a lightweight, cross-platform calculator built using the Kivy framework. Designed for speed and simplicity, it supports:

- Basic arithmetic (`+`, `-`, `×`, `÷`)
- Decimal entry and correction
- Percentage conversion
- Sign toggle (±)
- Backspace/delete
- Euler’s number (`e`)
- Trigonometric functions (`sin`, `cos`, `tan`) and their inverses (`asin`, `acos`, `atan`)

With intuitive touch and keyboard controls, `ProtoCalc` is perfect for students, professionals, and anyone needing a reliable, easy-to-use calculation tool.

---

## Technologies & Libraries Used 🛠️

The project is built with the following key modules and frameworks:

- **Python 3.7+**: The programming language powering the app.
  
- **Kivy**: A modern, open-source Python framework for cross-platform applications.
  
- **re**: Python’s regular expressions module for parsing and converting input expressions.
  
- **math**: Python’s math library for accurate trigonometric and arithmetic operations.

All other dependencies are part of the Python standard library—no extra downloads required!

---

## Getting Started 🚀
**Prerequisites** 📌
Before you start, ensure you have the following installed on your system:

- Python 3.7 or higher
  
- pip (Python package installer)

Additionally, you will need to have a Git client installed to clone the repository.

**Installation Steps** 🛠️
1. **Clone the Repository**
   Open your terminal or command prompt and run:
   ```bash
   git clone https://github.com/GFFB0314/ProtoCalc.git
   ```
   This command will create a local copy of the project on your machine.

2. **Navigate to the Project Directory**
   Change to the project directory:
   ```bash
   cd ProtoCalc
   ```

3. **Install the Required Libraries**
   Install the dependencies using `pip`:
   ```bash
   pip install kivy black mypy pylint pytest
   ```
   **Note**: `re` and `math` are built-in modules in Python and do not require installation

4. **Verify Installation**
   Ensure that all packages are correctly installed by running:
   ```bash
   pip list 
   ```
   This should display a list of installed packages, including all the dependencies mentioned.

---

## Usage Guide 📝
Once the installation is complete, you can start using **ProtoCalc**. Here’s how:
1. **Run the Application**
   To run the application, simply execute your main Python script:
   ```bash
   python main.py 
   ```
    The ProtoCalc window will open with a responsive, touch-friendly interface.

2. **Entering Numbers & Operators**
    - Tap or click the on-screen buttons, or use your keyboard keys (0–9, +, -, *, /).

    - Use `.` or `,` for decimal points.

3. **Special Functions**
    `%`: Converts the current number to its percentage (divides by 100).

    `±`: Toggles the sign of the current entry.

    `⌫ / Backspace`: Deletes the last digit or operator.

    `C / Escape`: Clears the entire input, resetting to 0.

    `e / E`: Inserts Euler’s number.

    `sin / cos / tan`: Calculates trig of the current angle in degrees.

    `asin / acos / atan`: Calculates the inverse trig, yielding an angle in degrees.

4. **Keyboard Shortcuts**
    `Enter or =`: Compute the result.

    `Shift+5`: %

    `Shift+8`: ×

    `Shift+=`: +

    `Backspace`: Delete

    `Escape / c / C`: Clear

    `n / N`: ± toggle

---

## Building an Executable 🔧
To distribute ProtoCalc as a standalone application, follow these steps:
1. **Edit the Spec File**
   Locate the spec file (e.g., ProtoCalc.spec) in the repository. Modify it if necessary to adjust settings such as the application name, icon, or additional data files.
2. **Generate the Executable**
    Run the following command to build the executable:
    ```bash
    pyinstaller ProtoCalc.spec
    ```
    This command uses PyInstaller to package the application into an executable file, making it easy to distribute and run on machines without Python pre-installed.
    **Note**: Ensure `pyinstaller` is correctly installed in your computer. 
    Run the following command to install `pyinstaller`
    ```bash
    pip install pyinstaller
    ```
3. **Locate the Executable**
   After the build process completes, you will find the executable in the dist folder within your project directory. You can now share this executable with your users! The executable may not work when located inside the `dist` folder, cut and paste it in the `root` directory containing your `python` and `kivy` files.

---

## Contributing 🤝
We welcome contributions from the community! If you'd like to improve xSAVE, please fork the repository and submit a pull request. Before making significant changes, feel free to open an issue to discuss your ideas. All contributions, whether code, documentation, or bug reports, are greatly appreciated!
Fork the repo.

- Create a feature branch `git checkout -b feature/YourFeature`.

- Commit your changes `git commit -m "Add awesome feature"`.

- Push to the branch `git push origin feature/YourFeature`.

- Open a Pull Request describing your changes.

Please ensure that your code follows PEP 8 style guidelines and includes meaningful commit messages.

---

## Contact 📬
For any questions, issues, or suggestions, please feel free to contact us at:
- Email: gbetnkom.bechir@gmail.com
- GitHub Issues: [Project Issues](https://github.com/GFFB0314/ProtoCalc/issues)

Thanks for using ProtoCalc! 🧮 Happy calculating! 😊