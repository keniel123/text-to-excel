import xlwt
import optparse

def getData(filename):
	data = []
	with open(filename) as f:
		for line in f:
			data.append([word for word in line.split(",") if word])
	return data

def exportToExcel(infile,outfile):
	data = getData(infile)
	wb = xlwt.Workbook()
	sheet = wb.add_sheet("New Sheet")
	for row_index in range(len(data)):
		for col_index in range(len(data[row_index])):
			sheet.write(row_index, col_index, data[row_index][col_index])
	wb.save(outfile)

if __name__ == "__main__":
	parser = optparse.OptionParser('usage%prog '+ '-I <inputfile>' + ' -O <outputfile>')
	parser.add_option('-I', dest='input', type='string',help='specify input textfile')
	parser.add_option('-O',dest='output',type='string',help='specify outputfile')
	(options, args) = parser.parse_args()
	filename = options.input
	output = options.output
	if (filename == None or output == None):
		print parser.usage
		exit(0)
	exportToExcel(filename,output)
  
