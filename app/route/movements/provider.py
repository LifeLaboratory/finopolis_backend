from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_movements(args):
        query = """
    with price as (
    select 
        "номенклатура",
        avg("цена") as "цена"
    from "движение"
    where "количество" > 0
    group by "номенклатура"
    union 
    select 
        null::integer "номенклатура",
        avg("цена") as "цена"
    from "движение"
    where "количество" > 0
    ),
    result as (
        select 
        "наименование",
        "датавремя",
        case when "количество" > 0 then 'поступление'
             else 'продажа' end "тип",
        case when "количество" > 0 then abs("количество") end "куплено",
        case when "количество" < 0 then abs("количество") end "продано",
        case when "количество" > 0 then mov."цена" end "цена_покупки",
        case when "количество" < 0 then mov."цена" end "цена_продажи",
        case when "количество" < 0 then mov."цена" - pr."цена"
             else null::integer 
             end "прибыль"
        from "движение" mov
        left join "номенклатура" n on n."номенклатура" = mov."номенклатура"
        left join price pr on pr."номенклатура" = mov."номенклатура"
        where mov."лицо" = {@лицо}
    )

    select
    null::text "наименование",
    null::timestamp "датавремя",
    'итоги' "тип",
    sum("куплено") "куплено",
    sum("продано") "продано",
    avg("цена_покупки") "цена_покупки",
    avg("цена_продажи") "цена_продажи",
    sum("прибыль") "прибыль"
    from result
    union
    select * from result
    order by "датавремя" desc nulls first
    """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def insert_into_movements(args):
        query = """
    insert into "движение" ("номенклатура", "датавремя", "количество", "цена", "лицо") 
        VALUES (
            '{номенклатура}'    , 
            '{датавремя}', 
            '{количество}',
            '{цена}',
            '{лицо}'
        )
        returning "@движение"
    """
        return Sql.exec(query=query, args=args)
