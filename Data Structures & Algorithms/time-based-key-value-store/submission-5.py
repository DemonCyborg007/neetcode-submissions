class TimeMap:

    def __init__(self):

        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.data:
            self.data[key] = {timestamp:value}
        else:
            self.data[key][timestamp] = value

        return None

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            if timestamp in self.data[key]:
                return self.data[key][timestamp]
            # elif not self.data[key]:
            #     return ''
            else:
                arr = list(self.data[key].keys())
                l = 0
                r = len(arr) - 1

                res = ''

                while l<=r:
                    m = (l+r)//2
                    
                    if arr[m] < timestamp:
                        res = self.data[key][arr[m]]
                        l = m + 1
                    else:
                        r = m - 1
                return res
        else:
            return ''

           
                

        
