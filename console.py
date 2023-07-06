#!/usr/bin/env python3
""" Import cmd for command line interpreters. """
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    cls = ["MyModel"]

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

    def do_create(self, arg):
        """
        Create a new instance of a class.
        Args:
        arg (str): The name of the class.
        """
        if not arg:
            # Print error message if class name is missing
            print("** class name missing **")
        elif arg not in class_list:
            # Print error message if class does not exist
            print("** class doesn't exist **")
        else:
            # Create a new instance of the specified class
            instance = BaseModel()
            # Save the instance to the database
            instance.save()
            # Print the ID of the instance
            print(instance.id)


    def do_show(self, args):
        """Show the details of an instance"""
        if not args:
            print("** class name missing **")
            return

        # Split the arguments into class name and instance id
        class_name, instance_id = args.split()

        # Check if the class exists
        if class_name not in class_list:
            print("** class doesn't exist **")
            return

        # Check if the instance id is provided
        if not instance_id:
            print("** instance id missing **")
            return

        # Find the instance with the given class name and instance id
        instance = storage.find(class_name, instance_id)

        # Check if the instance exists
        if not instance:
            print("** no instance found **")
        else:
            print(instance)



    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        # Check if class name is missing
        if not args:
            print("** class name missing **")
            return

        # Split the class name and instance id
        class_name, instance_id = args.split()

        # Check if class exists
        if class_name not in class_list:
            print("** class doesn't exist **")
            return

        # Check if instance id is missing
        if not instance_id:
            print("** instance id missing **")
            return

        # Find the instance
        instance = storage.find(class_name, instance_id)

        # Check if instance exists
        if not instance:
            print("** no instance found **")
        else:
            # Delete the instance
            storage.delete(instance)
            # Save the changes
            storage.save_changes()


   
    def do_all(self, arg):
        """Prints all string representations of instances"""
        if arg in self.cls or not arg:
            result = [str(obj) for obj in storage.all().values()]
            print(result)
        else:
            print("** class doesn't exist **")


    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            args = separarArgs(arg)
            if args[0] not in self.cls:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()