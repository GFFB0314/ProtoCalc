"""STILL NEED TO TREAT DECIMAL NUMBERS ACCURATELY"""
import time
import re
import math
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window  # For window size and keyboard
from kivy.config import Config  # For setting keyboard mode

# Set the window size
Window.size = (500, 630)

# Set the keyboard mode to system
Config.set("kivy", "keyboard_mode", "system")

# Load the KV file
Builder.load_file("main.kv")


def infos(func):
    """Decorator"""

    def wrapper(self, *args, **kwargs):
        """Closing Infos"""

        print("About to leave the App")
        func(self, *args, **kwargs)
        print("Left the App!")

    return wrapper


class CalculatorLayout(Widget):
    """This class is the main layout of the calculator."""

    def __init__(self, **kwargs):
        """Class Initialization"""

        super().__init__(**kwargs)  # Initialize the parent class properly

        # Initialize the keyboard
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)

        # Bind the keyboard to the window
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self) -> None:
        """Called when keyboard is released"""

        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers) -> bool:
        """Handle keyboard input"""

        key = keycode[1]  # Get the key character
        shift_pressed = "shift" in modifiers

        # First handle special shifted characters
        if shift_pressed:
            if key == "8":
                self.operator_sign("\u00d7")  # Shift+8 = *
                return True
            elif key == "5":
                self.percentage()  # Shift+5 = %
                return True
            elif key == "=":
                self.operator_sign("+")  # Shift+= is +
                return True
            elif key == "0":
                self.button_press("00")  # Shift+0 = 00
                return True

        # Then handle unshifted keys
        key_mapping = {
            "0": lambda: self.button_press(0),
            "1": lambda: self.button_press(1),
            "2": lambda: self.button_press(2),
            "3": lambda: self.button_press(3),
            "4": lambda: self.button_press(4),
            "5": lambda: self.button_press(5),
            "6": lambda: self.button_press(6),
            "7": lambda: self.button_press(7),
            "8": lambda: self.button_press(8),
            "9": lambda: self.button_press(9),
            "e": self.euler,  # euler key
            "E": self.euler,  # euler key (shifted)
            "=": self.calculate,
            "enter": self.calculate,  # Enter key
            "backspace": self.remove,  # Backspace
            "escape": self.clear,  # Escape (clear instead of closing)
            "delete": self.clear,  # Delete key also clears
            "c": self.clear,
            "C": self.clear,
            "n": self.pos_neg,  # For +/- functionality
            "N": self.pos_neg,
            "-": lambda: self.operator_sign("-"),
            "/": lambda: self.operator_sign("\u00f7"),
            "+": lambda: self.operator_sign("+"),  # Regular + key (numpad)
            ".": self.dot,
            ",": self.dot,  # Some keyboards use comma for decimal
        }

        if key in key_mapping:
            key_mapping[key]()
            return True  # Inidciate we handled the key event

        return False  # Let other keys pass through

    def clear(self) -> None:
        """Clear the textinput and place 0 instead"""

        self.ids.cal_input.text = "0"

    def pos_neg(self) -> None:
        """Change the sign of the integer. Either from positive to negative or vice-versa"""

        prior: str = self.ids.cal_input.text

        # Prevent the method from working if prior is ComplexInfinity or Error
        if prior in ["ComplexInfinity", "Error"]:
            return

        print(prior)
        if "-" not in prior:
            self.ids.cal_input.text = f"-{prior}"
        else:
            self.ids.cal_input.text = f"{prior.replace("-", "")}"

    def remove(self):
        """Deleting the last character"""

        prior: str = self.ids.cal_input.text

        # Prevent the method from working if prior is ComplexInfinity or Error
        if prior in ["ComplexInfinity", "Error"]:
            return

        if len(prior) > 1:
            self.ids.cal_input.text = prior[:-1]  # Remove the last character
        else:
            self.ids.cal_input.text = str(0)  # Default value

    def operator_sign(self, op: str):
        """Display the respective operator sign on the screen"""

        if self.ids.cal_input.text in ["ComplexInfinity", "Error"]:
            return  # Prevent the method from working if prior is ComplexInfinity or Error

        self.ids.cal_input.text += f"{op}"

    def button_press(self, button: int) -> None:
        """Display numbers on the screen"""

        prior: str = self.ids.cal_input.text

        # Prevent the method from working if prior is ComplexInfinity or Error
        if prior in ["ComplexInfinity", "Error"]:
            return

        if prior == "0":
            self.ids.cal_input.text = ""
            self.ids.cal_input.text += f"{button}"

        else:
            self.ids.cal_input.text += f"{button}"

    def percentage(self) -> None:
        """Append % only if last char is a digit, convert N% → N/100, then evaluate."""

        prior: str = self.ids.cal_input.text
        print(f"⚙️ percentage() called, display = '{prior}'")

        # don’t proceed on existing error states
        if prior in ["Error", "ComplexInfinity"]:
            print("⚠️ display is error state—aborting")
            return

        # ensure last character is a digit
        if not prior or not prior[-1].isdigit():
            print("❌ Cannot append % — last character is not a digit")
            self.ids.cal_input.text = "Error: not a number"
            return

        # append % so user sees it
        display_with_pct = prior + "%"
        self.ids.cal_input.text = display_with_pct
        print(f"✅ appended %, display now: '{display_with_pct}'")

        # build Python‑safe expression
        op_pattern = r"(\d+(\.\d+)?)%"  # matches N or N.N followed by %
        repl_pattern = lambda m: f"({float(m.group(1))}/100)"
        expr = display_with_pct.replace("×", "*").replace("÷", "/")
        expr = re.sub(op_pattern, repl_pattern, expr)
        print(f"🔄 converted to eval‑expr: '{expr}'")

        try:
            result = eval(expr)
            print(f"▶️ raw eval result: {result}")

            # format to three decimals
            formatted = f"{result:.3f}"
            print(f"🔧 formatted result: {formatted}")

            self.ids.cal_input.text = formatted
            print(f"🏁 final display: '{formatted}'")

        except Exception as e:
            print(f"❌ Error in percentage(): {e}")
            self.ids.cal_input.text = "Error"

    def dot(self):
        """Adds a dot to the number"""

        prior: str = self.ids.cal_input.text

        multiply_sign = chr(0x00D7)  # ×
        division_sign = chr(0x00F7)  # ÷

        # Prevent the method from working if prior is ComplexInfinity or Error
        if prior in ["ComplexInfinity", "Error"]:
            return

        # Identify the last part of the expression (after the last operator)
        operators: list = ["+", "-", multiply_sign, division_sign]
        last_op_index: int = max(prior.rfind(op) for op in operators)
        # Last part is the last number of the operation
        last_part: str = prior[last_op_index + 1 :] if last_op_index != -1 else prior
        print(f"🔍 last operator at index {last_op_index}, last_part = '{last_part}'")

        # Add a dot only if the last part doesn't already contain a dot
        if "." not in last_part:
            self.ids.cal_input.text = f"{prior}."

    def calculate(self):
        """Calculate the result of the expression"""

        prior: str = self.ids.cal_input.text
        # Replace Unicode math symbols with Python operators
        prior = (
            prior.replace("\u00d7", "*")
            .replace("\u00f7", "/")
            .replace("e", f"{math.e:.3f}")
        )
        print(f"⚙️ calculate() called, display = '{prior}'")

        try:
            result = eval(prior)
            print(result)
            # if isinstance(result, float):
            # result = "{:.3f}".format(result)
            self.ids.cal_input.text = str(result)
        except ZeroDivisionError:
            self.ids.cal_input.text = "ComplexInfinity"
        except Exception as e:
            print(f"Error: {e}")
            self.ids.cal_input.text = "Error"

    def trig(self, func_name: str) -> None:
        """Apply trig functions just like %: append fn, convert, eval, with debug emojis."""
        prior = self.ids.cal_input.text
        print(f"⚙️ trig({func_name}) called, display = '{prior}'")

        # 🚫 abort on error state
        if prior in ["Error", "ComplexInfinity"]:
            print("⚠️ display is error state—aborting")
            return

        # 🔢 ensure last char is digit
        if not prior or not prior[-1].isdigit():
            print("❌ last char not a digit—cannot apply trig")
            self.ids.cal_input.text = "Error: not a number"
            return

        # 👁️ show appended function
        display_with_fn = prior + func_name
        self.ids.cal_input.text = display_with_fn
        print(f"✅ appended {func_name}, display now: '{display_with_fn}'")

        # 🔧 build eval‑expr
        expr = display_with_fn.replace("×", "*").replace("÷", "/")
        trig_pattern = r"(?P<num>-?\d+(?:\.\d+)?)(?P<fn>sin|cos|tan|asin|acos|atan)"

        def repl(m):
            n = float(m.group("num"))
            fn = m.group("fn")
            # 👉 direct trig
            if fn in ("sin", "cos", "tan"):
                val = getattr(math, fn)(math.radians(n))
                print(f"↪️ {fn}({n}°) = {val}")
                return f"({val})"
            # 🔄 inverse trig
            if not -1.0 <= n <= 1.0:
                print(f"❌ domain error for {fn} with {n}")
                raise ValueError("domain")
            val = math.degrees(getattr(math, fn)(n))
            print(f"↪️ {fn}({n}) = {val}°")
            return f"({val})"

        try:
            expr = re.sub(trig_pattern, repl, expr)
            # ✳️ inject multiplication between number and '('
            expr = re.sub(r"(\d)\(", r"\1*(", expr)
            print(f"🔄 converted to eval-expr: '{expr}'")
        except ValueError:
            self.ids.cal_input.text = "Error: out of domain"
            return

        # 🧮 evaluate
        try:
            result = eval(expr)
            # … after `result = eval(expr)` …
            # 1) squash floating-point noise
            result = round(result, 12)
            # 2) always format to two decimals
            temp = f"{result:.2f}"
            # 3) strip off any unnecessary zeros (and dot if it ends up integer)
            out = temp.rstrip("0").rstrip(".")
            self.ids.cal_input.text = out
            print(f"🔧 formatted result: {out}")
            print(f"🏁 final display: '{out}'")

        except Exception as e:
            print(f"❌ Error in trig eval(): {e}")
            self.ids.cal_input.text = "Error"

    def euler(self) -> None:
        """Euler's number"""

        prior: str = self.ids.cal_input.text

        # Prevent the method from working if prior is ComplexInfinity or Error
        if prior in ["ComplexInfinity", "Error"]:
            return
        if prior == "0":
            self.ids.cal_input.text = "e"
            return

        # Append e to the display
        self.ids.cal_input.text += f"e"


class MyCalculator(App):
    """This class is the main app of the calculator."""

    def build(self) -> CalculatorLayout:
        """Build the app"""

        self.title = "ProtoCalc"

        return CalculatorLayout()

    def on_kv_post(self) -> None:
        """Called after the KV language has been loaded."""

        self.ids.cal_input.bind(text=lambda instance, value: self.update_input_height())

    def update_input_height(self):
        """Update the height of the input field based on its content."""

        self.ids.cal_input.height = self.ids.cal_input.minimum_height

    def on_start(self) -> None:
        """Initializing the Calculator"""

        self.root.ids.cal_input.text = "0"

    @infos
    def on_stop(self) -> None:
        """Closing the Calculator"""

        time.sleep(0.75)  # Simulate a delay before closing the app


if __name__ == "__main__":
    MyCalculator().run()
