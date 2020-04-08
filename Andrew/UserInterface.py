from pprint import pprint

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


class UserInterface:
    def __init__(self):
        self.current_user = None
        self.current_proj = None
        self.current_list = None
        self.current_task = None

        self.host = f"http://127.0.0.1:8000/todo/"

        self.main_menu = Menu("Main")
        self.main_options_dict = [
            {
                'command': 'C',
                'title': 'create',
                'des': 'ONLY ONE IMPLEMENTED        creates a new object'
            },
            {
                'command': 'E',
                'title': 'edit',
                'des': 'edits object with given id'
            },
            {
                'command': 'L',
                'title': 'link',
                'des': 'links one object to its parent or child\t'
                       'ex: Moving a task from one list to another'
            },
            {
                'command': 'D',
                'title': 'delete',
                'des': 'deletes object provided'
            },
            {
                'command': 'A',
                'title': 'add_cont',
                'des': 'adds an array [to be implemented] of contributors to the object'
            }
        ]
        for v in self.main_options_dict:
            self.main_menu.addOption(MenuOption(v))
        self.main_menu.createOption("X", "exit", "Exit")

        self.object_menu = Menu("Objects")
        self.object_options_dict = [
            {
                'command': 'U',
                'title': 'user',
                'des': 'Manipulate User Object'
            },
            {
                'command': 'P',
                'title': 'project',
                'des': 'Manipulate Project Object'
            },
            {
                'command': 'L',
                'title': 'list',
                'des': 'Manipulate List Object'
            },
            {
                'command': 'T',
                'title': 'task',
                'des': 'Manipulate Task Object'
            }
        ]
        for v in self.object_options_dict:
            self.object_menu.addOption(MenuOption(v))
        self.object_menu.createOption("X", "exit", "Exit")

    def run(self):
        print("Welcome to your ToDo-list\n")

        keepGoing = True
        while keepGoing:
            """2/api/project/?create=True&title=Sup&description=Yeah&content=No"""

            url = self.host

            menu_option = self.main_menu.show()
            if menu_option.command == 'X':
                keepGoing = False

            print("Which Object would you like to manipulate:\n")

            object_option = self.object_menu.show()

            url += self.build_url_obj(object_option)

            url += self.add_vars(menu_option)

            if object_option.command == 'X':
                keepGoing = False

            print(url)
            response = requests.get(url=url)
            print(response.text)


    def build_url_obj(self, object_option):
        url = ""

        for dict in self.object_options_dict:
            if object_option.command is dict['command']:

                if dict['title'] is 'user':
                    # TODO, create User
                    pass
                elif dict['title'] is 'project':
                    user_id = ask_user()
                    url += f'{user_id}/api/project/'
                elif dict['title'] is 'list':
                    user_id = ask_user()
                    url += f'{user_id}/api/project/'
                    proj_id = ask_project()
                    url += f'{proj_id}/list/'

                elif dict['title'] is 'task':
                    user_id = ask_user()
                    url += f'{user_id}/api/project/'
                    proj_id = ask_project()
                    url += f'{proj_id}/list/'
                    list_id = ask_list()
                    url += f'{list_id}/list/'

                else:
                    return "TODO, URL TO 404 Page"

        return url

    def add_vars(self, menu_option):
        url = "?"

        if menu_option.method is 'create':
            url += 'create=True&'
            dict = ask_TODO_info()
            for k,v in dict.items():
                url += f'{k}={v}&'  #   "{v}"&'

        elif menu_option.method is 'edit':
            pass
        elif menu_option.method is 'link':
            pass
        elif menu_option.method is 'delete':
            pass
        elif menu_option.method is 'add_cont':
            pass
        else:
            return 'error_no_command'

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