from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver= webdriver.Firefox()

driver.get("https://web.whatsapp.com")
time.sleep(40)

a = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[2]/div/label/input")
time.sleep(30)
a.click()
time.sleep(20)
print ("Number of people to send to :")
num= int(input())	
for i in range(num):
	#time.sleep(10)
	print("Enter recepient",i+1,"'s name:")
	inp=input()
	a.send_keys(inp +Keys.ENTER)
	time.sleep(10)
	b=driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/footer/div[1]/div[2]/div/div[2]")
	b.click()
	time.sleep(10)
	print("Enter number of texts to send:")
	n= int(input())
	for j in range(n):	
		time.sleep(10)
		print("Spam count" ,j)
		print("Enter custom text: ")
		string=input()
		time.sleep(10)
		b.send_keys(string+Keys.ENTER)
	time.sleep(10)

driver.close()
