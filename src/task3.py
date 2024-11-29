import pandas as pd


def professional_host_analysis():
    # Load the listings data
    try:
        listings = pd.read_csv(
            r"C:\Users\reddy\Downloads\Vacation Rental Listings and Reviews\data\listings.csv"
        )
    except FileNotFoundError:
        raise Exception("The file path is incorrect or the file does not exist.")

    # Ensure necessary columns are present
    required_columns = ["host_id", "neighbourhood_cleansed", "price"]
    missing_columns = [col for col in required_columns if col not in listings.columns]
    if missing_columns:
        raise Exception(
            f"The following required columns are missing in the dataset: {missing_columns}"
        )

    # Handle non-numeric and missing price data
    try:
        # Remove '$' and ',' symbols and convert to numeric
        listings["price"] = (
            listings["price"].replace({r"[\$,]": ""}, regex=True).astype(float)
        )
    except ValueError:
        raise Exception(
            "The 'price' column contains non-numeric values that could not be converted."
        )

    # Drop rows with missing values in required columns
    listings = listings.dropna(subset=required_columns)

    # Identify professional hosts
    host_counts = listings.groupby("host_id")["neighbourhood_cleansed"].nunique()
    professional_hosts = host_counts[host_counts > 5].index

    # Filter professional and non-professional hosts
    professional_listings = listings[listings["host_id"].isin(professional_hosts)]
    non_professional_listings = listings[~listings["host_id"].isin(professional_hosts)]

    # Calculate average price difference
    avg_price_difference = (
        professional_listings["price"].mean()
        - non_professional_listings["price"].mean()
    )

    return avg_price_difference
