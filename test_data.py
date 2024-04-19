import pandas as pd 

df = pd.read_csv('cleaned_data.csv')

def test_no_missing_values():
    missing_values = df.isnull().sum()
    assert (missing_values == 0).all(), f"Missing values found in columns: {missing_values[missing_values > 0].index.tolist()}"

def test_rating_range():
    assert df['rating'].between(0, 10).all(), "Rating should be within the range of 0 to 10"
    
def test_aspect_rating_range():
    rating_columns = ['Seat Comfort', 'Cabin Staff Service', 'Food & Beverages', 
                      'Inflight Entertainment', 'Ground Service', 'Value For Money']
    for column in rating_columns:
        assert df[column].between(0, 5).all(), f"Values in {column} column should be within the range of 0 to 5"
    
def test_same_number_of_rows():
    total_rows = len(df)
    column_counts = df.count()
    assert (column_counts == total_rows).all(), "Not all columns have the same number of rows"

def test_binary_values():
    binary_columns = ['Recommended', 'Verified']
    for column in binary_columns:
        assert df[column].isin([0, 1]).all(), f"Values in {column} column should only be 0 or 1"
        
def test_uppercase_country_codes():
    assert df['CODE2'].str.isupper().all(), "Country codes should be in uppercase format"
    assert df['CODE3'].str.isupper().all(), "Country codes should be in uppercase format"

def test_latitude_range():
    assert df['Latitude'].between(-90, 90).all(), "Latitude values should be within the range of -90 to 90"

def test_longitude_range():
    assert df['Longitude'].between(-180, 180).all(), "Longitude values should be within the range of -180 to 180"
