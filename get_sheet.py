from create_service import create_service

def get_sheet(sheet_id,sheet_name):
	service = create_service()
	sheet = service.spreadsheets()
	result = sheet.values().get(spreadsheetId=sheet_id,
                                range=sheet_name).execute()
	return result