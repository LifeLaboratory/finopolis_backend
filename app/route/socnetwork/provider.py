from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_socnetwork(args):
        query = """
         select *
         from соцсеть
         where "@соцсеть" = {соцсеть}
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
             values ('{наименование}', '{логин}', '{пароль}', '{ссылка}')
             returning "@соцсеть"
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_socnetwork(args):
        query = """
             update соцсеть
             set
             "наименование" = '{наименование}',
             "логин" = '{логин}',
             "пароль" = '{пароль}',
             "ссылка" = '{ссылка}'
             where "@соцсеть" = {соцсеть}
             returning "@соцсеть"
        """
        return Sql.exec(query=query, args=args)


