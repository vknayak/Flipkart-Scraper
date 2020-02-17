
import json
with open("red.json","r+") as naik:
	python_data=json.load(naik)



# for data in python_data:
# 	for i in data:
# 		for each in data[i]:
# 			if "https" in data[i][each]:
# 				print(data[i][each])




students_file =open("redmi_mobiles.html", "w")
students_file.write("<html>\n")
students_file.write("<head>\n")
students_file.write("<title>Mobile Phones</title>\n")
students_file.write("</head>\n")
students_file.write("<body>\n")
students_file.write("<table border=1>")
students_file.write("<thead><tr><td>Mobile NUmber</td><td>Battery</td><td>Screen details</td><td>Camera details</td><td>Battery</td><td>Processor</td><td>Others</td><td>Image</td></tr></thead>")
for data in python_data:
	for i in data:
		students_file.write("<tr><td>"+i+"</td>")
		for each in data[i]:
			if "https" in data[i][each]:
				# students_file.write("<td><img width="+"200"+"px height="+"200"+"px src="+data[i][each]+"></td>")
				students_file.write("<td><img src="+data[i][each]+"></td>")
				continue
			students_file.write("<td>"+data[i][each]+"</td>")
		students_file.write("</tr>")
	
students_file.write("</table>")

students_file.write("</body>\n")
students_file.write("</html>\n")
students_file.close()