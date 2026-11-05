class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key is not in the dictionary, create an empty list for it
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        res = ""
        values = self.store[key]

        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            # If the middle timestamp is less than or equal to our target timestamp,
            # its a valid candidate. Save it, then look to the right for a closer one.
            if values[m][0] <= timestamp:
                res = values[m][1] # Grab the 'value' attribute.
                l = m + 1
            else: 
                r = m - 1

        return res