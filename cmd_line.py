import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('Please use the following: test.py -i <inputfile> -o <outputfile>')
        sys.exit(0)
    for opt, arg in opts:
        if opt == '-h':
            #print help
            print ('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            print("test")
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            print("test1")
            outputfile = arg
    print ('Input file is ', inputfile)
    print ('Output file is ', outputfile)

if __name__ == "__main__":
    main(sys.argv[1:])