from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_nomenclature(args):
        query = """
         with balances as (
        select
        "номенклатура",
        sum("количество") "остаток" 
        from "движение" group by "номенклатура"
        )
    select n.*, b."остаток"
    from номенклатура n
    left join balances b on b."номенклатура" = n."номенклатура"
    where n."номенклатура" = {номенклатура} and n."лицо" = {@лицо}
    order by "остаток" desc
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_all_nomenclature(args):
        query = """
        with balances as (
        select
        "номенклатура",
        sum("количество") "остаток" 
        from "движение" group by "номенклатура"
        )
    select n.*, coalesce(b."остаток", 0) "остаток"
    from номенклатура n
    left join balances b on b."номенклатура" = n."номенклатура"
    where n."лицо" = {@лицо}
    order by "остаток" desc
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_nomenclature(args):
        query = """
    update "номенклатура" 
      set 
          наименование = '{наименование}'
        , описание = '{описание}'
        , категория = '{категория}'
        , цена = '{цена}'
        , фото = '{фото}'
        , лицо = '{лицо}'
        , удален = {удален}
      where "номенклатура" = {номенклатура}
      returning "номенклатура"
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def create_nomenclature(args):
        query = """
        insert into "номенклатура" ("наименование", "описание", "категория", "цена", "фото", "лицо", "удален") 
        VALUES ('{наименование}', 
        '{описание}', 
        '{категория}',
        '{цена}',
        '{фото}',
        '{лицо}',
        {удален}
        )
        returning "номенклатура"
        """
        return Sql.exec(query=query, args=args)
