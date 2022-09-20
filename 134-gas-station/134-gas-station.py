class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        total_surplus = 0
        surplus = 0
        start = 0
        for i in range(len(gas)):
            total_surplus += gas[i]-cost[i]
            surplus += gas[i]-cost[i]
            if surplus < 0:
                start = i+1
                surplus = 0
        
        if total_surplus >= 0:
            return start
        else:
            return -1
        