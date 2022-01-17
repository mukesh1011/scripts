from fabric.api import *

env.hosts=["cloud_user@52.56.93.52"]

# Set the username
# env.user="cloud_user"

# Set the password [NOT RECOMMENDED]
env.password="12shroot"


run("ls -l")
