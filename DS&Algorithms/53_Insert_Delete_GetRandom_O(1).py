class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.nums)
        self.nums.append(val)
        return True


    def remove(self, val: int) -> bool:
            if val not in self.map:
                return False
            idx_val = self.map[val]
            self.map[self.nums[-1]] = idx_val
            self.nums[idx_val], self.nums[-1] = self.nums[-1], val
            self.map.pop(val)
            self.nums.pop()
            return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


