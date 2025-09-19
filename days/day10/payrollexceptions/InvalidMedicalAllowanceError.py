class MedicalAllowanceError(Exception):
    def __init__(self):
        super().__init__("Medical allowance cannot be less than 2000!")



