class printing:

    def __init__(self,header):
        self.header ='\t' + header.upper()

    def print_header(self):
        print('------------------------')
        print(self.header)
        print('------------------------')
        print()