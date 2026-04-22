class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort a combined list of position and list
        new_arr = []
        for i in range(len(position)):
            new_arr.append([position[i],speed[i]])
        reverse = sorted(new_arr, reverse = True)

        # Time it will take for each car to reach without joining carFleet
        fleet = len(position)
        time_arr = []
        for i in range(len(position)):
            time = 0
            time = (target - reverse[i][0])/reverse[i][1]
            time_arr.append(time)
        
        fleet = 0
        cur_time = 0.0
        for t in time_arr:
            if t > cur_time:
                fleet += 1
                cur_time = t
            # else: merges into existing fleet (do nothing)
        return fleet
                        







        
        
