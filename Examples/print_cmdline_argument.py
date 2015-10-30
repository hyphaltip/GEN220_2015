import sys

# will print out the command line arguments you typed in e.g.
# python print_cmdline_argument.py one two buckle-my-shoe ... "three four"
for n in range(len(sys.argv)):
    print 'argv[%d] = %s' %(n, sys.argv[n])
