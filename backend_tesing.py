import json
import requests
import db_connector

#Post request for inserting a new user to the DB
def post_request(user_id,user_name):
        response = requests.post('http://127.0.0.1:5000/users/'+ str(user_id), json={"user_name": user_name})
        print(response.content)

#Get request for getting the user_name from the DB according to the user_id
def get_request(user_id):
    response = requests.get('http://127.0.0.1:5000/users/'+ str(user_id))
    if str(response.status_code) == "200":
        print("Request was successful, Status Code is 200")
    else:
        print("Request was unsuccessful, Status Code is 500")

    return response.content

def main():
    user_id = "1000"
    user_name = "emily"
    post_request(user_id,user_name)
    # Getting the Username by userid and checking if it matched original input
    get_res = json.loads(get_request(user_id))
    if user_name == get_res['user_name']:
        print("Data equals to the posted data")
    else:
        print("Data doesn't equal to the posted data")

    #Chcecking the DB for the user found according to userid
    print(f"User Name found in DB according to the ID: " + db_connector.get_user_name_by_user_id(int(user_id)))


if __name__ == "__main__":
    main()