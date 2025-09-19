class NoVowelsError(Exception):
    def __init__(self):
        super().__init__("no vowels bitch")