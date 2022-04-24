class UndergroundSystem:

    def __init__(self):
        self.hashmap = {}
        self.avgMarkers = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.hashmap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, time = self.hashmap[id]
        endStation = stationName
        t = t - time
        if (endStation, startStation) in self.avgMarkers:
            self.avgMarkers[(endStation, startStation)].append(t)
        else:
            self.avgMarkers[(endStation, startStation)] = [t]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if self.avgMarkers[(endStation, startStation)]:
            return sum(self.avgMarkers[(endStation, startStation)])/len(self.avgMarkers[(endStation, startStation)])
        return None

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)