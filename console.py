#!/usr/bin/python3
""" Console with command that begin with do """

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    """ Command that begin with do """
    def do_quit(self, arg):
        """
        Exits the program.
        """
        quit()

    def do_EOF(self, arg):
        """
        Exit the program.
        """
        quit()


    def emptyline(self, arg):
        """
        This function does nothing when an empty line is entered.
        """
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()