def detectNumberPlate(fileName):
	import time
	import openalpr_api
	from openalpr_api.rest import ApiException
	from pprint import pprint
	import json
	# create an instance of the API class
	api_instance = openalpr_api.DefaultApi()
	import base64
	encoded = base64.b64encode(open(fileName, "rb").read())
	image_bytes = encoded # str | The image file that you wish to analyze encoded in base64 
	secret_key = 'sk_97a11cda807cbf257bffa0fd' # str | The secret key used to authenticate your account.  You can view your  secret key by visiting  https://cloud.openalpr.com/ 
	country = 'in' # str | Defines the training data used by OpenALPR.  \"us\" analyzes  North-American style plates.  \"eu\" analyzes European-style plates.  This field is required if using the \"plate\" task  You may use multiple datasets by using commas between the country  codes.  For example, 'au,auwide' would analyze using both the  Australian plate styles.  A full list of supported country codes  can be found here https://github.com/openalpr/openalpr/tree/master/runtime_data/config 
	recognize_vehicle = 0 # int | If set to 1, the vehicle will also be recognized in the image This requires an additional credit per request  (optional) (default to 0)
	state = '' # str | Corresponds to a US state or EU country code used by OpenALPR pattern  recognition.  For example, using \"md\" matches US plates against the  Maryland plate patterns.  Using \"fr\" matches European plates against  the French plate patterns.  (optional) (default to )
	return_image = 1 # int | If set to 1, the image you uploaded will be encoded in base64 and  sent back along with the response  (optional) (default to 0)
	topn = 10 # int | The number of results you would like to be returned for plate  candidates and vehicle classifications  (optional) (default to 10)
	prewarp = '' # str | Prewarp configuration is used to calibrate the analyses for the  angle of a particular camera.  More information is available here http://doc.openalpr.com/accuracy_improvements.html#calibration  (optional) (default to )

	try:
		api_response = api_instance.recognize_bytes(image_bytes, secret_key, country, recognize_vehicle=recognize_vehicle, state=state, return_image=return_image, topn=topn, prewarp=prewarp)
		pprint(api_response)
		jsonFormat =str(api_response)
		jsonFormat = jsonFormat.replace('\'','"')
		jsonFormat = jsonFormat.replace('None','"None"')
		myDict = json.loads(jsonFormat)
		#print(some)
		#print('dic type is : '+ str(type(dic)))
		try:
			nplate = myDict["results"][0]["candidates"][0]['plate']
			import data
			return data.doQuery(nplate)
		except:
			print("No number plate detected")
		
	except ApiException as e:
		print "Exception when calling DefaultApi->recognize_bytes: %s\n" % e
				
#detectNumberPlate("car-del.png")
