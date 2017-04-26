import time
import random
import itertools
pop_size=50
k_n_generations = 50
tournment=16
mutation=1
crossover=1
arr2=[   [0,1,2,3,4],
	        [1,0,5,6,7],
			[2,5,0,8,9],
			[3,6,8,0,10],
			[4,7,9,10,0]]
arr=[[0,66,21,3,500,26,77,69,125,650],
	[66,0,35,115,36,65,85,90,44,54],
	[21,35,0,450,448,846,910,47,11,145],
	[3,115,450,0,65,478,432,214,356,251],
	[500,36,448,65,0,258,143,325,125,39],
	[26,65,846,478,258,0,369,256,345,110],
	[77,85,910,432,143,369,0,45,120,289],
	[69,90,47,214,325,256,45,0,325,981],
	[125,44,11,356,125,345,120,325,0,326],
	[650,54,145,251,39,110,289,981,326,0]]			
def fitness(r):
	distance=0
	
	for i in range(len(r)-1):
		distance=distance+arr[r[i]-1][r[i+1]-1]
	return distance

def sum_distance(gen):
	sum=0
	for i in range(pop_size):
		sum=sum+gen[i][10]
	return sum
def prob(r,gen):	
	return 1-(r[10]/sum_distance(gen))	
def selection(gen):
	selected=[]
	count=0
	
		
	for i in range(pop_size):
		sel=gen[i]
		if count==tournment:
		  break
		if sel in selected:
		  continue
		for j in range(pop_size):
		  if(prob(sel,gen)<prob(gen[j],gen) and gen[j] not in selected):
		    sel=gen[j]
		selected.append(sel)
		count=count+1
	return selected


def crossover(p1,p2):
        
        

        child_rt1 = []
        child_rt2= []
        for x in range(0,len(p1)):
            child_rt1.append( None) 
            child_rt2.append(None)		
        
        
		
        # Two random integer indices of the parent1:
        start_pos = random.randint(0,len(p1))
        end_pos = random.randint(0,len(p1))
        if start_pos==end_pos:
          if start_pos>0: start_pos-1
          else: end_pos+1		  
        # print("pos")		
        # print(start_pos)
        # print(end_pos)
        #### takes the sub-route from parent one and sticks it in itself:
        # if the start position is before the end:
        if start_pos < end_pos:
            # do it in the start-->end order
            for x in range(start_pos,end_pos):
                a=p1[x]
                b=p2[x]
                child_rt1[x]=b
                child_rt2[x]=a
                # print(a)
                # print(b)				
				# if the start position is after the end:
        elif start_pos > end_pos:
            # do it in the end-->start order
            for i in range(end_pos,start_pos):
                a=p1[i]
                b=p2[i]			
                child_rt2[i] = a # set the values to eachother
                child_rt1[i] = b
                # print(a)
                # print(b)
        # Cycles through the parent2. And fills in the child_rt
 
        for i in range(len(p1)):
            # if parent2 has a city that the child2 doesn't have yet:
            if not p2[i] in child_rt2:
                # it puts it in the first 'None' spot and breaks out of the loop.
                for x in range(len(child_rt2)):
                    if child_rt2[x] == None:
                        child_rt2[x] = p2[i]
                        break
            # if parent1 has a city that the child1 doesn't have yet:
						
            if not p1[i] in child_rt1:
                # it puts it in the first 'None' spot and breaks out of the loop.
                for x in range(len(child_rt1)):
                    if child_rt1[x] == None:
                        child_rt1[x] = p1[i]
                        break						
        # repeated until all the cities are in the child route

        return child_rt1,child_rt2	
def mutate( route_to_mut):
    
    if random.random() < mutation:

        mut_pos1 = random.randint(0,len(route_to_mut)-1)
        mut_pos2 = random.randint(0,len(route_to_mut)-1)
         # if they're the same, skip to the chase
        if mut_pos1 == mut_pos2:
            return route_to_mut

        # Otherwise swap them:
        city1 = route_to_mut[mut_pos1]
        city2 = route_to_mut[mut_pos2]
        route_to_mut[mut_pos2] = city1
        route_to_mut[mut_pos1] = city2


    return route_to_mut
def evolve_population(first_gen,s):
	
	m=[]
	count=0
	for a in range(pop_size):
		max=first_gen[a]
		if count==len(s): break
		if max in m: continue
		
		for b in range(pop_size):
		  #if first_gen[b][5]>max[5] or max not in m:
		  if(prob(max,first_gen)>prob(first_gen[b],first_gen) and first_gen[b] not in m):
		    max=first_gen[b]
		m.append(max) 
		count+=1
	next=first_gen
	def replace(L, X, Y):
		while X in L:
		  i = L.index(X)
		  L.insert(i, Y)
		  L.remove(X)
			
	for i in range(len(s)):
		if s[i] not in first_gen:
		  replace(first_gen,m[i],s[i])
	
	return next	
	
	
def GA(gen,n=0):
	start_time = time.time()
	# time
	# selection(gen)
	# crossover
	# mutate	
	# evolve_population
	# best yet
	def run(gen):
		children=[]
		p=selection(gen)
		best_route_yet=p[0]
		print("selected")
		print(p)
		#for i in range(len(p)-1):
		for index, item in enumerate(p):
			next = index + 1
			if next < len(p):
				#print( index, item, next)	
				f1=p[index].pop()
				f2=p[next].pop()
				c1,c2=crossover(p[index],p[next])
				#print("children crossed")
				#print(c1,c2)
				c1=mutate(c1)
				c2=mutate(c2)
				#print("children mutated")
				#print(c1,c2)
				c1.append(fitness(c1))
				c2.append(fitness(c2))
				children.append(c1)
				children.append(c2)
				p[index].append(f1)
				p[next].append(f2)
			
		return children	,best_route_yet	
	#print("previous generation")
	
	children,best_route_yet=run(gen)
	next_gen=evolve_population(gen,children)
	if selection(next_gen)[0][10]<best_route_yet[10]:
		best_route_yet=selection(next_gen)[0]
	
	
	
	
	
	for n in itertools.count():
		if n<k_n_generations:
			n+=1
			run(next_gen)
		else:
			end_time = time.time()	
	#print(start_time,end_time)
			print("Elapsed time was %f seconds."%(end_time - start_time))
			return best_route_yet

    

	
def main():
	
	
	first_gen =[]
	for population in range(pop_size):
		route = random.sample(range(1,11), 10)
		route.append(fitness(route))
		first_gen.append(route)
		
	print(first_gen)	
	
	print("initial shortest distance")
	print(selection(first_gen)[0])
	
	print("shortest distance after %d generations"%k_n_generations)
	s=GA(first_gen)
	print("hhhhhhhhhhhhh")
	print(s)
	
	
if __name__ == "__main__":
    main()	