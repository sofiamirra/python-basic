def read_products():
    products = []
    with open('products.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.rstrip('\n').split(' ')
            products.append({'product_id': fields[0], 'seller_id': fields[1]})
    return products

def read_transactions():
    transactions = []
    with open('transactions.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.rstrip('\n').split(' ')
            transactions.append({'product_id': fields[0], 'seller_id': fields[1]})
    return transactions

def suspect_transactions(products, transactions):
    print("Suspect transactions")
    for product in products:
        sellers = []
        for transaction in transactions:
            if transaction['product_id'] == product['product_id']:
                sellers.append(transaction['seller_id'])
                if transaction['seller_id'] != product['seller_id']:
                    suspect_product = product['product_id']
                    if transaction['seller_id'] not in sellers:
                        sellers.append(transaction['seller_id'])
        print(f"\nProduct code: {suspect_product}\nOfficial seller: {product['seller_id']}\nSellers list: {', '.join(sellers)}")


def main():
    products = read_products()
    transactions = read_transactions()
    suspect_transactions(products, transactions)

if __name__ == '__main__':
    main()
