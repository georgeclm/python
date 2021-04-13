from contextlib import contextmanager
with open('notes.txt', 'w') as file:
    file.write('Some todo text...')
# same result by using 'with' much cleaner and consise
file = open('notes.txt', 'w')
try:
    file.write('some todoo...')
finally:
    file.close()


class ManagedFile:
    # create the context manager file for enter and close
    def __init__(self, filename) -> None:
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # exception here
        if self.file:
            self.file.close()
        # handling own exception
        if exc_type is not None:
            print('exception has been handled')
        # print('exc: ', exc_type, exc_value)
        print('exit')
        return True


with ManagedFile('notes.txt') as file:
    print('do some stuf..')
    file.write('some todoo..')
    # the absurd method the with method will raise an exception the continue will not get printed
    file.somemethod()
print('continuing')


@contextmanager
# way for context manager other way
# by using the decorator will work the same
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        # the with statement will be here
        yield f
    finally:
        f.close()


with open_managed_file('notes.txt') as f:
    f.write('some todoo..')
