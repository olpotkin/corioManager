#
# 09/19/2016
# Oleg Potkin
#

import telnetlib
import re


# Default unit connection settings
DEFAULT_PORT = 10001
DEFAULT_USER = 'admin'
DEFAULT_PASSWORD = 'adminpw'
DEFAULT_TIMEOUT = 5


# Definition of Client class (connect/disconnect and send commands to/from corioMaster)
class Client:

    def __init__(self,
                 hostname,
                 port=DEFAULT_PORT,
                 user=DEFAULT_USER,
                 password=DEFAULT_PASSWORD):
        self.hostname = hostname
        self.port = port
        self.user = user
        self.password = password
        self.connection = None
        self.logged = False

    # 1. Check connection status
    def connected(self):
        return self.connection is not None

    # 2. Check login status
    def logged(self):
        return self.logged

    # 3. Login to the unit
    def login(self):
        try:
            self.connection = telnetlib.Telnet(self.hostname, self.port, DEFAULT_TIMEOUT)
        except:
            raise Exception("Can't connect to: {0}:{1}".format(self.hostname, self.port))

        # telnet features provided logs
        self.connection.set_debuglevel(10)

        # get initial data from corio
        self.connection.read_until("""Please login. Use 'login(username,password)'\r\n""")

        # send data to corio
        self.connection.write('login({0},{1})\n'.format(self.user, self.password))

        # getting response from corio
        expected = """!Info : User {0} Logged In\r\n""".format(self.user)
        # checking response
        result = self.connection.read_until(expected)

        # TODO: print (result) !!!
        # check for some useful information from result


        # if login is not correct
        if result != expected:
            raise Exception("Invalid login: {0}".format(result))
        else:
            self.logged = True

    # 3.1 Logout from the unit
    def close(self):
        if self.logged:
            self.connection.write('logout\n')
        self.connection.close()
        self.logged = False

    # 4. Send management command(s) to the unit
    def send_command(self, command, expected=None):
        response = ""
        if not self.logged:
            self.login()
        result = self.connection.write(command + "\r\n")

        if expected is not None:
            expected = "!Done " + command + "\r\n"
            try:
                index, obj, response = self.connection.expect([re.compile(expected)])
            except EOFError, e:
                print "Exception: e="+repr(e)
        return response
