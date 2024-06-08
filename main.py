import random
from docxtpl import DocxTemplate
from faker import Faker
from faker.providers import DynamicProvider

unit_provider = DynamicProvider(
     provider_name="unit",
     elements=["кг", "шт", "м", "шт"],
)


doc = DocxTemplate("tmp.docx")
fake = Faker('ru_RU')
fake.add_provider(unit_provider)

for i in range(1, 16):
    number_of_products = random.randint(1, 10)
    product_info = [{'amount': random.randint(1, 50),
                     'price': round(random.uniform(10, 10000), 2)}
                    for j in range(0, number_of_products)]
    year = random.randint(0, 24)

    context = {
        'check_number': i,
        'company': fake.company(),
        'seller': fake.name(),
        'address': fake.address(),
        'ORGN': random.randint(1000000000000, 9999999999999),
        'day': random.randint(1, 12),
        'month': fake.month_name(),
        'year': "0" + str(year) if year < 10 else str(year),
        'products': [{'title': fake.word(),
                      'code': random.randint(10000, 99999),
                      'unit': fake.unit(),
                      'amount': product_info[j]['amount'],
                      'price': product_info[j]['price'],
                      'sum': round(product_info[j]['amount']*product_info[0]['price'], 2)}
                     for j in range(0, number_of_products)],
        'general_sum': round(sum(e['amount']*e['price'] for e in product_info), 2)
    }
    doc.render(context)
    doc.save(f"res{i}.docx")

