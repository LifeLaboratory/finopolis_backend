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
        where "@лицо" = {лицо}
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_profile(args):
        query = """
        update "лицо" 
          set "фио" = '{фио}'
            , "описание" = '{описание}'
            , "фото" = '{фото}'
            , "заголовок" = '{заголовок}'
            , "статус" = {статус}
          where "@лицо" = {лицо}
        """
        return Sql.exec(query=query, args=args)
