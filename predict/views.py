from django.shortcuts import render
from results.models import ResultsModel
from predict.models import PredictionModel
from predict.mod import predictor
from accounts.models import UserProfile, User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponse

temp = predictor()
@login_required
@user_passes_test(lambda u: UserProfile.objects.get(user_id=User.objects.get(id=u.id).id).staff == 'Doctor')
def see_prediction(request):
    if request.method == 'POST':

        result_id = request.POST.get('result_id_input', None)

        if result_id is not None:
            try:
                result = ResultsModel.objects.filter(result_id=result_id).first()
                b = result.as_array()
                pre= temp.predict(b)
                return render(request, 'predictions/see_prediction.html', { 'result_id': result_id, 'result': result,
                                                                            'prediction': pre[0], 'probability': pre[1]})

            except ResultsModel.DoesNotExist:
                return HttpResponse("no such result")
    else:
        return render(request, 'predictions/see_prediction.html')
