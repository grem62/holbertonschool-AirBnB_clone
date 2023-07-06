#!/usr/bin/python3
"""
Module for the command interpreter
"""
import cmd
from models.base_model import BaseModel
import shlex
import models
import sys
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Class for the command interpreter """
    prompt = '(hbnb) '
    classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Revieuw": Review
                }

    def do_quit(self, arg):
        """ Quit command to exit the program """
        quit()
        return True

    def do_EOF(self, arg):
        """ Quit command to exit the program """
        quit()
        return True

    def emptyline(self):
        """Empty line + ENTER shouldn't execute anything"""
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id.
        Args:
        arg (str): The name of the class to create an instance of.
        """
        # Check if the class name is missing
        if not arg:
            print("** class name missing **")
        # Check if the class doesn't exist
        elif arg not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            # Create a new instance of BaseModel
            new_instance = BaseModel()
            # Save the new instance to the JSON file
            new_instance.save()
            # Print the id of the new instance
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
    Args:
        arg (str): The argument passed to the function.
        """
        # Split the argument into a list of strings
        args = arg.split()

        # Check if the argument is missing
        if not args:
            print("** class name missing **")

        # Check if the class doesn't exist
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")

        # Check if the instance id is missing
        elif len(args) < 2:
            print("** instance id missing **")

        else:
            # Get all objects from storage
            obj_dict = storage.all()

            # Create the key for searching the object
            key = args[0] + "." + args[1]

            # Check if the object exists and print it
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances based or not
        on the class name.
        """
        args = arg.split()
        obj_dict = storage.all()
        if not args:
            print([str(obj_dict[key]) for key in obj_dict])
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            print([str(obj_dict[key]) for key in obj_dict if
                  key.startswith(args[0])])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating an attribute.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_dict = storage.all()
            key = args[0] + "." + args[1]
            if key in obj_dict:
                obj = obj_dict[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
