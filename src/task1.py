import pandas as pd


def neighborhood_price_difference():
    # Load the listings data
    # Option 1: Use a raw string literal
    listings = pd.read_csv(
        r"C:\Users\reddy\Downloads\Vacation Rental Listings and Reviews\data\listings.csv"
    )

    # Option 2: Replace backslashes with forward slashes
    # listings = pd.read_csv("C:/Users/reddy/Downloads/Vacation Rental Listings and Reviews/data/listings.csv")

    # Calculate the median price difference
    superhosts = listings[listings["host_is_superhost"] == "t"]
    non_superhosts = listings[listings["host_is_superhost"] == "f"]

    # Merge the two datasets and calculate the price difference
    price_diff = (
        superhosts.groupby("neighbourhood_cleansed")["price"].median()
        - non_superhosts.groupby("neighbourhood_cleansed")["price"].median()
    )

    # Find the neighborhood with the biggest price difference
    result = price_diff.idxmax()
    return result
