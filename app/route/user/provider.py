from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def auth_user(args):
        query = """
    select "@лицо"
    from "лицо"
    where ("логин" = '{логин}'
      and "пароль" = '{пароль}'
      )
                """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def check_user(args):
        query = """
  select 1
  from "лицо"
  where ("логин" = '{логин}'
    and "пароль" = '{пароль}'
    )
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def register_user(args):
        query = """
    insert into "лицо"("логин", "пароль", "фио", "описание", "фото") 
    VALUES ('{логин}', 
    '{пароль}', 
    '{фио}',
    '{описание}',
    '{фото}')
    returning "@лицо"
    """
        print(query)
        return Sql.exec(query=query, args=args)
