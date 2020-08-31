class InventoryAllocator:
    def calc_shipping(self,order,storage):
        result=[]
        for i in order:
            j=0
            count=0
            countpop=0
            total_fruit=order[i]
            while j<=len(storage)-1:
                #If the total fruit order is fulfilled, no need to check further warehouses. 
                if total_fruit==0:
                    break
                if i in storage[j]['inventory'].keys():
                    if order[i]<=storage[j]['inventory'][i]:
                        result.append({storage[j]['name']:{i:order[i]}})
                        count+=order[i]
                        total_fruit=0
                        storage[j]['inventory'][i]=0
                    elif storage[j]['inventory'][i]==0:
                        continue
                    else:
                        result.append({storage[j]['name']:{i:storage[j]['inventory'][i]}})
                        total_fruit-=storage[j]['inventory'][i]
                        count+=storage[j]['inventory'][i]
                        countpop+=1
                        storage[j]['inventory'][i]=0
                else:
                    if j==len(storage)-1 and i not in storage[j]['inventory'].keys():
                        result=[]
                        break
                j+=1
            #Checking if total fruit order is fulfilled after checking every Warehouse.
            #If not, it will pop from the result
            if count<order[i]:
                for i in range(0,countpop):
                    result.pop()
        print("Output:- ")
        print(result)
def main():
    i=InventoryAllocator()
    print("Exact Inventory match:-")
    print("Input:- "+"{apple:1,},[{name:owd,inventory:{apple:1}}]")
    i.calc_shipping({"apple":1,},[{"name":"owd","inventory":{"apple":1}}])
    print("Multiple Warehouse Inventory:-")
    print("Input:- "+"{apple:10,},[{name:owd,inventory:{apple:5}},{name:dm,inventory:{apple:5}},{name:jbd,inventory:{orange:3}}]")
    i.calc_shipping({"apple":10},[{"name":"owd","inventory":{"apple":5}},{"name":"dm","inventory":{"apple":5}},{"name":"jbd","inventory":{"orange":3}}])
    print("Not enough Inventory even after checking Multiple Warehouses :-")
    print("Input:- "+"{apple:6,},[{name:random,inventory:{apple:3}},{name:owd,inventory:{apple:2}}]")
    i.calc_shipping({"apple":6},[{"name":"random","inventory":{"apple":3}},{"name":"owd","inventory":{"apple":2}}])
    print("One Inventory fulfills but other fails:-")
    print("Input:- "+"{apple:10,orange:5},[{name:owd,inventory:{apple:5}},{name:dm,inventory:{apple:5}}]")
    i.calc_shipping({"apple":10,"orange":5},[{"name":"owd","inventory":{"apple":5}},{"name":"dm","inventory":{"apple":5}}])
if __name__=="__main__":
    main()