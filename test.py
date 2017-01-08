import pip

def install(requirements):
    file = open(requirements, 'r')
    for package in file:
        pip.main(['install', package])

# Example
if __name__ == '__main__':
    install('requirements.txt')
