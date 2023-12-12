#!/usr/bin/python3
import cmd
import json
from models.engine.file_storage import storage


class HBNBCommand(cmd.Cmd):
    '''Entry point of the command interpreter'''
    prompt = "(hbnb) "

    def do_quit(self, _):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, _):
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

    def do_help(self, arg):
        """
        List available commands with "help" or detailed help with "help cmd".
        """
        if arg:
            print(self.namemap.get(arg).__doc__)
        else:
            print("List available commands: quit, EOF, help")

    def default(self, line):
        """
        Handle unknown commands
        """
        print("** Unknown command: {}".format(line))

    def do_create(self, arg):
        '''
        Creates a new instance of BaseModel, saves
        it (to the JSON file) and prints the id.
        '''
        args = arg.split()
        if not args or args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        class_name = args[0]

        # Check if the class exists before attempting to create an instance
        if class_name in storage.classes():
            new_instance = storage.classes()[class_name]()

            # Check if the instance is a dictionary
            if isinstance(new_instance, dict):
                print("** Failed to create instance. Check class definition. **")
                return

            storage.new(new_instance)
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        '''
        Prints the string representation of an instance
        based on the class name and id.
        '''
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instances_dict = storage.all().get(class_name, {})
        key = "{}.{}".format(class_name, instance_id)

        print([class_name, instance_id, key, instances_dict])

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        '''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instances_dict = storage.all().get(class_name, {})
        key = "{}.{}".format(class_name, instance_id)

        print("Key:", key)
        print("Instances Dict:", instances_dict)

        if key not in instances_dict:
            print("** no instance found **")
            return

        del instances_dict[key]
        storage.save()
        print("Instance deleted successfully")

    def do_all(self, arg):
        '''
        Prints all string representation of all instances
        based or not on the class name.
        '''
        args = arg.split()
        if not args or args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        class_name = args[0]
        new_instance = storage.classes()[class_name]()
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def do_update(self, arg):
        '''
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        '''
        args = arg.split()

        if not args or args[0] not in storage.classes():
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]

        print({class_name, instance_id, attribute_name, attribute_value})

        instances_dict = storage.all().get(class_name, {})
        key = "{}.{}".format(class_name, instance_id)

        instance = instances_dict[key]
        setattr(instance, attribute_name, attribute_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
