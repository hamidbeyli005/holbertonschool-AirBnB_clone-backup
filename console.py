#!/usr/bin/env python3
"""Module for console program."""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "
    __classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Help message for quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create method"""
        command = arg.split()
        if len(command) == 0:
            print("** class name missing **")
        elif command[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Show method"""
        command = arg.split()
        if len(command) == 0:
            print("** class name missing **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif command[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            key = f"{command[0]}.{command[1]}"
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy method"""
        command = arg.split()
        if len(command) == 0:
            print("** class name missing **")
        elif len(command) == 1:
            print("** instance id missing **")
        elif command[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            objects = storage.all()
            key = f"{command[0]}.{command[1]}"
            if key in objects.keys():
                objects.pop(key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Show all objects"""
        command = arg.split()
        objects = storage.all()
        if len(command) == 0:
            for key, value in objects.items():
                print(str(value))
        elif command[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split(".")[0] == command[0]:
                    print(str(value))

    def do_update(self, argument):
        """Updates an instance based on the class name and id """
        tokensU = shlex.split(argument)
        if len(tokensU) == 0:
            print("** class name missing **")
            return
        elif len(tokensU) == 1:
            print("** instance id missing **")
            return
        elif len(tokensU) == 2:
            print("** attribute name missing **")
            return
        elif len(tokensU) == 3:
            print("** value missing **")
            return
        elif tokensU[0] not in self.classes:
            print("** class doesn't exist **")
            return
        keyI = tokensU[0] + "." + tokensU[1]
        dicI = models.storage.all()
        try:
            instanceU = dicI[keyI]
        except KeyError:
            print("** no instance found **")
            return
        try:
            typeA = type(getattr(instanceU, tokensU[2]))
            tokensU[3] = typeA(tokensU[3])
        except AttributeError:
            pass
        setattr(instanceU, tokensU[2], tokensU[3])
        models.storage.save()

    def do_count(self, argument):
        """  retrieve the number of instances of a class """
        tokensA = shlex.split(argument)
        dic = models.storage.all()
        num_instances = 0
        if tokensA[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in dic:
                className = key.split('.')
                if className[0] == tokensA[0]:
                    num_instances += 1

            print(num_instances)

    def precmd(self, argument):
        """ executed just before the command line line is interpreted """
        args = argument.split('.', 1)
        if len(args) == 2:
            _class = args[0]
            args = args[1].split('(', 1)
            command = args[0]
            if len(args) == 2:
                args = args[1].split(')', 1)
                if len(args) == 2:
                    _id = args[0]
                    other_arguments = args[1]
            line = command + " " + _class + " " + _id + " " + other_arguments
            return line
        else:
            return argument


if __name__ == '__main__':
    """infinite loop"""
    HBNBCommand().cmdloop()
