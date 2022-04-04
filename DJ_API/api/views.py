import json
from django.http import JsonResponse
from django.views import View
from .models import Compania


class CompaniaView(View):
    def get(self, request, id=0):
        if (id > 0):
            companies = list(Compania.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {'message': "Success", 'company': company}
            else:
                datos = {'message': "Company not found..."}
            return JsonResponse(datos)
        else:
            companies = list(Compania.objects.values())
            if len(companies) > 0:
                datos = {'message': "Success", 'companies': companies}
            else:
                datos = {'message': "Companies not found..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Compania.objects.create(
            nombre=jd['nombre'], sitioweb=jd['sitioweb'], fundacion=jd['fundacion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Compania.objects.filter(id=id).values())
        if len(companies) > 0:
            company = Compania.objects.get(id=id)
            company.nombre = jd['nombre']
            company.sitioweb = jd['sitioweb']
            company.fundacion = jd['fundacion']
            company.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        companies = list(Compania.objects.filter(id=id).values())
        if len(companies) > 0:
            Compania.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Company not found..."}
        return JsonResponse(datos)
