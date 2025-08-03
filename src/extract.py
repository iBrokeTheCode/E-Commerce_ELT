import requests
from pandas import DataFrame, read_csv, to_datetime


def get_public_holidays(url: str, year: str) -> DataFrame:
    """
    Get public holidays for the given year for Brazil

    Args:
        url (str): The url to get the public holidays
        year (str): The year to get the public holidays

    Raises:
        SystemExit: If the request fails

    Returns:
        DataFrame: The public holidays
    """
    url = "{}/{}/BR".format(url, year)

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error if something went wrong

        data = DataFrame(response.json())

        # Drop the columns types and countries
        df = data.drop(["types", "counties"], axis=1)  # Miss spelling in the API
        # Convert the date column to datetime
        df["date"] = to_datetime(df["date"])

        return df

    except requests.exceptions.HTTPError:
        raise SystemExit


def extract(
    csv_folder: str, csv_table_mapping: dict[str, str], public_holidays_url: str
) -> dict[str, DataFrame]:
    """
    Extract the data from the csv files and load them into a dictionary of dataframes

    Args:
      csv_folder (str): The folder where the csv files are
      csv_table_mapping (dict[str, str]): The mapping between the csv files and the table names
      public_holidays_url (str): The url to get the public holidays

    Returns:
      Dict[str, DataFrame]: A dictionary with keys as the table names and values as the dataframes
    """
    dataframes = {
        table_name: read_csv("{}/{}".format(csv_folder, csv_file))
        for csv_file, table_name in csv_table_mapping.items()
    }

    public_holidays = get_public_holidays(url=public_holidays_url, year="2017")
    dataframes["public_holidays"] = public_holidays

    return dataframes
