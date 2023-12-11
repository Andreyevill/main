import copy
from pprint import pprint

site = {
	'html': {
		'head': {
			'title': 'Куплю/продам телефон недорого'
		},
		'body': {
			'h2': 'У нас самая низкая цена на iphone',
			'div': 'Купить',
			'p': 'продать'
		}
	}
}
def find_key(struct, key, meaning):
    if key in struct:
        struct[key] = meaning
        return site

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, meaning)
            if result:
                return site

d_copy = dict()
goods = dict()
count_sites = int(input('Введите кол-во сайтов: '))
for _ in range(count_sites):
    name_project = input('Введите название продукта для нового сайта: ')
    new_site = {'title' : f'Куплю/продам {name_project} недорого',
    'h2' : f'У нас самая низкая цена на {name_project}'}
    for i in new_site:
        find_key(site, i, new_site[i])
    name_of_site = f'Сайт для {name_project}:'
    d_copy = copy.deepcopy(site)
    goods = d_copy
    print(name_of_site)
    pprint(goods)
   
