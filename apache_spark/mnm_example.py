import pandas as pd
from pyspark.sql import SparkSession


def main():
    """Main script."""

    # Build a SparkSession
    spark = SparkSession.builder.appName("PythonMnMCount").getOrCreate()

    # Get the M&M data set via Github
    # Trying to avoid downloading large data files on local machine
    url_github = "https://raw.githubusercontent.com/databricks/LearningSparkV2/master/chapter2/py/src/data/mnm_dataset.csv"
    pd_df = pd.read_csv(url_github)

    spark_df = spark.createDataFrame(pd_df)

    # Select from the dataframe and groupby the State and Color
    # Sum Count of M&Ms and order by it
    # This is lazy evaluation
    count_mnm_df = (
        spark_df.select("State", "Color", "Count")
        .groupBy("State", "Color")
        .sum("Count")
        .orderBy("sum(Count)")
    )

    # Show the results (which is an "action")
    count_mnm_df.show(n=60, truncate=False)
    print(f"Total Rows = {count_mnm_df.count()}")

    # Filter for only California ("CA")
    # Lazy evaluation
    ca_count_mnm_df = (
        spark_df.select("State", "Color", "Count")
        .where(spark_df.State == "CA")
        .groupBy("State", "Color")
        .sum("Count")
        .orderBy("sum(Count)", ascending=False)
    )

    # Show the results (action)
    ca_count_mnm_df.show(n=10, truncate=False)

    # End the Spark Session
    spark.stop()


if __name__ == "__main__":
    main()
