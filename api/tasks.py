from celery import shared_task

@shared_task
def process_cnj_task(cnj_request_id):
    print(f"Processando o CNJ request: {cnj_request_id}")
    return cnj_request_id
