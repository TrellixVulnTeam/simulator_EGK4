class Plugin:

    # a group of commands, resources, and properties that all work together.

    # name : used by simsys for commands
    # resources, commands and properties : dictionaries of said objects
    # parent : Another plugin that this plugin can access

    def __init__(self, name, resources, commands, properties, parent=None):
        self.resources = resources
        self.commands = commands
        self.name = name
        self.parent = parent
        self.properties = properties

    def __call__(self, args):
        if args[0] in self.commands:
            temp = args[0]
            args.pop(0)
            output = self.commands[temp](self.resources, args, self.properties, self.parent)
            if output == False:
                output = "Command " + self.commands[temp].name + " needs to recharge."
            return output
        else:
            return False