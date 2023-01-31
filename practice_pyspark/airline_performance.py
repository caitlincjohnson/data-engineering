import logging

from pyspark.sql import SparkSession


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Main script."""

    # Build a SparkSession
    spark = SparkSession.builder.appName("AirlinePerformance").getOrCreate()

    # Create database
    spark.sql("CREATE DATABASE learn_spark_db")
    spark.sql("USE learn_spark_db")

    # Load the dataset into DataFrame
    # Note: the file will not be uploaded to Github due to size
    csv_file = "practice_pyspark/DelayedFlights.csv"

    # Specify schema
    schema = """
    `id` INT, `year` INT, `month` INT, `day_of_month` INT, `day_of_week` INT,
    `departure_time` FLOAT, `crs_departure_time` INT, `arrival_time` FLOAT,
    `crs_arrival_time` INT, `unique_carrier` STRING
    """

    spark_df = (
        spark.read.format("csv")
        .schema(schema=schema)
        .option("header", "true")
        .load(csv_file)
    )

    # Create a managed table
    # spark_df.write.saveAsTable("managed_us_delay_flights_table")

    # Create an unmanaged table
    # (
    #     spark_df
    #     .write
    #     .option("path", "/tmp/data/us_flights_delay")
    #     .saveAsTable("unmanaged_us_delay_flights_table")
    # )

    # Create a temporary view
    spark_df.createOrReplaceTempView("us_delay_flights_table")

    spark.sql(
        """
    SELECT *
    FROM us_delay_flights_table
    WHERE departure_time > crs_departure_time
    """
    ).show(10)

    spark.sql(
        """
    SELECT distinct unique_carrier
    FROM us_delay_flights_table
    """
    ).show()

    spark.sql(
        """
    SELECT
        id,
        year,
        unique_carrier,
        CASE
            WHEN departure_time - crs_departure_time > 360 THEN 'Very Long Delays'
            WHEN departure_time - crs_departure_time >= 120 AND departure_time - crs_departure_time < 360 THEN 'Long Delays'
            WHEN departure_time - crs_departure_time >= 60 AND departure_time - crs_departure_time < 120 THEN 'Short Delays'
            WHEN departure_time - crs_departure_time >= 0 AND departure_time - crs_departure_time < 60 THEN 'Tolerable Delays'
            WHEN departure_time - crs_departure_time = 0 THEN 'No Delays'
            ELSE 'Early'
        END AS flight_delays
    FROM us_delay_flights_table
    """
    ).show(10)

    # End the Spark Session
    spark.stop()


if __name__ == "__main__":
    main()
