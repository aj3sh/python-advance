"""
Running python in an optimize mode
-O  : completely ignores asserts 
      and sets the special builtin name __debug__ to False (which by default is True)
-OO : removes docstrings from the code

USAGE:
python -O python_optimize_mode.py
python -OO python_optimize_mode.py
"""

print("Hello world")

if __debug__:
    print("Debug mode")
