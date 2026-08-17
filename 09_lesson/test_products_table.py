from products_table import ProductsTable

db = ProductsTable("postgresql://postgres:Fly_steeps@127.0.0.1:5432/QA")


def test_get_products_list():
    db_result = db.get_products_list()
    assert len(db_result) == 12


def test_create_product():
    art = 'A13'
    product = 'шапка'
    category = 'одежда'
    db.create_product(art, product, category)


def test_edit():
    product = 'туфля'
    art = 'A11'
    db.edit_product(product, art)


def test_delete_product():
    art = 'A13'
    db.delete_product(art)


def test_add_new_product():
    before = len(db.get_products_list())

    art = 'A22'
    product = 'фонарик'
    category = 'туризм'
    db.create_product(art, product, category)

    after = len(db.get_products_list())

    new_product = db.get_product_by_art(art)
    print(new_product)

    db.delete_product(art)
    assert new_product['art'] == art
    assert after - before == 1
