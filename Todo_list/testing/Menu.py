class Menu:
    def __init__(self, header, prompt="", options=None):
        self.header = f"{header} menu: \n"
        self.prompt = f"{prompt}\n\n"
        self.menu_options = []

        if options is not None:
            for v in options:
                self.addOption(MenuOption(v))
            self.createOption("X", "exit", "Exit")


    def __str__(self):
        str = "\n\n"+self.prompt
        str += f"{self.header}"

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
        # ({str(var.command) for var in self.menu_options})
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
        self.title = dict['title']
        self.command = dict['command']
        self.des = dict['des']

    def __str__(self):
        return f" {self.command} - {self.title}\t\t\t\t\t\t{self.des}\n"

"""
Main menu:
C - Create a new deck
X - Exit

Enter a Main command (C, X)
"""