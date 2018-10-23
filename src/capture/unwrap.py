#
#  unwrap.py
#  capturePlate
#
#  Created by Komron Aripov on 23/10/2018.
#  Copyright © 2018 Komron. All rights reserved.
#

from json import load
from os.path import dirname, join


class Unwrap():
    def __init__(self,
                 file_name: str = "configuration.json",
                 mode: str = "HOME"):
        self.directory = dirname(dirname(__file__))
        self.file_name = file_name
        self.path = join(self.directory, self.file_name)

        self.values = self._unload()
        self.url = "{0}://{1}:{2}".format(self.values[mode]["PROTOCOL"],
                                          self.values[mode]["IP"],
                                          self.values[mode]["PORT"])

    def _unload(self, mode: str = "r") -> (dict):
        """ Unpacks the contents of the config file
        """
        with open(self.path, mode) as file:
            config = load(file)

        return config
