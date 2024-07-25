import pandas
from utils import COLUMNS, MAPPINGS, FEATURE_COLUMNS, shoe_gender, shoe_models


def preprocess():
    path = ""
    shoes_data = pandas.read_csv(path)

    def col_rename(df: pandas.DataFrame,) -> pandas.DataFrame:
        df = df.rename(mapper=MAPPINGS, axis='columns')
        return df
    
    col_rename(shoes_data)

    def to_dt(column: pandas.Series) -> pandas.Series:
        
        return pandas.to_datetime(column)

    def type_converter(column: pandas.Series, type: str) -> pandas.Series:
        
        return column.astype(type)

    def features(df: pandas.DataFrame):
        main_features = df.columns.drop(labels=[])

        return shoes_data[main_features]    

if __name__ == "__main__":
    preprocess()