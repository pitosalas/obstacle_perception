import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/pitosalas/linorobot2_ws/src/obstacle_perception/install/obstacle_perception'
