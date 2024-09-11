class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        search = []
        for i in range(len(searchWord)):
            search.append(searchWord[:i+1])
        
        products = sorted(products)
        pro = []
        for i in search:
            temp = []
            length = len(i)
            for j in products:
                if j[:length] == i:
                    temp.append(j)
                if len(temp) == 3:
                    break
            pro.append(temp)
                    
        return pro

                    
            