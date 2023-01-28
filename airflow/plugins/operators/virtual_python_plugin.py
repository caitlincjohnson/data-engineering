import os
from typing import List

import airflow.utils.python_virtualenv
from airflow.plugins_manager import AirflowPlugin


def _generate_virtualenv_cmd(
    tmp_dir: str, python_bin: str, system_site_packages: bool
) -> List[str]:
    cmd = [
        "python3",
        "/usr/local/airflow/.local/lib/python3.7/site-packages/virtualenv",
        tmp_dir,
    ]
    if system_site_packages:
        cmd.append("--system-site-packages")
    if python_bin is not None:
        cmd.append(f"--python={python_bin}")
    return cmd


airflow.utils.python_virtualenv._generate_virtualenv_cmd = _generate_virtualenv_cmd

# This is the added path code
os.environ["PATH"] = f"/usr/local/airflow/.local/bin:{os.environ['PATH']}"


class VirtualPythonPlugin(AirflowPlugin):
    name = "virtual_python_plugin"
