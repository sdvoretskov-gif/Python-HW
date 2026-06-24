from string import whitespace


class StringUtils:

    @staticmethod
    def capitalize(string: str) -> str:
        processed_text = string[0].upper() + string[1:]

        return processed_text

    @staticmethod
    def trim(string: str) -> str:
        return string.lstrip(whitespace)

    @staticmethod
    def contains(string: str, symbol: str) -> bool:
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass

        return res

    def delete_symbol(self, string: str, symbol: str) -> str:
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string
