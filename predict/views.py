from django.shortcuts import render
from results.models import ResultsModel
from predict.models import PredictionModel
from predict.mod import predictor
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse


@login_required
def see_prediction(request):
    if request.method == 'POST':

        result_id = request.POST.get('result_id_input', None)

        if result_id is not None:
            try:
                result = ResultsModel.objects.filter(result_id=result_id).first()
                pre = predictor.predict(result.as_array)
                return render(request, 'predictions/see_prediction.html', { 'result_id': result_id, 'result': result,
                                                                            'prediction': pre[0], 'probability': pre[1]})

            except ResultsModel.DoesNotExist:
                return HttpResponse("no such result")
    else:
        return render(request, 'predictions/see_prediction.html')
