import os
from tc_gen import generate


def check_zip():
    generate(4, 1)
    if os.system('rm -r test-cases.zip') == 0:
        assert(True)
