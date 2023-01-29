import logging

import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """Main script."""

    # Build a SparkSession
    spark = SparkSession.builder.appName("PythonMnMCount").getOrCreate()

    # Get the Fire Department data set via Github
    url_github = "https://raw.githubusercontent.com/databricks/LearningSparkV2/master/chapter3/data/sf-fire-calls.csv"
    pd_df = pd.read_csv(url_github)

    schema = StructType(
        [
            StructField("CallNumber", IntegerType(), True),
            StructField("UnitID", StringType(), True),
            StructField("IncidentNumber", IntegerType(), True),
            StructField("CallType", StringType(), True),
            StructField("CallDate", StringType(), True),
            StructField("WatchDate", StringType(), True),
            StructField("CallFinalDisposition", StringType(), True),
            StructField("AvailableDtTm", StringType(), True),
            StructField("Address", StringType(), True),
            StructField("City", StringType(), True),
            StructField("Zipcode", FloatType(), True),
            StructField("Battalion", StringType(), True),
            StructField("StationArea", StringType(), True),
            StructField("Box", StringType(), True),
            StructField("OriginalPriority", StringType(), True),
            StructField("Priority", StringType(), True),
            StructField("FinalPriority", IntegerType(), True),
            StructField("ALSUnit", BooleanType(), True),
            StructField("CallTypeGroup", StringType(), True),
            StructField("NumAlarms", IntegerType(), True),
            StructField("UnitType", StringType(), True),
            StructField("UnitSequenceInCallDispatch", FloatType(), True),
            StructField("FirePreventionDistrict", StringType(), True),
            StructField("SupervisorDistrict", StringType(), True),
            StructField("Neighborhood", StringType(), True),
            StructField("Location", StringType(), True),
            StructField("RowID", StringType(), True),
            StructField("Delay", FloatType(), True),
        ]
    )

    spark_df = spark.createDataFrame(pd_df, schema)

    # Check the schema
    logging.info(f"Schema: {spark_df.schema}")

    # Select a few components of data
    few_fire_df = spark_df.select("IncidentNumber", "AvailableDtTm", "CallType").where(
        col("CallType") != "MedicalIncident"
    )
    few_fire_df.show(5, truncate=False)

    # Count distinct CallTypes
    (
        spark_df.select("CallType")
        .where(col("CallType").isNotNull())
        .agg(countDistinct("CallType").alias("DistinctCallTypes"))
        .show()
    )

    # List the distinct CallTypes
    (
        spark_df.select("CallType")
        .where(col("CallType").isNotNull())
        .distinct()
        .show(10, truncate=False)
    )

    # Practice renaming columns and changing data types
    cleanup_df = (
        spark_df.withColumnRenamed("Delay", "ResponseDelayedinMins")
        .withColumn("IncidentDate", to_timestamp(col("CallDate"), "MM/dd/yyyy"))
        .drop("CallDate")
        .withColumn("OnWatchDate", to_timestamp(col("WatchDate"), "MM/dd/yyyy"))
        .drop("WatchDate")
        .withColumn(
            "AvailableDtTS", to_timestamp(col("AvailableDtTm"), "MM/dd/yyyy hh:mm:ss a")
        )
        .drop("AvailableDtTm")
    )

    # Preview changes
    (
        cleanup_df.select("IncidentDate", "OnWatchDate", "AvailableDtTS").show(
            5, truncate=False
        )
    )

    # Converting to actual date/time values allows you to use
    # a lot of date-based functions like "dayofyear()"
    (
        cleanup_df.select(year("IncidentDate"))
        .distinct()
        .orderBy(year("IncidentDate"))
        .show()
    )

    # What are the most common types of fire calls
    logging.info("Shown below are the most common types of fire calls:")
    (
        cleanup_df.select("CallType")
        .where(col("CallType").isNotNull())
        .groupBy("CallType")
        .count()
        .orderBy("count", ascending=False)
        .show(n=10, truncate=False)
    )

    # Compute the sum of alarms, the average response time, and minimum
    # and maximum response times to all fire calls
    (
        cleanup_df.select(
            sum("NumAlarms"),
            avg("ResponseDelayedinMins"),
            min("ResponseDelayedinMins"),
            max("ResponseDelayedinMins"),
        ).show()
    )

    # End the Spark Session
    spark.stop()


if __name__ == "__main__":
    main()
