import heapq as hq
import math

def shortest_path(M,start,goal):
    print("shortest path called")

    # paths_heap has [cost, line_dist, [path]]
    # use min heapq to prioritize the lowest cost node to explore
    paths_heap = []
    paths_heap.append((0, 0, [start]))
    hq.heapify(paths_heap)

    # intersect_costs is used to track the cost to reach the intersection from the start
    # This prevents exploration into intersections that have shorter paths to them. 
    intersect_costs = {}
    intersect_costs[start] = 0
    intersect_costs[goal] = math.inf
    
    while paths_heap:

        current_intersect, line_dist, current_path = hq.heappop(paths_heap)
        current_intersect = current_path[-1]

        # When the first instance of the goal is found, other paths with greater 
        # greater total distance traversed will be ignored. 
        if line_dist > intersect_costs[goal]:
            continue
            
        # Checks if a path to goal is shorter than the one found previously.
        if line_dist < intersect_costs[goal] and current_intersect == goal:
            intersect_costs[goal] = line_dist
            best_path = current_path
        
        # find connected intersections and calculate their total cost f = h + g
        # h is the straight line distance betweent the 2 intersections
        # g is the straight line distance of the target intersection from the goal
        # add the intersection to the heapq
        for road in M.roads[current_intersect]:
            
            g = dist_intersection(M, current_intersect, road)
            h = dist_intersection(M, road, goal)
            cost = h + g
            next_path = current_path + [road]
            total_dist = line_dist + g
            
            if not shorter_path_exists(intersect_costs, road, total_dist):
                hq.heappush(paths_heap, (cost, total_dist, next_path))

    # best path is found when all other paths have higher cost to the goal
    return best_path
    
def dist_intersection(M, intersect1, intersect2):
    point1 = M.intersections[intersect1]
    point2 = M.intersections[intersect2]
    return math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))

def shorter_path_exists(intersect_costs, intersect, dist):
    
    if intersect not in intersect_costs.keys():
        intersect_costs[intersect] = dist
        return False
    
    if intersect_costs[intersect] < dist:
        return True
    return False
