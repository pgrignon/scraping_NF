from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from pandas import DataFrame


def connect_to_db(
    db_username: str, db_password: str, db_ip: str, db_name: str
) -> Engine:
    """
    Connects to the SQL DB
    --------------
    Parameters:
        db_username: paul
        db_password: motdepasse
        db_ip: localhost
        db_name: NF
    Returns:
        DB connection
    """
    db_connection = create_engine(
        "mysql+mysqlconnector://{0}:{1}@{2}/{3}".format(
            db_username, db_password, db_ip, db_name
        )
    )
    return db_connection


def write_articles_to_sql(df: DataFrame, con: Engine, table: str) -> None:
    """
    Write records stored in a DataFrame to a SQL database
    --------------
    Parameters:
        df: the dataframe to be stored
        con: the sqlalchemy connection
        table: the table of the SQL DB in in which the df will be written
    """
    return df.to_sql(con=con, name=table, if_exists="replace")
