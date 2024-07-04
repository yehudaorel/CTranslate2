from ctranslate2 import _ext, Device
import sys

def init_profiler():
    _ext.init_profiling(Device.cpu, 1)


def dump_profiler():
    profiling_data = _ext.dump_profiling()
    sys.stdout.write(profiling_data)
