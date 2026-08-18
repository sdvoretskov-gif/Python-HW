from sqlalchemy import create_engine, text


class ProductsTable:
    __scripts = {
        "select": text("SELECT * FROM products"),
        "insert_new": text("INSERT INTO products (art, product, category)"
                           " values (:new_art, :new_product, :new_category)"),
        "select by art": text("SELECT * FROM products "
                              "WHERE (art) = :select_art"),
        "select by product": text("SELECT * FROM products "
                                  "WHERE (product) = :select_product"),
        "update by art": text("UPDATE products "
                              "SET art = :new_art"
                              " WHERE product = :product"),
        "delete by art": text("DELETE FROM products WHERE art = :product_art")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_products_list(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def create_product(self, art, product, category):
        conn = self.__db.connect()
        conn.execute(self.__scripts["insert_new"],
                     {"new_art": art, "new_product": product,
                      "new_category": category},)
        conn.commit()
        conn.close()

    def get_product_by_art(self, art):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select by art"],
                              {"select_art": art})
        company = result.mappings().one_or_none()
        conn.close()
        return company

    def get_product_by_product(self, product):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select by product"],
                              {"select_product": product})
        company = result.mappings().one_or_none()
        conn.close()
        return company

    def edit_product_by_art(self, art, product):
        conn = self.__db.connect()
        conn.execute(self.__scripts["update by art"],
                     {"new_art": art, "product": product})
        conn.commit()
        conn.close()

    def delete_product(self, art):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["delete by art"],
            {"product_art": art}
        )
        conn.commit()
        conn.close()
