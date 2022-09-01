def main():

    outfile = open('clients.txt', 'r')

    n = 1

    for clients in outfile:
        #output = outfile.read()
        print(n,". ", clients.rstrip('\n'),sep='')
        n += 1
        

    

main()