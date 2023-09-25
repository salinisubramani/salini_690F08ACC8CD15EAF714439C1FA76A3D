def linearSearchProduct(productlist,targetproduct):
    indices=[]
    for index,product in enumerate(productlist):
        if product==targetproduct:
            indices.append(index)
            return indices
product=["shoes","boot","loafter","shoes","sandel","shoes"]
target="boot"
result=linearSearchProduct(product,target)
print(result)
