from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_profile(args):
        query = """
        select "фио"
          , "описание"
          , "фото"
          , "заголовок"
          , "@лицо"
        from "лицо"
        where "@лицо" = %(лицо)d
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_profile(args):
        query = """
        update "лицо" 
          set "фио" = '%(фио)s'
            , "описание" = '%(описание)s'
            , "фото" = '%(фото)s'
            , "заголовок" = '%(заголовок)s'
            , "статус" = %(статус)r
          where "@лицо" = %(лицо)d
          returning "@лицо"
        """
        return Sql.exec(query=query, args=args)
