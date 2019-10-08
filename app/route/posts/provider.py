from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_post(args):
        query = """
    select 
        p.*
        , n."номенклатура"
        , n."наименование"
        , n."описание"
        , n."категория"
        , n."цена"
        , n."фото"
    from "пост" p
    left join "номенклатура" n on n."номенклатура" = p."номенклатура" 
    where "@пост" = %(@пост)d and p."лицо" = %(@лицо)d and "удален" is not true
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_all_post(args):
        query = """
    select  
        p.*
        , n."номенклатура"
        , n."наименование"
        , n."описание"
        , n."категория"
        , n."цена"
        , n."фото"
    from пост p
    left join "номенклатура" n on n."номенклатура" = p."номенклатура"
    where p."лицо" = %(@лицо)d and p."удален" is not true
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_post(args):
        query = """
    update пост 
      set 
          заголовок = '%(заголовок)s'
        , текст = '%(текст)s'
        , фото = '%(фото)s'
        , номенклатура = '%(номенклатура)s'
        , датавремя = '%(датавремя)s'
        , удален = %(удален)r
        , черновик = %(черновик)r
        , лицо = %(лицо)d
      where "@пост" = %(@пост)d
      returning "@пост"
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def create_post(args):
        query = """
        insert into "пост" ("заголовок", "текст", "фото", "номенклатура", "датавремя", "удален", "черновик", "лицо") 
                    VALUES (
                    '%(заголовок)s', 
                    '%(текст)s', 
                    '%(фото)s',
                    '%(номенклатура)s',
                    '%(датавремя)s', 
                    %(удален)r, 
                    %(черновик)r, 
                    %(лицо)d
        )
        returning "@пост"
        """
        return Sql.exec(query=query, args=args)
