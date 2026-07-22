#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == "__main__":
    n = int(input().strip())

    # Convierte a binario (omitiendo el prefijo '0b') y separa por ceros
    binary_str = bin(n)[2:]
    ones_groups = binary_str.split("0")

    # Imprime la longitud del grupo de unos mas largo
    print(len(max(ones_groups)))



