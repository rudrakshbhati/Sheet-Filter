from create_service import create_service


def update_sheet(sheet_id, update_values):

	service = create_service()
	body = {
	'values': update_values
	}
	result = service.spreadsheets().values().update(spreadsheetId=sheet_id, range="Sheet1",valueInputOption="USER_ENTERED", body=body).execute()

