#!/usr/bin/python3
""" Console Module """
import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
#from models import storage
import shlex


classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ exit """
        print()
        return True

    def emptyline(self):
        """emptyline"""
        return False


    def do_quit(self, arg):
        """ Method to exit the HBNB console"""
        return True

    def _key_value_parser(self, args):
        """creates a dictionary from a list of string"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                key_value_pair = arg.split('=', 1)
                key = key_value_pair[0]
                value = key_value_pair[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except Exception:
                        try:
                            value = float(value)
                        except Exception:
                            continue
                new_dict[key] = value
        return new_dict


    def do_create(self, args):
        """ Create an object of any class"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()
if __name__ == "__main__":
    HBNBCommand().cmdloop()
