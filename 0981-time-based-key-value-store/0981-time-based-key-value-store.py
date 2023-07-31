class TimeMap(object):

    def __init__(self):
        self.tilemapDict = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.tilemapDict[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        valueList = self.tilemapDict[key]
        left = 0
        right = len(valueList) -1

        if len(valueList) == 0 or timestamp < valueList[0][0]:
            return ""

        while left <= right:
            mid = (left + right) // 2

            if valueList[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1

        if left <= len(valueList) - 1 and valueList[left][0] <= timestamp:
            return valueList[left][1]
        else:
            return valueList[left - 1][1]
 

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)