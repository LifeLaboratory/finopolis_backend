from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_post(args):
        query = """
    select 
        p.*
        , n."@номенклатура"
        , n."наименование"
        , n."описание"
        , n."категория"
        , n."цена"
        , n."фото"
    from "пост" p
    left join "номенклатура" n on n."@номенклатура" = p."номенклатура" 
    where "@пост" = {@пост} and p."лицо" = {@лицо} and "удален" is not true
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_all_post(args):
        query = """
    select  
        p.*
        , n."@номенклатура"
        , n."наименование"
        , n."описание"
        , n."категория"
        , n."цена"
        , n."фото"
    from пост p
    left join "номенклатура" n on n."@номенклатура" = p."номенклатура"
    where p."лицо" = {@лицо} and "удален" is not true
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_post(args):
        query = """
    update пост 
      set 
          заголовок = '{заголовок}'
        , текст = '{текст}'
        , фото = '{фото}'
        , номенклатура = '{номенклатура}'
        , датавремя = '{датавремя}'
        , удален = '{удален}'
        , черновик = '{черновик}'
        , лицо = '{лицо}'
      where "@пост" = {@пост}
      returning "@пост"
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def create_post(args):
        query = """
        insert into "пост" ("заголовок", "текст", "фото", "номенклатура", "датавремя", "удален", "черновик", "лицо") 
                    VALUES ('{заголовок}', '{текст}', '{фото}','{номенклатура}','{датавремя}','{удален}','{черновик}', '{лицо}'
        )
        returning "@пост"
        """
        return Sql.exec(query=query, args=args)
