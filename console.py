#!/usr/bin/python3
import cmd


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

    def do_help(self, arg):
        """
        List available commands with "help" or detailed help with "help cmd".
        """
        super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
