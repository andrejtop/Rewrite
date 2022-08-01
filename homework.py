import json

def recept():
    cook_book = {}
    keys = ['ingridient_name', 'quantity', 'measure', ]
    with open('recipes.txt', encoding='utf-8') as file:
        lines = []
        for line in file:
            line = line.strip()
            if line:
                lines.append(line)
        lines = iter(lines)
        for name in lines:
            cook_book[name] = []
            num = next(lines)
            for i in range(int(num)):
                ingr_line = next(lines)
                ingrid = ingr_line.split(' | ')
                z = zip(keys, ingrid)
                ingr_dict = {k: v for (k, v) in z}
                cook_book[name].append(ingr_dict)

    return cook_book


def get_shop_list_by_dishes(list_dishes, person_count):
    cook_book = recept()
    dictionary_ingredients = {}
    for dishes in list_dishes:
        if dishes in cook_book.keys():
            for ingredients in cook_book[dishes]:
                ingridient_name = ingredients['ingridient_name']
                if ingridient_name not in dictionary_ingredients.keys():
                    dictionary_ingredients[ingridient_name] = {'measure': ingredients['measure'],
                                                               'quantity': int(
                                                                   ingredients['quantity']) * person_count}
                else:
                    plus = int(ingredients['quantity']) * person_count
                    dictionary_ingredients[ingridient_name]['quantity'] += plus
    # print(json.dumps(dictionary_ingredients, indent=1, ensure_ascii=False))
    return dictionary_ingredients

print(json.dumps(recept(), indent=1, ensure_ascii=False))
print(json.dumps(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), indent=1, ensure_ascii=False))