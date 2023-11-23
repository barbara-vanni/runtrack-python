def basket() :
    fruits=['pomme', 'cerise', 'orange', 'melon']
    return fruits

fruit_basket = basket()
fruit_basket.insert(2, "mangue")
print(fruit_basket)