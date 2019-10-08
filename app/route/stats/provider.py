from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_stat_by_face(args):
        query = """
         select *
         from статистика_постов
         where "лицо" = %(лицо)d
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_stat_by_post(args):
        query = """
         select *
         from статистика_постов
         where "пост" = %(пост)d
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_all_stat():
        query = """
         select *
         from "статистика_постов"
        """
        return Sql.exec(query=query)

    @staticmethod
    def create_stat(args):
        query = """
             insert into "статистика_постов" 
             (
             "лицо", 
             "пост", 
             "соцсеть", 
             "лайки", 
             "просмотры", 
             "комментарии"
             )
             values 
             (
             %(лицо)d, 
             %(пост)d, 
             %(соцсеть)d, 
             %(лайки)d, 
             %(просмотры)d, 
             %(комментарии)d
             )
             returning "@статистика_постов"
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_stat(args):
        query = """
             update статистика_постов
             set
             "лицо" = %(лицо)d,
             "пост" = %(пост)d,
             "соцсеть" = %(соцсеть)d,
             "лайки" = %(лайки)d,
             "просмотры" = %(просмотры)d
             "комментарии" = %(комментарии)d
             where "@статистика_постов" = %(статистика_постов)d
             returning "@статистика_постов"
        """
        return Sql.exec(query=query, args=args)


