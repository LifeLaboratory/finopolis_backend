from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_socnetwork(args):
        query = """
         select *
         from соцсеть
         where "@соцсеть" = %(соцсеть)d
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_all_socnetwork():
        query = """
         select *
         from "соцсеть"
        """
        return Sql.exec(query=query)

    @staticmethod
    def create_socnetwork(args):
        query = """
             insert into "соцсеть" ("наименование", "логин", "пароль", "ссылка")
             values ('%(наименование)s', '%(логин)s', '%(пароль)s', '%(ссылка)s')
             returning "@соцсеть"
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_socnetwork(args):
        query = """
             update соцсеть
             set
             "наименование" = '%(наименование)s',
             "логин" = '%(логин)s',
             "пароль" = '%(пароль)s',
             "ссылка" = '%(ссылка)s'
             where "@соцсеть" = %(соцсеть)d
             returning "@соцсеть"
        """
        return Sql.exec(query=query, args=args)


