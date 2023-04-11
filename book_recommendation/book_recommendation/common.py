from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import _get_queryset

def GetCustomResponse(result=True, err_msg=None, data=None, status=200):
	if err_msg is None:
		err_msg = []
	if data is None:
		data = {}
	
	body = {
	    "result": result,
	    "err_msg": err_msg,
	    "data": data
	}
	return JsonResponse(body, status=status)


def get_data_or_404(klass, name, **kwargs):
	queryset = _get_queryset(klass)
	try:
		data = queryset.get(**kwargs)
		return (data, None)
	except queryset.model.DoesNotExist:
		errors = ['The %s not found' % name]
		resp = GetCustomResponse(result=False, err_msg=errors, status=404)
		return (None, resp)