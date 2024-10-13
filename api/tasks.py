import logging
from celery import shared_task


logger = logging.getLogger(__name__)

@shared_task
def process_cnj_task(cnj_request_id):
    logger.info(f"Processando o CNJ request: {cnj_request_id}")
    return cnj_request_id
