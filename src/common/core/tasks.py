import os
from datetime import datetime as dt
import logging

from celery import shared_task

@shared_task
def test_task():
    logging.info(f"Running test task at {dt.now()}")
    return "Test task ran successfully"
