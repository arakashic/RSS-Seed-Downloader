# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="root"
__date__ ="$Dec 21, 2009 2:41:43 PM$"

import os, sys, time
from signal import SIGTERM

def daemonize(stdout='/dev/null', stderr=None, stdin='/dev/null',
              pidfile=None, startmsg = 'started with pid %s' ):
    '''
        This forks the current process into a daemon.
        The stdin, stdout, and stderr arguments are file names that
        will be opened and be used to replace the standard file descriptors
        in sys.stdin, sys.stdout, and sys.stderr.
        These arguments are optional and default to /dev/null.
        Note that stderr is opened unbuffered, so
        if it shares a file with stdout then interleaved output
        may not appear in the order that you expect.
    '''
    # Do first fork.
    try:
        pid = os.fork()
        if pid > 0: sys.exit(0) # Exit first parent.
    except OSError, e:
        sys.stderr.write("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)

    # Decouple from parent environment.
    os.chdir("/")
    os.umask(0)
    os.setsid()

    # Do second fork.
    try:
        pid = os.fork()
        if pid > 0: sys.exit(0) # Exit second parent.
    except OSError, e:
        sys.stderr.write("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)

    # Open file descriptors and print start message
    if not stderr: stderr = stdout
    si = file(stdin, 'r')
    so = file(stdout, 'a+')
    se = file(stderr, 'a+', 0)
    pid = str(os.getpid())
    sys.stderr.write("%s\n" % startmsg % pid)
    sys.stderr.flush()
    if pidfile: file(pidfile,'w+').write("%s\n" % pid)

    # Redirect standard file descriptors.
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())
    
if __name__ == "__main__":
    print "Hello World";
