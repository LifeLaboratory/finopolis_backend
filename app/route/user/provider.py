from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def auth_user(args):
        query = """
    select "@лицо"
    from "лицо"
    where ("логин" = '%{логин}s'
      and "пароль" = '%{пароль}s'
      )
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def check_user(args):
        query = """
  select 1
  from "лицо"
  where ("логин" = '%(логин)s'
    and "пароль" = '%(пароль)s'
    )
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def register_user(args):
        print(args)
        query = """
        insert into "лицо"("логин", "пароль", "фио", "описание", "фото") 
        VALUES ('%(логин)s', 
        '%(пароль)s', 
        '%(фио)s',
        '%(описание)s',
        '%(фото)s')
        returning "@лицо"
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_user_id(args):
        query = """
        select "@лицо"
        from "лицо"
        where "логин" = '%(логин)s'
        """
        return Sql.exec(query=query, args=args)
