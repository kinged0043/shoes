from feast import FeatureView, Field, FileSource, Entity
from feast.types import Float32, Int32, String

import pandas

data = pandas.read_parquet("/home/kinged/Documents/shoes/feast_features/feature_repo/data/features.parquet")

sales = Entity(name="date of sale", join_keys=['dos'])

sales_source = FileSource(
    name="shoes_sales_data",
    path="/home/kinged/Documents/shoes/feast_features/feature_repo/data/features.parquet",
    timestamp_field="",
    created_timestamp_column=""
)
