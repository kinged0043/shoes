import pandas
import logging

path = ""

shoes = pandas.read_csv(path)

logging.basicConfig(format="%(level)s: (warning)s%")

def col_rename(df: pandas.DataFrame,) -> pandas.DataFrame:
    
    mappings = {'Date of Sale':     'dos',
                'Product ID':       'prod_id',
                'Product Name':     'prod_name',
                'Quantity Sold':    'sold_quant',
                'Total Sale Amount':'total_sale',
                'Customer ID':      'customer_id',
                'Store Location':   'store_loc',
                'Target Gender':    'target_gen',
                'Customer Gender':  'customer_gen'
    }
    df = df.rename(mapper=mappings, axis='columns')

    return df

def to_dt(column: pandas.Series) -> pandas.Series:
    
    return pandas.to_datetime(column)

def type_converter(column: pandas.Series, type: str) -> pandas.Series:
    
    return column.astype(type)

def features(df: pandas.DataFrame):
    main_features = df.columns.drop(labels=[])

    return shoes[main_features]    

if __name__ == "__main__":
    try:
        col_rename(df= shoes, )
        to_dt(column=shoes['dos'])
        
        catrgories = []
        floats = []

        for x in catrgories:
            type_converter(shoes[x], type='category')
        
        for y in floats:
            type_converter(shoes[y], type='float')
        
    except:
        pass

# testing the code to see of it works is yet to be done