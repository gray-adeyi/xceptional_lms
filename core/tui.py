from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer, Static, Label, Input, Button
from core.config import ADVANCED_MATH_PACKAGE
from core.adapters import AdvancedMathAdapter


class AddWidget(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="First value", id="add-first-value", type="number")
        yield Input(placeholder="Second value", id="add-second-value", type="number")
        yield Label("Your result will appear here", id="add-answer")
        yield Button("Add")

    def on_button_pressed(self, event: Button.Pressed):
        first = self.query_one("#add-first-value")
        second = self.query_one("#add-second-value")
        label = self.query_one("#add-answer")
        label.update(f"{float(first.value) + float(second.value)}")


class AdvancedMathWidget(Static):
    def compose(self) -> ComposeResult:
        if not ADVANCED_MATH_PACKAGE:
            yield Label("No advanced math plugin provided")
        else:
            functions = [
                Label(
                    "Using Advanced math package: <PACKAGE_NAME> BY: <AUTHOR> VERSION: <VERSION>"
                ),
                PowerWidget(),
                FactorialWidget(),
                PermutationWidget(),
                CombinationWidget(),
            ]
            for function in functions:
                yield function


class PowerWidget(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Base", id="power-base", type="integer")
        yield Input(placeholder="Exponent", id="power-exponent", type="integer")
        yield Label("Your result will appear here", id="power-answer")
        yield Button("Power")

    def on_button_pressed(self, event: Button.Pressed):
        base = self.query_one("#power-base")
        exponent = self.query_one("#power-exponent")
        label = self.query_one("#power-answer")
        answer = AdvancedMathAdapter().power(int(base.value), int(exponent.value))
        label.update(str(answer))


class FactorialWidget(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Value", id="factorial-value")
        yield Label("Your result will appear here", id="factorial-answer")
        yield Button("Factorial")

    def on_button_pressed(self, event: Button.Pressed):
        value = self.query_one("#factorial-value")
        label = self.query_one("#factorial-answer")
        answer = AdvancedMathAdapter().factorial(int(value.value))
        label.update(str(answer))


class PermutationWidget(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="N value", id="permutation-n-val", type="integer")
        yield Input(placeholder="R value", id="permutation-r-val", type="integer")
        yield Label("Your result will appear here", id="permutation-answer")
        yield Button("Permutaion")

    def on_button_pressed(self, event: Button.Pressed):
        n = self.query_one("#permutation-n-val")
        r = self.query_one("#permutation-r-val")
        label = self.query_one("#permutation-answer")
        answer = AdvancedMathAdapter().permutation(int(n.value), int(r.value))
        label.update(str(answer))


class CombinationWidget(Static):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="N value", id="combination-n-val", type="integer")
        yield Input(placeholder="R value", id="combination-r-val", type="integer")
        yield Label("Your result will appear here", id="combination-answer")
        yield Button("Permutaion")

    def on_button_pressed(self, event: Button.Pressed):
        n = self.query_one("#combination-n-val")
        r = self.query_one("#combination-r-val")
        label = self.query_one("#combination-answer")
        answer = AdvancedMathAdapter().combination(int(n.value), int(r.value))
        label.update(str(answer))


class XceptionalLMSApp(App):
    BINDINGS = [("d", "toggle_color_scheme", "Toggle color scheme")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ScrollableContainer(AddWidget(), AdvancedMathWidget())

    def action_toggle_color_scheme(self):
        self.dark = not self.dark
