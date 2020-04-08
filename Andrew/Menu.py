class Menu:
    def __init__(self, header):
        self.header = f"{header} menu: \n"
        self.menu_options = []


    def __str__(self):
        str = f"{self.header}"

        for option in self.menu_options:
            str += f"{option}"

        return str

    def createOption(self, command, title, des):
        self.menu_options.append(MenuOption({
            'command': command,
            'title': title,
            'des': des
        }))

    def addOption(self, mo):
        self.menu_options.append(mo)

    def show(self):
        print(self)
        cmd = input(f"Enter a Command: \n\n")
        for option in self.menu_options:
            if cmd is option.command:
                return option

        return MenuOption({
            'command': "X",
            'title': "exit",
            'des': "Exit"
        })



class MenuOption:
    def __init__(self, dict):
        self.method = dict['title']
        self.command = dict['command']
        self.des = dict['des']

    def __str__(self):
        return f" {self.command} - {self.method}\t\t\t\t\t\t{self.des}\n"

"""
Main menu:
C - Create a new deck
X - Exit

Enter a Main command (C, X)
"""