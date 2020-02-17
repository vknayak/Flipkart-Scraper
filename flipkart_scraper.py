from bs4 import BeautifulSoup
import requests
import json,pprint,random,time,os
mobiles_list=[]
def redmi_in_flipkart():
	i=0
	z=0
	for page in range(1,14):
		r=requests.get(f"https://www.flipkart.com/search?q=redmi+mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={page}")
		value=random.randint(1,3)
		time.sleep(value)
		mobile_names_list=[]
		
		images_list=[]
	
		soup=BeautifulSoup(r.text,"html.parser")
		mobile=soup.findAll("div",class_="_3wU53n")
		feautres=soup.findAll("ul",class_="vFw0gD")
		poster_urls=soup.findAll("a",class_="_31qSD5")



		for mobile_div in mobile:
			
			for mobile_name in mobile_div:
				each_mobile_dict={}
				mobile_names_list.append(mobile_name)

				each_mobile_dict[f"{mobile_name}"]={}
				mobiles_list.append(each_mobile_dict)
		
		k=0
		for each_ul in feautres:
			feautres_list=["Ram and Rom","Screen","Camera details","Battery","processor","others"]
			j=0
			for each_li in each_ul:
				mobiles_list[i][mobile_names_list[k]][feautres_list[j]]=each_li.text
				j+=1
				if j==6:
					break
			i+=1
			k+=1
			
		for each_poster_url in poster_urls:
			poster_link="https://www.flipkart.com"+each_poster_url["href"]
			response=requests.get(poster_link)
			image_soup=BeautifulSoup(response.text,"html.parser")
			n=image_soup.findAll("div",class_="_2_AcLJ")
			a=0
			img=""
			for ii in n[0]["style"]:
				if ii==")":
					a=0
				elif ii=="(":
					a=1
				elif a==1:
					img+=ii
			images_list.append(img)
		for l in range(len(images_list)):
			mobiles_list[z][mobile_names_list[l]]["cast link"]=images_list[l]
			z+=1
	return (mobiles_list)
	
python_data= redmi_in_flipkart()
# print(python_data)
if os.path.exists("red.json"):
	pass
else:
	with open("red.json","w+") as naik:
		json_data=json.dump(python_data,naik,indent=2)

