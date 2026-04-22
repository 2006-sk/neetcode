class TimeMap:

    def __init__(self):
        
        self.hashm = defaultdict(list)
        self.prev = 0
    def set(self, key: str, value: str, timestamp: int) -> None:
        ## if timestamp and value iven for same key but different timestamp then all futire timestamp's oint to the last timestamp's value
        #unless theya re assigned values
        #we can go for a list inside the dict with lists so like {key:[[timestamp,value],[nxt timestamp, value]]}
        self.hashm[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashm:
            return ''
        if self.hashm[key][-1][0] == timestamp:
            return self.hashm[key][-1][1]
        elif self.hashm[key][-1][0] < timestamp: #this means if prev is smaller than timestamp than return but if not than we start a while loop that loops until either 

            return self.hashm[key][-1][1]
        else:
            l = 0
            h = len(self.hashm[key])- 2
            value = 0
            while h >= l:
                mid = (h+l)//2
                if self.hashm[key][mid][0] == timestamp:
                    return self.hashm[key][mid][1]
                elif self.hashm[key][mid][0] < timestamp:
                    value = self.hashm[key][mid][1]
                    l = mid +1
                else:
                    h = mid - 1
            if not value:
                return ''

            else:
                return value


                


        

