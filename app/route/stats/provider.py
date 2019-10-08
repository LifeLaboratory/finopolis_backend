from app.api.base.base_sql import Sql


class Provider:
    @staticmethod
    def get_stat_by_face(args):
        query = """
         select *
         from статистика_постов
         where "лицо" = {лицо}
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def get_stat_by_post(args):
        query = """
         select *
         from статистика_постов
         where "пост" = {пост}
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
             {лицо}, 
             {пост}, 
             {соцсеть}, 
             {лайки}, 
             {просмотры}, 
             {комментарии}
             )
             returning "@статистика_постов"
        """
        return Sql.exec(query=query, args=args)

    @staticmethod
    def update_stat(args):
        print(args)
        query = """
             update статистика_постов
             set
             "лицо" = {пост},
             "соцсеть" = {соцсеть},
             "лайки" = {лайки},
             "просмотры" = {просмотры}
             "комментарии" = {комментарии}
             where "@статистика_постов" = {статистика_постов}
             returning "@статистика_постов"
        """
        return Sql.exec(query=query, args=args)


