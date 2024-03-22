# Xceptional LMS

A toy learning management system to try out functionality as plugins.


## Development Setup

- clone this repository.
- create a virtual env for the project. `virtualenv venv`. If you don't have `virtualenv` installed, install it with `pip install virtualenv`
- switch to the virtual environment with `venv\Scripts\activate` on windows or `source venv/bin/activate`
- install project requirements with `pip install -r requirements.txt`
- run the app with `python xceptional_lms.py`

## Using Advanced Math Functions

- paste your advanced math package into `xceptional_lms/core/plugins/`
- edit the `ADVANCED_MATH_PACKAGE` in `xceptional_lms/core/config.py` to match the name of the advanced math package
- run the app with `python xceptional_lms.py`

### Example

Using [gray_adeyi_math](https://github.com/gray-adeyi/gray_adeyi_math).

- clone [gray_adeyi_math](https://github.com/gray-adeyi/gray_adeyi_math)
- copy the `gray_adeyi_math` package within the project root of [gray_adeyi_math](https://github.com/gray-adeyi/gray_adeyi_math) into
    `xceptional_lms/core/plugins`.
- replace `ADVANCED_MATH_PACKAGE=""` with `ADVANCED_MATH_PACKAGE="gray_adeyi_math"` in `xceptional_lms/core/config.py`
- run the app with `python xceptional_lms.py`
