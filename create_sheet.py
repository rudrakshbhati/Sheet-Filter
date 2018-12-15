from create_service import create_service
import time


def create_sheet(value):
	service = create_service()
	ts = time.time()
	title = value + '_' + str(ts)
	spreadsheet = {
	    'properties': {
	        'title': title
	    }
	}
	request = service.spreadsheets().create(body=spreadsheet)
	response = request.execute()
	return response.get('spreadsheetId') , title

