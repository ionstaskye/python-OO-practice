"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """make a new generator"""
        self.start = self.next = start
    def __repr__
        """show current number"""
        return f"Serial generator Start = {self.start} next = {self.next}"
    def generate():
        """generate a new number"""
        self.next += 1
        return self.next -1
    def reset():
        """reset to start"""
        self.next = start
