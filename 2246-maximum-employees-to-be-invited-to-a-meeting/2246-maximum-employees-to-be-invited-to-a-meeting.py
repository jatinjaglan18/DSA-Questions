class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        topo,trim = [0]*n,[0]*n # topological degree, side-sitting count
        for i,j in enumerate(favorite):
            topo[j] += 1
        curzero = [i for i,j in enumerate(topo) if not j]

        while curzero: # trim the non-loop nodes
            nex = []
            for i in curzero:
                temp = favorite[i]
                trim[temp] = trim[i] + 1
                topo[temp] -= 1
                if not topo[temp]:
                    nex.append(temp)
            curzero = nex

        curone = [i for i,j in enumerate(topo) if j]
        two,loop = 0,0 # pair total, longest loop
        for i in curone: # deal with the loop nodes
            if topo[i]:
                temp = favorite[i]
                if favorite[temp]==i: # pairs
                    two += trim[i] + trim[temp] + 2
                    topo[i] = topo[temp] = 0
                else: # long loop
                    cnt = 1
                    topo[i] = 0
                    while temp!=i:
                        topo[temp] = 0
                        temp = favorite[temp]
                        cnt += 1
                    loop = max(loop,cnt)
        
        return max(loop,two)

