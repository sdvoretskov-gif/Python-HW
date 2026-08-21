from sqlalchemy import create_engine, text
import allure


class CompanyTable:
    __scripts = {
        "select": text("SELECT * FROM company"),
        "select only active": text(
            "SELECT * FROM company WHERE \"is_active\" = true "),
        "delete by id": text("DELETE FROM company WHERE id = :id_to_delete"),
        "insert_new": text("INSERT INTO company(\"name\") values (:new_name)"),
        "get_max_id": text("SELECT MAX(\"id\") "
                           "FROM company WHERE deleted_at IS NULL"),
        "select by id": text("SELECT * FROM company "
                             "WHERE id =:select_id AND deleted_at IS NULL"),
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    @allure.step("Получить список компаний")
    def get_companies(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        query_string = str(result.context.compiled)
        allure.attach(query_string, 'SQL', allure.attachment_type.TEXT)
        conn.close()
        return rows

    @allure.step("Получить список активных компаний")
    def get_active_companies(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select only active"])
        rows = result.mappings().all()
        query_string = str(result.context.compiled)
        allure.attach(query_string, 'SQL', allure.attachment_type.TEXT)
        conn.close()
        return rows

    @allure.step("Удалить компанию по {id}")
    def delete(self, id):
        conn = self.__db.connect()
        query = conn.execute(
            self.__scripts["delete by id"],
            {"id_to_delete": id}
        )
        query_string = str(query.context.compiled)
        allure.attach(query_string, 'SQL', allure.attachment_type.TEXT)
        conn.commit()
        conn.close()

    @allure.step("Создать компанию {name}")
    def create(self, name):
        conn = self.__db.connect()
        query = conn.execute(self.__scripts["insert_new"], {"new_name": name})
        query_string = str(query.context.compiled)
        allure.attach(query_string, 'SQL', allure.attachment_type.TEXT)
        conn.commit()
        conn.close()

    @allure.step("Получить компанию по максимальному {id} ")
    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        query_string = str(result.context.compiled)
        allure.attach(query_string, 'SQL', allure.attachment_type.TEXT)
        conn.close()
        return max_id

    @allure.step("Получить компанию по {id}")
    def get_company_by_id(self, id):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select by id"],
        {"select_id": id})
        company = result.mappings().all()
        query_string = str(result.context.compiled)
        allure.attach(query_string, 'SQL', allure.attachment_type.TEXT)
        conn.close()
        return company
