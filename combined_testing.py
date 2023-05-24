import json
import requests
import db_connector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Post request for inserting a new user to the DB
def post_request(user_id,user_name):
    response = requests.post('http://127.0.0.1:5000/users/'+ str(user_id), json={"user_name": user_name})
    return response.content

#Get request for getting the user_name from the DB according to the user_id
def get_request(user_id):
    response = requests.get('http://127.0.0.1:5000/users/'+ str(user_id))
    return response.content


def main():
    #Asking the user to input a user_id and user_name and posting the inputs to the DB
    user_id,user_name = input('Please Insert a unique User ID and a User Name to Insert to "Users" table: \n').split()
    post_res = post_request(user_id, user_name)

    #Getting the Username by userid and checking if it matched original input
    get_res = json.loads(get_request(user_id))
    if str(user_name) == get_res['user_name']:
        print("Data equals to the posted data")
    else:
        raise Exception("test failed")

    #Chcecking the DB if the posted data is successfully stored
    db_result = db_connector.get_user_name_by_user_id(int(user_id))
    if str(db_result) == str(user_name):
        print("Posted data is successfully stored inside DB")
    else:
        raise Exception("test failed")

    #Navigating to web interface URL using the new user id and checking that the user name is correct
    driver = webdriver.Chrome(service=Service("/Users/edubnik/Downloads/chromedriver_mac_arm64"))
    driver.get('http://127.0.0.1:5001/users/get_user_data/' + str(user_id))
    user_element = driver.find_element(By.ID, "user")
    user_name_from_e = user_element.text
    if str(user_name_from_e) == str(user_name):
        print("The user name matches")
    else:
        raise Exception("test failed")
    driver.quit()


if __name__ == "__main__":
    main()
