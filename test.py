import requests
import sys

def start():
    option = input("""
                    Enter:
                    1 to test get,
                    2 to test post,
                    3 to test patch,
                    4 to test delete,
                    5 to view endpoints,
                    0 to exit.
                    """)

    if option == '1':
        print(get())
    elif option == '2':
        print(post())
    elif option == '3':
        print(patch())
    elif option == '4':
        print(delete())
    elif option == '5':
        print(endpoints())
    if option != '0':
        start()

def endpoints():
    r = requests.get(url)
    return r.text

def get():
    get = input("Enter a valid endpoint, like /containers: ")
    get = url + get
    r = requests.get(get)
    return r.text

def post():
    post = input("Enter a valid endpoint, like /containers: ")
    if post == "/containers":
        image = input("Enter an image: ")
        payload = {'image': image}
        post = url + post
        r = requests.post(post, json=payload)
        return r.text
    elif post == "/images":
        path = input("Enter the path to create the image: ")
        tag = input("Enter a tag or enter '0': ")
        if tag != '0':
            payload = {'path': path, 'tag': tag}
        else:
            payload = {'path': path}
        post = url + post
        r = requests.post(post, json=payload)
        return r.text

def patch():
    patch = input("Enter a valid endpoint, like /containers/<id>: ")
    state = input("If you want to change the container's state enter: run/pause/stop ")
    tag = input("If you want to change the tag of the image, enter a tag ")
    payload = {'state': state, 'tag': tag}
    patch = url + patch
    r = requests.patch(patch, json=payload)
    return r.text

def delete():
    delete = input("Enter a valid endpoint, like /containers: ")
    delete = url + delete
    r = requests.delete(delete)
    return r.text

url = 'http://35.189.193.233'
start()
