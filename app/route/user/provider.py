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
    insert into "лицо"("логин", "пароль", "фио", "описание", "фото", "почта", "номер") 
    VALUES ('{логин}', 
    '{пароль}', 
    '{фио}',
    '{описание}',
    '{фото}', 
    '{почта}', 
    '{номер}')
    returning "@лицо"
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_user_id(args):
        query = """
    select "@лицо"
    from "лицо"
    where "логин" = '{логин}'
                """
        return Sql.exec(query=query, args=args)
