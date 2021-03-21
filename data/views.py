from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from .models import CsvData


import csv, io

import json
import pandas as pd

def DataView(request):

    data_csvdata = CsvData.objects.all()

    context = {
        "countries": data_csvdata
    }

    df_assets = pd.DataFrame(list(data_csvdata.values()))

    # parsing the DataFrame in json format. 
    json_records = df_assets.reset_index().to_json(orient ='records') 
    data = [] 
    data = json.loads(json_records) 
    context = {'d': data} 
  
    return render(request, 'table.html', context) 


def UploadView(request):
    # declaring template
    template_name = "upload.html"
    data = CsvData.objects.all()
    # prompt is a context variable that can have different values depending on their context
    prompt = {
        'order': 'Order of the CSV should be country, latitude, longitude, name',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template_name, prompt)
    elif request.method == 'POST':

        csv_file = request.FILES['file']
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we are able to handle a data in a stream
        io_string = io.StringIO(data_set)
        next(io_string)
        CsvData.objects.all().delete()
        for column in csv.reader(io_string, delimiter=';', quotechar="|"):
            _, created = CsvData.objects.update_or_create(
                country=column[0],
                latitude=column[1],
                longitude=column[2],
                name=column[3]
            )
        context = {}
        return render(request, template_name, context)
