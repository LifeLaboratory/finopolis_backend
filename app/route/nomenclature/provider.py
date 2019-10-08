from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_nomenclature(args):
        query = """
    select *
    from "номенклатура"
    where "номенклатура" = %(номенклатура)d and "лицо" = %(@лицо)d
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_all_nomenclature(args):
        query = """
    select *
    from номенклатура
    where "лицо" = %(@лицо)d
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_nomenclature(args):
        query = """
    update "номенклатура" 
      set 
          наименование = '%(наименование)s'
        , описание = '%(описание)s'
        , категория = '%(категория)s'
        , цена = '%(цена)s'::double precision
        , фото = '%(фото)s'
        , лицо = %(лицо)d
        , удален = %(удален)r
      where "номенклатура" = %(номенклатура)d
      returning "номенклатура"
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def create_nomenclature(args):
        query = """
        insert into "номенклатура" ("наименование", "описание", "категория", "цена", "фото", "лицо", "удален") 
        VALUES ('%(наименование)s', 
        '%(описание)s', 
        '%(категория)s',
        '%(цена)s'::double precision,
        '%(фото)s',
        %(лицо)d,
        %(удален)r
        )
        returning "номенклатура"
        """
        return Sql.exec(query=query, args=args)
