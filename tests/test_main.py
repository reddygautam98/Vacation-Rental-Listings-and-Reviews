# tests/test_main.py
import sys
import os

# Add the 'src' directory to sys.path so Python can find the task1 module
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

# Import the function from task1.py in the src directory
from task1 import neighborhood_price_difference


def test_neighborhood_price_difference():
    # Run the function
    result = neighborhood_price_difference()

    # Replace "expected_neighborhood" with the actual expected neighborhood name
    expected_neighborhood = "SomeNeighborhood"  # Update with the actual expected value
    assert (
        result == expected_neighborhood
    ), f"Expected {expected_neighborhood}, but got {result}"
