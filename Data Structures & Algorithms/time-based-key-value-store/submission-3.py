from sortedcontainers import SortedDict

class TimeMap:
    def __init__(self):
        self.m = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # print(self.m)
        if key not in self.m:
            return ""

        timestamps = self.m[key]
        idx = timestamps.bisect_right(timestamp) - 1

        if idx >= 0:
            closest_time = timestamps.iloc[idx]
            # print(timestamps)
            # print(idx)
            # print(closest_time)
            # print(timestamps[closest_time])
            return timestamps[closest_time]
        return ""