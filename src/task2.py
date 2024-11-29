import pandas as pd


def correlation_analysis():
    # Load the listings data
    try:
        listings = pd.read_csv(
            r"C:\Users\reddy\Downloads\Vacation Rental Listings and Reviews\data\listings.csv"
        )
    except FileNotFoundError:
        raise Exception("The file path is incorrect or the file does not exist.")

    # Select review score columns and price
    review_columns = [
        "review_scores_rating",
        "review_scores_accuracy",
        "review_scores_cleanliness",
        "review_scores_checkin",
        "review_scores_communication",
        "review_scores_location",
        "review_scores_value",
    ]

    # Ensure the necessary columns are in the DataFrame
    missing_columns = [
        col for col in review_columns + ["price"] if col not in listings.columns
    ]
    if missing_columns:
        raise Exception(
            f"The following required columns are missing in the dataset: {missing_columns}"
        )

    # Handle missing values in the selected columns
    listings = listings[review_columns + ["price"]].dropna()

    # Calculate correlation with price
    correlations = listings[review_columns].corrwith(listings["price"])

    # Ensure correlations exist
    if correlations.empty:
        raise Exception(
            "No correlations could be calculated. Check the dataset for valid data."
        )

    # Return the review score with the strongest correlation
    result = correlations.idxmax()
    return result
