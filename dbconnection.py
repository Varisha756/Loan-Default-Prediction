import pandas as pd
from sqlalchemy import create_engine

def load_data():
    engine = create_engine(
        "mysql+pymysql://root:i7gbbtm1l.z96166@localhost/loan_risk"
    )
    query = "SELECT * FROM loan_data"
    df = pd.read_sql(query, engine)
    return df
