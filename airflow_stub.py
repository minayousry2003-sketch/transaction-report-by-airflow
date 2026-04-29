# Airflow stub for Windows development
# This provides basic type hints for DAG development on Windows

import datetimeyt
from typing import Any, Dict, Optional, Union

class DAG:
    def __init__(
        self,
        dag_id: str,
        start_date: Optional[datetime.datetime] = None,
        schedule_interval: Optional[Union[str, datetime.timedelta]] = None,
        **kwargs: Any
    ) -> None:
        self.dag_id = dag_id
        self.start_date = start_date
        self.schedule_interval = schedule_interval

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class BaseOperator:
    def __init__(self, task_id: str, **kwargs: Any) -> None:
        self.task_id = task_id

class BashOperator(BaseOperator):
    def __init__(self, task_id: str, bash_command: str, **kwargs: Any) -> None:
        super().__init__(task_id, **kwargs)
        self.bash_command = bash_command