from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver= webdriver.Firefox()

driver.get("https://web.whatsapp.com")
time.sleep(10)

a = driver.find_element_by_css_selector(".jN-F5")
time.sleep(5)
a.click()
time.sleep(5)
print ("Number of people to send to :")
num= int(input())	
for i in range(num):
	#time.sleep(10)
	print("Enter recepient",i+1,"'s name:")
	inp=input()
	a.send_keys(inp +Keys.ENTER)
	time.sleep(5)
	b=driver.find_element_by_css_selector("._2S1VP")
	b.click()
	time.sleep(5)
	print("Enter number of different texts to send:")
	n= int(input())
	for j in range(n):	
		time.sleep(5)
		#print("Spam count" ,j)
		print("Enter the text: ")
		string=input()
		time.sleep(5)
		print("Enter number of times to send the above text: ")
		number= int(input())
		time.sleep(5)
		for _ in range(number):
			b.send_keys(string+Keys.ENTER)
	time.sleep(5)

driver.close()
