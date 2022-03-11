from model.ExampleTable import Example_Table

def example_ReceivedAndStored(data):
	from app import sqldb
	
	error = None
	rows = []
	try:
		if data:
			for res in data:
				name = res['name']
				timestamp = res['timestamp']
				lucky_number = res['lucky_number']
				example_row = Example_Table(example_string=name, example_timestamp=timestamp, example_int=lucky_number)
				rows.append(example_row)
		else:
			raise ValueError('No Data!') 
		
		sqldb.session.add_all(rows)
		sqldb.session.commit()
		result = [{'insertedData':data, 'Success':True}]
		return error, result

	except Exception as err:
		sqldb.session.rollback()
		error = str(err)
		result = [{'Error':error, 'Success':False}]
		return error, result
 
