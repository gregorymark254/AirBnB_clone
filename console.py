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

    def do_create(self, arg):
        """Create a new instance of BaseModel, saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_ins = eval(arg)()
            new_ins.save()
            print(new_ins.id)
        except NameError:
            print('*** Class does not exist ***')

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("class name missing")
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
        print(storage.all()[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id (save the change into the JSON file). """
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
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in storage.classes():
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in storage.all().items()
                  if args[0] == key.split('.')[0]])

    def do_update(self, arg):
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
