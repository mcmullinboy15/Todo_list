from pprint import pprint

from Options import Object_Options, Main_Options
from Menu import Menu, MenuOption
import requests


# TODO, I might be able to make this find the Users and give me a list of Users to choose from
def ask_user():
    return input("What's the user_id? ")


def ask_project():
    return input("What's the proj_id? ")


def ask_list():
    return input("What's the list_id? ")


# TODO, until here


def ask_TODO_info():
    return {
        "title": input("Title: "),
        "description": input("Description: "),
        "content": input("Content: "),
        "contributors": input("Contributors: "),
    }

def ask_USER_info():
    return {
        "username": input("Username: "), 
        "email": input("Email: "), 
        "password": input("Password: "),
        # "is_staff": input("Is_staff: "),
        # "is_superuser": input("Is_superuser: "),
    }


class UserInterface:
    def __init__(self):
        self.current_user = None
        self.current_proj = None
        self.current_list = None
        self.current_task = None

        self.host = f"http://127.0.0.1:8000/todo/"

        self.main_menu = Menu("Main", "What would you like to do?", Main_Options)

        self.object_menu = Menu("Objects", "Which Object would you like to manipulate:", Object_Options)


    def run(self):
        print("Welcome to your ToDo-list\n")

        keepGoing = True
        while keepGoing:
            """2/api/project/?create=True&title=Sup&description=Yeah&content=No"""

            url = self.host

            menu_option = self.main_menu.show()
            if menu_option.command == 'X':
                keepGoing = False

            object_option = self.object_menu.show()

            url += self.build_url_obj(self.object_menu, object_option)

            url += self.add_vars(menu_option, object_option)

            if object_option.command == 'X':
                keepGoing = False

            print(url)
            response = requests.get(url=url)
            print(str(response)+"\n\n")


    def build_url_obj(self, menu,  object_option):
        url = ""

        for option in menu.menu_options:
            if object_option.command is option.command:

                if option.title is 'user':
                    url += 'api/'

                elif option.title is 'project':
                    user_id = ask_user()
                    url += f'{user_id}/api/project/'

                elif option.title is 'list':
                    user_id = ask_user()
                    url += f'{user_id}/api/project/'
                    proj_id = ask_project()
                    url += f'{proj_id}/list/'

                elif option.title is 'task':
                    user_id = ask_user()
                    url += f'{user_id}/api/project/'
                    proj_id = ask_project()
                    url += f'{proj_id}/list/'
                    list_id = ask_list()
                    url += f'{list_id}/list/'

                else:
                    return "TODO, URL TO 404 Page"

        return url

    def add_vars(self, menu_option, object_option):
        url = "?"


        if menu_option.title is 'create':
            dict = ask_TODO_info() if (object_option.title != 'user') else ask_USER_info()

            url += 'create=True&'

            for k,v in dict.items():
                url += f'{k}={v}&'

        elif menu_option.title is 'edit':
            pass
        elif menu_option.title is 'link':
            pass
        elif menu_option.title is 'delete':
            pass
        elif menu_option.title is 'add_cont':
            pass
        else:
            url += 'error_no_command=True'

        return url

"""
C
P
1
EZ_Salt
This is where me and Micheal will corelate ideas and tasks
We'll make this Project be incharge of Coding tasks
mcmullinboy1@gmail.com
"""
ui = UserInterface()
ui.run()