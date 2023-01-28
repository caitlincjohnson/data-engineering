"""
This module holds the example Airflow DAG for Looker job

Description
-----------
This script is solely used for code snippets and is not meant
to be executable.
"""
import logging
import os

from airflow import DAG, Variable
from airflow.decorators import task
import pendulum


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dag_params = {
    "dag_id": "looker_script_example",
    "schedule": None,
    "start_date": pendulum.datetime(2021, 1, 1, tz="UTC"),
}

logger.info("Setting environment variables for looker_sdk")
os.environ["LOOKERSDK_API_VERSION"] = Variable.get("LOOKERSDK_API_VERSION")
os.environ["LOOKERSDK_BASE_URL"] = Variable.get("LOOKERSDK_BASE_URL")
os.environ["LOOKERSDK_CLIENT_ID"] = Variable.get("LOOKERSDK_CLIENT_ID")
os.environ["LOOKERSDK_CLIENT_SECRET"] = Variable.get("LOOKERSDK_CLIENT_SECRET")
os.environ["LOOKERSDK_VERIFY_SSL"] = Variable.get("LOOKERSDK_VERIFY_SSL")


@task.virtualenv(
    task_id="virtualenv_python",
    requirements=["colorama==0.4.0"],
    system_site_packages=False,
)
def callable_virtualenv():
    """
    Example function that will be performed in a virtual environment.
    """
    import logging
    import looker_sdk

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        logger.info("Connecting to Looker")
        sdk = looker_sdk.init40()

        logger.info(f"Looker SDK object: {sdk}")

        # insert code that utilizes the looker_sdk object

    except Exception as e:
        logger.error(f"Error: {e}")

    # return results if applicable


with DAG(**dag_params) as dag:

    virtualenv_task = callable_virtualenv()

    # insert additional tasks that leverage the Looker results (if applicable)


virtualenv_task
