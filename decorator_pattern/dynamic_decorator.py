"""
Calls are forwarded to the underlying object -
proxying of underlying calls may be done dynamically as opposed to copying every single method by hand.
"""


class FileWithLogging:
    def __init__(self, file):
        self.file = file

    def writelines(self, strings):
        self.file.writelines(strings)
        print(f"wrote {len(strings)} lines")

    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()

    def __getattr__(self, item):  # to redirect all requests to the underlying file (to mask it)
        return getattr(self.__dict__["file"], item)

    def __setattr__(self, key, value):
        if key == "file":
            self.__dict__[key] = value  # when needed to change the underlying file
        else:
            setattr(self.__dict__["file"], key, value)

    def __delattr__(self, item):
        delattr(self.__dict__["file"], item)


if __name__ == "__main__":
    file = FileWithLogging(open("hello.txt", "w"))
    file.writelines(["Hello", "world"])
    file.write("testing")  # directly accesses the "write" method of an underlying file (via __getattr__ above)
    file.close()
