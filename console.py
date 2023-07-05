#!/usr/bin/env python3
""" Import cmd for command line interpreters. """
import cmd



class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Exits the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program.
        """
        return True

    def emptyline(self):
        """Do nothing if line is empty."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()