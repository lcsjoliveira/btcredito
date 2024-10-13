import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from api.models import CNJRequest
from api.tasks import process_cnj_task


class CNJProcessView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

        cnj_number = data.get("cnj_number")
        if not cnj_number:
            return JsonResponse({"error": "CNJ number is required"}, status=400)

        try:
            cnj_request, created = CNJRequest.objects.get_or_create(cnj_number=cnj_number)
        except Exception as e:
            return JsonResponse({"error": f"Failed to process request: {str(e)}"}, status=500)

        process_cnj_task.delay(cnj_request.id)
        return JsonResponse({"message": "CNJ is being processed"}, status=202)

class CNJExternalServiceView(View):
    def post(self, request, *args, **kwargs):
        cnj_number = request.POST.get("cnj_number")
        if not cnj_number:
            return JsonResponse({"error": "CNJ number is required"}, status=400)

        try:
            cnj_request = CNJRequest.objects.get(cnj_number=cnj_number)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "CNJ not found"}, status=404)

        external_response = call_external_service(cnj_number)
        if "error" in external_response:
            return JsonResponse({"error": "Failed to call external service", "details": external_response["details"]}, status=500)

        cnj_request.external_service_response = external_response
        cnj_request.save()
        return JsonResponse({"message": "External service called", "response": external_response}, status=200)

def call_external_service(cnj_number):
    external_service_url = settings.EXTERNAL_SERVICE_URL
    try:
        response = requests.post(external_service_url, data={"cnj_number": cnj_number})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": "External service call failed", "details": str(e)}
