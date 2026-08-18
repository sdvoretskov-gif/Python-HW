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
    db_result = db.get_products_list()
    new_product = db.get_product_by_art(art)
    print(new_product)

    assert new_product['art'] == art
    assert len(db_result) == 13


def test_edit():
    art = 'A111'
    product = 'туфли'
    db.edit_product_by_art(art, product)

    new_product = db.get_product_by_art(art)
    print(new_product)

    assert new_product['art'] == art

    old_art = 'A11'
    product = 'туфли'
    db.edit_product_by_art(old_art, product)


def test_delete_product():
    art = 'A13'
    product_before = db.get_product_by_art(art)
    print(product_before)

    if not product_before:
        raise AssertionError("Товара A13 не существует!")

    db.delete_product(art)

    deleted_product = db.get_product_by_art(art)

    assert deleted_product is None, \
        "Продукт с артикулом A13 всё ещё существует!"


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
