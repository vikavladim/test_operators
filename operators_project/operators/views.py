from django.shortcuts import render
from rest_framework.views import APIView

from .models import Operator
from .serializers import OperatorSerializer
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from django.views import View

def process_excel_file(file):
    try:
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            ne = row.get('ne', None)
            address = row.get('address', None)
            latitude = row.get('latitude', None)
            longitude = row.get('longitude', None)
            gsm = row.get('gsm', None)
            umts = row.get('umts', None)
            lte = row.get('lte', None)
            status = row.get('status', None)
            operator = Operator.objects.create(ne=ne, address=address, latitude=latitude, longitude=longitude, gsm=gsm, umts=umts, lte=lte, status=status)
            print(operator)
        return True, "Данные успешно обработаны и сохранены в базу данных."
    except Exception as e:
        return False, f"Произошла ошибка при обработке файла: {str(e)}"


class OperatorList(APIView):
    def get(self, request):
        '''
        GET-запрос для получения списка операторов.
        :param request:
        :return:
        '''
        operators = Operator.objects.all()
        serializer = OperatorSerializer(operators, many=True)
        return Response(serializer.data)

    def post(self, request):
        '''
        POST-запрос для добавления новых операторов из файла.
        :param request:
        :return:
        '''
        file = request.data.get('file')
        if file:
            success, message = process_excel_file(file)
            if success:
                return Response({"message": message}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": message}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Файл не найден в запросе"}, status=status.HTTP_400_BAD_REQUEST)


class OperatorTableView(View):
    def get(self, request):
        operators = Operator.objects.all()
        return render(request, 'operators/operator_table.html', {'operators': operators})