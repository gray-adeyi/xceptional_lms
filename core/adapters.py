from core.config import ADVANCED_MATH_PACKAGE
import importlib


class AdvancedMathAdapter:
    def __init__(self):
        if not ADVANCED_MATH_PACKAGE:
            raise ValueError("ADVANCED_MATH_PACKAGE not set in config")
        self.advanced_math_package = self.load_plugin(ADVANCED_MATH_PACKAGE)

    @property
    def package_name(self) -> str:
        return self.advanced_math_package.__name__

    @property
    def package_author(self) -> str:
        return self.advanced_math_package.__author__

    @property
    def package_version(self) -> str:
        return self.advanced_math_package.__version__

    def load_plugin(self, package: str):
        try:
            module = importlib.import_module("core.plugins." + package)
            return module
        except ImportError:
            raise ValueError(f"Unable to load plugin {package}")

    def power(self, base: int, exponent: int) -> int:
        return self.advanced_math_package.power(base, exponent)

    def factorial(self, value: int) -> int:
        return self.advanced_math_package.factorial(value)

    def permutation(self, n: int, r: int) -> int:
        return self.advanced_math_package.permutation(n, r)

    def combination(self, n: int, r: int) -> int:
        return self.advanced_math_package.combination(n, r)
