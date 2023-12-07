#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    '''Entry point of the command interpreter'''
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when EOF (Ctrl+D) is encountered
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line + ENTER
        """
        pass

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        instance = storage.all()[key]
        attribute_name = args[2]
        attribute_value = args[3].strip('"')
        if hasattr(instance, attribute_name):
            attribute_type = type(getattr(instance, attribute_name))
            try:
                setattr(instance, attribute_name,
                        attribute_type(attribute_value))
                storage.save()
            except ValueError:
                print("** invalid value **")
        else:
            print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
