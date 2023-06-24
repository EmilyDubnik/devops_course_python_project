import json
import requests

def perform_test():
    # Read the K8S URL from k8s_url.txt file
    with open("k8s_url.txt", "r") as file:
        k8s_url = file.read().strip()

    # Perform the test using the K8S URL
    user_id = "1000"
    user_name = "emily"

    # Post request for inserting a new user to the deployed application
    response = requests.post(f"{k8s_url}/users/{user_id}", json={"user_name": user_name})
    print(response.content)

    # Get request for getting the user_name from the deployed application according to the user_id
    response = requests.get(f"{k8s_url}/users/{user_id}")
    if response.status_code == 200:
        print("Request was successful, Status Code is 200")
    else:
        print("Request was unsuccessful, Status Code is 500")

    get_res = json.loads(response.content)
    if user_name == get_res['user_name']:
        print("Data equals to the posted data")
    else:
        print("Data doesn't equal to the posted data")

def main():
    perform_test()

if __name__ == "__main__":
    main()
