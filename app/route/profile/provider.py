from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_profile(args):
        query = """
        select "фио"
          , "описание"
          , "фото"
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
            , "статус" = {статус}
          where "@лицо" = {лицо}
        """
        return Sql.exec(query=query, args=args)
