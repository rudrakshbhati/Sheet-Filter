from googleapiclient.discovery import build
from oauth2client import file, client, tools
from create_sheet import create_sheet
from create_service import create_service
from get_sheet import get_sheet
from update_sheet import update_sheet





def main(sheet_id,sheet_name,column_name,values):
   
	result = get_sheet(sheet_id,sheet_name)
	sheet_data = result.get('values', [])
	# asd = create()
	if not sheet_data:
	   print('No data found.')
	   return
	if len(sheet_data) < 2:
		print('No data found.')
		return
	headers = sheet_data[0]
	del sheet_data[0]
	del sheet_data[0]
	try:
		column_no = headers.index(column_name)
	except Exception as e:
		print("Column "+ column_name+ " not found") 
		return
	for value in values:
		filtered_data , sheet_data = filter_data(value,column_no,sheet_data)
		new_sheet_id , new_sheet_name = create_sheet(value)
		print("empty sheet created\n")
		filtered_data.insert(0, headers)
		update_sheet(new_sheet_id,filtered_data)
		print("sheet populated with data\n")
		print("Sheet id: " + new_sheet_id)
		print("Sheet title: "+ new_sheet_name)

		



def filter_data(filter_by,column_no,data):
	filtered_data = []
	c = len(data)
	for i in xrange(c - 1, -1, -1):
		row = data[i]
		if len(row) >= column_no: 
			if row[column_no] == filter_by:
				filtered_data.append(row)
				del data[i]
	return filtered_data, data

if __name__ == '__main__':
	sheet_id = raw_input("Enter Sheet Id - ")
	sheet_name = raw_input("Enter Sheet name - ")
	column_name = raw_input("Enter Column name to extract - ")
	values = [x for x in raw_input("Enter values to extract : ").split()]
	main(sheet_id,sheet_name,column_name,values)