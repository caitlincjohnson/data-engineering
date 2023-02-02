import logging

import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Main script."""

    # Set file paths
    delays_file_path = "https://raw.githubusercontent.com/databricks/LearningSparkV2/master/databricks-datasets/learning-spark-v2/flights/departuredelays.csv"
    airport_code_file_path = "https://raw.githubusercontent.com/databricks/LearningSparkV2/master/databricks-datasets/learning-spark-v2/flights/airport-codes-na.txt"

    # Build a SparkSession
    spark = SparkSession.builder.appName("AirlineDelays").getOrCreate()

    # Pull data into Pandas DataFrames
    delays_data = pd.read_csv(delays_file_path)
    airport_code_data = pd.read_csv(airport_code_file_path, delimiter="\t")

    # Pull into Spark DataFrames
    delays_schema = """
    `date` STRING, `delay` INT, `distance` INT, `origin` STRING, `destination` STRING
    """
    delays_df = spark.createDataFrame(delays_data, schema=delays_schema)
    airport_code_schema = """
    `City` STRING, `State` STRING, `Country` STRING, `IATA` STRING
    """
    airport_code_df = spark.createDataFrame(
        airport_code_data, schema=airport_code_schema
    )

    airport_code_df.createOrReplaceTempView("airports_na")

    delays = delays_df.withColumn(
        "delay", expr("CAST(delay as INT) as delay")
    ).withColumn("distance", expr("CAST(distance as INT) as distance"))
    delays.createOrReplaceTempView("delays")

    # Create a temporary small table
    delays_filtered = delays.filter(
        expr(
            """
        origin == 'SEA' and destination == 'SFO' and delay > 0
        """
        )
    )
    delays_filtered.createOrReplaceTempView("delays_filtered")

    # Practice an inner join
    delays_filtered.join(
        airport_code_df, airport_code_df.IATA == delays_filtered.origin
    ).select("City", "State", "date", "delay", "distance", "destination").show(10)

    spark.sql(
        """
    CREATE TABLE departure_delay_window AS
    SELECT origin, destination, SUM(delay) AS total_delays
    FROM delays
    WHERE origin IN ('SEA', 'SFO', 'JFK')
    AND destination in ('SEA', 'SFO', 'JFK', 'DEN', 'ORD', 'LAX', 'ATL')
    GROUP BY origin, destination;
    """
    )

    spark.sql("""SELECT * FROM departure_delays_window LIMIT 10;""")


if __name__ == "__main__":
    main()
